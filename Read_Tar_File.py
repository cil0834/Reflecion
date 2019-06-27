# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 08:20:17 2019

@author: KLAGG
"""


import shutil
import os.path
import numpy as np
import glob
import warnings
import pandas

# Returns a 1D array of all of the valid days in (yyyymmdd)
# Years is a 1D array of the years that we are trying to find
def dates_in_myrors(years, months, days):
   conventional_dates = np.array([])
   # In the 'yyyy-mm-dd'
   for year in years:
       for month in months:
           if month == ('04' or '06' or '09' or '11'):
               for day in days[:-1]:
                   for hour in range(0, 24):
                       h = str(hour)
                       if hour < 10:
                           h = '0' + h
                       for minute in range(0, 60, 5):
                           m = str(minute)    
                           if minute < 10:
                               m = '0' + m
                           time = h + m + '00'
                           conventional_dates = np.append(conventional_dates, 
                                                          year + '-' + month + '-' + day + '-' + time)
                   
           if month == ('01' or '03' or '05' or '07' or '08' or '10' or '12'):
                for day in days:
                   for hour in range(0, 24):
                       h = str(hour)
                       if hour < 10:
                           h = '0' + h
                       for minute in range(0, 60, 5):
                           m = str(minute)    
                           if minute < 10:
                               m = '0' + m
                           time = h + m + '00'
                           conventional_dates = np.append(conventional_dates, 
                                                          year + '-' + month + '-' + day + '-' + time)
                   
           if month == ('02'):
               for day in days[:-3]:
                  for hour in range(0, 24):
                       h = str(hour)
                       if hour < 10:
                           h = '0' + h
                       for minute in range(0, 60, 5):
                           m = str(minute)    
                           if minute < 10:
                               m = '0' + m
                           time = h + m + '00'
                           conventional_dates = np.append(conventional_dates, 
                                                          year + '-' + month + '-' + day + '-' + time)
                   
   return conventional_dates

y = np.array(['1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', 
                  '2008', '2009', '2010', '2011', '2014', '2017'])
m = np.array(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'])

d = np.array(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', 
              '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', 
              '27', '28', '29', '30', '31'])

dates = dates_in_myrors(y, m, d)
       

print(dates.item(0))