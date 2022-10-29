from functions import *
brigadas_fitosanitarias = file_upload_brigadas("brigadas_fitosanitarias_preprocesada_copy.xlsx")
# print(brigadas_fitosanitarias.columns)
brigadas_fitosanitarias = brigadas_fitosanitarias[[ 'anio_bd', 'semestre_ajustado',
       'mes_siembra_est', 'mes_cosecha', 'fecha_siembra_est',
       'fecha_cosecha_est', 'zona', 'departamento', 'municipio', 'vereda',
       'finca', 'lote', 'variedad', 'variedad_ajustada', 'edad_dde',
       'propietario', 'puntos_eval', 'y_lat', 'x_long', 'inc_rhizoctonia',
       'inc_piricularia', 'inc_gaeumanomices', 'inc_helmitosporium',
       'inc_mancha_cafe', 'sev_mancha_cafe', 'inc_complejo_bacteriano',
       'frec_sspinki_acaro', 'porc_vaneamiento', 'inc_barrenador',
       'pr_rhizoctonia', 'pr_piricularia', 'pr_gaeumanomices',
       'pr_helmitosporium', 'pr_barrenador', 'pr_mancha_cafe',
       'pr_complejo_bacteriano']]


brigadas_fitosanitarias.to_csv("brigadas_fitosanitarias_postgresql.csv", index = False)
