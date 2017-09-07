#! /usr/bin/env python
#-*- coding: utf-8 -*-

# use : python -m memory_profiler test2.py

@profile
def my_func():
    a = [1] * (10*6)
    b = [2] * (10*7)
    del b
    return a
    
if __name__ == "__main__" :
    my_func()
    
