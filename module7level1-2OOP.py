from __future__ import annotations
import requests
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt
import datetime
from abc import ABC, abstractmethod

class RequestHtmlInterface(ABC):
    @abstractmethod
    def get_raw_data(self):
        raise NotImplementedError

class DataExtractorInterface(ABC):
    @abstractmethod
    def extract_currency_timeline(self, raw_data) -> CurrencyTimeline:
        raise NotImplementedError

class ExchangeRatesInformer(ABC):
    @abstractmethod
    def print_data(currency, crawler):
        raise NotImplementedError

class AbstractGraphPlotter(ABC):
    @abstractmethod
    def plot_graph(currency, crawler):
        raise NotImplementedError

class CurrencyTimeRate:
    def __init__(self, date_at: date, rate: Decimal):
        self.__date_at = date_at
        self.__rate = rate

    @property
    def date(self):
        return self.__date_at

    @property
    def rate(self):
        return self.__rate

class CurrencyTimeline:
    def __init__(self, currency: str, rates: list[CurrencyTimeRate]):
        self.__currency = currency
        self.__rates = rates

    @property
    def currency(self):
        return self.__currency

    @property
    def rates(self):
        return self.__rates

class CurrencyCrawler:
    def __init__(self, request, extractor):
        self.__request = request
        self.__extractor = extractor
        self.__all_timelines = {}

    def run(self):
        raw_data = self.__request.get_raw_data()
        timeline = self.__extractor.extract_currency_timeline(raw_data)
        self.__all_timelines[timeline.currency] = timeline

    @property
    def timelines(self):
        return self.__all_timelines

class MfdRequest(RequestHtmlInterface):
    def get_raw_data(self):
        response = requests.get('https://mfd.ru/currency/?currency=USD')
        soup = BeautifulSoup(response.text, 'lxml')
        return soup

class MfdExtractor(DataExtractorInterface):
    def extract_currency_timeline(self, raw_data) -> CurrencyTimeline:
        table_tag = 'table'
        table_tag_class = 'mfd-currency-table'
        currency_info_tag = 'tr'
        date_start_str = 'с '
        exchange_rate_start = ('0', '1', '2', '3', '4', '5', '6', '7', '8',
                               '9')
        found_tag = raw_data.find(table_tag, {'class': table_tag_class})
        currency_list = []
        for tag in found_tag.find_all(currency_info_tag):
            temp_list = [None, None]
            temp_tag = tag
            for string in temp_tag.stripped_strings:
                if string.startswith(date_start_str):
                    date_str = re.sub(date_start_str, '', string)
                    date = datetime.datetime.strptime(date_str,
                                                      '%d.%m.%Y').date()
                    temp_list[0] = date
                elif string.startswith(exchange_rate_start):
                    temp_list[1] = float(string)
            if temp_list[0] is not None:
                currency_list.append(temp_list)
        currency_time_rate_list = [CurrencyTimeRate(date, rate)
                                   for date, rate in currency_list]
        timeline = CurrencyTimeline('USD', currency_time_rate_list)
        return timeline

class TablePrinter(ExchangeRatesInformer):
    def print_data(currency: str, crawler: CurrencyCrawler):
        have_forecast = False
        today = datetime.date.today()
        all_timelines = crawler.timelines
        timeline_to_print = all_timelines.get(currency)
        rates_list = timeline_to_print.rates
        if rates_list[0].date > today:
            have_forecast = True
        if have_forecast:
            print(f'Прогнозируемый курс {currency} на {rates_list[0].date} '
                  f'составляет {rates_list[0].rate} рублей.')
            for i in rates_list[1:]:
                print(f'Курс {currency} на {i.date} составляет {i.rate} '
                      f'рублей.')
        else:
            for i in rates_list:
                print(f'Курс {currency} на {i.date} составляет {i.rate} '
                      f'рублей.')

class GraphPlotter(AbstractGraphPlotter):
    def plot_graph(currency: str, crawler: CurrencyCrawler):
        today = datetime.date.today()
        all_timelines = crawler.timelines
        timeline_to_plot = all_timelines.get(currency)
        rates_list = timeline_to_plot.rates
        end_rate_list = None
        if rates_list[0].date > today:
            end_rate_list = 0
        x_list = []
        y_list = []
        for i in rates_list[-1: end_rate_list: -1]:
            x = i.date.strftime('%d.%m.%Y')
            x_list.append(x)
            y_list.append(i.rate)
        plt.xlabel('Дата')
        plt.ylabel('Курс доллара')
        plt.ylabel('График курса доллара.')
        plt.xticks(ticks=range(len(x_list) - 1, 0, -10), rotation='vertical')
        plt.grid(True)
        plt.plot(x_list, y_list)
        plt.show()

mfd_crawler = CurrencyCrawler(MfdRequest(), MfdExtractor())
mfd_crawler.run()
currency_to_print = 'USD'
TablePrinter.print_data(currency_to_print, mfd_crawler)
GraphPlotter.plot_graph(currency_to_print, mfd_crawler)