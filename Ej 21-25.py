#21 Multiplica una cadena de texto por un nro entero

nro = 8
cad = "3"

resultado = nro*int(cad)
print(resultado)


#22 Divide una cadena en una lista de subcadenas

cad1 = "Divide una cadena en una lista de subcadenas"
division = cad1.split(" ",6)

print(division)


#23 verifica si una palabra es un palindromo

pal = "radar"
resultado = pal == pal[::-1]
print(resultado)


#24 Elimina un elemento especifico de una lista

list = ["pepe", 4,5,"bueno", "revolver",19]

eliminar = list.remove("bueno")

print(list)


#25 Genera una lista de numeros del 1 al 200

# numeros= list.range(1-201)
# print(numeros)

for i in range(1,201):
    print(i)