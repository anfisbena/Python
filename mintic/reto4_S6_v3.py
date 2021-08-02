#General: Cola donde los clientes de la entidad bancaria reclaman un ficho para pasar a una de las otras filas
    #Caja: Cola donde los clientes de la entidad bancaria pueden retirar o consignar la cantidad que ellos desean (En el caso de retiro, solo pueden retirar como máximo la cantidad disponible en sus cuentas bancarias).
    #Información: Cola donde los clientes de la entidad bancaria pueden solicitar cualquier tipo de información.

def sede_bancaria(cola_general):
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    cola_caja=[]
    cola_info=[]
    suma_retiros=0
    suma_consignaciones=0
    edad_minima_retiro=-1
    edad_minima_info=-1
    edad_minima_consignacion=-1
    
    
    for i in range (len(cola_general)):
        #me dice que tipo de operacion va a hacer
        if cola_general[i].fila_interes == "caja":
            cola_caja.append(cola_general[i].nombre)
            #codigo retiro
            if cola_general[i].transaccion == "retirar":
                suma_retiros += cola_general[i].cantidad_retirar
                if edad_minima_retiro==-1:
                    edad_minima_retiro=cola_general[i].edad
                else:
                    if edad_minima_retiro > cola_general[i].edad:
                        edad_minima_retiro = cola_general[i].edad
            #codigo consignacion
            elif cola_general[i].transaccion == "consignar":
                suma_consignaciones +=cola_general[i].cantidad_consignar
                if edad_minima_consignacion==-1:
                    edad_minima_consignacion=cola_general[i].edad
                else:
                    if edad_minima_consignacion > cola_general[i].edad:
                        edad_minima_consignacion = cola_general[i].edad
        else:
            cola_info.append(cola_general[i].nombre)
            if edad_minima_info==-1:
                edad_minima_info=cola_general[i].edad
            else:
                if edad_minima_info > cola_general[i].edad:
                    edad_minima_info = cola_general[i].edad
                
        
    


    
    return cola_caja, cola_info, suma_retiros, suma_consignaciones, edad_minima_retiro, edad_minima_info, edad_minima_consignacion

"""
NO PEDIR DATOS CON LA FUNCIÓN input(), NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED CREE
Esta línea de código que sigue, permite probar si su ejercicio es correcto
Por favor NO ELIMINARLA, NO MODIFICARLA
"""
pruebas_codigo_estudiante(sede_bancaria)