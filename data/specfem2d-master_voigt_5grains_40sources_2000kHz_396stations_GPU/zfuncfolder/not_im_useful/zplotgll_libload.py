

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
multi_locator_spc = 0.00525
half_x= 0.0105
half_z= 0.0105

multi_locator_spc = half_x/2.0 
# acoustic
###levelsvp = np.arange(1450, 1550, 2)
# elastic
levelsvp = np.arange(5700, 6300, 5)
levelsvs = np.arange(3050, 3450, 5)

sysHOME=os.environ.get('HOME', '/home/username/')    
pyfuncFolder=sysHOME + '/Desktop/my_files/my_python/ze_sys_pyfunc/my_sp2d/'
