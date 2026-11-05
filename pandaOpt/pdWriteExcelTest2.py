#! /usr/bin/env python3
#-*- coding:utf-8 -*-
#windows10 + python3.9 ok

import  pandas  as pd
from pandas import DataFrame

#写
dic1 = {
    '标题列1': ['张三','李四'],
    '标题列2': [80, 90]
}
df = pd.DataFrame(dic1)
df.to_excel('1.xlsx', index=False)

