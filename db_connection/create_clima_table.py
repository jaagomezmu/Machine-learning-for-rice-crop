from decouple import (
    config
)
from sqlalchemy import (
    create_engine as ce,
    Column,
    Date,
    Float,
    Integer,
    String,
)
from sqlalchemy.ext.declarative import (
    declarative_base,
)
from sqlalchemy.orm import (
    sessionmaker
)

SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI')
print(SQLALCHEMY_DATABASE_URI)

# Create the db engine for file database
db = ce(SQLALCHEMY_DATABASE_URI)
base = declarative_base()
print("Se creo exitosamente el motor de la base de datos")

## Creacion de la tabla de clima
class Clima(base):
    __tablename__='clima_tt'

    id = Column(Integer, primary_key = True)
    date = Column(Date)
    rain = Column(Float)
    rain_days = Column(Float)
    tmax = Column(Float)
    tmin = Column(Float)
    tmean = Column(Float)
    tt = Column(Float)
    t_dew_point = Column(Float)
    vapor_pressure_deficit = Column(Float)
    rhum = Column(Float)
    esol = Column(Float)
    month = Column(String)
    year = Column(Integer)
    modif = Column(String)
    x = Column(Float)
    y = Column(Float)
    station = Column(String)

Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

