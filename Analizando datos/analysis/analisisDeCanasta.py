#1. Importar el paquete o paquetes con los que voy a analisar la informacion

import pandas as pd
from helpers.creacionTabla import crearTabla 

def analizarCanastaBasica():
    #2. Sin importar la fuente (sql, xls, JSON ,csv...)
    #Crear una tabla tabulada que se llama DATAFRAME
    tabla=pd.read_csv("./data/bdcanasta.csv")    
    #print(tabla)
    crearTabla(tabla,"Canastabasica")
    
#3. aplico filtro para limpiar o seleccionar datos

    #print(tabla.head(20)) #Primeros N registros
    #print(tabla.tail()) #ultimos
    #print(tabla.describe())
    #filtroPanes=tabla.query("(Producto=='Pan') and (Origen=='India')")
    filtroPrecios=tabla.query("Precio por Unidad<50")
    crearTabla(filtroprecio,"filtroprecios")
    

