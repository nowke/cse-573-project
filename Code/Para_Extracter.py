# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 12:46:35 2021

@author: rchokkam
"""
import pandas as pd
import os
import time

stock = 'Apple'
if stock == 'Apple':
    sym = 'AAPL'
elif stock == 'Amazon':
    sym = 'AMZN'
    
st = time.time()
df = pd.DataFrame()
new_rec = pd.DataFrame()
count = 0
fpath = '../DataSets/News/'
for root, subdirs, files in os.walk(fpath):
    for file in files:
        if 'json' in file:
            count += 1
            if count % 100 == 0:
                print("Articles read =", count)
            json_path = os.path.join(root, file)
            with open(json_path, 'r'):
                json_data = pd.read_json(json_path, lines=True)
                if json_data.language[0] != 'english' or len(json_data.text[0]) > 32767:
                    continue
                new_rec['Source'] = json_data['thread'][0]['site_full']
                new_rec[stock] = 'No'
                new_rec['text'] = ''
                new_rec['DateTime'] = pd.to_datetime(json_data.published,utc=True)
                for para in json_data.text[0].split('\n'):
                    if (sym or stock) in para:
                        new_rec['text'] += para
                        new_rec[stock] = 'Yes'
                if new_rec[stock][0] == 'Yes':
                    df = df.append(new_rec[['Source','text','DateTime']], ignore_index=True)

df = df.sort_values(by='DateTime')
csv_name = '../DataSets/Extracted_Para_' + str(stock) + '.csv'
df.to_csv(csv_name, header = None, index = False)

mt = time.time()
et = st - mt
print("Reading time is", int((et) // (60*60)), "hours", int(((et) % (60*60)) // 60), "minutes", int((et) % 60), "seconds")