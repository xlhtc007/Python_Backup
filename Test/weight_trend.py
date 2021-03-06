# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 08:33:57 2015

weight calculation

@author: Lynnhom
"""
import pandas as pd
import numpy as np
from pandas import DataFrame
import matplotlib as mpl
import matplotlib.pyplot as plt
from datetime import datetime

weight = DataFrame([57.1,57.1,56.5,56.4,55.7,55.7,55.6,56.0,56.3,55.6,55.8,55.7,56.2,55.4,55.9,
                    56.5,56.4,56.7,56.4,56.0,55.7,56.5,56.3,56.9,56.6,56.2,55.9,56.4,56.3,56.4,56.5,58.1,57.2,56.2,56.2,56.3,56.3,56.2,57.0,56.6,56.5,56.1,56.1,55.9,56.4,56.3,
                    56.4,56.5,56.5,56.0,55.9,56.5,56.5,56.2,56.2,56.4,55.8,56.5,56.2,56.4,56.0,56.2,56.1,56.7,56.3,56.7,56.8,57.0,56.6,56.5,57.5,57.1,57.5,57.4,56.9,57.2,57.8,
                    57.3,57.4,57.3,57.5,57.9,57.6,58.4,58.5,58.5,58.9,58.1,58.9,57.6,59.0,59.4,59.3,59.3,59.1,58.8,58.9,58.9,59.5,60.7,59.6,60.2,59.5,59.5,60.1,60.2,59.9,
                    60.4,59.6,60.7,60.5,60.5,60.3,60.8,61.5,61.1,61.3,60.9,60.7,60.5,60.4,60.2,60.5,61.3,61.7,61.0,61.3,61.2,62.0,60.5,61.4,61.9,61.8,62.6,62.1,63.1,62.1,62.8,
                    63.1,62.8,63.1,63.1,63.6,63.1,63.2,63.5,63.7,62.8,63.7,63.1,63.7,63.5,63.6,63.4,64.2,64.2,64.1,64.6,63.7,64.6,63.9,64.4,64.4,64.7,64.9,64.8,64.3,64.5,
                    64.7,64.7,65.5,65.3,65.0,64.5,66.1],index=pd.date_range('2015-06-16', '2015-12-07'),columns=['weight'])
weight['weight'] = weight['weight']*2                    
weight['3d'] = pd.rolling_mean(weight['weight'], window=3)
weight['7d'] = pd.rolling_mean(weight['weight'], window=7)
weight['3d*'] = weight['3d']-np.nanmin(weight['3d'])
weight['7d*'] = weight['7d']-np.nanmin(weight['7d'])
weight['weeks'] = (weight.index - datetime(2015, 05,15)).days/7.0
plt.figure(figsize=(7, 7))
plt.subplot(311)
plt.plot(weight['weeks'], weight['weight'], lw=1.5, label='weight')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.ylabel('weight value')
plt.title('weight trend')
plt.subplot(312)
plt.plot(weight['weeks'], weight['3d*'], 'g', lw=1.5, label='3d')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.ylabel('weight change(0.5kg)')
plt.subplot(313)
plt.plot(weight['weeks'], weight['7d*'], 'g', lw=1.5, label='7d')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.xlabel('weeks')
plt.ylabel('weight change(0.5kg)')

