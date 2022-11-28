#Crea un script que le pida al usuario una lista de países 
# (separados por comas). Éstos se deben almacenar en una lista. 
# No debería haber países repetidos (haz uso de set). 
# Finalmente, muestra por consola la lista de países ordenados 
# alfabéticamente y separados por comas.


paises = input ('Escribe varios paises (separado por comas): ')
listaPaises = []

for i in paises.split (', '):
    listaPaises.append (i)

print (', '.join (sorted (list (set (listaPaises)))))