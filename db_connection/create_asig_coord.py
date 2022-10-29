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
class Asignacion(base):
    __tablename__='asignacion_coordenadas'

    id = Column(Integer, primary_key = True)
    estacion = Column(String)
    dist_km = Column(Float)
    llave = Column(String)
    altitud_estacion = Column(Integer)
    altitud_lote_sensor = Column(Integer)
    dif_altitud = Column(Integer)
    union_estacion_lote = Column(String)

Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

