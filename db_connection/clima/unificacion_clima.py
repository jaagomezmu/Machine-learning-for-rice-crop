import glob 
import pandas as pd

# Lectura de todos los archivos de interes
l = [pd.read_csv(filename, sep = "\t") for filename in glob.glob("origen/*.txt")]
df = pd.concat(l, axis=0)
df['Date'] = pd.to_datetime(df['Date'], format = "%d/%M/%Y")
df['Date'] = df['Date'].dt.strftime("%Y-%M-%d")
print(df.info())
df.to_csv("data_climatica_formateada.csv", index = False, sep = ';', header = False)
print("Finalizado")
