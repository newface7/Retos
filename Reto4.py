import os
os.system("cls")

def imc(info:dict)->tuple:
    cedulas = info.keys()
    resultado = {}
    for i in cedulas:
        peso = info[i]["infoSalud"]["peso"]
        altura = info[i]["infoSalud"]["altura"]
        #Se crea un for intenro para crear la lista de IMCs
        imc = []
        for j in range(0, len(peso)+1):
            imc.append(peso[j]/altura[j**2])
        #Se crea un for interno con el objetivo de almacenar el promedio de leucocitos por paciente:
        suma = 0
        imcs = len (imc)
        for ccitems, imcitems in (info[i]["infosalud"].items()): 
        #Devuelve tupla con clave y su valor
            suma = suma + imcitems
        resultado[i] = round(suma/imcs, 1)
        suma = 0

        leucosMayor10 = dict(filter(lambda leuco: leuco[1] >= 10.1, resultado.items()))
        return (resultado, leucosMayor10)


info1 = {
 1144154: {
 "nombreCompleto": "Lina Maria Valencia",
 "infoSalud":
 {
 "peso": [60, 55, 45, 43, 55],
 "altura": [1.8, 1.8, 1.8, 1.8, 1.8]
 }
 },
 1088852: {
 "nombreCompleto": "Mariana Sandoval",
 "infoSalud":
 {
 "peso": [80, 88, 65, 62, 70],
 "altura": [1.7, 1.7, 1.7, 1.7, 1.7]
 }
 },
 1664558: {
 "nombreCompleto": "Sara Torres",
 "infoSalud":
 {
 "peso": [45, 40, 44, 40, 50],
 "altura": [1.50, 1.51, 1.52, 1.55, 1.6]
 }
 }
}

print(imc(info1))
"""
info2 = {
 6668145: {
 "nombreCompleto": "Pablo Perez",
 "infoSalud":
 {
 "peso": [60, 61, 62, 63, 64],
 "altura": [1.6, 1.6, 1.6, 1.6, 1.6]
 }
 },
 7412589: {
 "nombreCompleto": "Juan Esteban Sanchez",
 "infoSalud":
 {
 "peso": [40, 50, 41, 42, 43],
 "altura": [1.45, 1.46, 1.47, 1.48, 1.5]
 }
 },
 9632145: {
 "nombreCompleto": "Daniel Molano",
 "infoSalud":
 {
 "peso": [56, 57, 62, 63, 60],
 "altura": [1.55, 1.55, 1.55, 1.55, 1.55]
 }
 }
}
"""
