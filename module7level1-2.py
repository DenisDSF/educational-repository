import requests
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt
import datetime

url = 'https://mfd.ru/currency/?currency=USD'
today = datetime.date.today()

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
currency_table = soup.find('table', {'class': 'mfd-currency-table'})
irrelevant_tag = ['th', 'span', 'a']
[tag.decompose() for tag in currency_table.find_all(irrelevant_tag)]
[tag.decompose() for tag
 in currency_table.find_all(lambda tag: not tag.contents
                                        or len(tag.get_text(strip=True)) == 0)]

currency_list = []
date_start_str = 'с '
for tag in currency_table.find_all('tr'):
    temp_list = [None, None]
    temp_tag = tag.extract()
    for string in temp_tag.stripped_strings:
        if string.startswith(date_start_str):
            date = re.sub(date_start_str, '', string)
            temp_list[0] = date
        else:
            temp_list[1] = float(string)
    currency_list.append(temp_list)

last_date = currency_list[0]
if (datetime.datetime.strptime(last_date[0], '%d.%m.%Y')).date() > today:
    have_forecast = True

if have_forecast:
    forecast = currency_list.pop(0)
    print(f'Прогнозируемый курс доллара на {forecast[0]} составляет '
          f'{forecast[1]} рублей.')
for i in currency_list:
    print(f'Курс доллара на {i[0]} составляет {i[1]} рублей.')

currency_list.reverse()
x_list = []
y_list = []
for i in currency_list:
    x_list.append(i[0])
    y_list.append(i[1])
plt.xlabel('Дата')
plt.ylabel('Курс доллара')
plt.ylabel('График курса доллара.')
plt.xticks(range(len(x_list) - 1, 0, -10), rotation='vertical')
plt.grid(True)
plt.plot(x_list, y_list)
plt.show()
