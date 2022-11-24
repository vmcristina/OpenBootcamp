# crear un archivo py y dentro crearéis una clase Vehículo, 
# haréis un objeto de ella, lo guardaréis en un archivo 
# y luego lo cargamos.

import pickle

class Vehiculo():
    puertas = 0
    color = ''
    
    def __init__(self, puertas, color):
        self.puertas = puertas
        self.color = color
    
    def getColor (self):
        print (f'El color del coche es: {self.color}')
        

v1 = Vehiculo (5, 'azul')
v1.getColor ()

        

def exportarDatos():
    f = open ('/Users/cristina/Documents/OB/OB/GitHub/C/OpenBootcamp/03. Python/08. Ejercicios Tema 8/archivo.bin', 'wb')
    pickle.dump (v1, f)
    f.close()
    
    
    
def importarDatos():
    f = open ('/Users/cristina/Documents/OB/OB/GitHub/C/OpenBootcamp/03. Python/08. Ejercicios Tema 8/archivo.bin', 'rb')
    contenidoArchivos = pickle.load (f)
    print (contenidoArchivos)
    f.close()
    
    
    
exportarDatos()
importarDatos()



