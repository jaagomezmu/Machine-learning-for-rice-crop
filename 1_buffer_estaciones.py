import numpy as np
import pandas as pd
import geopandas as gpd
# Carga de datos
lotes_sensores = pd.read_table('lotes_sensores.txt', sep=',')
estaciones = pd.read_excel('estaciones_climaticas.xlsx')
estaciones = estaciones.drop(0, axis=1)
# Creación de poligonos
gdf_estaciones = gpd.GeoDataFrame(estaciones,geometry=gpd.points_from_xy(estaciones.x,estaciones.y)).set_crs(epsg=4326)
gdf_lotes_sensores = gpd.GeoDataFrame(lotes_sensores,geometry=gpd.points_from_xy(lotes_sensores.x_long,lotes_sensores.y_lat)).set_crs(epsg=4326)
# Project a GeoDataFrame
gdf_estaciones_10km = gdf_estaciones.to_crs(epsg=21818)
gdf_estaciones_30km = gdf_estaciones.to_crs(epsg=21818)
gdf_lotes_sensores = gdf_lotes_sensores.to_crs(epsg=21818)
# validation
# gdf_lotes_sensores.to_file('validar_lotes_sensores.geojson')
# Buffer
gdf_estaciones_10km.geometry = gdf_estaciones_10km.geometry.buffer(10000)
gdf_estaciones_30km.geometry = gdf_estaciones_30km.geometry.buffer(30000)
# Para el buffer de 10 km
lotes_sensores_clima10km = gpd.sjoin(gdf_lotes_sensores,gdf_estaciones_10km,how='left')
lotes_sensores_clima10km = lotes_sensores_clima10km.drop(['geometry','x','y'],axis = 1)
lotes_sensores_clima10km.to_csv('lotes_sensores_clima10km.txt', index = False)
# Para el buffer de 30 km
lotes_sensores_clima30km = gpd.sjoin(gdf_lotes_sensores,gdf_estaciones_30km,how='left')
lotes_sensores_clima30km = lotes_sensores_clima30km.drop(['geometry','x','y'],axis = 1)
lotes_sensores_clima30km.to_csv('lotes_sensores_clima30km.txt', index = False)
# Validation
# gdf_estaciones_10km.to_file('validar_buffer_10km.geojson')
# gdf_estaciones_30km.to_file('validar_buffer_30km.geojson')