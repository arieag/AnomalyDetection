'''
Created on 9/07/2015

@author: aagranonik
'''
import unittest
from anom.AnomalyDetection import AnomalyDetection
from pandas import Series
import pandas as pd
from datetime import datetime
import numpy as np



class Test(unittest.TestCase):


    def testAnomalyDetectionTs(self):


        ano = AnomalyDetection()
        rawcsv = pd.read_csv("C:/GIT/tlv-ds/syslogs/R/anomalydetection/raw.csv",index_col=0, parse_dates=True)
        dates = rawcsv.index
        vals = [k[0] for k in rawcsv.values.tolist()]
        ts = Series(vals, dates)
        ret = ano.AnomalyDetectionTs(ts)

        print ret

        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testAnomalyDetectionTs']
    unittest.main()