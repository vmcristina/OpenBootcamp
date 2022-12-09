numeros = list (input ('Escribe cinco números separados por una ,: '))
print ('LISTA COMPLETA')
print (numeros)

for i in numeros:
    if i == ',':
        numeros.remove (i)

for i in range (len(numeros)):          
    numeros [i] = int (numeros [i])

filtrar = list (filter(lambda x: x % 2 == 0, numeros))
print (type(filtrar))
print (filtrar)

print (type(numeros))
print (numeros)
# a = ['1','2','3']
# for i in range(len(a)):
#     a[i] = int(a[i])


# lista2 = [1,2,3,4,5]
# lista3 = ['1', '2']
# print (lista2)


# # print (filtrar)