README.md

Integrantes del equipo:
    Ana Inés López
    Luis Vázquez
    Carlos Chabay

Antecedentes:
Para la habilitación de las farmacias de primera categoría, los emprendedores deben presentar ante el MSP, entre otros documentos, una constancia expedida por el INE con la población que vive en un radio de 1 km a la redonda de la ubicación prevista (https://www.gub.uy/tramites/habilitacion-apertura-farmacia-primera-categoria). Por otra parte, el MSP rechaza la instalación si la población anteriormente descrita es menor a 3.000 hb.
A los efectos de evitar inconvenientes y pérdidas de tiempo y recursos, se entiende pertinente disponibilizar a los emprendedores y a los organismos encargados de aprobar las solicitudes, información vinculada a la ubicación de farmacias autorizadas y la cantidad de población objetivo.
Objetivos:
Los objetivos de este trabajo son:
1.	Calcular la cantidad de farmacias por departamento.
2.	Calcular la cantidad de farmacias en las localidades del interior y analizar si hay localidades de más de 3000 habitantes que no tienen farmacias.
3.	Verificar si el área de influencia de las distintas farmacias de primera categoría (1 km) es acorde con los 3.000 habitantes que indica la normativa.
4.	Verificar cuántas personas están bajo el área de influencia de más de una farmacia.
NOTAS:
•	Podría haber farmacias que no figuran en la capa usada para este trabajo.
•	Los datos de población corresponden al Censo 2011 dado que no están disponibles los del Censo 2023.
•	Este ejercicio es sólo un esbozo de lo que podría ser un servicio en la página del INE, que incluyera un mapa de las zonas censales con la cantidad de personas y que los usuarios pudieran procesar en línea la población para sus áreas de interés.
•	Datos originales:
Archivo	Datos que contiene	Formato	Ubicación
Marco_2011	Marco censo 2011	dbf	https://www.gub.uy/instituto-nacional-estadistica/datos-y-estadisticas/estadisticas/marcos-censales

Ine_zonas_11	Capa de zonas censo 2011	shp	
https://www.gub.uy/instituto-nacional-estadistica/datos-y-estadisticas/estadisticas/mapas-vectoriales-ano-2011

farmacias	Farmacias habilitadas de primera categoría	gpck	Base de datos de Geomática

•	Procedimiento:
En QGIS:
1.	Incorporar las dos capas y el marco
2.	Asociar marco a capa de zonas (resultado: Geopackage zonas_con_pob)
3.	Generar área de influencia de las farmacias de radio 1 km (resultado: Geopackage buffer_1_km)
4.	Asignar datos de área de influencia a zonas_con_pob (resultado: Geopackage buffer_1_km)
5.	Exportar la tabla de zonas a nivel país con los datos asociados de cantidad de población y del área de influencia de farmacia a la que pertenece  si correspondiera (resultado: csv intersección_zonas_buffer)
W:\ServTecn\Cartogra\0_borrar\ana\PARA_CHABAY_IMAGENES\trabajo_final\datos_procesar_python
Procesamiento python:

1.	Calcular la cantidad de farmacias por departamento (resultado: csv farmacias_departamento).
Procedimiento:
•	en tabla intersección_zonas_buffer group by DEPTO y sum _TOT_FARM_DEPTO y contar (NOMBRE y DIRECCIÓN) concatenadas

2.	Calcular la cantidad de farmacias en las localidades del interior y analizar si hay localidades de más de 3000 habitantes que no tienen farmacias.
Procedimiento:
•	en tabla intersección_zonas_buffer group by CODLOC y sum _P_TOT y contar (NOMBRE y DIRECCIÓN) concatenadas
•	seleccionar _P_TOT >3000 y sin farmacias

3.	Verificar si el área de influencia de las distintas farmacias de primera categoría (en Montevideo 1km y en interior la localidad entera) es acorde con los 3.000 habitantes que indica la normativa (resultado: farmacias que no cumplen que su área de influencia no llega a 3.000)
Procedimiento:
•	en tabla intersección_zonas_buffer group by NOMBRE y DIRECCION y sum _P_TOT y generar campo POB_RADIO_1KM
•	seleccionar POB_RADIO_1KM >3000
•	seleccionar POB_RADIO_1KM<3000

4.	Verificar cuántas personas están bajo el área de influencia de más de una farmacia.
Procedimiento:
•	En tabla intersección_zonas_buffer frecuencia (contar registros) de codcomp.

VISUALIZAR:
•	Total de personas y de farmacias por departamento (promedio de personas por farmacia?)
•	Total de personas y de farmacias por localidad, indicando las localidades de más de 3.000 que no tienen farmacias?
•	% de población a menos de 1 km de una farmacia/ total de población por localidad (o por depto.?)
•	Total de farmacias (por departamento?) cuya área de influencia es menor a 3.000 hb
•	Total de personas por localidad que están en más de un área de influencia.
