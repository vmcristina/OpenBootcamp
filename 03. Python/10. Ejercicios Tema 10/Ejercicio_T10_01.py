
import tkinter as tk
from tkinter import ttk

raiz = tk.Tk()

raiz.columnconfigure (0, weight=1)
raiz.columnconfigure (0, weight=4)


def reiniciar (event):
    print ('Reiiiiinicio')
    seleccionado.set (None)

#CREAR RADIOBUTTON
seleccionado = tk.StringVar ()
r1 = ttk.Radiobutton (raiz, text= 'Primer botón', value='1', variable=seleccionado)
r2 = ttk.Radiobutton (raiz, text= 'Segundo botón', value='2', variable=seleccionado)
r3 = ttk.Radiobutton (raiz, text= 'Tercer botón', value='3', variable=seleccionado)
r4 = ttk.Radiobutton (raiz, text= 'Cuarto botón', value='4', variable=seleccionado)

#POSICIONAR RADIOBUTTON
r1.grid (row=1, column=0, pady=5, padx=5)
r2.grid (row=2, column=0, pady=5, padx=5)
r3.grid (row=3, column=0, pady=5, padx=5)
r4.grid (row=4, column=0, pady=5, padx=5)

#CREAR, POSICIONAR Y CONFIGURAR BOTON
botonReinicio = ttk.Button (raiz, text='REINICIAR')
botonReinicio.grid (row=5, column=0, pady=5, padx=5)
botonReinicio.bind ('<Button-1>', reiniciar)



raiz.mainloop()