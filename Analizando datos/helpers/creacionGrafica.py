import matplotlib.pyplot as plt 
def generalGrafica(dataFrame):
    #Agrupar datos del dataframe segun el analisis que quiera graficar
    #estadisticas de un alimento (PAN) por pais y su promedio al año 
    preciosPromedioPais= dataFrame.groupby('Origen')['PrecioporUnidad'].mean()
    print(preciosPromedioPais)
    
    #0.Generando lista de colores 
    colores=["#F56C4F","#D12B08","#F77E64"]
    #1.Generar una figura
    plt.figure(figsize=(10,10))
    
    #2.Genero la grafica que deseo
    plt.bar(preciosPromedioPais.index, preciosPromedioPais.values, color=colores)
    
    #3.Agrego titulo a la grafica
    plt.title("Ventas promedio de panes por paises")
    
    #4.Etiqueta o nombre del eje X
    plt.xlabel("Paises")
    
    #5. Etiqueta o nombre del eje Y
    plt.ylabel("Precio promedio ")
    
    #6.Activar el grid
    plt.grid(True)
    
    #7.Rotar los labels X
    plt.xticks(rotation=45)
    
    #8. Guardando nuestra gráfica
    plt.savefig("./graphs/promediopanes.png")

    