# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 16:54:51 2018

@author: hjw8393
"""
from pandas import Series, DataFrame

raw_data = {'col0': [1, 2, 3, 4],
            'col1': [10, 20, 30, 40],
            'col2': [100, 200, 300, 400]}

data = DataFrame(raw_data)
print(data)

print(type(data['col2']))


daeshin = {'open':  [11650, 11100, 11200, 11100, 11000],
           'high':  [12100, 11800, 11200, 11100, 11150],
           'low' :  [11600, 11050, 10900, 10950, 10900],
           'close': [11900, 11600, 11000, 11100, 11050]}

daeshin_day = DataFrame(daeshin)
print(daeshin_day)

date = ['16.02.29', '16.02.26', '16.02.25', '16.02.24', '16.02.23']
daeshin_day2 = DataFrame(daeshin, columns=['open', 'low', 'high', 'close'], index=date)

print(daeshin_day2)

day_data = daeshin_day2.loc['16.02.24']
print(day_data)
print(type(day_data))

print(daeshin_day2.columns)
print(daeshin_day2.index)