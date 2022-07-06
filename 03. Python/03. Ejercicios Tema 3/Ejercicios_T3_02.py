peso = float (input ('Peso en KG: '))
estatura = float (input ('Estatura en metros: '))

imc = (peso / (estatura)**2)

print ('Tu IMC es: ' + "{0:.2f}".format (imc))



