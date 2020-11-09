#!/bin/bash

target="../地形データ_第06系/"
curent="pwd"

sh ./dat2csv_06.sh

mkdir $target/dem_files
cd $target/

for f in *.csv
do 
echo "$f"; 
gdal_translate "$f" "${f%.csv}.tif";
done

for t in *.tif
do 
gdalwarp -overwrite "$t" $target/dem_files/"${t%.dat.tif}.tif" -s_srs EPSG:30166 -t_srs EPSG:4326;
rm "$t"
done

cd $curent