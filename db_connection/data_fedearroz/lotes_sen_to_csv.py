from functions import *
lotes_sensores = file_upload_sensores("lotes_sensores_base_completa_MODELS_FEB_2022_copia.xlsx")
# print(lotes_sensores.columns)
lotes_sensores = lotes_sensores[['evaluador', 'anio_db_org', 'fecha_evaluacion',
       'fecha_siembra_emergencia', 'departamento', 'municipio', 'vereda',
       'finca', 'lote', 'propietario', 'x_long', 'y_lat', 'edad_dde',
       'variedad', 'tipo_ciclo_variedad', 'etapa_fenologica', 'n_muestreos',
       'n_tallos', 'nt_con_entorchamiento', 'nt_con__hoja_blanca',
       'nt_con_piricularia_hoja', 'sev_piricularia_hoja',
       'nt_con_helmitosporium', 'sev_helmitosporium', 'nt_con_rhizoctonia',
       'sev_rhizoctonia', 'nt_con_cercospora', 'sev_cercospora',
       'nt_con_escaldado', 'sev_escaldado', 'nt_con_mancha_cafe',
       'sev_mancha_cafe', 'nt_con_gaeumanomices', 'sev_gaeumanomices',
       'nt_con_piricularia_cuello', 'nt_con_sarna_orejas',
       'nt_con_complejo_bacterial', 'sev_manchado_grano', 'n_paniculas_m2',
       'porc_vaneamiento_ajustado', 'n_ granos_panicula',
       'n_ granos_llenos_panicula', 'peso _1000 _granos_g', 'granos_por m2',
       'peso_grano_g', 'rend_estimado_kg', 'pr_i_entorchamiento',
       'pr_i_hoja blanca', 'pr_inc_piri_hoja', 'pr_inc_helm_hoja',
       'pr_inc_rhizoctonia', 'pr_inc_cercospora', 'pr_inc_escaldado',
       'pr_inc_mancha_cafe', 'pr_inc_gaeumanomices',
       'pr_inc_piricularia_cuello', 'pr_inc_sarna_orejas',
       'pr_inc_complejo_bacterial', 'inc_entorchamiento', 'inc_hoja blanca',
       'inc_piri_hoja', 'inc_helmitosporium', 'inc_rhizoctonia',
       'inc_cercospora', 'inc_escaldado', 'inc_mancha_cafe',
       'inc_gaeumanomices', 'inc_piricularia_cuello', 'inc_sarna_orejas',
       'inc_complejo_bacterial']]
print(lotes_sensores.info())
lotes_sensores.to_csv("lotes_sensores_postgresql.csv", index = False)


