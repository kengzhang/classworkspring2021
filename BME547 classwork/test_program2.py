# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 15:05:34 2021

@author: zhang
"""

def test_coordinate2 ():
    from program2 import coordinate2
    result = coordinate2 ((1,2),(3,4),(5,6))
    expected = True
    assert result == expected