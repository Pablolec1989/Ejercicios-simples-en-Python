#6 Crear cadena de texto y mostrar su longitud

cad= "Rebelde"
longitud= len(cad)

print(f"la longitud de la cadena es de {longitud}")

#7 Calcular el promedio de una lista de numeros

my_list = [35, 24, 62, 52, 30, 30, 17]
promedio = sum(my_list)//len(my_list)

print(promedio)

# usando numpy
import numpy as np

media = np.mean(my_list)
print(media)

#8 Crear una tupla e imprimirla

mi_tupla= tuple()
mi_tupla = (35, 24, 62, 52, 30, 30, 17)
print(mi_tupla)

#9 Realizar la potencia de un numero

n=5
exp=2

potencia = n**exp
print(potencia)

#10 Invertir una cadena

cadena="Realizar la potencia de un numero"
invertida=cadena[::-1]

print(invertida)