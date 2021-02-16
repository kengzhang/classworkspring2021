# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:50:06 2021

@author: zhang
"""

def coordinate (a, b, x):
    slope = (a[1]-b[1])/(a[0]-b[0])
    y = slope * (x-a[0])+a[1]
    return y