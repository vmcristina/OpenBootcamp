#Escribe una función que pueda decirte si un número (número entero) es primo o no.

def num_primo ():
    numero = int (input ("Escriba un numero par saber si es primo: "))

    if numero > 1:
        for i in range (1, numero):
            if numero % i == 0:
                print ("No es primo")
                break
                
            else:
                print ("Es primo")
                break

    else:
        print ("El numero tiene que ser mayor de 1")


num_primo ()            


        