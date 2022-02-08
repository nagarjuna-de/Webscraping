from bs4 import BeautifulSoup
import requests

page = requests.get('https://forecast.weather.gov/MapClick.php?x=276&y=148&site=lox&zmx=&zmy=&map_x=276&map_y=148#.YgGVvLrMKUl')

soup = BeautifulSoup(page.content,'html.parser')

lists_days = []
lists_desc = []

days_list = soup.find_all('div',class_ ="tombstone-container" )
for days in days_list:
    day_time = days.p.text
    lists_days.append(day_time)

#print(lists_days)

## short description

days_desc = soup.find_all('div', class_ ="col-sm-10 forecast-text")
for desc in days_desc:
    short_desc = desc.text
    lists_desc.append(short_desc)

#print(lists_desc)










