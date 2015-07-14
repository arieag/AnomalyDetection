'''
Created on 8/07/2015

@author: aagranonik
'''


import pyloess
import os
from numpy import fromiter
from numpy import bool_, float_



dfile = open(os.path.join('madeup_data'), 'r')
dfile.readline()
x = fromiter((float(v) for v in dfile.readline().rstrip().split()),
             float_).reshape(-1,2)
dfile.readline()
y = fromiter((float(v) for v in dfile.readline().rstrip().split()),
             float_)

print pyloess.stl(y)

