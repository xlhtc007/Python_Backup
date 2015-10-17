# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 21:12:37 2015
http://austinrochford.com/posts/2015-10-05-bayes-survival.html
Bayesian Survival Analysis in Python with pymc3
@author: xuelinghong
"""

from matplotlib import pyplot as plt
import numpy as np
import pymc3 as pm
from pymc3.distributions.timeseries import GaussianRandomWalk
import seaborn as sns
from statsmodels import datasets
from theano import tensor as T

df = datasets.get_rdataset('mastectomy', 'HSAUR', cache=True).data
df.event = df.event.astype(np.int64)
df.metastized = (df.metastized == 'yes').astype(np.int64)
n_patients = df.shape[0]
patients = np.arange(n_patients)

df.head()
n_patients


