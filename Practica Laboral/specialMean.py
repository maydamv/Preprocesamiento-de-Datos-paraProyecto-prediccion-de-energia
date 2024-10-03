import pandas as pd

def calcularPromedioEspecial(df, posicion, columna):
    
    # Obtener los índices de las filas a promediar
    indices = [posicion - j * 14 for j in range(1,8)]
    
    # Calcular el promedio de los valores en la columna deseada
    promedio = df.iloc[indices, columna].mean()
    
    # Reemplazar el valor en la fila actual con el promedio calculado
    df.iloc[posicion, columna] = promedio  


    return df



