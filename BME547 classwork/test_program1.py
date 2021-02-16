# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:59:47 2021

@author: zhang
"""

def test_coordinate():
    from program1 import coordinate
    result = coordinate((1,2),(3,4),5)
    expected = 6
    assert result == expected