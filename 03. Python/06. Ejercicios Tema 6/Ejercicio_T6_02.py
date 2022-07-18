# En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. 
# Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.


class Alumno ():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        
        if self.nota >= 5:
            print ("Tu nota es:",self.nota, "has aprobado")
        else:
            print ("Tu nota es:",self.nota, "has suspendido")
            
a = Alumno ("Julia", 3)
b = Alumno ("Enriqueta", 10)
            
    