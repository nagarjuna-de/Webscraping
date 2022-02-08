from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime
page = requests.get('https://forecast.weather.gov/MapClick.php?x=276&y=148&site=lox&zmx=&zmy=&map_x=276&map_y=148#.YgGVvLrMKUl')

soup = BeautifulSoup(page.content,'html.parser')

lists_days = []
lists_desc = []
lists_temp = []
c_temp = []
## scraping days from website.
days_list = soup.find_all('div',class_ ="tombstone-container" )
for days in days_list:
    day_time = days.p.text
    lists_days.append(day_time)

#print(len(lists_days))

## short description

days_desc = soup.find_all('div', class_ ="col-sm-10 forecast-text")[0:9:1]
for desc in days_desc:
    short_desc = desc.text
    lists_desc.append(short_desc)

print(len(lists_desc))

##Temprature
days_temp =soup.find_all('p', class_="temp")
for d in days_temp:
    temp = d.text.split()[1]
    lists_temp.append(temp)

#print(lists_temp)
for i in range(0, len(lists_temp)):
    lists_temp[i] = int(lists_temp[i])
#print(lists_temp)

##Farenheit to Celcius
def Temperature():
    for i in lists_temp:
        new_temp = round((i-32)*(5/9))
        c_temp.append(new_temp)
Temperature()
print(len(c_temp))

### we  creating a list of our own dates.
date_list =['2022.02.7','2022.02.8','2022.02.8','2022.02.9','2022.02.9','2022.02.10','2022.02.10','2022.02.11','2022.02.12']
print(len(date_list))

data = {'Day':lists_days,'Date':date_list,'Description':lists_desc,'Temperature':c_temp}
df = pd.DataFrame(data)
print(df)


print(len(lists_desc))


