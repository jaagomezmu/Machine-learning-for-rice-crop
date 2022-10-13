from os import (
    listdir,
)
from os.path import (
    isfile,
    join
)
import glob 
import pandas as pd

# Listar los nombres de los archivos por concatenar
#onlyfiles = [f for f in listdir("origen/") if isfile(join("origen/", f))]
#print(onlyfiles)

# Lectura de todos los archivos de interes
l = [pd.read_csv(filename) for filename in glob.glob("origen/*.txt")]
df = pd.concat(l, axis=0)
df.to_csv("data_climatica.csv", index = False)
