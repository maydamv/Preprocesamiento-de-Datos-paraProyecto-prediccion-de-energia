


import pandas as pd
import os
from datetime import datetime

def actualizarDesdeHistorico(df, posicion, columna, nombreParque):
    # Separar fecha y hora
    fechaHora = df.iloc[posicion, 0]
    fecha, hora = fechaHora.split(' ')
    
   # Convertir la fecha a objeto datetime
    fechaComp = pd.to_datetime(fecha)

    # Verificar si la fecha es anterior al 1 de enero de 2023 dado que no existen los registros
    fechaLimite = datetime(2023, 1, 1)
    if fechaComp < fechaLimite:
        #print("La fecha es anterior al 1 de enero de 2023.")
        return df  
    
    # Formatear la fecha y hora
    fechaFormateada = fechaComp.strftime('%m/%d/%Y')  # Cambiar a formato DD/MM/YYYY
    dia = fechaComp.day
    mes = fechaComp.month
    anno = fechaComp.year
    fechaFormateada = f"{mes}/{dia}/{anno}"
    fechaFormateadaPath = pd.to_datetime(fecha).strftime('%Y%m%d')  # Convertir a formato YYYYMMDD
    horaFormateada = f"h{int(hora.split(':')[0])}"  # Cambiar a formato h#

    # Crear variable para la columna
    columnaDict = {
        'irradiancia': 'IR ',
        'potencia': 'P  ',
        'tmodulo': 'TM ',
        'tambiente': 'TA '
    }
    
    idpar = columnaDict.get(columna.lower())  # Obtener idpar según la columna
    
    
    # Construir el path del hisotrico
    pathCsvHistorico = os.path.join("C:\\Users\\Administrador\\Desktop\\Practica Laboral\\historicos", f"{fechaFormateadaPath}.csv")
    #print(fechaFormateada)
    #print(nombreParque)
    #print(idpar)
    #print(horaFormateada)
    try:
        dfHistorico = pd.read_csv(pathCsvHistorico, encoding='latin1')  # o 'windows-1252'
        
        # Buscar el valor a reemplazar
        #condicion_fecha = (dfHistorico['fecha'] == fechaFormateada)
        #ondicion_nombre = (dfHistorico['nombre'] == nombreParque)
        #condicion_idpar = (dfHistorico['idpar'] == idpar)
        #print("Condición Fecha:", condicion_fecha.any())   # Imprime True si hay coincidencias
        #print("Condición Nombre:", condicion_nombre.any())  # Imprime True si hay coincidencias
        #print("Condición IDPAR:", condicion_idpar.any())     # Imprime True si hay coincidencias
        #print(dfHistorico['fecha'])
        valorHistorico = dfHistorico.loc[
            (dfHistorico['fecha'] == fechaFormateada) &
            (dfHistorico['nombre'] == nombreParque) &
            (dfHistorico['idpar'] == idpar)
        ].iloc[0][horaFormateada]
        
        # Reemplazar el valor en el df
        df.iloc[posicion, df.columns.get_loc(columna)] = valorHistorico
        #print("done")    
    except IndexError:
        #print("", end="")
        print("No se encontro un valor coincidente en el archivo historico.")
    except FileNotFoundError:
        #print("", end="")
        print(f"Error: No se encontró el archivo {pathCsvHistorico}.")
    return df


