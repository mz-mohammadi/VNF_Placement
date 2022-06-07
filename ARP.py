# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 18:20:39 2019

@author: mareed
"""

import random

def ARP(itr, max_iter, f_alpha, f_x):# 1: exploitation, 0: explration
    Pi=(f_alpha/f_x)*((itr+max_iter)/(2*max_iter))
    rand=random.random()
    if rand <Pi:
        return 1
    else:
        return 0