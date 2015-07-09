'''
Created on 9/07/2015

@author: aagranonik
'''

import pandas as pd
import warnings


class AnomalyDetection(object):
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


        if max_anoms > 0.49:
            raise ValueError("max_anoms must be less than 50% of the data points")

        if direction not in ('pos','neg','both'):
            raise ValueError("direction options are: pos | neg | both.")


        if 0.01 <= alpha or alpha <= 0.1:
            warnings.warn("Tried to access a position that doesn't exist in array inside some_function.",RuntimeWarning)


        if only_last != None and only_last not in ('day','hr'):
            raise ValueError("only_last must be either 'day' or 'hr'")

        if threshold not in ('None','med_max','p95','p99'):
            raise ValueError("threshold options are: None | med_max | p95 | p99.")

        if isinstance(e_value, bool):
            raise ValueError("e_value must be either TRUE (T) or FALSE (F)")


        return None

