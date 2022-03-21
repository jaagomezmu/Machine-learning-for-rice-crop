import pandas as pd
from datetime import datetime, timedelta
lotes_sensores = pd.read_table('lotes_sensores_clima30km.txt', sep=',')
lotes_sensores['fecha_evaluacion'] = pd.to_datetime(lotes_sensores['fecha_evaluacion'], infer_datetime_format=True)
lotes_sensores['fecha_siembra_emergencia'] = pd.to_datetime(lotes_sensores['fecha_siembra_emergencia'], infer_datetime_format=True)
db_without_rain = pd.read_table('db_without_rain.txt', sep = ',')
db_without_rain['date'] = pd.to_datetime(db_without_rain['date'], infer_datetime_format=True)
db_rain = pd.read_table('db_rain.txt', sep = ',')
db_rain['date'] = pd.to_datetime(db_rain['date'], infer_datetime_format=True)
lotes_sensores1 = lotes_sensores.copy()
lotes_sensores1['tmax'] = ''
lotes_sensores1['tmin'] = ''
lotes_sensores1['rhum'] = ''
lotes_sensores1['esol'] = ''
lotes_sensores1['rain'] = ''

# Función tmax, tmin, rhum, esol
def calculo_piricularia():
    datos_resueltos = lotes_sensores1[lotes_sensores1.estacion.notnull()]
    piricularia = datos_resueltos[(datos_resueltos['fecha_evaluacion'].notnull()) & (datos_resueltos['nt_con_piricularia_hoja'].notnull())]
    piricularia = piricularia.sort_values(by=['fecha_evaluacion'])
    for i in range(len(datos_resueltos)):
        filtro_estaciones = db_without_rain[db_without_rain['estacion'] == datos_resueltos['estacion'].iloc[i]]
        for j in range(len(piricularia)):
            beginning = filtro_estaciones[filtro_estaciones['date'] == (piricularia['fecha_evaluacion'].iloc[j] + timedelta(days=-7))].index
            beginning = beginning[0]
            end = filtro_estaciones[filtro_estaciones['date'] == (piricularia['fecha_evaluacion'].iloc[j])].index
            end = end[0]
            process = filtro_estaciones.loc[beginning:end]
            process = process[['tmax','tmin','rhum','esol']]
            media = process.mean()
            index_fill = lotes_sensores[lotes_sensores['id'] == piricularia.iloc[0][0]].index
            index_fill = index_fill[0]
            lotes_sensores1['tmax'].loc[index_fill] = media[0]
            lotes_sensores1['tmin'].loc[index_fill] = media[1]
            lotes_sensores1['rhum'].loc[index_fill] = media[2]
            lotes_sensores1['esol'].loc[index_fill] = media[3]
    return lotes_sensores1

lotes_sensores2 = calculo_piricularia()
lotes_sensores2.to_csv('lotes_sensores_piricularia.txt', index = False)
