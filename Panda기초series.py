# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 16:45:50 2018

@author: hjw8393
"""

from pandas import Series, DataFrame

mine   = Series([10, 20, 30], index=['naver', 'sk', 'kt'])
friend = Series([10, 30, 20], index=['kt', 'naver', 'sk'])
merge = mine + friend
print(merge)

kakao = Series([92600, 92400, 92100, 94300, 92300])
print(kakao)

kakao2 = Series([92600, 92400, 92100, 94300, 92300], index=['2016-02-19',
                                                            '2016-02-18',
                                                            '2016-02-17',
                                                            '2016-02-16',
                                                            '2016-02-15'])
print(kakao2)

for date in kakao2.index:
    print(date)

for ending_price in kakao2.values:
    print(ending_price)