# TEMA 11. EJERCICIO 1.
# En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: 
# la columna id de tipo entero, 
# la columna nombre que será de tipo texto y 
# la columna apellido que también será de tipo texto.

# Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.

# Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.


import sqlite3

# Conexión a Base datos
conn = sqlite3.connect ('e11cristinabbdd.bd')
cursor = conn.cursor()

# Crear Tabla
cursor.execute ("CREATE TABLE Alumnos (id INTEGER PRIMARY KEY, nombre TEXT, apellido TEXT)")

cursor.execute ("INSERT INTO Alumnos (id, nombre, apellido) VALUES (1, 'Cristina', 'VM')")
cursor.execute ("INSERT INTO Alumnos (id, nombre, apellido) VALUES (2, 'Marta', 'VM')")
cursor.execute ("INSERT INTO Alumnos (id, nombre, apellido) VALUES (3, 'Abril', 'TB')")
cursor.execute ("INSERT INTO Alumnos (id, nombre, apellido) VALUES (4, 'Laia', 'GH')")
cursor.execute ("INSERT INTO Alumnos (id, nombre, apellido) VALUES (5, 'Sergio', 'RC')")
cursor.execute ("INSERT INTO Alumnos (id, nombre, apellido) VALUES (6, 'Adrián', 'DS')")
cursor.execute ("INSERT INTO Alumnos (id, nombre, apellido) VALUES (7, 'Roberto', 'VV')")
cursor.execute ("INSERT INTO Alumnos (id, nombre, apellido) VALUES (8, 'Andrés', 'SS')")


# Commit
conn.commit()

# Buscar Usuario
var1 = input ('¿Cómo te llamas?: ')
cursor.execute (f"SELECT * FROM Alumnos WHERE nombre='{var1}'")

busqueda = cursor.fetchone()
print (busqueda)

# Cerrar el cursor
cursor.close()

# Cerrar conexión con la base de datos
conn.close()
