import pandas as pd
import specialMean as sm
import exchengeFromHistorical as efh

#archivos CSV
dataframes = {
    'data1': {
        'path': r"C:\Users\Administrador\Desktop\Practica Laboral\IMIAS\IMIAS.csv",
        'name': "IMIAS (PARQUE SOLAR IMIAS)",
        'output': r"C:\Users\Administrador\Desktop\Practica Laboral\IMIAS\ok.csv"
    },
    'data2': {
        'path': r"C:\Users\Administrador\Desktop\Practica Laboral\MAYAS\MAYAS.csv",
        'name': "MAYAS (PARQUE SOLAR MAYARI II)",
        'output': r"C:\Users\Administrador\Desktop\Practica Laboral\MAYAS\ok.csv"
    },
    'data3': {
        'path': r"C:\Users\Administrador\Desktop\Practica Laboral\STE2S\STE2S.csv",
        'name': "STE2S (PARQUE SOLAR SANTA TERESA II)",
        'output': r"C:\Users\Administrador\Desktop\Practica Laboral\STE2S\ok.csv"
    },
    'data4': {
        'path': r"C:\Users\Administrador\Desktop\Practica Laboral\STERS\STERS.csv",
        'name': "STERS (PARQUE SOLAR SANTA TERESA I)",
        'output': r"C:\Users\Administrador\Desktop\Practica Laboral\STERS\ok.csv"
    }
}
for key, values in dataframes.items():
    df = pd.read_csv(values['path'])
    numColumna=0
    CuentaTotal=0
    for columna in df.columns[1:]:
        posicionesCambiadas = []
        numColumna+=1
        for pos,valor in  enumerate(df[columna]):
            if valor == 0 and pos>112:
                indices= [pos - j * 14 for j in range(1,8)]
                #print(indices)
                count_cambiadas = sum(1 for i in indices if i in posicionesCambiadas)
                #print(count_cambiadas)
                if count_cambiadas < 4:
                    df = sm.calcularPromedioEspecial(df, pos, numColumna)
                    posicionesCambiadas.append(pos)
                    CuentaTotal+=1
                    #print("si")
        #print(len(posicionesCambiadas))
        #print(posicionesCambiadas)
    for columna in df.columns[1:]:
         for pos,valor in enumerate(df[columna]):
             #print(columna)
             #print(values['name'])
             #print(pos)
             if valor == 0:
                #print(pos)
                #print(columna)
                df = efh.actualizarDesdeHistorico(df,pos,columna,values['name'])   
    df.to_csv(values['output'])