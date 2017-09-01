#! /usr/bin/python
#-*- coding: utf-8 -*-  

# get same day of next month  

from dateutil import relativedelta
import datetime

d1 = datetime.date.today().replace(month=12,day=1)
print d1
d2 = d1 + relativedelta.relativedelta(months=1)

print d2
