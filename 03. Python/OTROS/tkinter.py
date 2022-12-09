import tkinter as tk
from tkinter import ttk


window = tk.Tk ()

# window.columnconfigure (0, weight=1)
# window.columnconfigure (0, weight=3)

# ...

#LABEL
# label1 = tk.Label (window, text= 'Posicionamiento absoluto', bg='blue', fg='white')
# label1.place (x=10, y=50)

# label2 = tk.Label (window, text= 'Otro', bg='red', fg='yellow')
# label2.place (relx=0.10, rely=0.15, relwidth=0.5, anchor='ne')

# -----------------------------------------------------#

#LISTA
# lista = ['Windows', 'macOS', 'Linux', 'MS DOS', 'AmigaOS', 'BeOS', 'OS/2']
# lista_items = tk.StringVar (value=lista)
# listbox = tk.Listbox (window, height=30, listvariable=lista_items)
# listbox.grid (row=0, column=0, sticky=tk.W, padx=50, pady=50)


# frame = ttk.Frame (window)
# frame.grid (row=0, column=0, sticky=tk.W, padx=50, pady=50)

# label = ttk.Label (frame, text = 'Hola')
# label.grid (row=0, column=0, sticky=tk.W, padx=50, pady=50)

# -----------------------------------------------------#

# #RADIOBUTTON
# seleccionado = tk.StringVar ()
# r1 = ttk.Radiobutton (window, text='Si', value='1', variable=seleccionado)
# r2 = ttk.Radiobutton (window, text='No', value='2', variable=seleccionado)
# r3 = ttk.Radiobutton (window, text='Quizá', value='3', variable=seleccionado)

# r1.grid (row=1, column=0, pady=5, padx=5)
# r2.grid (row=2, column=0, pady=5, padx=5)
# r3.grid (row=3, column=0, pady=5, padx=5)


# seleccionado2 = tk.StringVar ()
# rs1 = ttk.Radiobutton (window, text='Si2', value='12', variable=seleccionado2)
# rs1.grid (row=1, column=1, pady=5, padx=5)

# -----------------------------------------------------#


# CHECKBOX

# def mifuncion():
#     print ('Clicado')
    
    
# seleccionado=tk.StringVar()
# checkbox=ttk.Checkbutton(window, text='Acepto las condiciones', variable=seleccionado, command=mifuncion)

# checkbox.grid (row=1, column=0, pady=5, padx=5)

# -----------------------------------------------------#

#EVENTOS
# def salir (event):
#     print ('Adios')
#     window.quit()

# def saludar (event):
#     print ('Clik en saludar')
    
# def saludarDobleClick (event):
#     print ('Doble click en saludar')


# boton = tk.Button (window, text='Haz click')
# boton.pack()

# boton.bind ('<Button-1>', saludar)
# boton.bind ('<Double-1>', saludarDobleClick)


# botonSalir = tk.Button (window, text='Salir')
# botonSalir.pack()
# botonSalir.bind ('<Button-1>', salir)

window.mainloop()