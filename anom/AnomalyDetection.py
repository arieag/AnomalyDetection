'''
Created on 9/07/2015

@author: aagranonik
'''

import pandas as pd
import warnings
import math
import numpy as np
import datetime

def get_gran(tseries):

    tseries.sort()
    lastdelta = tseries.index[-1] - tseries.index[-2]
    gran = lastdelta.total_seconds()

    if gran >= 86400:
        return "day"
    elif gran >= 3600:
        return "hr"
    elif gran >= 60:
        return "min"
    elif gran >=1:
        return "sec"
    else:
        return "ms"


class AnomalyDetection(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor

        '''


    def AnomalyDetectionTs(self, x, max_anoms = 0.10, direction = 'pos',
                               alpha = 0.05, only_last = None, threshold = 'None',
                               e_value = False, longterm = False, piecewise_median_period_weeks = 2, verbose=False):

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

        if not isinstance(e_value, bool):
            raise ValueError("e_value must be either True or False")

        if not isinstance(longterm, bool):
            raise ValueError("longterm must be either True or False")

        if piecewise_median_period_weeks < 2:
            raise ValueError("piecewise_median_period_weeks must be at greater than 2 weeks")

        # -- Main analysis: Perform S-H-ESD
        # Derive number of observations in a single day.
        # Although we derive this in S-H-ESD, we also need it to be minutley later on so we do it here first.
        gran = get_gran(x)


        if gran == "day":
            num_days_per_line = 7
            if only_last != None and only_last == "hr":
                only_last = "day"
        else:
            num_days_per_line = 1

        # Aggregate data to minutely if secondly
        if gran == "sec":
            x = x.resample("1Min", how="sum")

        period =  {
                  'min' : 1440,
                  'hr' : 24,
                  # if the data is daily, then we need to bump the period to weekly to get multiple examples
                  'day' : 7
                  }[gran]

        num_obs = len(x)

        if max_anoms < 1/num_obs:
            max_anoms = 1/num_obs

        all_data = dict()
        if longterm:

            if gran == "day":
                # STL needs 2*period + 1 observations
                num_obs_in_period = period*piecewise_median_period_weeks + 1
                num_days_in_period = (7*piecewise_median_period_weeks) + 1
            else:
                num_obs_in_period = period*7*piecewise_median_period_weeks
                num_days_in_period = (7*piecewise_median_period_weeks)


            last_date = x.index[-1]

            for i in xrange(0, len(x)-1, num_obs_in_period):
                start_date = x.index[i]
                b = start_date + datetime.timedelta(days = num_days_in_period)
                end_date = np.min(start_date.value, b.value)
                if (end_date - start_date).days == num_days_in_period:
                    all_data[(i / num_obs_in_period)] = x[x.index[x.index >= start_date and x.index < end_date]]
                else:
                    all_data[(i / num_obs_in_period)] = x[x.index[x.index >= (last_date- datetime.timedelta(days = num_days_in_period)) and x.index < last_date]]
        else:
            all_data[0] = x



        return None

