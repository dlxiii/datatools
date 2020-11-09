#!/bin/bash

# './kawaguchiko/1991-2017_wind.csv' \
python stn2uwnd.py 10 './ajiro/1991-2017_wind.csv' \
'./chiba/1991-2017_wind.csv' \
'./chichibu/1991-2017_wind.csv' \
'./choshi/1991-2017_wind.csv' \
'./irozaki/1991-2017_wind.csv' \
'./katsuura/1991-2017_wind.csv' \
'./kofu/1991-2017_wind.csv' \
'./kumagaya/1991-2017_wind.csv' \
'./maebashi/1991-2017_wind.csv' \
'./mishima/1991-2017_wind.csv' \
'./mito/1991-2017_wind.csv' \
'./miyakejima/1991-2017_wind.csv' \
'./oshima/1991-2017_wind.csv' \
'./tateno/1991-2017_wind.csv' \
'./tateyama/1991-2017_wind.csv' \
'./tokyo/1991-2017_wind.csv' \
'./utsunomiya/1991-2017_wind.csv' \
'./yokohama/1991-2017_wind.csv' \
'./chichijima/1991-2017_wind.csv' \
'./2014-2017_uwnd.nc'

python stn2vwnd.py 10 './ajiro/1991-2017_wind.csv' \
'./chiba/1991-2017_wind.csv' \
'./chichibu/1991-2017_wind.csv' \
'./choshi/1991-2017_wind.csv' \
'./irozaki/1991-2017_wind.csv' \
'./katsuura/1991-2017_wind.csv' \
'./kofu/1991-2017_wind.csv' \
'./kumagaya/1991-2017_wind.csv' \
'./maebashi/1991-2017_wind.csv' \
'./mishima/1991-2017_wind.csv' \
'./mito/1991-2017_wind.csv' \
'./miyakejima/1991-2017_wind.csv' \
'./oshima/1991-2017_wind.csv' \
'./tateno/1991-2017_wind.csv' \
'./tateyama/1991-2017_wind.csv' \
'./tokyo/1991-2017_wind.csv' \
'./utsunomiya/1991-2017_wind.csv' \
'./yokohama/1991-2017_wind.csv' \
'./chichijima/1991-2017_wind.csv' \
'./2014-2017_vwnd.nc'

# './kawaguchiko/1991-2017_temp.csv' \
python stn2air.py 10 './ajiro/1991-2017_temp.csv' \
'./chiba/1991-2017_temp.csv' \
'./chichibu/1991-2017_temp.csv' \
'./choshi/1991-2017_temp.csv' \
'./irozaki/1991-2017_temp.csv' \
'./katsuura/1991-2017_temp.csv' \
'./kofu/1991-2017_temp.csv' \
'./kumagaya/1991-2017_temp.csv' \
'./maebashi/1991-2017_temp.csv' \
'./mishima/1991-2017_temp.csv' \
'./mito/1991-2017_temp.csv' \
'./miyakejima/1991-2017_temp.csv' \
'./oshima/1991-2017_temp.csv' \
'./tateno/1991-2017_temp.csv' \
'./tateyama/1991-2017_temp.csv' \
'./tokyo/1991-2017_temp.csv' \
'./utsunomiya/1991-2017_temp.csv' \
'./yokohama/1991-2017_temp.csv' \
'./chichijima/1991-2017_temp.csv' \
'./2014-2017_air.nc'

# './kawaguchiko/1991-2017_clod.csv' \
python stn2cld.py 10 './ajiro/1991-2017_clod.csv' \
'./chiba/1991-2017_clod.csv' \
'./chichibu/1991-2017_clod.csv' \
'./choshi/1991-2017_clod.csv' \
'./irozaki/1991-2017_clod.csv' \
'./katsuura/1991-2017_clod.csv' \
'./kofu/1991-2017_clod.csv' \
'./kumagaya/1991-2017_clod.csv' \
'./maebashi/1991-2017_clod.csv' \
'./mishima/1991-2017_clod.csv' \
'./mito/1991-2017_clod.csv' \
'./miyakejima/1991-2017_clod.csv' \
'./oshima/1991-2017_clod.csv' \
'./tateno/1991-2017_clod.csv' \
'./tateyama/1991-2017_clod.csv' \
'./tokyo/1991-2017_clod.csv' \
'./utsunomiya/1991-2017_clod.csv' \
'./yokohama/1991-2017_clod.csv' \
'./chichijima/1991-2017_clod.csv' \
'./2014-2017_cld.nc'

# './kawaguchiko/1991-2017_rhum.csv' \
python stn2hum.py 10 './ajiro/1991-2017_rhum.csv' \
'./chiba/1991-2017_rhum.csv' \
'./chichibu/1991-2017_rhum.csv' \
'./choshi/1991-2017_rhum.csv' \
'./irozaki/1991-2017_rhum.csv' \
'./katsuura/1991-2017_rhum.csv' \
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
'./chichijima/1991-2017_rhum.csv' \
'./2014-2017_hum.nc'

# './kawaguchiko/1991-2017_prec.csv' \
python stn2rin.py 10 './ajiro/1991-2017_prec.csv' \
'./chiba/1991-2017_prec.csv' \
'./chichibu/1991-2017_prec.csv' \
'./choshi/1991-2017_prec.csv' \
'./irozaki/1991-2017_prec.csv' \
'./katsuura/1991-2017_prec.csv' \
'./kofu/1991-2017_prec.csv' \
'./kumagaya/1991-2017_prec.csv' \
'./maebashi/1991-2017_prec.csv' \
'./mishima/1991-2017_prec.csv' \
'./mito/1991-2017_prec.csv' \
'./miyakejima/1991-2017_prec.csv' \
'./oshima/1991-2017_prec.csv' \
'./tateno/1991-2017_prec.csv' \
'./tateyama/1991-2017_prec.csv' \
'./tokyo/1991-2017_prec.csv' \
'./utsunomiya/1991-2017_prec.csv' \
'./yokohama/1991-2017_prec.csv' \
'./chichijima/1991-2017_prec.csv' \
'./2014-2017_rin.nc'

# ./kawaguchiko/1991-2017_pres.csv' \
python stn2prs.py 10 './ajiro/1991-2017_pres.csv' \
'./chiba/1991-2017_pres.csv' \
'./chichibu/1991-2017_pres.csv' \
'./choshi/1991-2017_pres.csv' \
'./irozaki/1991-2017_pres.csv' \
'./katsuura/1991-2017_pres.csv' \
'./kofu/1991-2017_pres.csv' \
'./kumagaya/1991-2017_pres.csv' \
'./katsuura/1991-2017_pres.csv' \
'./maebashi/1991-2017_pres.csv' \
'./mishima/1991-2017_pres.csv' \
'./mito/1991-2017_pres.csv' \
'./miyakejima/1991-2017_pres.csv' \
'./oshima/1991-2017_pres.csv' \
'./tateno/1991-2017_pres.csv' \
'./tateyama/1991-2017_pres.csv' \
'./tokyo/1991-2017_pres.csv' \
'./utsunomiya/1991-2017_pres.csv' \
'./yokohama/1991-2017_pres.csv' \
'./chichijima/1991-2017_pres.csv' \
'./2014-2017_prs.nc'

# './ajiro/1991-2017_dswr.csv'
# './chiba/1991-2017_dswr.csv' \
# './chichibu/1991-2017_dswr.csv' \
# './irozaki/1991-2017_dswr.csv' \
# './katsuura/1991-2017_dswr.csv' \
# './kawaguchiko/1991-2017_dswr.csv' \
# './kumagaya/1991-2017_dswr.csv' \
# './mishima/1991-2017_dswr.csv' \
# './mito/1991-2017_dswr.csv' \
# './miyakejima/1991-2017_dswr.csv' \
# './tateyama/1991-2017_dswr.csv' \
# './yokohama/1991-2017_dswr.csv' \
# './oshima/1991-2017_dswr.csv' \
python stn2dsw.py 10 './chichijima/1991-2017_dswr.csv' \
'./choshi/1991-2017_dswr.csv' \
'./kofu/1991-2017_dswr.csv' \
'./maebashi/1991-2017_dswr.csv' \
'./tateno/1991-2017_dswr.csv' \
'./tokyo/1991-2017_dswr.csv' \
'./utsunomiya/1991-2017_dswr.csv' \
'./2014-2017_dsw.nc'