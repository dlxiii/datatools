#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 1 2020
@author: yulong
Intorpolate time series data in stations to map.
"""

import sys
import time
import numpy as np
import pandas as pd
from datetime import datetime

anum = len(sys.argv)
mesh = int(sys.argv[1])
optf = sys.argv[anum-1]
inpf = sys.argv[2:anum-1]

"""
inpf = ['./ajiro/1991-2017_rhum.csv', \
        './chiba/1991-2017_rhum.csv', \
        './chichibu/1991-2017_rhum.csv', \
        './choshi/1991-2017_rhum.csv', \
        './irozaki/1991-2017_rhum.csv', \
        './katsuura/1991-2017_rhum.csv', \
        './kawaguchiko/1991-2017_rhum.csv', \
        './kofu/1991-2017_rhum.csv', \
        './kumagaya/1991-2017_rhum.csv', \
        './maebashi/1991-2017_rhum.csv', \
        './mishima/1991-2017_rhum.csv', \
        './mito/1991-2017_rhum.csv', \
        './miyakejima/1991-2017_rhum.csv', \
        './oshima/1991-2017_rhum.csv', \
        './tateno/1991-2017_rhum.csv', \
        './tateyama/1991-2017_rhum.csv', \
        './tokyo/1991-2017_rhum.csv', \
        './utsunomiya/1991-2017_rhum.csv', \
        './yokohama/1991-2017_rhum.csv']
    
optf='./2014-2017_hum.nc'
    
mesh = 100
"""

"""
example:
    python csv2dat.py [mesh number] [input1] \
                                    [input2] \
                                    [input3] \
                                    [output file]
                                    
python stn2map.py 100 './ajiro/1991-2017_rhum.csv' \
'./chiba/1991-2017_rhum.csv' \
'./chichibu/1991-2017_rhum.csv' \
'./choshi/1991-2017_rhum.csv' \
'./irozaki/1991-2017_rhum.csv' \
'./katsuura/1991-2017_rhum.csv' \
'./kawaguchiko/1991-2017_rhum.csv' \
'./kofu/1991-2017_rhum.csv' \
'./kumagaya/1991-2017_rhum.csv' \
'./maebashi/1991-2017_rhum.csv' \
'./mishima/1991-2017_rhum.csv' \
'./mito/1991-2017_rhum.csv' \
'./miyakejima/1991-2017_rhum.csv' \
'./oshima/1991-2017_rhum.csv' \
'./tateno/1991-2017_rhum.csv' \
'./tateyama/1991-2017_rhum.csv' \
'./tokyo/1991-2017_rhum.csv' \
'./utsunomiya/1991-2017_rhum.csv' \
'./yokohama/1991-2017_rhum.csv' \
'./1991-2017_hum.nc'

    inpf = ['input1.csv','input2.csv','input3.csv']
    inpf = ['./ajiro/1991-2017_rhum.csv', \
'./chiba/1991-2017_rhum.csv', \
'./chichibu/1991-2017_rhum.csv', \
'./choshi/1991-2017_rhum.csv', \
'./irozaki/1991-2017_rhum.csv', \
'./katsuura/1991-2017_rhum.csv', \
'./kawaguchiko/1991-2017_rhum.csv', \
'./kofu/1991-2017_rhum.csv', \
'./kumagaya/1991-2017_rhum.csv', \
'./maebashi/1991-2017_rhum.csv', \
'./mishima/1991-2017_rhum.csv', \
'./mito/1991-2017_rhum.csv', \
'./miyakejima/1991-2017_rhum.csv', \
'./oshima/1991-2017_rhum.csv', \
'./tateno/1991-2017_rhum.csv', \
'./tateyama/1991-2017_rhum.csv', \
'./tokyo/1991-2017_rhum.csv', \
'./utsunomiya/1991-2017_rhum.csv', \
'./yokohama/1991-2017_rhum.csv']
    
    optf='./1991-2017_rhum.nc'
    
    mesh = 100

#print ('参数个数为:', len(sys.argv), '个参数。')
#print ('参数列表:', str(sys.argv))
print ('表示为网格数量的参数是:', str(mesh))
for i in sys.argv[2:anum-1]:
    print ('表示为输入文件的参数是:', i)
print ('表示为输出文件的参数是:', str(optf))

file = "input.csv"
rnam = "output"

No	観測所ID	緯度	経度	海抜(m)	気圧計の高さ(m)	風速計の高さ(m)	観測所名
001	401	45.413333	141.683333	2.80	11.00	23.40	稚内
002	402	44.938333	142.590000	6.70	8.00	10.40	北見枝幸
003	404	44.361667	141.705000	7.90	12.50	13.50	羽幌
004	405	44.578333	142.968333	13.80	15.40	11.30	雄武
005	406	43.943333	141.636667	23.60	27.80	15.80	留萌
006	407	43.770000	142.373333	111.90	115.90	14.60	旭川
007	409	44.016667	144.283333	37.60	42.80	15.60	網走
008	411	43.180000	141.020000	24.90	26.10	12.30	小樽
009	412	43.056667	141.331667	17.20	18.60	31.30	札幌
010	413	43.210000	141.788333	42.30	50.90	20.00	岩見沢
011	417	42.918333	143.215000	38.40	43.20	14.50	帯広
012	418	42.967500	144.384167	31.70	36.70	22.10	釧路
013	420	43.328333	145.590000	25.20	38.50	29.10	根室
014	421	42.784167	140.226667	33.40	37.80	13.40	寿都
015	423	42.310000	140.981667	39.90	49.20	18.20	室蘭
016	424	42.620000	141.550000	6.30	10.90	15.90	苫小牧
017	426	42.150833	142.780000	32.50	36.50	14.50	浦河
018	428	41.865000	140.128333	3.70	11.60	19.50	江差
019	430	41.813333	140.756667	35.00	43.40	25.60	函館
020	433	42.898333	140.761667	176.10	187.60	30.30	倶知安
021	435	44.343333	143.360000	15.80	16.40	18.10	紋別
022	440	42.284167	143.320000	32.40	33.30	12.90	広尾
023	512	39.060000	141.718333	36.90	41.30	22.10	大船渡
024	520	38.753333	140.315000	105.10	113.00	30.90	新庄
025	570	37.485000	139.913333	212.10	212.80	13.40	若松
026	574	40.643333	139.936667	66.10	67.20	13.40	深浦
027	575	40.818333	140.771667	2.80	3.40	30.40	青森
028	576	41.281667	141.215000	2.90	4.50	15.00	むつ
029	581	40.517500	141.517500	27.10	27.90	16.10	八戸
030	582	39.715000	140.103333	6.30	21.10	40.00	秋田
031	584	39.695000	141.168333	155.20	153.40	15.60	盛岡
032	585	39.645000	141.968333	42.50	46.40	20.20	宮古
033	587	38.905000	139.846667	3.10	3.80	27.60	酒田
034	588	38.253333	140.348333	152.50	153.20	13.80	山形
035	590	38.250833	140.900000	38.90	43.30	52.00	仙台
036	592	38.417500	141.303333	42.50	50.00	28.50	石巻
037	595	37.756667	140.467500	67.40	68.70	26.00	福島
038	597	37.128333	140.220000	355.00	372.10	45.50	白河
039	598	36.943333	140.906667	3.20	4.80	15.00	小名浜
040	600	37.390000	136.898333	5.20	13.90	28.30	輪島
041	602	38.017500	138.234167	5.50	16.70	33.60	相川
042	604	37.900833	139.050000	1.90	6.40	18.50	新潟
043	605	36.586667	136.638333	5.70	33.00	48.40	金沢
044	606	36.788333	137.056667	11.60	12.60	15.20	伏木
045	607	36.706667	137.205000	8.60	16.80	20.00	富山
046	610	36.660000	138.195000	418.20	419.30	19.00	長野
047	612	37.103333	138.250000	12.90	18.20	16.70	高田
048	615	36.546667	139.871667	119.40	139.90	49.20	宇都宮
049	616	36.053333	136.226667	8.80	16.80	26.10	福井
050	617	36.153333	137.256667	560.10	561.40	15.20	高山
051	618	36.243333	137.973333	610.00	611.10	16.20	松本
052	620	36.043333	138.111667	760.30	761.80	12.50	諏訪
053	622	36.338333	138.548333	999.10	1004.40	15.10	軽井沢
054	624	36.401667	139.063333	112.10	113.10	17.30	前橋
055	626	36.146667	139.383333	30.00	30.70	16.80	熊谷
056	629	36.376667	140.470000	29.30	30.70	14.00	水戸
057	631	35.650000	136.065000	1.60	11.80	27.70	敦賀
058	632	35.396667	136.765000	12.70	16.70	22.80	岐阜
059	636	35.165000	136.968333	51.10	55.70	17.90	名古屋
060	637	35.500833	137.838333	482.30	484.40	12.70	飯田
061	638	35.663333	138.556667	272.80	280.90	26.90	甲府
062	640	35.496667	138.763333	859.80	860.50	12.80	河口湖
063	641	35.990000	139.078333	218.00	219.40	12.60	秩父
064	646	36.055000	140.130000	25.20	30.50	20.50	館野
065	648	35.736667	140.860000	20.10	27.60	28.20	銚子
066	649	34.750833	136.145000	159.10	165.00	21.90	上野
067	651	34.730000	136.521667	2.60	17.80	39.60	津
068	653	34.617500	137.096667	6.20	7.50	13.10	伊良湖
069	654	34.706667	137.723333	31.70	33.10	13.80	浜松
070	655	34.601667	138.215000	44.70	46.50	16.30	御前崎
071	656	34.971667	138.406667	14.10	15.30	16.30	静岡
072	657	35.111667	138.930000	20.50	21.70	12.70	三島
073	662	35.683333	139.763333	6.50	35.80	74.50	東京
074	663	34.065000	136.195000	15.30	26.90	28.50	尾鷲
075	666	34.600000	138.846667	54.70	55.80	12.40	石廊崎
076	668	35.043333	139.095000	66.90	67.90	12.50	網代
077	670	35.436667	139.655000	39.10	41.80	19.50	横浜
078	672	34.983333	139.868333	5.80	6.70	14.70	館山
079	674	35.146667	140.315000	11.90	13.00	12.30	勝浦
080	675	34.746667	139.365000	74.00	79.30	27.10	大島
081	677	34.120000	139.523333	36.20	37.10	12.90	三宅島
082	678	33.101667	139.788333	79.20	80.30	13.60	八丈島
083	682	35.598333	140.106667	3.50	19.20	47.80	千葉
084	684	34.926667	136.588333	47.20	51.70	12.20	四日市
085	690	36.735000	139.503333	1291.90	1297.70	17.20	日光
086	740	36.201667	133.336667	26.50	31.40	17.50	西郷
087	741	35.453333	133.068333	16.90	21.70	26.70	松江
088	742	35.534167	133.236667	2.00	2.90	11.90	境
089	744	35.431667	133.334167	6.40	7.80	18.20	米子
090	746	35.485000	134.240000	7.10	15.20	32.00	鳥取
091	747	35.533333	134.817500	3.40	4.20	12.90	豊岡
092	750	35.446667	135.320000	2.50	22.10	41.30	舞鶴
093	751	35.415000	136.410000	1375.80	1376.80	15.50	伊吹山
094	754	34.411667	131.393333	5.50	7.00	18.10	萩
095	755	34.893333	132.073333	19.00	20.10	15.20	浜田
096	756	35.061667	134.011667	145.70	147.10	11.80	津山
097	759	35.011667	135.735000	41.40	45.90	16.20	京都
098	761	35.273333	136.246667	87.30	88.50	17.50	彦根
099	762	33.945000	130.928333	3.30	19.00	14.50	下関
100	765	34.395000	132.465000	3.60	53.40	95.50	広島
101	766	34.238333	132.553333	3.50	12.00	17.50	呉
102	767	34.443333	133.250000	1.90	2.80	13.80	福山
103	768	34.656667	133.918333	2.80	18.00	70.90	岡山
104	769	34.836667	134.667500	38.20	39.70	28.10	姫路
105	770	34.688333	135.180000	57.50	59.20	21.90	神戸
106	772	34.678333	135.521667	23.10	82.50	94.20	大阪
107	776	34.335000	134.906667	109.30	112.40	15.50	洲本
108	777	34.226667	135.016667	13.90	17.60	38.90	和歌山
109	778	33.448333	135.763333	73.00	74.70	15.10	潮岬
110	780	34.690000	135.830000	104.40	105.50	11.20	奈良
111	784	34.156667	131.450833	16.70	17.80	15.30	山口
112	800	34.195000	129.293333	3.70	18.60	36.10	厳原
113	805	33.356667	129.553333	57.80	58.20	11.00	平戸
114	807	33.580000	130.376667	2.50	14.50	24.50	福岡
115	809	33.650000	130.695000	37.10	38.30	11.10	飯塚
116	812	33.151667	129.735000	16.70	15.20	13.10	佐世保
117	813	33.261667	130.306667	3.60	32.40	56.20	佐賀
118	814	33.318333	130.931667	82.90	84.20	10.60	日田
119	815	33.231667	131.620000	4.60	12.70	19.80	大分
120	817	32.730000	129.870000	26.90	35.20	18.70	長崎
121	819	32.810000	130.710000	37.70	39.00	14.80	熊本
122	821	32.876667	131.067500	1142.80	1143.70	10.30	阿蘇山
123	822	32.578333	131.660000	19.20	20.50	13.20	延岡
124	823	32.017500	130.203333	40.10	45.20	13.40	阿久根
125	824	32.215000	130.756667	145.80	147.30	12.10	人吉
126	827	31.551667	130.551667	3.90	31.10	44.90	鹿児島
127	829	31.726667	131.083333	153.80	155.10	11.70	都城
128	830	31.920000	131.423333	6.30	7.20	23.30	宮崎
129	831	31.268333	130.295000	29.50	31.00	10.40	枕崎
130	835	31.567500	131.410000	2.90	14.60	19.00	油津
131	836	30.378333	130.661667	36.40	37.80	9.90	屋久島
132	837	30.735000	130.993333	17.00	18.20	10.60	種子島
133	838	32.195000	130.028333	3.00	14.40	20.60	牛深
134	843	32.693333	128.817500	25.10	26.20	10.30	福江
135	887	33.840000	132.780000	32.20	33.60	20.50	松山
136	890	34.273333	133.755000	3.70	4.80	13.20	多度津
137	891	34.313333	134.056667	8.70	9.90	16.60	高松
138	892	33.223333	132.555000	2.40	14.20	33.10	宇和島
139	893	33.565000	133.551667	0.50	17.60	15.40	高知
140	894	33.850000	134.096667	1944.80	1945.60	8.20	剣山
141	895	34.065000	134.576667	1.60	5.80	17.50	徳島
142	897	32.918333	132.696667	2.20	10.70	17.90	宿毛
143	898	32.718333	133.011667	31.00	32.70	13.70	清水
144	899	33.248333	134.180000	185.00	186.40	41.80	室戸岬
145	909	28.376667	129.498333	2.80	7.40	20.80	名瀬
146	912	24.461667	123.010000	30.00	36.00	14.40	与那国島
147	918	24.331667	124.163333	5.70	6.80	22.20	石垣島
148	927	24.790000	125.278333	39.90	40.90	13.60	宮古島
149	929	26.335000	126.805000	4.00	4.90	9.70	久米島
150	936	26.203333	127.688333	28.10	53.10	47.80	那覇
151	940	26.590000	127.968333	6.10	17.80	25.60	名護
152	942	27.428333	128.706667	26.60	29.40	13.50	沖永良部
153	945	25.828333	131.226667	15.30	20.20	22.20	南大東島
154	971	27.083333	142.183333	2.70	7.70	15.90	父島
155	991	24.300000	153.966667	8.30	9.00	13.40	南鳥島

"""
stnDict = {} 

stnDict['401'] = [45.413333,141.683333]
stnDict['402'] = [44.938333,142.590000]
stnDict['404'] = [44.361667,141.705000]
stnDict['405'] = [44.578333,142.968333]
stnDict['406'] = [43.943333,141.636667]
stnDict['407'] = [43.770000,142.373333]
stnDict['409'] = [44.016667,144.283333]
stnDict['411'] = [43.180000,141.020000]
stnDict['412'] = [43.056667,141.331667]
stnDict['413'] = [43.210000,141.788333]
stnDict['417'] = [42.918333,143.215000]
stnDict['418'] = [42.967500,144.384167]
stnDict['420'] = [43.328333,145.590000]
stnDict['421'] = [42.784167,140.226667]
stnDict['423'] = [42.310000,140.981667]
stnDict['424'] = [42.620000,141.550000]
stnDict['426'] = [42.150833,142.780000]
stnDict['428'] = [41.865000,140.128333]
stnDict['430'] = [41.813333,140.756667]
stnDict['433'] = [42.898333,140.761667]
stnDict['435'] = [44.343333,143.360000]
stnDict['440'] = [42.284167,143.320000]
stnDict['512'] = [39.060000,141.718333]
stnDict['520'] = [38.753333,140.315000]
stnDict['570'] = [37.485000,139.913333]
stnDict['574'] = [40.643333,139.936667]
stnDict['575'] = [40.818333,140.771667]
stnDict['576'] = [41.281667,141.215000]
stnDict['581'] = [40.517500,141.517500]
stnDict['582'] = [39.715000,140.103333]
stnDict['584'] = [39.695000,141.168333]
stnDict['585'] = [39.645000,141.968333]
stnDict['587'] = [38.905000,139.846667]
stnDict['588'] = [38.253333,140.348333]
stnDict['590'] = [38.250833,140.900000]
stnDict['592'] = [38.417500,141.303333]
stnDict['595'] = [37.756667,140.467500]
stnDict['597'] = [37.128333,140.220000]
stnDict['598'] = [36.943333,140.906667]
stnDict['600'] = [37.390000,136.898333]
stnDict['602'] = [38.017500,138.234167]
stnDict['604'] = [37.900833,139.050000]
stnDict['605'] = [36.586667,136.638333]
stnDict['606'] = [36.788333,137.056667]
stnDict['607'] = [36.706667,137.205000]
stnDict['610'] = [36.660000,138.195000]
stnDict['612'] = [37.103333,138.250000]
stnDict['615'] = [36.546667,139.871667]
stnDict['616'] = [36.053333,136.226667]
stnDict['617'] = [36.153333,137.256667]
stnDict['618'] = [36.243333,137.973333]
stnDict['620'] = [36.043333,138.111667]
stnDict['622'] = [36.338333,138.548333]
stnDict['624'] = [36.401667,139.063333]
stnDict['626'] = [36.146667,139.383333]
stnDict['629'] = [36.376667,140.470000]
stnDict['631'] = [35.650000,136.065000]
stnDict['632'] = [35.396667,136.765000]
stnDict['636'] = [35.165000,136.968333]
stnDict['637'] = [35.500833,137.838333]
stnDict['638'] = [35.663333,138.556667]
stnDict['640'] = [35.496667,138.763333]
stnDict['641'] = [35.990000,139.078333]
stnDict['646'] = [36.055000,140.130000]
stnDict['648'] = [35.736667,140.860000]
stnDict['649'] = [34.750833,136.145000]
stnDict['651'] = [34.730000,136.521667]
stnDict['653'] = [34.617500,137.096667]
stnDict['654'] = [34.706667,137.723333]
stnDict['655'] = [34.601667,138.215000]
stnDict['656'] = [34.971667,138.406667]
stnDict['657'] = [35.111667,138.930000]
stnDict['662'] = [35.683333,139.763333]
stnDict['663'] = [34.065000,136.195000]
stnDict['666'] = [34.600000,138.846667]
stnDict['668'] = [35.043333,139.095000]
stnDict['670'] = [35.436667,139.655000]
stnDict['672'] = [34.983333,139.868333]
stnDict['674'] = [35.146667,140.315000]
stnDict['675'] = [34.746667,139.365000]
stnDict['677'] = [34.120000,139.523333]
stnDict['678'] = [33.101667,139.788333]
stnDict['682'] = [35.598333,140.106667]
stnDict['684'] = [34.926667,136.588333]
stnDict['690'] = [36.735000,139.503333]
stnDict['740'] = [36.201667,133.336667]
stnDict['741'] = [35.453333,133.068333]
stnDict['742'] = [35.534167,133.236667]
stnDict['744'] = [35.431667,133.334167]
stnDict['746'] = [35.485000,134.240000]
stnDict['747'] = [35.533333,134.817500]
stnDict['750'] = [35.446667,135.320000]
stnDict['751'] = [35.415000,136.410000]
stnDict['754'] = [34.411667,131.393333]
stnDict['755'] = [34.893333,132.073333]
stnDict['756'] = [35.061667,134.011667]
stnDict['759'] = [35.011667,135.735000]
stnDict['761'] = [35.273333,136.246667]
stnDict['762'] = [33.945000,130.928333]
stnDict['765'] = [34.395000,132.465000]
stnDict['766'] = [34.238333,132.553333]
stnDict['767'] = [34.443333,133.250000]
stnDict['768'] = [34.656667,133.918333]
stnDict['769'] = [34.836667,134.667500]
stnDict['770'] = [34.688333,135.180000]
stnDict['772'] = [34.678333,135.521667]
stnDict['776'] = [34.335000,134.906667]
stnDict['777'] = [34.226667,135.016667]
stnDict['778'] = [33.448333,135.763333]
stnDict['780'] = [34.690000,135.830000]
stnDict['784'] = [34.156667,131.450833]
stnDict['800'] = [34.195000,129.293333]
stnDict['805'] = [33.356667,129.553333]
stnDict['807'] = [33.580000,130.376667]
stnDict['809'] = [33.650000,130.695000]
stnDict['812'] = [33.151667,129.735000]
stnDict['813'] = [33.261667,130.306667]
stnDict['814'] = [33.318333,130.931667]
stnDict['815'] = [33.231667,131.620000]
stnDict['817'] = [32.730000,129.870000]
stnDict['819'] = [32.810000,130.710000]
stnDict['821'] = [32.876667,131.067500]
stnDict['822'] = [32.578333,131.660000]
stnDict['823'] = [32.017500,130.203333]
stnDict['824'] = [32.215000,130.756667]
stnDict['827'] = [31.551667,130.551667]
stnDict['829'] = [31.726667,131.083333]
stnDict['830'] = [31.920000,131.423333]
stnDict['831'] = [31.268333,130.295000]
stnDict['835'] = [31.567500,131.410000]
stnDict['836'] = [30.378333,130.661667]
stnDict['837'] = [30.735000,130.993333]
stnDict['838'] = [32.195000,130.028333]
stnDict['843'] = [32.693333,128.817500]
stnDict['887'] = [33.840000,132.780000]
stnDict['890'] = [34.273333,133.755000]
stnDict['891'] = [34.313333,134.056667]
stnDict['892'] = [33.223333,132.555000]
stnDict['893'] = [33.565000,133.551667]
stnDict['894'] = [33.850000,134.096667]
stnDict['895'] = [34.065000,134.576667]
stnDict['897'] = [32.918333,132.696667]
stnDict['898'] = [32.718333,133.011667]
stnDict['899'] = [33.248333,134.180000]
stnDict['909'] = [28.376667,129.498333]
stnDict['912'] = [24.461667,123.010000]
stnDict['918'] = [24.331667,124.163333]
stnDict['927'] = [24.790000,125.278333]
stnDict['929'] = [26.335000,126.805000]
stnDict['936'] = [26.203333,127.688333]
stnDict['940'] = [26.590000,127.968333]
stnDict['942'] = [27.428333,128.706667]
stnDict['945'] = [25.828333,131.226667]
stnDict['971'] = [27.083333,142.183333]
stnDict['991'] = [24.300000,153.966667]

# print(stnDict) 
# stnDict['991'][0]
# stnDict['991'][1]


# read station id
###############################################################################
st_id = []
for i in inpf:#sys.argv[2:anum-1]:
    stni = pd.read_csv(i, nrows=1, header=None)
    st_id.append(stni.iloc[0,0])
#print(st_id)
    

# read first datetime and last datetime
###############################################################################
st_tm0 = []
st_tm1 = []
st_tm2 = []
for i in inpf:#sys.argv[2:anum-1]:
    stnt = pd.read_csv(i, sep=',', skiprows=1, header=None)
    st_tm0.append(len(stnt))
    st_tm1.append(stnt.iloc[0,0])
    st_tm2.append(stnt.iloc[-1,0])
if st_tm1.count(st_tm1[0]) == len(st_tm1):
    print('\nBeging time is '+st_tm1[0]+'.')
    ts_bg = datetime.strptime(st_tm1[0],"%Y-%m-%dT%H:%M:%S")
    # time.strftime("%Y-%m-%d %H:%M:%S", ts_bg)
else:
    raise SystemExit('Beging time not identical, fix input file it manually!')
if st_tm2.count(st_tm2[0]) == len(st_tm2):
    print('Ending time is '+st_tm2[0]+'.')
    ts_ed = datetime.strptime(st_tm2[0], "%Y-%m-%dT%H:%M:%S")  
    # time.strftime("%Y-%m-%d %H:%M:%S", ts_ed)
else:
    raise SystemExit('Ending time not identical, fix input file it manually!')
    
# check missing time
###############################################################################
st_vl = []
ts_lg = (ts_ed - ts_bg).days*24+23
ts_og = np.linspace(time.mktime(ts_bg.timetuple()), time.mktime(ts_ed.timetuple()), ts_lg)
for i in range(len(inpf)):
    stnv = pd.read_csv(inpf[i], sep=',', skiprows=1, header=None)
    ts_ms = ts_lg - st_tm0[i]
    print('  ' + inpf[i] +' is missing ' + str(ts_ms) + ' time value(s).')
    
    ts_cp = np.array([time.mktime(datetime.strptime(j,"%Y-%m-%dT%H:%M:%S").timetuple()) for j in stnv.iloc[:,0]])   
    difference = set(ts_og).symmetric_difference(set(ts_cp))
    list_difference = list(difference)
#    for j in range(ts_ms):
#        print('    ' + str(time.strftime('%Y-%m-%dT%H:%M:%S',time.localtime(list_difference[j]))) + \
#              ' value will be intorpolated ...')
    st_vl_st = []
    for j in range(len(ts_cp)-1):
        cur_time = ts_og[j]
        cur_time_n = ts_og[j+1]
        if cur_time_n in list_difference:
            st_vl_st.append(float(stnv.iloc[j,1]))
            st_vl_st.append(float(st_vl_st[-1]))
        else:
            st_vl_st.append(float(stnv.iloc[j,1]))
    st_vl_st.append(float(stnv.iloc[-1,1]))
    st_vl.append(st_vl_st)
values = np.array(st_vl)

# get station location points from dict
###############################################################################
lonv = np.array([stnDict[str(i)][0] for i in st_id])
latv = np.array([stnDict[str(i)][1] for i in st_id])
points = np.resize([lonv,latv],(2,len(st_id)))
points = np.transpose(points)

# make mesh based on range of lat and lon
###############################################################################
nx, ny = (mesh, mesh)
# (139.145, 140.390) (34.73, 35.88)
#x = np.linspace(min(lonv), max(lonv), nx)
#y = np.linspace(min(latv), max(latv), ny)
y = np.linspace(139.145, 140.390, nx)
x = np.linspace(34.73, 35.88, ny)
xv, yv = np.meshgrid(x, y)

# interpolate values
###############################################################################
zv = []
from scipy.interpolate import griddata
print('    Wait for intorpolation ...')
for k in range(201623,236687):
#for k in range(len(ts_og)):
#for k in range(480):
    grid_z0 = griddata(points, values[:,k], (xv, yv), method='cubic')
    zv.append(grid_z0)
    # print('Making interpolation, '+str(k)+' of '+str(ts_lg)+' ...')
zz = np.array(zv)
zz = zz.clip(min=0)
zz = zz.clip(max=1)
zz = 100 * zz


# set the time Julian date
###############################################################################
juliantime = []
datelist = pd.date_range(start = pd.datetime(ts_bg.year, ts_bg.month, ts_bg.day, ts_bg.hour), \
                         end = pd.datetime(ts_ed.year, ts_ed.month, ts_ed.day, ts_ed.hour), \
                         freq = "H")
#for k in range(len(ts_og)):
#for k in range(480):
for k in range(201623,236687):
#    print(pd.Timestamp(ts_og[ts], unit='s').to_julian_date())
    juliantime.append(datelist[k].to_julian_date()-2400000.5000000)
    

# write netcdf file
###############################################################################
import netCDF4 as nc4
ncout = nc4.Dataset(optf,'w', format='NETCDF4')
print(ncout)

# Creating group in netcdf file
# tempgrp = ncout.createGroup('GWO_DATA')

#Specifying dimensions
time_dim = ncout.createDimension('time', None) # unlimited
lon_dim = ncout.createDimension('lon', len(x))
lat_dim = ncout.createDimension('lat', len(y))
for dim in ncout.dimensions.items():
    print(dim)

# Specifying time
time = ncout.createVariable('time', np.float64, ('time',), fill_value=np.nan)
time.long_name = 'time'
time.units = 'days since 1858-11-17 00:00:00'
time.calendar = 'standard'
time.axis = 'T'
print(time)

# Building variables longitude
lon = ncout.createVariable('lon', np.float32, ('lon',), fill_value=np.nan)
lon.standard_name = 'longitude'
lon.long_name = 'longitude'
lon.units = 'degrees_east'
lon.axis = 'X'
print(lon)

# Building variables longitude
lat = ncout.createVariable('lat', np.float32, ('lat',), fill_value=np.nan)
lat.standard_name = 'latitude'
lat.long_name = 'latitude'
lat.units = 'degrees_north'
lat.axis = 'Y'
print(lat)

# Building variables variable
hum = ncout.createVariable('hum', np.float64, ('time','lon','lat'), fill_value=np.nan)
hum.standard_name = 'humidity'
hum.long_name = 'relative humidity'
hum.units = '%'
hum.axis = 'RH'
print(hum)

# Passing data into variables
time[:] = juliantime
lon[:] = y
lat[:] = x
hum[:,:,:] = zz
print("-- Wrote data, hum.shape is now ", hum.shape)
# read data back from variable (by slicing it), print min and max
print("-- Min/Max values:", hum[:,:,:].min(), hum[:,:,:].max())

#Add global attributes
ncout.type    = 'Meteology File'
ncout.title   = 'Relative humidity'
ncout.institution = 'by Yulong Wang, Sasaki Lab, The University of Tokyo'
ncout.source  = 'Ground Observation Data'
ncout.history = "Created "+datetime.now().strftime("%Y-%m-%d")
ncout.CoordinateProjection ='init=WGS84'

#Closing the dataset
ncout.close()


"""   
#import matplotlib.pyplot as plt
#for k in range(8760):#ts_lg):
#    #plt.imshow(grid_z0.T, extent=(0,1,0,1), origin='lower')
#    CS = plt.contour(yv, xv, zz[k,:,:], 20, linewidths=0.5, colors='k')
#    CS = plt.contourf(yv, xv, zz[k,:,:], 20)
#    plt.colorbar()  # draw colorbar
#    # plot data points.
#    plt.scatter(latv, lonv, c='m', marker='o', s=6, zorder=10)
#    plt.xlim(139.145, 140.390)
#    plt.ylim(34.73, 35.88)
#    plt.title('griddata test (%d points)' % len(points))
#    plt.show()


grid_z0 = griddata(points, values[:,k], (xv, yv), method='nearest')
grid_z0 = griddata(points, values[:,k], (xv, yv), method='linear')
grid_z0 = griddata(points, values[:,k], (xv, yv), method='cubic')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
#plt.imshow(grid_z0.T, extent=(0,1,0,1), origin='lower')
CS = plt.contour(yv, xv, grid_z0, 20, linewidths=0.5, colors='k')
CS = plt.contourf(yv, xv, grid_z0, 20)
plt.colorbar()  # draw colorbar
# plot data points.
plt.scatter(latv, lonv, c='m', marker='o', s=6, zorder=10)
#plt.xlim(139.145, 140.390)
#plt.ylim(34.73, 35.88)

currentAxis = plt.gca()
currentAxis.add_patch(Rectangle((139.7675 - .625, 35.3050 - .6), 1.25, 1.2, fill=None, alpha=1))
plt.title('griddata test (%d points)' % len(points))
plt.show()
"""