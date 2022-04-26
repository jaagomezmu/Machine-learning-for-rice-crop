import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
lsp = pd.read_excel('C:\\Users\\Biomodelacion\\Desktop\\ProyectoArroz\\lotes_sensores_pesos.xlsx')

########### Consideraciones iniciales ############
nombres = {'sev_entorchamiento':'Entorchamiento', 'sev_hoja blanca':'Hoja Blanca',
           'sev_piricularia_hoja':'Piricularia en hoja', 'sev_helmitosporium':'Helminthosporium',
           'sev_rhizoctonia':'Rhizoctonia', 'sev_cercospora':'Cercospora',
           'sev_escaldado':'Escaldado', 'sev_mancha_cafe':'Mancha Café',
           'sev_gaeumanomices':'Gaeumannomyces', 'sev_piricularia_cuello':'Piricularia en cuello',
           'sev_sarna_orejas':'Sarna de las orejas', 'sev_complejo_bacterial':'Complejo bacteriano',
           'sev_manchado_grano':'Manchado grano'}

colores_arroz = {'Entorchamiento':'#073763','Hoja Blanca': '#07674D','Piricularia en hoja':'#387025',
                 'Helminthosporium':'#674ea7','Rhizoctonia':'#0075A2','Cercospora':'#099AA2',
                 'Escaldado':'#33CCCC','Mancha Café':'#54A738','Gaeumannomyces':'#66FF99',
                 'Piricularia en cuello':'#CC99FF','Sarna de las orejas':'#5EEFF7','Complejo bacteriano':'#77C4E8',
                 'Barrenador':'#741b47','Ácaro Steneotarsonemus spinki':'#9900ff'}

marcadores_arroz = {'Entorchamiento':'o','Hoja Blanca': 'x','Piricularia en hoja':'s',
                 'Helminthosporium':'p','Rizhoctonia':'d','Cercospora':'+',
                 'Escaldado':'^','Mancha Café':'*','Gaemanomices':'H',
                 'Piricularia en cuello':'I','Sarna de las orejas':'2','Complejo Bacteriano':'X',
                 'Barrenador':'_','Ácaro Steneotarsonemus spinki':' >'}

############ Modificacion del dataset ############
valores = lsp.iloc[:,np.where(lsp.columns.str.startswith('sev_'))[0].tolist()]
identificadores = lsp[['anio_db_org', 'fecha_evaluacion']]
# Corrección del año 2015 para la correcta visualización.
iea = pd.concat([identificadores,valores],axis = 1)
iea['año'] = np.where(iea.fecha_evaluacion.dt.year == 2015, iea['fecha_evaluacion'].dt.year,iea['anio_db_org'])
iea['año'] = iea['año'].astype(int)
iea.drop(['anio_db_org', 'fecha_evaluacion'], axis=1, inplace = True)
iea.rename(columns=nombres, inplace=True)

########### Transformacion del dataset ###########
dd=pd.melt(iea,id_vars=['año'],value_vars=[*iea.columns][0:len([*iea.columns])-1],var_name='Enfermedad')

######## Se calcula la paleta de colores #########
#l = [*iea.columns][0:len([*iea.columns])-2] # Se resta el ultimo, que es el año en este caso.
#lcolores = [colores_arroz[x] for x in l]
#paleta = {[*nombres.values()][i]: lcolores[i] for i in range(len([*nombres.values()]))} # Paleta de colores para grafica

############ Se realizan las graficas ############
sns.set(style="white")
plt.figure(figsize=(11.7,8.27),dpi=900)
ax = sns.boxplot(x='año',y='value',data=dd,hue='Enfermedad', fliersize = 1) # palette=paleta,
sns.despine()
plt.xlabel('AÑO')
plt.ylabel('SEVERIDAD')
plt.savefig("analisis_descriptivo\\plot3_1.png")

############ Modificacion del dataset ############
valores1 = lsp.iloc[:,np.where(lsp.columns.str.startswith('sev_'))[0].tolist()]
identificadores1 = lsp[['etapa_fenologica']]
# Corrección del año 2015 para la correcta visualización.
iea1 = pd.concat([valores1,identificadores1],axis = 1)
iea1.rename(columns=nombres, inplace=True)

########### Transformacion del dataset ###########
dd1=pd.melt(iea1,id_vars=['etapa_fenologica'],value_vars=[*iea1.columns][0:len([*iea.columns])-1],var_name='Enfermedad')

######## Se calcula la paleta de colores #########
# l1 = [*iea1.columns][0:len([*iea1.columns])-1] # Se resta el ultimo, que es el año en este caso.
# lcolores1 = [colores_arroz[x] for x in l1]
# paleta1 = {[*nombres.values()][i]: lcolores1[i] for i in range(len([*nombres.values()]))} # Paleta de colores para grafica

############ Se realizan las graficas ############
sns.set(style="white")
plt.figure(figsize=(11.7,8.27),dpi=900)
ax = sns.boxplot(x='etapa_fenologica',y='value',data=dd1,hue='Enfermedad', fliersize = 1) # palette=paleta1,
sns.despine()
plt.xlabel('etapa_fenologica')
plt.ylabel('SEVERIDAD')
plt.savefig("analisis_descriptivo\\plot3_2.png")

######### Generación de los comentarios ##########
# txt = " Generación de los comentarios "
# x = txt.center(50, "#")
# print(x)