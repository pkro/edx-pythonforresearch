#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 08:23:59 2019

@author: pk
"""

import time
def timeit(func):
    def timed(*args):
        start = time.clock()
        func(*args)
        print(time.clock() - start)
    return timed

@timeit
def say(word, word2):
    print(word + word2)
    
say("hello", " you")
    