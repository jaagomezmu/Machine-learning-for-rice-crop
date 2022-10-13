from collections import (
    namedtuple
)
from datetime import (
    datetime,
    timedelta
)
from decouple import (
    config
)
from sqlalchemy import (
    create_engine as ce
)
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker
)
from sqlalchemy.types import (
    Integer,
    Text,
    DateTime
)
import numpy as np
import pandas as pd
import pytz

SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI')
# print(SQLALCHEMY_DATABASE_URI)

# Create the db engine for file database
engine = ce(SQLALCHEMY_DATABASE_URI)
db = scoped_session(sessionmaker(bind=engine))

# Settings
pd.set_option('display.max_columns', None)

# UTC zone settings
tz = pytz.timezone('America/Bogota')
today = datetime.now(tz)

# Function QueryTool
def model_tool(sql):

    """
    Esta función ejecuta un sql a la base de datos arroz db
    Parametros: sql como cadena de texto
    Salida: Dataframe pandas con los resultados
    """
    try:
        result = db.execute(sql)
        print('SQL Finalizado')
        
    except Exception as e:
        print(e)
        db.rollback()
        return pd.DataFrame({"hubo":["error"],"un":["grave"]})
    else:
        db.commit()
        return resultados_df
    finally:
        db.close()

## Creacion de la tabla de clima
tabla_clima = """
CREATE TABLE 'clima' (
    'id' int NOT NULL AUTO_INCREMENT,
    'date' datetime, 
    'rain' float, 
    'rain_days' int,
    'tmax' float, 
    'tmin' float,
    'tmean' float,
    't_dew_point' float,
    'vapor_pressure_deficit' float,
    'rhum' float,
    'esol' float,
    'month'  text,
    'year' integer,
    'modif' text,
    'x' float,
    'y' float,
    'station' text,
    PRIMARY KEY ('id')
);
"""

model_tool(tabla_clima)