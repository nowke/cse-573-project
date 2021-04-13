import pandas as pd

time = 240
amzn_csv = '../DataSets/Extract/Train_Data/Individual/Para_News' + str(time) + '_Amazon' + str(time) + '.csv'
amzn_df = pd.read_csv(amzn_csv, header = 0)
amzn_df['Stock'] = 'Amazon'

aapl_csv = '../DataSets/Extract/Train_Data/Individual/Para_News' + str(time) + '_Apple' + str(time) + '.csv'
aapl_df = pd.read_csv(aapl_csv, header = 0)
aapl_df['Stock'] = 'Apple'

csv_name = '../DataSets/Extract/Train_Data/Para_News' + str(time) + '_Combined' + str(time) + '.csv'

data = pd.concat([amzn_df,aapl_df])
data = data.fillna('No')
data = data.sort_values(by='DateTime')


#data.to_csv(csv_name, index = False)