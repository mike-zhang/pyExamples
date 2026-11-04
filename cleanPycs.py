#! /usr/bin/env python3
#-*- coding: utf-8 -*-

import os

for root, dirs, files in os.walk(".", topdown=False):
    for filename in files:
        if filename.split('.')[-1] == 'pyc' :
            print(os.path.join(root,filename))
            os.remove(os.path.join(root,filename))

print('Done')
