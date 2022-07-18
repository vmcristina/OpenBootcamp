#En este ejercicio tendréis que crear un módulo que contenga las operaciones básicas de una calculadora: 
# sumar, restar, multiplicar y dividir.
#Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas. 
# Los resultados tenéis que mostrarlos por consola.


from operaciones import suma, resta, multiplicacion, division


def main ():
    suma(1,2)
    print ("El resultado de la resta es: ", resta(3,4))
    print ("El resultado de la multiplicacion es: ", multiplicacion(5,6))
    print ("El resultado de la division: ", division(7,8))


if __name__ == "__main__":
    main()


