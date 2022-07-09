#Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final
#Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]


numero_inicial = int (input ("Escriba el numero inicial: "))
numero_final = int (input ("Escriba el numero final: "))

rango_numeros = range (numero_inicial, numero_final)

for i in rango_numeros:
    if i % 2 != 0:
        print (i)