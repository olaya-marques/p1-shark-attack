![Portada](https://user-images.githubusercontent.com/64830147/121803758-47897d00-cc43-11eb-86ca-a41f26d8c19e.png)

*Este repositorio contiene el primer proyecto del Bootcamp: Data Analytics de IronHack el cual consisitía en el análisis y limpieza de datos de la dataframe extraída de kaggle : shark attacks y del planteamiento y posterior resolución de las hipótesis.*

# Índice de Contenido 📎
En el repositorio se encuentran los siguientes archivos:
- 1. Cleaning_Data: Contiene todo el proceso de tratamiento de datos en materia a exploración, tratamiento y limpieza.
- 2. Visualization_Data: Contiene los gráficos y el estudio de las hipotesis planteadas.
- Carpeta de funciones: Dónde se encuentra todo el contenido en materia a las funciones empleadas en los dos jupyter notebooks.
- Carpeta de imágenes
- Dataset limpio denominado attacks_limpio.
- Las conclusiones se muestran a continuación

*Para la realización de este ejercicio se han empleado las siguientes bibliotecas: pandas, seaborn, matplotlib.pyplot, numpy, re, iteration_utilities. Las demás fuentes empleadas se especifican en el apartado de la bibliografía de cada jupyter notebook*

# Descripción 📄
![Descripción](https://user-images.githubusercontent.com/64830147/121817545-58a5ae80-cc82-11eb-8402-6807696947e7.png)

Se ha propuesto la idea de organizar "IronWater" un campeonato internacional cuyo principal protagonista sean los deportes acuáticos a fin de concienciar a la población del riesgo que supone la realización de este tipo de deporte (sin supervisión) causado por los continuos ataques de tiburón. Además de promover la protección y respeto a estos animales.

El campeonato constará de tres deportes: surf, pesca y natación. El país donde se celebrará aun no se ha decidido , pero se barajean lo siguientes países para su celebración: USA, Australia, Irlanda y Sudáfrica. Asímismo tampoco se han concluido la fecha, hora, características de los participantes (edad, sexo) y demás aspectos.

El trabajo del analista será determinar dichas variables teniendo como principal objetivo que el campeonato no se vea interrumpido por los ataques de tiburón. Para ello se estudiará:

- Veracidad de sí en los últimos años ha disminuido el ataque de los tiburones
- Relaccion entre el número de ataques producidos con el sexo y la edad del afectado
- País con menos accidentes (entre los propuestos)
- Mejor hora y época del año (mes) para realizar el campeonato
- Actividad con mayor riesgo (entre las propuestas)

# Metodología 🔎
### *Tratatamiento de datos* 🧹
La metodología seguida para obtener el DataFrame del que se estudian y plantean las hipotesis fue la siguiente:
- Exploración de los datos
- Eliminación de datos duplicados y/o irrelevantes para el caso de estudio
- Limpieza y sustitución de los valores NaNs
- Organización y estructuración de los datos obtenidos
- Visualización y estudio de hipótesis mediante gráficos

### *Visualización de datos* 👀
La metodología empleada para este apartado ha sido contabilizar el número de ataques en cada variable para determinar en que valor se producían un menor número, considerando tal, la opción más segura (objetivo final que persigue el análisi: determinar los aspectos del evento en el instante más seguro). También se ha comparado con la letalidad de tales ataques. Considero que dichas variables son dependientes ya que no es lo mismo; que se produzcan muchos ataques, de los cuales ninguno es mortal a que se produzcan pocos y que dichos tengan un alto grado de letalidad y/o viceversa. 

### *Consideraciones finales* ⭐
En lo que respecta a los criterios de eliminación datos son meramentes subjetivos, por ello destacar que los resultados no muestran una visión 100% real de los mismos, además la base de la DataFrame original se encontraba muy corrupta por datos vacíos o incompletos lo que hacía más compleja la realización del trabajo de procesamiento. A fin de conseguir la máxima fiabilidad se ha procedido a realizar un filtro mediante los países y actividades planteadas en el ejercicio, manteniendo algunos NaNs bajo el nombre de "0" o "Unknowns" que se eliminan más tarde por columna, que no la fila entera (que puede tener información relevante para otras preguntas) en el analisis y visualización única de cada variable. 

Por último mencionar que para alcanzar los resultados se han empleado diversos métodos en los que se destacan: regex, replace, extract, drop...etc. Finalmente puntualizar dos limitaciones que me he encontrado a la hora de realizar el proyecto: La primera; el archivo de funciones no se me cargaba al jupyter notebook y la segunda en mi biblioteca de matplotlib no reconoce el comando axvline y axs. Igualmente se han indicado como comentario la realización de tales operaciones.

# Resultados 🤔
*Este análisis se pretende determinar las variables mencionadas anteriormente para la celebración de "Iron Water". Para más gráficas véase 2. Data_visualization.*

### *Tendencia de los últimos años* 📆

La tendencia en los últimos años tal y como se muestra en la gráfica es bastante altiva aunque si que se produce un descendo en el año 2000, ello se puede explicar por el aumento de la población que obliga a los tiburones, a desplazarse a habitats menos habitadas por el ser humano; además de la práctica de actividades como la caza furtiva o el aumento de la contaminación en mares y océanos. Por otro lado el aumento que se produce desde 1950 hasta el año 2000 puede ser causado también por la aparición de metodologías y herramientas tecnológicas más precisas y que facilitan la medición de los ataques producidos, registrando por tanto un mayor número que en 1850.

En cualquiera de los casos para IronWater no supone ningún impedimento ya que el evento garantiza la seguridad de todos sus participantes.

### *¿Quién podrá asistir al evento?* 👫🏻

![Sexo](https://user-images.githubusercontent.com/64830147/121910391-19816700-cd2f-11eb-8410-3edc51adab8d.png)
![Edad](https://user-images.githubusercontent.com/64830147/121910593-46357e80-cd2f-11eb-9b07-54130b41e341.png)

La competeción será para mujeres (ya que tienen menor probabiblidad de ser atacadas mortalmente) entre los 25 y 40 años (que es cuando la mortalidad y los ataques disminuyen).

### *¿Dónde se celebrá el evento?* 🌏

![País](https://user-images.githubusercontent.com/64830147/121911263-e9869380-cd2f-11eb-8936-8e6a7fe9b5b1.png)

El evento tendrá lugar en Indonesia

### *¿Cuándo? ¿Mes? ¿Hora?* 🕔

![Mes](https://user-images.githubusercontent.com/64830147/121911701-47b37680-cd30-11eb-9bdc-443cdbc24e0c.png)
![Hora](https://user-images.githubusercontent.com/64830147/121911802-5bf77380-cd30-11eb-87d4-f65d7498052d.png)

Se pretende celebrar en un mes que meramente hago calor y buen tiempo para que se puedan disfrutar y realizar las 3 actividades propuestas. Por ello se propone el mes de Mayo que no presenta un gran grado de mortalidad o número de accidentes. En cuanto a las horas, el campeonato quedará dividido en dos por la mañana se realizarán las actividad de pesca en horario de 7:00 a 10:00 y por la tarde las dos actividades restantes: surf y natación entre las 18:00 - 23:00.

### *Seguridad de las actividades* 🏄🏻‍♀️
Tras el estudio se ha determinado que la actividad más segura es la pesca en lo que respecta al surf es donde se produce un mayor número de accidentes seguido de la natación. Sin embargo podríamos considerar que la natación es mucho más peligrosa ya que el índice de la letalidad es bastante más alto que en comparación con el surf.

 Esto se ha tenido en cuenta a la hora de establecer el horario de las actividades.

### *Recopilación de resultados* 🦈
![Resultados](https://user-images.githubusercontent.com/64830147/121913342-9a416280-cd31-11eb-9a89-d23968e94b88.png)
