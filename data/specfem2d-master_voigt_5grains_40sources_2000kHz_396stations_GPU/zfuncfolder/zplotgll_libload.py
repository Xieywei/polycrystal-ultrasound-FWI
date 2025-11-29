# -*- coding: utf-8 -*-

## created on Fri Dec 14 17:30:13 EST 2018 
## created by Jiaze He 

## preparation for pringgllmap


import os, argparse
import sys
import numpy as np
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import pylab
from glob import glob
from seisflows.plugins.solver_io.fortran_binary import _read
from seisflows.config import loadpy, Dict
## added on Fri May 24 09:14:52 EDT 2019
from my_sfs.ze_plot_section import getcoords, meshplot, getnames


msg = ''' 
%s\nmin, max: %f, %f
'''

undersamp_fact = 1
clip_fact = 1.0 
half_x= 0.00012
half_z= half_x
multi_locator_spc = half_x/2.0 
# steel 
levelsvp = np.arange(5500, 6500, 5)
levelsvs = np.arange(2800, 3400, 5)

levelsc11 = np.arange(16.0e10, 18.2e10, 1e8)
levelsc13 = np.arange(6.5e10, 7.5e10, 1e8)
levelsc15 = np.arange(0.15e10, 0.55e10, 0.5e8)
levelsc33 = np.arange(15.5e10, 17.0e10, 1e8)
levelsc35 = np.arange(0.0005e10, 0.55e10, 0.05e8)
levelsc55 = np.arange(4.0e10, 5.5e10, 1e8)


cij_large=[162566870876.10,   70580623625.37,     513575748.21,  177371881873.16,    4864659310.26,   48280623625.37]
cij_small=[162400000000.00,   69000000000.00,             0.00,  180700000000.00,             0.00,   46700000000.00]
cinit=[162440160405.77,   69817123342.84,     181151883.83,  179025592908.54,    3685805211.10,   47517123342.84]


cnames = ['c11', 'c13','c15','c33','c35','c55']
plotRangeFactor = 0.05
cij_large = np.array(cij_large)
cij_small = np.array(cij_small)
cij_large_names = dict(zip(cnames, cij_large))
cij_small_names = dict(zip(cnames, cij_small))
cinit_names = dict(zip(cnames, cinit))

LevelsDict = {}
for key in cij_small_names:
    if (cij_small_names[key] > 0):
        plotRange =1 - plotRangeFactor
    else: 
        plotRange =1 + plotRangeFactor 
    print('plotRange: ', plotRange)

    if (cinit_names[key] > 0):
        plotRangeLarge =1 + plotRangeFactor
        plotRangeSmall =1 - plotRangeFactor
    else:  
        plotRangeLarge =1 - plotRangeFactor
        plotRangeSmall =1 + plotRangeFactor
    #LevelsDict[key] = np.arange(cij_small_names[key] * plotRange, cij_large_names[key] * (1+plotRangeFactor), (cij_large_names[key]*(1+plotRangeFactor) - cij_small_names[key]*plotRange)/20)
    LevelsDict[key] = np.arange(cinit_names[key] * plotRangeSmall, cinit_names[key] * plotRangeLarge, abs(cinit_names[key]) * (2*plotRangeFactor)/20)



#levelsvp = np.arange(5700, 6300, 5)
#levelsvs = np.arange(3050, 3450, 5)

# AA5083
#levelsvp = np.arange(4500, 6300, 5)
#levelsvs = np.arange(2200, 3170, 5)

#levelsvp = np.arange(1470, 1620, 1)
flag_varying_levels=True
flag_load_levels=False
flag_save_levels=True
flag_varying_levels_theta=False
flag_save_levels_theta=True
flag_load_levels_theta=False
flag_rm_dups=True
flag_sp2d_plot=1   #if flag_sp2d_plot ==0:xz_dirname = './model_init'

sysHOME=os.environ.get('HOME', '/home/username/')           
pyfuncFolder=sysHOME + '/Desktop/my_files/my_python/ze_sys_pyfunc/my_it2d/'
#pyfuncFolder=sysHOME + '/Desktop/my_files/my_python/ze_sys_pyfunc/my_sp2d/'

'''
#保存
flag_varying_levels=True
flag_load_levels=False
flag_save_levels=True
flag_varying_levels_theta=False
flag_save_levels_theta=True
flag_load_levels_theta=False
flag_rm_dups=True
flag_sp2d_plot=0 

#使用
flag_varying_levels=False
flag_load_levels=True
flag_save_levels=False
flag_varying_levels_theta=False
flag_save_levels_theta=True
flag_load_levels_theta=False
flag_rm_dups=True
flag_sp2d_plot=0 
'''
