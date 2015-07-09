'''
Created on 9/07/2015

@author: aagranonik
'''
import unittest
from anom.AnomalyDetection import AnomalyDetection
from pandas import Series
from datetime import datetime
import numpy as np

class Test(unittest.TestCase):


    def testAnomalyDetectionTs(self):


        ano = AnomalyDetection()
        dates = [datetime(2012, 5, 1), datetime(2012, 5, 2), datetime(2012, 5, 3)]
        vals = [1,2,3]
        ts = Series(vals, dates)
        ret = ano.AnomalyDetectionTs(ts)


        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testAnomalyDetectionTs']
    unittest.main()