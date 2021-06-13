#Funciones w2-pandas-project
def isnull(x):
    """ Esta función muestra la suma de todos los NaNs ordenados de mayor a menor"""
    return x.isnull().sum().sort_values(ascending = False)

def comprobacion_duplicados (x):
     """ Esta función muestra el número de datos repetidos"""
    repetidos = list(unique_everseen(duplicates(x)))
    return len(repetidos)

def extract (dataframe,columna1,columna2,patron):
     """ Inputs:
     dataframe = nombre del dataframe sobre el que quieres realizar los cambios
     columna 1 = nombre de la nueva columna
     columna 2 = nombre de la columna sobre la que quieres realizar los cambios
     patron = patron regex de los valores por los que quieres filtrar (encapsular) o realizar los cambios
     """
    dataframe.columna1 = dataframe.columna2.extract(patron, expand = False )
    return dataframe