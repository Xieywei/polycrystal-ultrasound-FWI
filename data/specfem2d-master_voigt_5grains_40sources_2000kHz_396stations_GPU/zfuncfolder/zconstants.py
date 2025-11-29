# -*- coding: utf-8 -*-
#!/usr/bin/env python

###! /usr/bin/python

import glob
import os 
import numpy as np
import pandas as pd

import time

import obspy
from myFormat.data_format import para_struct
from seisflows.tools.graphics import _convert_to_array
from scipy.interpolate import interp1d

## for parallel computing
from multiprocessing import Process, current_process

## for ploting
import matplotlib.pyplot as plt
from seisflows.tools.graphics import plot_section
import argparse

## for i/o
from obspy import read
import scipy.io as sio
from obspy.core.stream import Stream
import os, sys
from seisflows.config import loadpy, Dict
from my_sfs.ze_seisflows import load_su2np,zplot_signals_one_src_all_rec,zplot_signals_one_iter_one_source
import pickle

# for file finding
import glob

t1 = time.time()

### the parameters collection for all signal plotting 
sig_plot_para = para_struct('sig_plot_para')
flag_seismotype = 6; sig_plot_para.flag_seismotype = flag_seismotype
parameters = loadpy('parameters.py')
sys.modules['seisflows_parameters'] = Dict(parameters)
PAR = sys.modules['seisflows_parameters']

D_T = PAR.DT; sig_plot_para.D_T = sig_plot_para
NSTEP = PAR.NT; sig_plot_para.NSTEP = NSTEP
flag_plot_spectrum = 1; sig_plot_para.flag_plot_spectrum = flag_plot_spectrum
t_star_showobs = 1; sig_plot_para.t_star_showobs = t_star_showobs
t_end_showobs= PAR.NT; sig_plot_para.t_end_showobs = t_end_showobs

t_total_obs = np.arange(D_T,NSTEP*D_T+D_T,D_T)*1e6
sig_plot_para.t_total_obs=t_total_obs

save_sig_plot_para_pickledump_fn = 'obf/sig_plot_para_pickle'
sig_plot_para.save_sig_plot_para_pickledump_fn=save_sig_plot_para_pickledump_fn

#seismofold_matrix= ['obs']
#seismofold_matrix= ['syn','obs']
seismofold_matrix= ['syn','obs','adj']
sig_plot_para.seismofold_matrix=seismofold_matrix


srcnum_matrix = [5]
#srcnum_matrix = np.arange(0,8,2)
sig_plot_para.srcnum_matrix=srcnum_matrix

flag_data_or_scratch=2
sig_plot_para.flag_data_or_scratch=flag_data_or_scratch

yaxis_spc=1000  #与seismo图的y轴有关，被my_sfs的plot_seismo_su调用
sig_plot_para.yaxis_spc=yaxis_spc

## source matrix for signals 
srcnum_matrix_sig = [5]
sig_plot_para.srcnum_matrix_sig=srcnum_matrix_sig

## paramters for parallel computing 
rec_matrix = np.arange(0,316,20)
#rec_matrix = np.arange(0,180,60)
sig_plot_para.rec_matrix=rec_matrix
#rec_matrix_cc = np.arange(0,176,1)

#iter_matrix=[0,1,2,3,4,5,6,7,8,9,10]
iter_matrix=np.arange(0,101,10)
#iter_matrix=[0,1,2,3,4]
#iter_matrix=[0,1,2,3,4,5,6,7,8,9,10]
#iter_matrix=[0,1,2,3,4,5,6,7,8,9,10,12,14,16,18,20,22,24,26,28,30]
sig_plot_para.iter_matrix=iter_matrix

dt=PAR.DT
sig_plot_para.dt=dt

#dt_syn=PAR.DT
#dt_obs=5e-8
#dt_obs=PAR.DT

source_num=1
sig_plot_para.source_num=source_num
#iter_num=0

t_len = PAR.NT 
sig_plot_para.t_len=t_len
t_star_showsyn=0
sig_plot_para.t_star_showsyn=t_star_showsyn
t_end_showsyn= t_star_showsyn + t_len
sig_plot_para.t_end_showsyn=t_end_showsyn

t_star_showobs=0
sig_plot_para.t_star_showobs=t_star_showobs
t_end_showobs=t_star_showobs + t_len
sig_plot_para.t_end_showobs=t_end_showobs

t_star_showadj=0
sig_plot_para.t_star_showadj=t_star_showadj
t_end_showadj=t_star_showadj + t_len
sig_plot_para.t_end_showadj=t_end_showadj

#t_star_showobs=0
#t_end_showobs=PAR.NT
xintsyn = 2
yintsyn = 1000   #与seismo图的y轴有关，别psaveseismo调用
sig_plot_para.yintsyn=yintsyn
yintobs = 1000
sig_plot_para.yintobs=yintobs
flag_range=1
sig_plot_para.flag_range=flag_range
flag_delay_cal=0
sig_plot_para.flag_delay_cal=flag_delay_cal
flag_same_range=0
sig_plot_para.flag_same_range=flag_same_range
flag_savepng=1
sig_plot_para.flag_savepng=flag_savepng
### flag_sc 2&3 requires manu-backup; other wise will erase 
flag_sc = 1 # 1 - p_p, 2 xd, 3 zd 
sig_plot_para.flag_sc=flag_sc

## added on Fri May 24 15:37:17 EDT 2019
#execfile('zplot_seismo_main.py')
#execfile('zfuncfolder/zmulti_signal_comp_main.py')

pickle.dump(sig_plot_para,open(save_sig_plot_para_pickledump_fn,'wb'))



print("constant time is located ")
#t2 = time.time()
#print("total time is " + str(t2-t1))



