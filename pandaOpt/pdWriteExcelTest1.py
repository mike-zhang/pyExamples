#! /usr/bin/env python3
#-*- coding:utf-8 -*-
#windows10 + python3.9 ok

import  pandas  as pd
from pandas import DataFrame
       
df = pd.DataFrame([["11", 21, 31], ["12", 22, 32], ["31", 32, 33]],
                  index=['one', 'two', 'three'], 
                  columns=['a', 'b', 'c'])
print(df)
#         a   b   c
# one    11  21  31
# two    12  22  32
# three  31  32  33        

df.to_excel('1.xlsx', index=False)

