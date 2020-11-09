#!/bin/bash

cd ../地形データ_第09系/dem_files/

gdal_merge.py \
-o "depth_0090-05+06+07.tif" \
"depth_0090-05.tif" \
"depth_0090-06.tif" \
"depth_0090-07.tif"

gdal_translate -of NetCDF "depth_0090-05+06+07.tif" ../nc_files/"depth_0090-05+06+07.nc"

gdal_merge.py \
-o "depth_0030-11+12+13+14+15.tif" \
"depth_0030-11.tif" \
"depth_0030-12.tif" \
"depth_0030-13.tif" \
"depth_0030-14.tif" \
"depth_0030-15.tif"

gdal_translate -of NetCDF "depth_0030-11+12+13+14+15.tif" ../nc_files/"depth_0030-11+12+13+14+15.nc"

gdal_merge.py \
-o "depth_0010-16+17+18+19+20+21+22+23.tif" \
"depth_0010-16.tif" \
"depth_0010-17.tif" \
"depth_0010-18.tif" \
"depth_0010-19.tif" \
"depth_0010-20.tif" \
"depth_0010-21.tif" \
"depth_0010-22.tif" \
"depth_0010-23.tif"

gdal_translate -of NetCDF "depth_0010-16+17+18+19+20+21+22+23.tif" ../nc_files/"depth_0010-16+17+18+19+20+21+22+23.nc"