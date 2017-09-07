#! /usr/bin/env python
#-*- coding:utf-8 -*-

def foo():
    sum = 0
    for i in range(100):
        sum += i
    return sum
    
if __name__ == "__main__" :
    import cProfile 
    cProfile.run("foo()") 
    exit(0)
    