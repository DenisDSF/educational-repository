import requests
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt
import datetime
from abc import ABC, abstractmethod

class AbstractDataPuller(ABC):
    @abstractmethod
    def get_text(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

class AbstractTagSeparator(ABC):
    @abstractmethod
    def get_separated_tag(self):
        pass

class AbstractInterestedInfoFinder(ABC):
    @abstractmethod
    def get_interested_info(self):
        pass

class AbstractDataInformer(ABC):
    @abstractmethod
    def print_data(self):
        pass

class AbstractGraphPlotter(ABC):
    @abstractmethod
    def plot_graph(self):
        pass

class SoupObject(AbstractDataPuller):
    def __init__(self, url, parser):
        self.url = url
        self.parser = parser
        self.response = requests.get(self.url)
        self.soup = BeautifulSoup(self.response.text, self.parser)

    def get_text(self):
        return self.soup.text

    def get_data(self):
        return self.soup

class SeparatedTag(AbstractTagSeparator):
    def __init__(self, soup_object, interesting_tag, **kwargs):
        self.interesting_tag = interesting_tag
        self.kwargs = {
            'class': kwargs.get('tag_class', None),
            'id': kwargs.get('id', None),
            'method': kwargs.get('method', None),
            'action': kwargs.get('action', None)
        }
        self.kwargs = {key: value for key, value in self.kwargs.items()
                       if value is not None}
        self.found_tag = soup_object.get_data().find(self.interesting_tag,
                                                     self.kwargs)

    def get_separated_tag(self):
        return self.found_tag

class InterestedInfoFinder(AbstractInterestedInfoFinder):
    def __init__(self, separated_tag, interested_info_parent_tag,
                 date_start_str,
                 exchange_rate_start):
        self.interested_info_parent_tag = interested_info_parent_tag
        self.date_start_str = date_start_str
        self.exchange_rate_start = exchange_rate_start
        self.currency_list = []
        for tag in separated_tag.find_all(self.interested_info_parent_tag):
            self.temp_list = [None, None]
            temp_tag = tag
            for string in temp_tag.stripped_strings:
                if string.startswith(date_start_str):
                    date = re.sub(date_start_str, '', string)
                    self.temp_list[0] = date
                elif string.startswith(self.exchange_rate_start):
                    self.temp_list[1] = float(string)
            if self.temp_list[0] is not None:
                self.currency_list.append(self.temp_list)

    def get_interested_info(self):
        return self.currency_list

class ExchangeRatesInformer(AbstractDataInformer):
    def __init__(self, currency_list):
        self.currency_list = []
        self.currency_list += currency_list
        self.today = datetime.date.today()
        self.last_date = self.currency_list[0]
        self.have_forecast = False

    def print_data(self):
        if (datetime.datetime.strptime(self.last_date[0], '%d.%m.%Y')).date() > self.today:
            self.have_forecast = True
        if self.have_forecast:
            self.forecast = self.currency_list.pop(0)
            print(f'Прогнозируемый курс доллара на {self.forecast[0]} составляет '
                  f'{self.forecast[1]} рублей.')
        for i in self.currency_list:
            print(f'Курс доллара на {i[0]} составляет {i[1]} рублей.')

class ExchangeRatesGraphPlotter(AbstractGraphPlotter):
    def __init__(self, currency_list):
        self.currency_list = []
        self.currency_list += currency_list
        self.today = datetime.date.today()
        self.last_date = self.currency_list[0]
        if (datetime.datetime.strptime(self.last_date[0], '%d.%m.%Y')).date() > self.today:
            del self.currency_list[0]
        self.currency_list.reverse()
    def plot_graph(self):
        self.x_list = []
        self.y_list = []
        for i in self.currency_list:
            self.x_list.append(i[0])
            self.y_list.append(i[1])
        plt.xlabel('Дата')
        plt.ylabel('Курс доллара')
        plt.ylabel('График курса доллара.')
        plt.xticks(range(len(self.x_list) - 1, 0, -10), rotation='vertical')
        plt.grid(True)
        plt.plot(self.x_list, self.y_list)
        plt.show()

url = 'https://mfd.ru/currency/?currency=USD'
parser = 'lxml'
soup = SoupObject(url, parser)

table_tag = 'table'
table_tag_class = 'mfd-currency-table'
table_tag_id = None
table_tag_method = None
table_tag_action = None
currency_table = SeparatedTag(soup, table_tag, tag_class=table_tag_class,
                              id=table_tag_id, method=table_tag_method,
                              action=table_tag_action)

currency_info_tag = 'tr'
date_start_str = 'с '
exchange_rate_start = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
currency_list = InterestedInfoFinder(currency_table.get_separated_tag(),
                                     currency_info_tag, date_start_str,
                                     exchange_rate_start)

exchange_rate_informer = ExchangeRatesInformer(currency_list.get_interested_info())
exchange_rate_informer.print_data()

exchange_rate_graph = ExchangeRatesGraphPlotter(currency_list.get_interested_info())
exchange_rate_graph.plot_graph()












