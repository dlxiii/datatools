#!/bin/bash

target="../地形データ_第09系"
curent=$(pwd)

mkdir $target/slp_files
cd $target/dem_files

for t in *.tif
do 
gdaldem slope -p -s 111120 "$t" ../slp_files/"${t%.tif}_slp.tif";
# gdaldem slope -s 111120 "$t" ../slp_files/"${t%.tif}_temp.tif";
# gdal_translate -of GTiff -gcp 139.829 -35.5383 139.826 35.5416 -gcp 139.805 -35.521 139.802 35.5246 -gcp 139.812 -35.5357 139.809 35.5388 -gcp 139.892 -35.6188 139.888 35.6218 -gcp 139.795 -35.5906 139.792 35.5939 -gcp 139.839 -35.6091 139.836 35.6125 -gcp 139.844 -35.6447 139.841 35.6479 -gcp 139.943 -35.6374 139.94 35.6407 -gcp 139.89 -35.6612 139.887 35.6645 -gcp 139.876 -35.6298 139.872 35.633 -gcp 139.853 -35.6394 139.85 35.6428 ../slp_files/"${t%.tif}_temp.tif" ../slp_files/"${t%.tif}_temp_temp.tif" 
# gdalwarp -r near -order 1 -co COMPRESS=NONE -t_srs EPSG:4326 ../slp_files/"${t%.tif}_temp_temp.tif" ../slp_files/"${t%.tif}_slp.tif" 
# rm ../slp_files/"${t%.tif}_temp.tif" 
# rm ../slp_files/"${t%.tif}_temp_temp.tif" 
done

cd $curent