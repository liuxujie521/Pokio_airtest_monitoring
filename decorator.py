#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = "Morrow"

import time
import functools
def time_consuming(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        a = func(*args,**kwargs)
        end = time.time()
        maketime=round(end-start,2)
        print('耗时：%ds'%maketime)
        return a
    return wrapper
