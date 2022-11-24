#Crear un archivo py donde creéis un archivo txt, 
# lo abráis y escribáis dentro del archivo. 
# Para ello, tendréis que acceder dos veces al archivo creado.


f = open ('datos.txt', 'w')
f.close()


f = open ('datos.txt', 'a')
f.write ('Ejercicio de datos\n')
f.write ('Ejercicio de datos 01\n')
f.close()


