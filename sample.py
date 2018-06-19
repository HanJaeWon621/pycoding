# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 16:37:06 2018

@author: hjw8393
"""
from pandas import Series, DataFrame

kakao = Series([92600, 92400, 92100, 94300, 92300])
print(kakao
      
kakao_daily_ending_prices = {'2016-02-19': 92600,
                             '2016-02-18': 92400,
                             '2016-02-17': 92100,
                             '2016-02-16': 94300,
                             '2016-02-15': 92300}
print(kakao_daily_ending_prices['2016-02-19'])

kakao_daily_ending_prices = [92300, 94300, 92100, 92400, 92600]

for price in kakao_daily_ending_prices:
    print(price)
    
mystock = ['kakao', 'naver']
print(mystock[0])
print(mystock[1])

exam_dic = {'key1': 'room1', 'key2':'room2'}
print(exam_dic['key1'])
print(exam_dic['key2'])