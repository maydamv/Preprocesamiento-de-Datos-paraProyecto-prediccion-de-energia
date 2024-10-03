import pandas as pd
import os

#archivos CSV
dataframes = {
    'data1': {
        'path': r"C:\Users\Administrador\Desktop\Practica Laboral\IMIAS\IMIAS.csv",
        'data': pd.read_csv(r"C:\Users\Administrador\Desktop\Practica Laboral\IMIAS\IMIAS.csv")
    },
    'data2': {
        'path': r"C:\Users\Administrador\Desktop\Practica Laboral\MAYAS\MAYAS.csv",
        'data': pd.read_csv(r"C:\Users\Administrador\Desktop\Practica Laboral\MAYAS\MAYAS.csv")
    },
    'data3': {
        'path': r"C:\Users\Administrador\Desktop\Practica Laboral\STE2S\STE2S.csv",
        'data': pd.read_csv(r"C:\Users\Administrador\Desktop\Practica Laboral\STE2S\STE2S.csv")
    },
    'data4': {
        'path': r"C:\Users\Administrador\Desktop\Practica Laboral\STERS\STERS.csv",
        'data': pd.read_csv(r"C:\Users\Administrador\Desktop\Practica Laboral\STERS\STERS.csv")
    }
}


for key, values in dataframes.items():
    df = values['data']
    #Filtrar datos distintos de 0
    filteredData = df[(df != 0).all(axis=1)]
    #Filtrar datos con 0
    filteredData_0 = df[(df ==0).any(axis=1)]

    #Calcular estadísticas sin 0
    stats = {
        'irradiancia': {
            'min': filteredData['Irradiancia'].min(),
            'max': filteredData['Irradiancia'].max(),
            'mean': filteredData['Irradiancia'].mean(),
        },
        'tambiente': {
            'min': filteredData['Tambiente'].min(),
            'max': filteredData['Tambiente'].max(),
            'mean': filteredData['Tambiente'].mean(),
        },
        'tmodulo': {
            'min': filteredData['Tmodulo'].min(),
            'max': filteredData['Tmodulo'].max(),
            'mean': filteredData['Tmodulo'].mean(),
        },
        'potencia': {
            'min': filteredData['Potencia'].min(),
            'max': filteredData['Potencia'].max(),
            'mean': filteredData['Potencia'].mean(),
        }
    }
    #Calcular estadísticas sin 0
    stats_0 = {
        'irradiancia': {
            'min': filteredData_0['Irradiancia'].min(),
            'max': filteredData_0['Irradiancia'].max(),
            'mean': filteredData_0['Irradiancia'].mean(),
        },
        'tambiente': {
            'min': filteredData_0['Tambiente'].min(),
            'max': filteredData_0['Tambiente'].max(),
            'mean': filteredData_0['Tambiente'].mean(),
        },
        'tmodulo': {
            'min': filteredData_0['Tmodulo'].min(),
            'max': filteredData_0['Tmodulo'].max(),
            'mean': filteredData_0['Tmodulo'].mean(),
        },
        'potencia': {
            'min': filteredData_0['Potencia'].min(),
            'max': filteredData_0['Potencia'].max(),
            'mean': filteredData_0['Potencia'].mean(),
        }
    }

    #Guardar Info
    directory = os.path.dirname(values['path'])
    infoPath = os.path.join(directory,'InfoIni.txt')
    with open(infoPath, 'w') as f:
        for column, details in stats.items():
            f.write(f"Columna: {column}\n")
            f.write(f"Min: {details['min']}\n")
            f.write(f"Max: {details['max']}\n\n")
        f.write(f"Total de Filas analisadas: {len(filteredData)}\n")
        f.write(f"Total de Filas con 0: {len(filteredData_0)}\n")  
        f.write(f"Total de Filas: {len(df)}\n")
