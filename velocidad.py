
velocidad = [
    25, 12, 19, 16, 11, 11, 24, 1,
    14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
    14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
    14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
    10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
    11, 10, 18, 10, 14, 5, 23, 20, 23, 21

]


#CALCULAR EL PROMEDIO DE VELOCIDAD 
def promedio(lista):
    return sum(lista)/len(lista)

#REVISAR LISTA DE VELOCIDAD, IDENTIFICAR LOS VALORES MAYORES AL PROMEDIO EN SU POSICION (INDICE)
def posicion_mayor_promedio(lista, promedio_valor):
    return [i for i, valor in enumerate(lista) if valor > promedio_valor]

#ASIGNAR VALOR PROMEDIO CALCULADO PARA LISTA VELOCIDAD
promedio_velocidades = promedio(velocidad)
        
#LLAMAR LA FUNCION POSICIÓN, PARA LAS VELOCIDADES MAYORES AL PROMEDIO
posiciones_mayores = posicion_mayor_promedio(velocidad, promedio_velocidades)
import math

print(posiciones_mayores)