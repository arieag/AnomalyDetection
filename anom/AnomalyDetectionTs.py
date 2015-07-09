'''
Created on 9/07/2015

@author: aagranonik
'''

import pandas as pd

class AnomalyDetectionTSSTL(object):
    '''
    classdocs
    '''

    def __init__(self, params=None):
        '''
        Constructor

        '''




    def AnomalyDetectionTs(self, x, max_anoms = 0.10, direction = 'pos',
                               alpha = 0.05, only_last = None, threshold = 'None',
                               e_value = False, longterm = False, piecewise_median_period_weeks = 2, plot = False,
                               y_log = False, xlabel = '', ylabel = 'count',
                               title = None, verbose=False):

        if not isinstance(x, pd.Series):
            raise ValueError("data must be a single Time Series.")
        else:
            numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
            if x.dtype not in numerics:
                raise ValueError("data must be a time series with numeric values")






        return None

