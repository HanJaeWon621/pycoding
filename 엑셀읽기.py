# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 16:19:38 2018

@author: hjw8393
"""

import win32com.client

excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True
wb = excel.Workbooks.Open('C:\\Users\\hjw8393\\Downloads\\RSM_Membership_개발체크리스트_20180411.xlsx')

ws = wb.ActiveSheet
print(ws.Cells(1,1).Value)
print(ws.Cells(5,1).Value)
ws.Range("H1").Interior.ColorIndex = 10
excel.Quit()