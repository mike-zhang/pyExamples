#! /usr/bin/env python
#-*- coding:utf-8 -*-
# version : Python 2.7.13

import pylab
import math

def frange(start,stop,step):
    while start < stop :
        yield start
        start += step

arrX = list(frange(1,20,0.01))
arrY = [math.sin(n) for n in arrX]

pylab.plot(arrX,arrY)
pylab.show()
	
	
	
	
	