#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Transfer depth data (depth_xxxx-xx.dat) to x,y,z format.

Parameters
----------
file : str
    The depth data file to read.
orig : num
    X in [X, Y] of Northern West original point.
orig : num
    Y in [X, Y] of Northern West original point.
mesh : num
    Size of the mesh dx or dy, defalt same value.
mesh : num
    Size of the mesh dx or dy, defalt same value.
mesh : num
    Size of the mesh dx or dy, defalt same value.
use : 
    python dat2gis.py depth_xxxx-xx.dat [X, Y] [Mx, My] [dx, dy]

"""

import sys
import numpy as np
import pandas as pd

file = sys.argv[1]
##orig = sys.argv[2]
##numb = sys.argv[3]
##mesh = sys.argv[4]
#strA = sys.argv[2].replace('[', ' ').replace(']', ' ').replace(',', ' ').split()
#strB = sys.argv[3].replace('[', ' ').replace(']', ' ').replace(',', ' ').split()
#strC = sys.argv[4].replace('[', ' ').replace(']', ' ').replace(',', ' ').split()
#orig = [float(i) for i in strA]
#numb = [float (i) for i in strB]
#mesh = [float (i) for i in strC]
origx = int(sys.argv[2])
origy = int(sys.argv[3])
numbx = int(sys.argv[4])
numby = int(sys.argv[5])
mesh = int(sys.argv[6])

orig = [origx,origy]
numb = [numbx,numby]
mesh = [mesh,mesh]

"""
file = "地形データ_第09系/depth_0010-01.dat"
orig = [42300,-609100]
numb = [510,510]
mesh = [10,10]
file = "地形データ_第09系/depth_0010-02.dat"
orig = [-9300,-389800]
numb = [630,600]
mesh = [10,10]
file = "地形データ_第09系/depth_0010-03.dat"
orig = [-9900,-313900]
numb = [1350,1470]
mesh = [10,10]
"""

"""
try:
    data = pd.read_csv(file, sep='\\s+', skiprows=None, header=None)
except BaseException:
    col_widths = [8,8,8,8,8,8,8,8,8,8]
    data = pd.read_fwf(file, widths=col_widths, skiprows=None, header=None)
"""
col_widths = [8,8,8,8,8,8,8,8,8,8]
data = pd.read_fwf(file, widths=col_widths, skiprows=None, header=None)

data = data.values.reshape(numb[0],numb[1])
list = data.tolist()
depth = [val for sublist in list for val in sublist]

x = [+1*np.arange(numb[0])*mesh[0]+orig[0]]*numb[1]
xx = [val for sublist in x for val in sublist]
y = np.repeat(np.array([-1*np.arange(numb[1])*mesh[1]+orig[1]]).T, numb[0], axis=1)
yy = [val for sublist in y for val in sublist]

with open(file + ".csv","w") as f:
        f.write("x,y,z"+'\n')
        for i in range(len(depth)-1):
            f.write(str(xx[i]+301.783)+',')
            f.write(str(yy[i]-364.461)+',')
            f.write(str(depth[i]*-1)+'\n')
            
print("File "+file+" convertion done!\n")