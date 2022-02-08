import requests
from bs4 import BeautifulSoup
import pandas as pd
page = requests.get('https://forecast.weather.gov/MapClick.php?x=276&y=148&site=lox&zmx=&zmy=&map_x=276&map_y=148')
#print(page)
soup =BeautifulSoup(page.content, 'html.parser')

#days =soup.find_all('p', class_ ="Period-name" )
#print(days)

panel = soup.find_all('div', id='seven-day-forecast-body')[0]
#print(len(panel))

day_lists = panel.find_all('li', class_ ='forecast-tombstone')[1::2]
print(len(day_lists))

#night_lists = panel.find_all('li', class_='forecast-tombstone')[2::2]
#print(night_lists)

############################################################################
