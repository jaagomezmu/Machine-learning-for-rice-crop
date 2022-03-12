# %%
import pandas as pd
import glob
import warnings
warnings.filterwarnings("ignore")
my_files_path = glob.glob(r'C:/Users/javie/Desktop/ProyectoArroz/Bases_datos_climaticas/*.txt')

# %%
# Creating a file upload function
def file_upload(path):
    df = pd.read_table(path)
    df.columns = df.columns.str.lower()
    df = df.rename(columns = {'estacio':'estacion'})
    df['estacion'] = df['estacion'].astype(str) + '-' + df['nombre_estacion'].astype(str)
    df = df[['estacion','date', 'rain', 'tmax', 'tmin', 'rhum', 'esol', 'x', 'y', 'modif']]
    df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True)
    if df['x'][0] > 0:
        df = df.rename(columns = {'y':'x','x':'y'})
    df['estacion'] = df['estacion'].astype(str)
    df['rain'] = df['rain'].astype(float)
    df['tmax'] = df['tmax'].astype(float)
    df['tmin'] = df['tmin'].astype(float)
    df['rhum'] = df['rhum'].astype(float)
    df['esol'] = df['esol'].astype(float)
    df['x'] = df['x'].astype(float)
    df['y'] = df['y'].astype(float)
    df['modif'] = df['modif'].astype(str)
    return df

# %%
db_clim = pd.DataFrame()
for tabla in my_files_path:
    prueba = file_upload(tabla)
    db_clim = pd.concat([db_clim,prueba])


# %%
db_clim[['estacion','date','rain','x','y','modif']].to_csv('db_rain.csv',index = False)
db_clim[['estacion','date','tmax','tmin','rhum','esol','x','y','modif']].to_csv('db_withouth_rain.csv',index = False)