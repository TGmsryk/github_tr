#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

print(sys.version)

def islist(l1, l2):
    if l1 == l2:
    	return True
    else:
    	return False

l1 = [1, 2]
s1 = {1,2}
s1_list = list(s1)

print(islist(l1, s1))
print(islist(l1,s1_list))
