'''
Created on 9/07/2015

@author: aagranonik
'''
import unittest
from anom.AnomalyDetectionTs import AnomalyDetectionTSSTL
from pandas import Series
from datetime import datetime
import numpy as np

class Test(unittest.TestCase):


    def testAnomalyDetectionTs(self):


        ano = AnomalyDetectionTSSTL()
        dates = [datetime(2012, 5, 1), datetime(2012, 5, 2), datetime(2012, 5, 3)]
        vals = ["a","vb","c"]
        ts = Series(vals, dates)
        ret = ano.AnomalyDetectionTs(ts)


        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testAnomalyDetectionTs']
    unittest.main()