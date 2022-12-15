#En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual 
# debe de contener una lista de elementos seleccionables, 
# también debe de tener un label con el texto que queráis.

import tkinter
from tkinter import StringVar, ttk
from turtle import width



#CREAR frame/VENTANA
root = tkinter.Tk()



#CREAR Y COLOCAR FRAME
frame = ttk.Frame(root)
frame.grid (row=0, column=0)


frame.columnconfigure (0, weight=1)
frame.columnconfigure (0, weight=1)


#LABEL 
label1 = tkinter.Label (frame, text='Lista de la compra:', bg='orange', fg='lightgreen')
label1.grid (row=0, column=0)


#RADIOBUTTON
selected=tkinter.StringVar()

r1 = ttk.Radiobutton (frame, text='Naranjas', value=1, variable=selected)
r1.grid (row=1, column=0, padx=5, pady=5)
r2 = ttk.Radiobutton (frame, text='Limones', value=2, variable=selected)
r2.grid (row=2, column=0, padx=5, pady=5)
r3 = ttk.Radiobutton (frame, text='Bananas', value=3, variable=selected)
r3.grid (row=3, column=0, padx=5, pady=5)



root.mainloop()





