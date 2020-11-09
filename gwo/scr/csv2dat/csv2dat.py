#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Created on Sun Nov 1 2020
@author: yulong
Transfer ground observation data *.csv to dat files.

CSV File contents
----------------
KanID         INT,                       観測所ＩＤ
YYYY     SMALLINT,                       年
MM       SMALLINT,                       月
DD       SMALLINT,                       日
HH       SMALLINT,                       時            1～24
lhpa     SMALLINT,lhpaRMK  SMALLINT,     現地気圧      0.1hPa
shpa     SMALLINT,shpaRMK  SMALLINT,     海面気圧      0.1hPa
kion     SMALLINT,kionRMK  SMALLINT,     気温          0.1゜C
stem     SMALLINT,stemRMK  SMALLINT,     蒸気圧        0.1hPa
rhum     SMALLINT,rhumRMK  SMALLINT,     相対湿度      1%
muki     SMALLINT,mukiRMK  SMALLINT,     風向          16方位
sped     SMALLINT,spedRMK  SMALLINT,     風速          0.1m/s
clod     SMALLINT,clodRMK  SMALLINT,     雲量          10分比
tnki     SMALLINT,tnkiRMK  SMALLINT,     現在天気      符号(00～xxx)
humd     SMALLINT,humdRMK  SMALLINT,     露点温度      0.1゜C
lght     SMALLINT,lghtRMK  SMALLINT,     日照時間      0.1時間
slht     SMALLINT,slhtRMK  SMALLINT,     全天日射量    0.01MJ/㎡
kous     SMALLINT,kousRMK  SMALLINT      降水量        0.1mm

Table header
------------
[    00      01     02   03 04 05 06   07      08   09      10]
 KanID1 KanName KanID2 YYYY MM DD HH lhpa lhpaRMK shpa shpaRMK
[  11      12   13      14   15      16   17      18   19      20]
 kion kionRMK stem stemRMK rhum rhumRMK muki mukiRMK sped spedRMK
[  21      22   23      24   25      26   27      28   29      30   31      32]
 clod clodRMK tnki tnkiRMK humd humdRMK lght lghtRMK slht slhtRMK kous kousRMK

# 風向の16方位は次の通りである。
# +----+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
# |数値| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12| 13| 14| 15| 16|
# +----+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
# |風向| - |NNE| NE|ENE| E |ESE| SE|SSE| S |SSW| SW|WSW| W |WNW| NW|NNW| N |
# +----+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+

"""

import sys
import numpy as np
import pandas as pd
import datetime

def str2datetime(s):
    ss = s.split('-')
    Y = int(ss[0])
    m = int(ss[1])
    d = int(ss[2])
    H = int(ss[3])
    # Y,m,d,H,M = map(int, (s[:4], s[5:7], s[8:10], s[11:13], s[14:16]))
    return datetime.datetime(Y,m,d) + datetime.timedelta(hours=H)


file = sys.argv[1]
rnam = sys.argv[2]
showme = 24

"""
file = "Tokyo1991-2017.csv"
rnam = "output"

example:
    python csv2dat.py [input file] [output file
    python csv2dat.py 'ajiro/Ajiro1991-2017.csv' 'ajiro/1991-2017'
"""

data = pd.read_csv(file, sep=',', skiprows=None, header=None, encoding="SHIFT-JIS")

dt_old = []
for i in range(len(data)-1):
    dt_old.append(str(data.iloc[i,3])+'-'+str(data.iloc[i,4])+'-'+ \
                str(data.iloc[i,5])+'-'+str(data.iloc[i,6]))

dt_new = []
for i in range(len(data)-1):
    temp=str2datetime(dt_old[i])
    dt_new.append(temp.strftime("%Y-%m-%dT%H:%M:%S"))
    

"""
Wind Velocity (m/s)
----
"""
print('%19s %12s %12s %12s %12s\n'%( \
        'sped    Date & time', \
        'Speed', \
        'Direction', \
        'X', \
        'Y', \
        ))
for i in range(showme):    
    if data.iloc[i,17] == 0:
        # whtn the degree value is zero
        print('%19s %8.2f m/s %8.1f deg %8.2f m/s %8.2f m/s\n'%( \
            dt_new[i], \
            data.iloc[i,19]/10, \
            data.iloc[i,17]*360/16, \
            0, \
            0, \
            ))
    else:
        print('%19s %8.2f m/s %8.1f deg %8.2f m/s %8.2f m/s\n'%( \
            dt_new[i], \
            data.iloc[i,19]/10, \
            data.iloc[i,17]*360/16, \
            data.iloc[i,19]/10*np.cos(data.iloc[i,17]*360/16*np.pi/180), \
            data.iloc[i,19]/10*np.sin(data.iloc[i,17]*360/16*np.pi/180), \
            ))
print('%s\n'%( \
        '...', \
        ))

with open(rnam + "_wind.csv","w") as f:
        f.write('%3d\n'%(data.iloc[0,0]))
        for i in range(len(data)-1):  
            if data.iloc[i,17] == 0:
                f.write('%19s, %8.3f, %8.3f,\n'%( \
                      dt_new[i], \
                      0, \
                      0, \
                      ))
            else:
                f.write('%19s, %8.3f, %8.3f,\n'%( \
                      dt_new[i], \
                      data.iloc[i,19]/10*np.cos(data.iloc[i,17]*360/16*np.pi/180), \
                      data.iloc[i,19]/10*np.sin(data.iloc[i,17]*360/16*np.pi/180), \
                      ))
            
"""
Atmosphric Temperature (deg/C)
----------
"""
print('%19s %14s\n'%( \
        'kion    Date & time', \
        'Temp', \
        ))
for i in range(showme):    
    print('%19s %8.1f deg/C\n'%( \
            dt_new[i], \
            data.iloc[i,11]/10, \
            ))
print('%s\n'%( \
        '...', \
        ))

with open(rnam + "_temp.csv","w") as f:
        f.write('%3d\n'%(data.iloc[0,0]))
        for i in range(len(data)-1):        
            f.write('%19s, %8.1f,\n'%( \
                      dt_new[i], \
                      data.iloc[i,11]/10, \
            ))
            
"""
Relative Humidity (-)
----------
"""
print('%19s %17s\n'%( \
        'rhum    Date & time', \
        'Relative humidity', \
        ))
for i in range(showme):    
    print('%19s %12.2f (-)\n'%( \
            dt_new[i], \
            data.iloc[i,15]/100, \
            ))
print('%s\n'%( \
        '...', \
        ))

with open(rnam + "_rhum.csv","w") as f:
        f.write('%3d\n'%(data.iloc[0,0]))
        for i in range(len(data)-1):        
            f.write('%19s, %8.2f,\n'%( \
                      dt_new[i], \
                      data.iloc[i,15]/100, \
            ))
            
"""
Atmospheric pressure (hPa)
----------
"""
print('%19s %12s\n'%( \
        'shpa    Date & time', \
        'pressure', \
        ))
for i in range(showme):    
    print('%19s %8.2f hPa\n'%( \
            dt_new[i], \
            data.iloc[i,9]/10, \
            ))
print('%s\n'%( \
        '...', \
        ))

with open(rnam + "_pres.csv","w") as f:
        f.write('%3d\n'%(data.iloc[0,0]))
        for i in range(len(data)-1):        
            f.write('%19s, %8.2f,\n'%( \
                      dt_new[i], \
                      data.iloc[i,9]/10, \
            ))
            
"""
Cloud (-)
----------
"""
print('%19s %12s\n'%( \
        'clod    Date & time', \
        'Cloud', \
        ))
for i in range(showme):    
    print('%19s %8.1f (-)\n'%( \
            dt_new[i], \
            data.iloc[i,21]/10, \
            ))
print('%s\n'%( \
        '...', \
        ))

with open(rnam + "_clod.csv","w") as f:
        f.write('%3d\n'%(data.iloc[0,0]))
        for i in range(len(data)-1):        
            f.write('%19s, %8.1f,\n'%( \
                      dt_new[i], \
                      data.iloc[i,21]/10, \
            ))
            
"""
Solar radiation (W/m2)
----------
"""
print('%19s %16s\n'%( \
        'slht    Date & time', \
        'Solar ridation', \
        ))
for i in range(showme):    
    print('%19s %8.2f (MJ/m2) %8.2f (W/m2)\n'%( \
            dt_new[i], \
            data.iloc[i,29]/100, \
            data.iloc[i,29]/100/3600*1e6, \
            ))
print('%s\n'%( \
        '...', \
        ))

with open(rnam + "_dswr.csv","w") as f:
        f.write('%3d\n'%(data.iloc[0,0]))
        for i in range(len(data)-1):        
            f.write('%19s, %8.2f,\n'%( \
                      dt_new[i], \
                      data.iloc[i,29]/100/3600*1e6, \
            ))
            
"""
Precipitation (m/s)
----------
"""
print('%19s %47s\n'%( \
        'kous    Date & time', \
        'Precipitation', \
        ))
for i in range(showme):    
    print('%19s %8.2f (mm/h) %8.2e (kg/m2/s) %8.2e (m/s)\n'%( \
            dt_new[i], \
            data.iloc[i,31]/10, \
            data.iloc[i,31]/10/3600, \
            data.iloc[i,31]/10/3600/1000, \
            ))
print('%s\n'%( \
        '...', \
        ))

with open(rnam + "_prec.csv","w") as f:
        f.write('%3d\n'%(data.iloc[0,0]))
        for i in range(len(data)-1):        
            f.write('%19s, %8.2e,\n'%( \
                      dt_new[i], \
                      data.iloc[i,31]/10/3600/1000, \
            ))
            
print("File "+file+" convertion done!\n")