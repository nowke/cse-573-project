# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 12:46:35 2021

@author: rchokkam
"""
import pandas as pd
import os
import time

st = time.time()
df = pd.DataFrame()
new_rec = pd.DataFrame()
count = 0
count_apple = 0
count_amazon = 0
#fpath = '../DataSets/Temp/'
#fpath = '../DataSets/News/2018_01_d157b48c57be246ec7dd80e7af4388a2/'
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
                for para in json_data.text[0].split('\n'):
                    new_rec['Source'] = json_data['thread'][0]['site_full']
                    new_rec['Apple'] = 'No'
                    new_rec['Amazon'] = 'No'
                    if ('AAPL' or 'Apple') in para:
                        new_rec['Apple'] = 'Yes'
                    if ('AMZN' or 'Amazon') in para:
                        new_rec['Amazon'] = 'Yes'
                    new_rec['text'] = para
                    new_rec['DateTime'] = pd.to_datetime(json_data.published,utc=True)
                    if new_rec['Apple'][0] == 'Yes' or new_rec['Amazon'][0] == 'Yes':
                        df = df.append(new_rec[['Source','text','Apple','Amazon','DateTime']], ignore_index=True)

df = df.sort_values(by='DateTime')
csv_name = '../DataSets/Extracted_Para.csv'
df.to_csv(csv_name, header = None, index = False)

mt = time.time()
et = st - mt
print("Reading time is", int((et) // (60*60)), "hours", int(((et) % (60*60)) // 60), "minutes", int((et) % 60), "seconds")