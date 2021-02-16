# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 15:03:35 2021

@author: zhang
"""

def coordinate2 (a, b, x):
    slope = (a[1]-b[1])/(a[0]-b[0])
    slope2 = (a[1]-x[1])/(a[0]-x[0])
    if slope == slope2:
        return True
    else:
        return False