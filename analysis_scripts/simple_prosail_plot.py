#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import sys
import os
import csv
import matplotlib.pyplot as plt
import numpy as np

filename_in = sys.argv[1]
f2 = open(filename_in, 'r') 
lines = f2.readlines()
x = []
y = [] 
for line in lines:
    p = line.split()
    x.append(float(p[0]))
    y.append(float(p[1]))
f2.close() 

plt.plot(x,y, label='PROSAIL-D')
plt.xlabel('x')
plt.ylabel('y')
#plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()