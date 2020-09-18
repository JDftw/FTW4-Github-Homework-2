# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 23:39:29 2020

@author: Julie Ann Delda
"""

import pandas as pd

df = pd.read_csv('DataSeerGrabPrizeData.csv')

df.describe()

df = df.dropna()

df.describe()

df.to_csv('grab_on_spyder.csv', index=False)
