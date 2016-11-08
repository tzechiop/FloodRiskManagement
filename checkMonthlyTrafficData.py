# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 11:47:51 2016

This script checks to see the types of traffic data that is avaiable for Mobile,
Alabama.

Traffic data is from https://aldotgis.dot.state.al.us/atd/default.aspx

@author: thasegawa
"""

import os
import calendar
import pandas as pd

# Specify path and get filenames
path = r'C:\Users\thasegawa\Documents\71 FRM Resilience Cast Study\05 Data\Traffic Data'
os.chdir(path)
fname_list = os.listdir()

# Create lists for years and months
year_list = [str(year) for year in range(2005, 2017)]
month_list = [calendar.month_name[i] for i in range(1,13)]

# Create list for types of datasets
typ_list = ['total', 'Total', 'lane', 'Lane', 'direction', 'Direction']

out_fnames = []
out_typs = []
yearnum_list = []
monthnum_list = []
trigger = 0
for year in year_list:
    for monthnum, month in enumerate(month_list):
        potential_fnames = [fname for fname in fname_list if (year in fname) and (month in fname)]
        for typ in typ_list:
            for fname in potential_fnames:
                if typ in fname:
                    out_fnames.append(fname)
                    out_typs.append(typ.lower())
                    yearnum_list.append(str(year))
                    monthnum_list.append(monthnum + 1)
                    trigger = 1
                    potential_fnames = []
                    break
        if trigger == 0:
            print('No file found for {0} {1}'.format(month, year))
        else:
            trigger = 1
            
result = pd.DataFrame({'Filename': out_fnames, 'Type': out_typs, 'Year': yearnum_list, 'Month': monthnum_list})
result.to_csv('result.csv', index = False)