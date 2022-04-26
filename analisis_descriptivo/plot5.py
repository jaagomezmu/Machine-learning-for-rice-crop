import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
lsp = pd.read_excel('C:\\Users\\Biomodelacion\\Desktop\\ProyectoArroz\\lotes_sensores_pesos.xlsx')

########### Consideraciones iniciales ############
nombres = {'inc_entorchamiento':'Entorchamiento', 'inc_hoja blanca':'Hoja Blanca',
           'inc_piri_hoja':'Piricularia en hoja', 'inc_helmitosporium':'Helminthosporium',
           'inc_rhizoctonia':'Rhizoctonia', 'inc_cercospora':'Cercospora',
           'inc_escaldado':'Escaldado', 'inc_mancha_cafe':'Mancha Café',
           'inc_gaeumanomices':'Gaeumannomyces', 'inc_piricularia_cuello':'Piricularia en cuello',
           'inc_sarna_orejas':'Sarna de las orejas', 'inc_complejo_bacterial':'Complejo bacteriano'}

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
valores = lsp.iloc[:,np.where(lsp.columns.str.startswith('inc_'))[0].tolist()]
identificadores = lsp[['etapa_fenologica']]
# Corrección del año 2015 para la correcta visualización.
iea = pd.concat([valores,identificadores],axis = 1)
iea.rename(columns=nombres, inplace=True)

########### Transformacion del dataset ###########
dd=pd.melt(iea,id_vars=['etapa_fenologica'],value_vars=[*nombres.values()],var_name='Enfermedad')

######## Se calcula la paleta de colores #########
l = [*iea.columns][0:len([*iea.columns])-1] # Se resta el ultimo, que es el año en este caso.
lcolores = [colores_arroz[x] for x in l]
paleta = {[*nombres.values()][i]: lcolores[i] for i in range(len([*nombres.values()]))} # Paleta de colores para grafica

############ Se realizan las graficas ############
sns.set(style="white")
plt.figure(figsize=(11.7,8.27),dpi=900)
ax = sns.lineplot(x='etapa_fenologica',y='value',data=dd,hue='Enfermedad',palette=paleta)
sns.despine()
plt.xlabel('etapa_fenologica')
plt.ylabel('INCIDENCIA')
plt.savefig("analisis_descriptivo\\plot5.png")

######### Generación de los comentarios ##########
# txt = " Generación de los comentarios "
# x = txt.center(50, "#")
# print(x)