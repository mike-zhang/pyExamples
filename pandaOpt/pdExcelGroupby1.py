#! /user/bin/env python3
#-*- coding:utf-8 -*-

import pandas as pd

def genFile(fileSrc,sheetName,fileDst):
    xlsx2 = pd.read_excel(fileSrc,sheetName)
    dt2 = xlsx2.groupby(['网点名称']).sum()
    writer = pd.ExcelWriter(fileDst)
    dt2.to_excel(writer)
    writer.save()

genFile('账单_自整理.xlsx','8月坐席','output1.xlsx')
genFile('账单_自整理.xlsx','系统账单','output2.xlsx')
