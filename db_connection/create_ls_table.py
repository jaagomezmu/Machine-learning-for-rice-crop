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
class LotesSensores(base):
    __tablename__='lotes_sensores'

    id = Column(Integer, primary_key = True)
    evaluador = Column(String)
    anio_db_org = Column(Integer)
    fecha_evaluacion = Column(Date)
    fecha_siembra_emergencia = Column(Date)
    departamento = Column(String)
    municipio = Column(String)
    vereda = Column(String)
    finca = Column(String)
    lote = Column(String)
    propietario = Column(String)
    x_long = Column(Float)
    y_lat = Column(Float)
    edad_dde = Column(Float)
    variedad = Column(String)
    tipo_ciclo_variedad = Column(String)
    etapa_fenologico = Column(Float)
    n_muestreos = Column(Integer)
    n_tallos = Column(Integer)
    nt_con_entorchamiento = Column(Float)
    nt_con_hoja_blanca = Column(Float)
    nt_con_piricularia_hoja = Column(Float)
    sev_piricularia_hoja = Column(Float)
    nt_con_helmitosporium = Column(Float)
    sev_helmitosporium = Column(Float)
    nt_con_rhizoctonia = Column(Float)
    sev_rhizoctonia = Column(Float)
    nt_con_cercospora = Column(Float)
    sev_cercospora = Column(Float)
    nt_con_escaldado = Column(Float)
    sev_escaldado = Column(Float)
    nt_con_mancha_cafe = Column(Float)
    sev_mancha_cafe = Column(Float)
    nt_con_gaeumanomices = Column(Float)
    sev_gaeumanomices = Column(Float)
    nt_con_piricularia_cuello = Column(Float)
    nt_con_sarna_orejas = Column(Float)
    nt_con_complejo_bacterial = Column(Float)
    sev_manchado_grano = Column(Float)
    n_paniculas_m2 = Column(Float)
    porc_vaneamiento_ajustado = Column(Float)
    n_granos_panicula = Column(Float)
    n_granos_llenos_panicula = Column(Float)
    peso_1000_granos_g = Column(Float)
    granos_por_m2 = Column(Float)
    peso_grano_g = Column(Float)
    rend_estimado_kg = Column(Float)
    pr_i_entorchamiento = Column(Float)
    pr_i_hoja_blanca = Column(Float)
    pr_inc_piri_hoja = Column(Float)
    pr_inc_helm_hoja = Column(Float)
    pr_inc_rhizoctonia = Column(Float)
    pr_inc_cercospora = Column(Float)
    pr_inc_escaldado = Column(Float)
    pr_inc_mancha_cafe = Column(Float)
    pr_inc_gaeumanomices = Column(Float)
    pr_inc_piricularia_cuello = Column(Float)
    pr_inc_sarna_orejas = Column(Float)
    pr_inc_complejo_bacterial = Column(Float)
    inc_entorchamiento = Column(Float)
    inc_hoja_blanca = Column(Float)
    inc_piri_hoja = Column(Float)
    inc_helmitosporium = Column(Float)
    inc_rhizoctonia = Column(Float)
    inc_cercospora = Column(Float)
    inc_escaldado = Column(Float)
    inc_mancha_cafe = Column(Float)
    inc_gaeumanomices = Column(Float)
    inc_piricularia_cuello = Column(Float)
    inc_sarna_orejas = Column(Float)
    inc_complejo_bacterial = Column(Float)

Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)
