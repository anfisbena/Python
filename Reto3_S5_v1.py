#NO ELIMINAR LA SIGUIENTE IMPORTACIÓN, sirve para probar tu código en consola


#NOTA: PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
#LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO

#En este espacio podrás programar las funciones que deseas usar en la función solución (NO ES OBLIGATORIO CREAR OTRAS FUNCIONES)
"""Inicio espacio para programar funciones propias"""



#PUEDES PROGRAMAR CUANTAS FUNCIONES DESEES 



"""Fin espacio para programar funciones propias"""

def traductor_a_morse(mensaje_a_traducir):
    #PROGRAMA ACÁ TU SOLUCIÓN
    mensaje_a_traducir=mensaje_a_traducir.upper()
    mensaje_traducido=[]
    for i in range (len(mensaje_a_traducir)):

        if mensaje_a_traducir[i]== 'A':
            r= '.-'
        elif mensaje_a_traducir[i] == 'B':    
            r= '-..'
        elif mensaje_a_traducir[i] == 'C':    
            r= '-.-.'
        elif mensaje_a_traducir[i] == 'D':    
            r= '-..'
        elif mensaje_a_traducir[i] == 'E':    
            r= '.'
        elif mensaje_a_traducir[i] == 'F':    
            r= '..-.'
        elif mensaje_a_traducir[i] == 'G':    
            r= '--.'
        elif mensaje_a_traducir[i] == 'H':    
            r= '....'
        elif mensaje_a_traducir[i] == 'I':    
            r= '..'
        elif mensaje_a_traducir[i] == 'J':    
            r= '.---'
        elif mensaje_a_traducir[i] == 'K':    
            r='-.-'
        elif mensaje_a_traducir[i] == 'L':    
            r='.-..'
        elif mensaje_a_traducir[i] == 'M':    
            r='--'
        elif mensaje_a_traducir[i] == 'N':    
            r='-.'
        elif mensaje_a_traducir[i] == 'O':    
            r='---'
        elif mensaje_a_traducir[i] == 'P':    
            r='.--.'
        elif mensaje_a_traducir[i] == 'Q':    
            r='--.-'
        elif mensaje_a_traducir[i] == 'R':    
            r='.-.'
        elif mensaje_a_traducir[i] == 'S':    
            r='...'
        elif mensaje_a_traducir[i] == 'T':    
            r='-'
        elif mensaje_a_traducir[i] == 'U':    
            r='..-'
        elif mensaje_a_traducir[i] == 'V':    
            r='...-'
        elif mensaje_a_traducir[i] == 'W':    
            r='.--'
        elif mensaje_a_traducir[i] == 'X':    
            r='-..-'
        elif mensaje_a_traducir[i] == 'Y':    
            r='-.--'
        elif mensaje_a_traducir[i] == 'Z':    
            r= '--..'
        elif mensaje_a_traducir[i] == ' ':
            r='/'
        mensaje_traducido + r
    print(mensaje_traducido)
    return mensaje_traducido

caca=traductor_a_morse('caquita rica')

"""
Esta línea de código que sigue, permite probar si su ejercicio es correcto
"""
#NO ELIMINAR LA SIGUIENTE LÍNEA DE CÓDIGO
#pruebas_codigo_estudiante(traductor_a_morse)







    