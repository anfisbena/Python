#NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, sirven para probar tu código en consola, y el funcionamiento del módulo csv respectivamente
# 0. Date: Fecha del dato
# 1. Open: Precio de apertura de la acción en la bolsa
# 2. High: Precio más alto durante el día
# 3. Low: Precio más bajo durante el día
# 4. Close: Precio de cierre de la acción
# 5. Adj Close: Precio de cierre ajustado de la acción
# 6. Volume: Volumen de acciones transadas durante el día
# "Fecha Mean-Min-Max Concepto" (Lo señalado en rojo es equivalente a una tabulación). FECHA, (𝐻𝑖𝑔ℎ𝑖 + 𝐿𝑜𝑤𝑖)/2, 
# Una cadena de texto que será un concepto respecto al
# promedio calculado anteriormente:
# • MUY BAJO: Si el precio es menor que $239
# • BAJO: Si el precio es mayor o igual que $239 y menor
# que $265
# • MEDIO: Si el precio es mayor o igual que $265 y menor
# que $291
# • ALTO: Si el precio es mayor o igual que $291 y menor
# que $317
# • MUY ALTO: Si el precio es mayor o igual que $317.
# Es decir, las primeras líneas se deberían ver así:

import csv

date_lowest_mean= '01/01/1000'
lowest_mean=-420
date_highest_mean='01/01/1000'
highest_mean= -420

with open('FB.csv') as data_origen:
    with open('analisis_archivo.csv','w', newline ='') as data_destino:
        reader_origen=csv.reader(data_origen)
        writer_destino=csv.writer(data_destino,delimiter="\t")
        data=[["Fecha","Mean-Min-Max","Concepto"]]
            
        for row in reader_origen:
                
            if row[0]=='Date':
                    row.pop()
                    continue
                
            if (float(row[2])+float(row[3]))/2 < 239:
                concepto='MUY BAJO'
            if (float(row[2])+float(row[3]))/2 >= 239 and (float(row[2])+float(row[3]))/2 < 265:
                concepto='BAJO'                
            if (float(row[2])+float(row[3]))/2 >= 265 and (float(row[2])+float(row[3]))/2 < 291:
                concepto='MEDIO'                            
            if (float(row[2])+float(row[3]))/2 >= 291 and (float(row[2])+float(row[3]))/2 < 317:
                concepto='ALTO'                    
            if (float(row[2])+float(row[3]))/2 >= 317:
                concepto='MUY ALTO'
                
            data.append([row[0],(float(row[2])+float(row[3]))/2,concepto])
                
            if date_lowest_mean == '01/01/1000':
                date_lowest_mean = row[0]
                lowest_mean= (float(row[2])+float(row[3]))/2
                date_highest_mean = row[0]
                highest_mean= (float(row[2])+float(row[3]))/2
                continue

            elif lowest_mean > (float(row[2])+float(row[3]))/2:
                lowest_mean = (float(row[2])+float(row[3]))/2
                date_lowest_mean = row[0]
            elif highest_mean < (float(row[2])+float(row[3]))/2:
                highest_mean = (float(row[2])+float(row[3]))/2
                date_highest_mean = row[0]
                    
        writer_destino.writerows(data)
print (date_lowest_mean, lowest_mean, date_highest_mean, highest_mean)

