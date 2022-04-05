import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests 



page = requests.get("https://weather.com/weather/tenday/l/San+Francisco+CA?canonicalCityId=dfdaba8cbe3a4d12a8796e1f7b1ccc7174b4b0a2d5ddb1c8566ae9f154fa638c")
soup = BeautifulSoup(page.content,'html.parser')
#print(soup)
#print(page)


# Getting list of days

days_list = soup.find_all('div', class_ = 'DetailsSummary--DetailsSummary--2HluQ DetailsSummary--fadeOnOpen--vFCc_')

list_day = []

for days in days_list:
    day_time = days.h2.text.split()[0]
    list_day.append(day_time)

ld1 = list_day[1:11]
#print(len(ld1))

# Getting the descriptions

des = soup.find_all('div', class_ ='DaypartDetails--Content--hJ52O DaypartDetails--contentGrid--1SWty')

sd = []

for i in des:
    s_d = i.p.text
    sd.append(s_d)

sd1 = sd[1:11]
#print(len(sd1))

# Getting temperatures

temp = soup.find_all('div', class_ = 'DailyContent--ConditionSummary--1X5kT')

t = []

for i in temp:
    t_ = i.span.text
    t.append(t_)
#print((t))

h = t[0::2]
#print(h)

l = t[1::2]
#print(l)

def sti(n):  #converting string to int

    for i in range(len(n)):
        n[i] = int(n[i][0:2])

    return n

hn = sti(h)

#print(hn)

ln = sti(l)

def ftc(newlist): # converting Farenheit to Celcius
    newtemp = []

    for i in newlist:
        new_temp = round((i - 32)*(5/9),2)
        newtemp.append(new_temp)

    return newtemp
    

hc = ftc(hn)
#print(hc)

lc = ftc(ln)
#print(lc)


hc1 = hc[1:11]
#print(len(lc1))

lc1 = lc[0:10]
#print((hc1))

# generating the dataframe

df = pd.DataFrame({ 'Day': ld1,
                            'Description': sd1,
                            'Day-Temp °C': hc1,
                            'Night-Temp °C': lc1})

df['Date'] = pd.date_range(start='02/08/2022', periods=len(df), freq='D')

df[['Day','Date', 'Day-Temp °C', 'Night-Temp °C', 'Description']]



