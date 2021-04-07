# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 14:28:17 2021

@author: rchokkam
"""
import pandas as pd
import numpy as np
import time
import math

df = pd.read_csv('../DataSets/Extracted_Para.csv', names = ['Source','text','Apple','Amazon','DateTime'])
df['DateTime'] = pd.to_datetime(df.DateTime,utc=True)

interval = 5
stock = 'Apple'
news_time = 60

csv_name = '../DataSets/Extract/NewsGroupTime_' + str(news_time) + '/' + str(stock) + str(interval) + '.csv'

charts_path = '../DataSets/CHARTS/CHARTS/'
charts_path += str.upper(stock) + str(interval) + '.csv'

chart_data = pd.read_csv(charts_path, names = ['Date', 'Time', 'Open', 'High', 'Low', 'Close', 'Volume'])

chart_data['DateTime'] = chart_data.Date + "T" + chart_data.Time
chart_data['DateTime'] = pd.to_datetime(chart_data['DateTime'], format='%Y.%m.%d %H:%M',utc=True)
chart_data['Movement'] = np.where(chart_data['Open'] < chart_data['Close'],1,0)

mt = time.time()
print("Mapping begins")

ch_paras = 0
pct = 0
data = pd.DataFrame(columns=['Source', 'News', 'Movement'])
for news_index, news in df.iterrows():
    ch_paras += 1
    if (math.floor(ch_paras*100/df.shape[0]) - pct) > 0:
        pct = math.floor(ch_paras*100/df.shape[0])
        print("Paragraphs checked =", pct, "%")
    if news[stock] == 'Yes':
        for chart_index, chart in chart_data.iterrows():
            react_time = (chart.DateTime - news.DateTime).total_seconds()
            if react_time >= news_time*60 and react_time < (interval+news_time)*60:
                new_link = {'Source': news.Source, 'News': news.text, 'Movement': chart.Movement}
                data = data.append(new_link, ignore_index = True)
                if data.shape[0] % 100 == 0:
                    print(data.shape[0], "news paragraphs mapped")
                break
            elif react_time < 0:
                chart_data.drop(chart_index, inplace = True)
            if react_time > (interval+news_time)*60:
                break

data.to_csv(csv_name, index = False)
et = time.time() - mt
print("Mapping time is", int((et) // (60*60)), "hours", int(((et) % (60*60)) // 60), "minutes", int((et) % 60), "seconds")
print("Mapped", stock, "with", interval, "minutes interval")
