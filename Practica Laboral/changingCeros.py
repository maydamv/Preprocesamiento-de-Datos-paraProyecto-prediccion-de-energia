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
for key, values in dataframes.items(): #iterando sobre el diccionario dataframes
    
    df = pd.read_csv(values['path']) #creando el data frame 
    
    numColumna=0 #columna en la que se empieza a iterar
    
    #CuentaTotal=0 #esta variable seria para hacer una traza de todas las columnas que se modificaron
    
    for columna in df.columns[1:]: #primer ciclo para promediar
        
        posicionesCambiadas = [] #arreglo para guadar las posiciones cambiadas en la columna
        
        numColumna+=1 #cambiando de columna dado que empezamos en la primera
        
        for pos,valor in  enumerate(df[columna]): #iterando sobre los valores de la columna
            
            if valor == 0 and pos>112: #comprobando que existan 7 valores anteriores de la misma hora y que el valor act es 0
                
                indices= [pos - j * 14 for j in range(1,8)]
                
                count_cambiadas = sum(1 for i in indices if i in posicionesCambiadas) #comprobando que en no existan mas de 3 columnas ya promediadas para usar
                
                if count_cambiadas < 4:
                    
                    df = sm.calcularPromedioEspecial(df, pos, numColumna) #calculando el promedio
                    
                    posicionesCambiadas.append(pos) #adicionando a columnas cambiadas
                    
                    #CuentaTotal+=1 #actualizando la cuenta total
         
    for columna in df.columns[1:]: #segundo ciclo
        
         for pos,valor in enumerate(df[columna]):

             if valor == 0:

                df = efh.actualizarDesdeHistorico(df,pos,columna,values['name']) # reemplazando desde el historico
                
    df.to_csv(values['output']) #creando el csv en la direccion de salida