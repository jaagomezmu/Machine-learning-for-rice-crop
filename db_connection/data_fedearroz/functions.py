import pandas as pd
import numpy as np

def file_upload_brigadas(path):
    """
    En esta funcion se garantiza el cargue y casteo de la informacion 
    con la que se va a trabajar

    argumentos: la ruta del archivo
    salida: la base de datos de brigadas fitosanitarias.

    """

    df = pd.read_excel(path)
    df.columns = df.columns.str.lower()
    # Casteo columnas de enteros
    df['id_registro'] = pd.to_numeric(df['id_registro'], downcast = 'integer')
    df['anio_bd'] = pd.to_numeric(df['anio_bd'], downcast='integer')
    df['mes_siembra_est'] = pd.to_numeric(df['mes_siembra_est'], downcast='integer') 
    df['mes_cosecha'] = pd.to_numeric(df['mes_cosecha'], downcast='integer') 
    df['edad_dde'] = pd.to_numeric(df['edad_dde'], downcast='integer') 
    df['puntos_eval'] = pd.to_numeric(df['puntos_eval'], downcast='integer')
    # Casteo columnas con flotantes
    df['x_long'] = pd.to_numeric(df['x_long'], downcast='float')
    df['y_lat'] = pd.to_numeric(df['y_lat'], downcast='float')
    df['inc_rhizoctonia'] = pd.to_numeric(df['inc_rhizoctonia'], downcast='float')
    df['inc_piricularia'] = pd.to_numeric(df['inc_piricularia'], downcast='float')
    df['inc_gaeumanomices'] = pd.to_numeric(df['inc_gaeumanomices'], downcast='float')
    df['inc_helmitosporium'] = pd.to_numeric(df['inc_helmitosporium'], downcast='float')
    df['inc_barrenador'] = pd.to_numeric(df['inc_barrenador'], downcast='float')
    # df.drop('inc_barrenador', axis = 1, inplace=True) Se modifico para que corra de la version de las variedades
    df['inc_mancha_cafe'] = pd.to_numeric(df['inc_mancha_cafe'], downcast='float')
    df['sev_mancha_cafe'] = pd.to_numeric(df['sev_mancha_cafe'], downcast='float')
    df['inc_complejo_bacteriano'] = pd.to_numeric(df['inc_complejo_bacteriano'], downcast='float')
    df['frec_sspinki_acaro'] = pd.to_numeric(df['frec_sspinki_acaro'], downcast='float')
    df['porc_vaneamiento'] = pd.to_numeric(df['porc_vaneamiento'], downcast='float')
    # Casteo de columnas de cadenas
    df[['codigo','semestre_ajustado','zona','departamento','municipio','vereda','finca','lote','variedad','propietario']] = df[['codigo','semestre_ajustado','zona','departamento','municipio','vereda','finca','lote','variedad','propietario']].values.astype(str)
    # Casteo de columnas con fechas
    df['fecha_siembra_est'] = pd.to_datetime(df['fecha_siembra_est'], infer_datetime_format=True)
    df['fecha_cosecha_est'] = pd.to_datetime(df['fecha_cosecha_est'], infer_datetime_format=True)
    # Calculo de formulas
    df['pr_rhizoctonia'] = np.where(df['inc_rhizoctonia']> 0,1,np.where(df['inc_rhizoctonia'] <= 0,0,None))
    df['pr_piricularia'] = np.where(df['inc_piricularia']> 0,1,np.where(df['inc_piricularia'] <= 0,0,None))
    df['pr_gaeumanomices'] = np.where(df['inc_gaeumanomices']> 0,1,np.where(df['inc_gaeumanomices'] <= 0,0,None))
    df['pr_helmitosporium'] = np.where(df['inc_helmitosporium']> 0,1,np.where(df['inc_helmitosporium'] <= 0,0,None))
    df['pr_barrenador'] = np.where(df['inc_barrenador']> 0,1,np.where(df['inc_barrenador'] <= 0,0,None))
    df['pr_mancha_cafe'] = np.where(df['inc_mancha_cafe']> 0,1,np.where(df['inc_mancha_cafe'] <= 0,0,None))
    df['pr_complejo_bacteriano'] = np.where(df['inc_complejo_bacteriano']> 0,1,np.where(df['inc_complejo_bacteriano'] <= 0,0,None))
    return df

def file_upload_sensores(path):
    """
     En esta funcion se garantiza el cargue y casteo de la informacion
    con la que se va a trabajar

    argumentos: la ruta del archivo
    salida: la base de datos de lotes sensores

    """
    df = pd.read_excel(path)
    df.columns = df.columns.str.lower()
    # Casteo columnas de enteros
    df['id'] = pd.to_numeric(df['id'], downcast = 'integer')
    df['anio_db_org'] = pd.to_numeric(df['anio_db_org'], downcast = 'integer')
    df['edad_dde'] = pd.to_numeric(df['edad_dde'], downcast = 'integer')
    df['etapa_fenologica'] = pd.to_numeric(df['etapa_fenologica'], downcast = 'integer')
    df['n_muestreos'] = pd.to_numeric(df['n_muestreos'], downcast = 'integer')
    df['n_tallos'] = pd.to_numeric(df['n_tallos'], downcast = 'integer')
    df['nt_con_entorchamiento'] = pd.to_numeric(df['nt_con_entorchamiento'], downcast = 'integer')
    df[ 'nt_con__hoja_blanca'] = pd.to_numeric(df[ 'nt_con__hoja_blanca'], downcast = 'integer')
    df['nt_con_piricularia_hoja'] = pd.to_numeric(df['nt_con_piricularia_hoja'], downcast = 'integer')
    df['sev_piricularia_hoja'] = pd.to_numeric(df['sev_piricularia_hoja'], downcast = 'integer')
    df['nt_con_helmitosporium'] = pd.to_numeric(df['nt_con_helmitosporium'], downcast = 'integer')
    df['sev_helmitosporium'] = pd.to_numeric(df['sev_helmitosporium'], downcast = 'integer')
    df['nt_con_rhizoctonia'] = pd.to_numeric(df['nt_con_rhizoctonia'], downcast = 'integer')
    df['sev_rhizoctonia'] = pd.to_numeric(df['sev_rhizoctonia'], downcast = 'integer')
    df['nt_con_cercospora'] = pd.to_numeric(df['nt_con_cercospora'], downcast = 'integer')
    df['sev_cercospora'] = pd.to_numeric(df['sev_cercospora'], downcast = 'integer')
    df['nt_con_escaldado'] = pd.to_numeric(df['nt_con_escaldado'], downcast = 'integer')
    df['sev_escaldado'] = pd.to_numeric(df['sev_escaldado'], downcast = 'integer')
    df['nt_con_mancha_cafe'] = pd.to_numeric(df['nt_con_mancha_cafe'], downcast = 'integer')
    df['sev_mancha_cafe'] = pd.to_numeric(df['sev_mancha_cafe'], downcast = 'integer')
    df['nt_con_gaeumanomices'] = pd.to_numeric(df['nt_con_gaeumanomices'], downcast = 'integer')
    df['sev_gaeumanomices'] = pd.to_numeric(df['sev_gaeumanomices'], downcast = 'integer')
    df['nt_con_piricularia_cuello'] = pd.to_numeric(df['nt_con_piricularia_cuello'], downcast = 'integer')
    df['nt_con_sarna_orejas'] = pd.to_numeric(df['nt_con_sarna_orejas'], downcast = 'integer')
    df['nt_con_complejo_bacterial'] = pd.to_numeric(df['nt_con_complejo_bacterial'], downcast = 'integer')
    df['sev_manchado_grano'] = pd.to_numeric(df['sev_manchado_grano'], downcast = 'integer')
    df['n_paniculas_m2'] = pd.to_numeric(df['n_paniculas_m2'], downcast = 'integer')
    df['porc_vaneamiento_ajustado'] = pd.to_numeric(df['porc_vaneamiento_ajustado'], downcast = 'integer')
    df['n_ granos_panicula'] = pd.to_numeric(df['n_ granos_panicula'], downcast = 'integer')
    df['n_ granos_llenos_panicula'] = pd.to_numeric(df['n_ granos_llenos_panicula'], downcast = 'integer')
    df['peso _1000 _granos_g'] = pd.to_numeric(df['peso _1000 _granos_g'], downcast = 'integer')
    df['granos_por m2'] = pd.to_numeric(df['granos_por m2'], downcast = 'integer')
    df['peso_grano_g'] = pd.to_numeric(df['peso_grano_g'], downcast = 'integer')
    df['rend_estimado_kg'] = pd.to_numeric(df['rend_estimado_kg'], downcast = 'integer')
    # Casteo de columnas de flotantes
    df['x_long'] =pd.to_numeric(df['x_long'],downcast='float')
    df['y_lat'] =pd.to_numeric(df['y_lat'],downcast='float')
    # Casteo de columnas de cadenas
    df[['codigo','evaluador','departamento','municipio','vereda','finca','lote','propietario','variedad',
        'tipo_ciclo_variedad']] = df[['codigo','evaluador','departamento','municipio','vereda','finca','lote','propietario','variedad','tipo_ciclo_variedad']].values.astype(str)
    # Casteo de columnas con fechas
    df['fecha_evaluacion'] = pd.to_datetime(df['fecha_evaluacion'], infer_datetime_format=True)
    df['fecha_siembra_emergencia'] = pd.to_datetime(df['fecha_siembra_emergencia'], infer_datetime_format=True)
    # Calculo de formulas
    df['pr_i_entorchamiento'] = np.where(df['nt_con_entorchamiento'] > 0,1,np.where(df['nt_con_entorchamiento'] <= 0,0,None))
    df['pr_i_entorchamiento'] = pd.to_numeric(df['pr_i_entorchamiento'], downcast = 'integer')
    df['pr_i_hoja blanca'] = np.where(df['nt_con__hoja_blanca'] > 0,1,np.where(df['nt_con__hoja_blanca'] <= 0,0,None))
    df['pr_i_hoja blanca'] = pd.to_numeric(df['pr_i_hoja blanca'], downcast = 'integer')
    df['pr_inc_piri_hoja'] = np.where(df['nt_con_piricularia_hoja'] > 0,1,np.where(df['nt_con_piricularia_hoja'] <= 0,0,None))
    df['pr_inc_piri_hoja'] = pd.to_numeric(df['pr_inc_piri_hoja'], downcast = 'integer')
    df['pr_inc_helm_hoja'] = np.where(df['nt_con_helmitosporium'] > 0,1,np.where(df['nt_con_helmitosporium'] <= 0,0,None))
    df['pr_inc_helm_hoja'] = pd.to_numeric(df['pr_inc_helm_hoja'], downcast = 'integer')
    df['pr_inc_rhizoctonia'] = np.where(df['nt_con_rhizoctonia'] > 0,1,np.where(df['nt_con_rhizoctonia'] <= 0,0,None))
    df['pr_inc_rhizoctonia'] = pd.to_numeric(df['pr_inc_rhizoctonia'], downcast = 'integer')
    df['pr_inc_cercospora'] = np.where(df['nt_con_cercospora'] > 0,1,np.where(df['nt_con_cercospora'] <= 0,0,None))
    df['pr_inc_cercospora'] = pd.to_numeric(df['pr_inc_cercospora'], downcast = 'integer')
    df['pr_inc_escaldado'] = np.where(df['nt_con_escaldado'] > 0,1,np.where(df['nt_con_escaldado'] <= 0,0,None))
    df['pr_inc_escaldado'] = pd.to_numeric(df['pr_inc_escaldado'], downcast = 'integer')
    df['pr_inc_mancha_cafe'] = np.where(df['nt_con_mancha_cafe'] > 0,1,np.where(df['nt_con_mancha_cafe'] <= 0,0,None))
    df['pr_inc_mancha_cafe'] = pd.to_numeric(df['pr_inc_mancha_cafe'], downcast = 'integer')
    df['pr_inc_gaeumanomices'] = np.where(df['nt_con_gaeumanomices'] > 0,1,np.where(df['nt_con_gaeumanomices'] <= 0,0,None))
    df['pr_inc_gaeumanomices'] = pd.to_numeric(df['pr_inc_gaeumanomices'], downcast = 'integer')
    df['pr_inc_piricularia_cuello'] = np.where(df['nt_con_piricularia_cuello'] > 0,1,np.where(df['nt_con_piricularia_cuello'] <= 0,0,None))
    df['pr_inc_piricularia_cuello'] = pd.to_numeric(df['pr_inc_piricularia_cuello'], downcast = 'integer')
    df['pr_inc_sarna_orejas'] = np.where(df['nt_con_sarna_orejas'] > 0,1,np.where(df['nt_con_sarna_orejas'] <= 0,0,None))
    df['pr_inc_sarna_orejas'] = pd.to_numeric(df['pr_inc_sarna_orejas'], downcast = 'integer')
    df['pr_inc_complejo_bacterial'] = np.where(df['nt_con_complejo_bacterial'] > 0,1,np.where(df['nt_con_complejo_bacterial'] <= 0,0,None))
    df['pr_inc_complejo_bacterial'] = pd.to_numeric(df['pr_inc_complejo_bacterial'], downcast = 'integer')
    # Calculo de las incidencias
    df['inc_entorchamiento'] = np.where(df['n_tallos'] < df['nt_con_entorchamiento'], 1, (df['nt_con_entorchamiento']/df['n_tallos']))
    df['inc_hoja blanca'] = np.where(df['n_tallos'] < df['nt_con__hoja_blanca'],1, df['nt_con__hoja_blanca']/df['n_tallos'])
    df['inc_piri_hoja'] = np.where(df['n_tallos'] < df['nt_con_piricularia_hoja'],1,df['nt_con_piricularia_hoja']/df['n_tallos'])
    df['inc_helmitosporium'] = np.where(df['n_tallos'] < df['nt_con_helmitosporium'],1,df['nt_con_helmitosporium']/df['n_tallos'])
    df['inc_rhizoctonia'] = np.where(df['n_tallos'] < df['nt_con_rhizoctonia'],1,df['nt_con_rhizoctonia']/df['n_tallos'])
    df['inc_cercospora'] = np.where(df['n_tallos'] < df['nt_con_cercospora'],1,df['nt_con_cercospora']/df['n_tallos'])
    df['inc_escaldado'] = np.where(df['n_tallos'] < df['nt_con_escaldado'],1,df['nt_con_escaldado']/df['n_tallos'])
    df['inc_mancha_cafe'] = np.where(df['n_tallos'] < df['nt_con_mancha_cafe'],1,df['nt_con_mancha_cafe']/df['n_tallos'])
    df['inc_gaeumanomices'] = np.where(df['n_tallos'] < df['nt_con_gaeumanomices'],1,df['nt_con_gaeumanomices']/df['n_tallos'])
    df['inc_piricularia_cuello'] = np.where(df['n_tallos'] < df['nt_con_piricularia_cuello'], 1 ,df['nt_con_piricularia_cuello']/df['n_tallos'])
    df['inc_sarna_orejas'] = np.where(df['n_tallos'] < df['nt_con_sarna_orejas'],1,df['nt_con_sarna_orejas']/df['n_tallos'])
    df['inc_complejo_bacterial'] = np.where(df['n_tallos'] < df['nt_con_complejo_bacterial'],1,df['nt_con_complejo_bacterial']/df['n_tallos'])
    # Se suprimen los registros donde los valores donde la variedad es nula
    df = df[df['variedad'] != 'nan']
    # Se castean los nulos
    df = df.fillna(value=np.nan)
    return df

def media_ponderada_ls(lotes_sensores,enfermedad = 'sev_piricularia_hoja'):
    """
    Esta funcion calcula los pesos relativos de acuerdo con el argumento de 
    enfermedad, luego calcula su media ponderada.

    Las entradas son: 
        - dataframe de Lotes sensores
        - la enfermedad de acuerdo a la columna de lotes sensores; revisar los requerimientos.

    """
    # Correccion de los años == 2015
    lotes_sensores.loc[lotes_sensores['fecha_siembra_emergencia'].dt.year == 2015, 'anio_db_org'] = 2015
    # Filtro de lotes sensores por la enfermedad y columnas de interes ['anio_db_org', 'departamento', 'variedad', 'etapa_fenologica']
    df_ls = lotes_sensores[['anio_db_org', 'departamento', 'variedad', 'etapa_fenologica',enfermedad]]  
    # generate a table of those rows which are duplicated:
    dups = df_ls.groupby(df_ls.columns.tolist()).size().reset_index().rename(columns={0:'count'})
    # generate weighted average
    weighted_avg = round(np.average(dups[enfermedad], weights = dups['count']),2)

    return enfermedad,weighted_avg, dups

def media_ponderada_bf(brigadas_fitosanitarias,enfermedad = 'inc_rhizoctonia'):
    """
    Esta funcion calcula los pesos relativos de acuerdo con el argumento de 
    enfermedad, luego calcula su media ponderada.

    Las entradas son: 
        - dataframe de brigadas fitosanitarias
        - la enfermedad de acuerdo a la columna de lotes sensores; revisar los requerimientos.

    """
    # Filtro de lotes sensores por la enfermedad y columnas de interes ['anio_bd', 'departamento', 'variedad_ajustada']
    df_bf = brigadas_fitosanitarias[['anio_bd', 'departamento', 'variedad_ajustada',enfermedad]]  
    # generate a table of those rows which are duplicated:
    dups = df_bf.groupby(df_bf.columns.tolist()).size().reset_index().rename(columns={0:'count'})
    # generate weighted average
    weighted_avg = round(np.average(dups[enfermedad], weights = dups['count']),2)

    return enfermedad,weighted_avg, dups
    
