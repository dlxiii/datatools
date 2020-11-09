#!/bin/bash

target="../地形データ_第09系"
curent=$(pwd)

mkdir $target/nc_files
cd $target/dem_files

for t in *.tif
do 
gdal_translate -of NetCDF "$t" ../nc_files/"${t%.tif}.nc";
done

cd $curent