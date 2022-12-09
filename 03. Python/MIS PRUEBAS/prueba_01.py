#from functools import reduce
#lista = range (50)
#def suma (lista):
    #sum = 0
    #for i in lista:
        #sum += i
        #print ('Estoy en el número:', i, 'y llevo sumado:', sum)
    #print ('Total:',sum)
#suma (lista)
    
#sumatorio = reduce (lambda a,b: a+b, lista)





#FILTER Y REDUCE 
#SPLIT 
# GENERAR FICHERO 
# ESCRIBIR FICHERO
# ABRIR FICHERO


from functools import reduce

numeros = list (input ('Escribe cinco números separados por una ,: '))
listaNumeros = []

def separacionComa (numeros):
    for i in numeros.split (','):
        listaNumeros.append (i) 
    print (', '.join (sorted (list (set ((listaNumeros))))))
separacionComa(numeros)

def conversionStrAInt ():                   # CONVERTIR CONTENIDO INTERNO DE UNA LISTA. DE STR A INT.
    for i in range (len(listaNumeros)):
        listaNumeros [i] = int (listaNumeros [i])

def filtrar (numeros):
    sum = 0
    for x in numeros:
        sum += 1
    print (sum)
filtrar (numeros)

#filtrado = list (filter (lambda x: x % 2 == 0, numeros))
#print (filtrado)

def reducir (numeros):
    total = reduce (lambda a,b: a + b, numeros)
    print (total)
reducir (numeros)


#mult = reduce (lambda a,b: a*b, filtrar)
#print (mult)