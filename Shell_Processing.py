# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 22:14:23 2021

@author: arpendu.ganguly
"""

grep 2017-07 seasonal/spring.csv | wc -l

cut -d , -f 2 seasonal/summer.csv | grep -v Tooth | head -1