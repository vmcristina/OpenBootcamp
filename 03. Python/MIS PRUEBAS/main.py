# Crear una clase: constructor
# Descripción técnica e informal 
# Crear destructor
# Crear Logging

# (a través de módulos y paquetes)
# Crear métodos inputs 
# Buscar Usuario a través de "filter"
# DOS Método Get (DNI y Teléfono)
# Método Set 
# Exportar usuario a TXT 
# Exportar usuario a Bin 
# Importar usuario 
# Borrar datos usuario, objeto asociado y volver a exportar datos

import pickle

class Usuario ():
    def __init__ (self):
        self.__nombre = ''
        self.__apellido = ''
        self.__dni = ''
        self.__telefono = ''
    
    def __str__ (self):
        return ('Usuario de entrada a taller')
        
    def __repr__ (self):
        return (f'Objeto: {self.__nombre}\nClase: {self.__class__}')
    
    def __del__ (self):
        print ('Elemento borrado en:', self.__class__)
        
        
        
    def entradaUsuario (self):
        self.__nombre = input ('Nombre: ')
        self.__apellido = input ('Apellido: ')
        self.__dni = input ('DNI: ')
        self.__telefono = input ('Teléfono: ')
    
    def exportarDatos (self):
        users = [self.__dni, self.__telefono, self.__nombre, self.__apellido]
        f = open ('clientes_recepcion.txt', 'a')
        f2 = open ('clientes_recepcion_bin', 'wb')
        pickle.dump (users, f2)
        f.write ('DNI/NIE\t\tTELÉFONO\tNOMBRE\t\tAPELLIDO\n')
        for i in users:
            f.write (i + '\t')
        f.write ('\n')
        f.close(), f2.close()
        
    
    def importarDatos (self):
        datoIn = input ('Escribe tu búsqueda: ')
        letras = list (map(chr, range(97, 123)))
        
        for i in datoIn [-1]:
            pass
        
        for x in letras:
            if x == i:
                print ('El dato introducido es un DNI')
                break
    
        else:
            print ('El dato introducido es Teléfono')
            
    
        f = open ('clientes_recepcion.txt', 'r')
        contenido = f.read ()
        for linea in contenido:
            if datoIn == linea:
                print (linea)
        
        
        
        
        print (contenido)
        
    def nombreDni (self):
        '''Función para descubrir si el dato introducido es Teléfono o DNI'''
        datoIn = input ('Escribe tu búsqueda: ')
        letras = list (map(chr, range(97, 123)))
    
        for i in datoIn [-1]:
            pass
     
        for x in letras:
            if x == i:
                print ('El dato introducido es un DNI')
                break
    
        else:
            print ('El dato introducido es Teléfono')

            if letras == True:
                print ('IMPRIMO LISTA', letras [-3:2])
        
    def getInfo (self):
        '''Recupera los datos del contacto, introduciendo la instancia'''
        print (f'====== DATOS DEL CONTACTO ======\nNombre: {self.__nombre.capitalize()}\nApellido: {self.__apellido.capitalize()}\nDNI: {self.__dni.capitalize()} \nTeléfono: {self.__telefono}')
        






u1 = Usuario ()
u1.entradaUsuario ()
u1.exportarDatos ()
u1.importarDatos ()
u1.nombreDni()

