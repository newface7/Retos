import os
os.system("cls")

"""def costo_telegrama (mensajes:list)-> dict:
    letras = [] 
    costo = 0
    descuento = 0
    respuesta = {}
    for i in mensajes:
        for j in i :
            if j in letras:
                costo = costo + 200
            else:
                costo = costo + 300
        resultado[i] =  costo
        costo= 0
    if len(mensajes) >= 9:
        resultado = costo - 500
    else:
        resultado = 0

    return resultado"""

def costo_telegrama (mensajes:list)-> dict:
    costo1 = 0
    costo2 = 0
    descuento = 500
    respuesta = {}
            
    for i in mensajes:
        palabras = list(i.split())
        if len(palabras) < 9:
            costo1 = 0
        else: 
            costo1 = costo1 - descuento
        
        for j in palabras:
            letras = list(j.split())
            if len(j) <=5:
                costo2 = costo2 + 200
            else:
                costo2 = costo2 + 300
        respuesta[i] = costo1 + costo2
        costo2 = 0
    return respuesta
print(costo_telegrama(["Bienvenidos tripulantes a misión tic 2022 es un placer que estén aprendiendo programación en la UTP", "Saludos con mucho amor", "El 5 de mayo de 2021 entrará a trabajar en el área de mantenimiento"]))
print(costo_telegrama(["ñññññ ooooo", "¿es importante conocer el signo????"]))
print(costo_telegrama(["Buenos noches compañeros", "Pequeñas palabras", "Muchos exitos!"]))