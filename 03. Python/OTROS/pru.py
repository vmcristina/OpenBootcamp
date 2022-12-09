import tkinter as tk

# raiz = tk.Tk()


# label1 = tk.Label (raiz, text = 'Label1', bg = 'yellow', fg = 'blue')
# label1.pack (ipadx= 45, ipady=15, fill = 'x')

# label2 = tk.Label (raiz, text = 'Label2', bg = 'purple', fg = 'white')
# label2.pack (ipadx= 45, ipady=15, fill = 'x')

# label3 = tk.Label (raiz, text = 'Label3', bg = 'green', fg = 'red')
# label3.pack (ipadx= 45, ipady=15, fill = 'x')

# label4 = tk.Label (raiz, text = 'Label4', bg = 'black', fg = 'white')
# label4.pack (ipadx= 15, ipady=15, side = 'left', fill = 'x')

# label5 = tk.Label (raiz, text = 'Label5', bg = 'blue', fg = 'black')
# label5.pack (ipadx= 15, ipady=15, side = 'left', fill = 'x')

# label6 = tk.Label (raiz, text = 'Label6', bg = 'orange', fg = 'yellow')
# label6.pack (ipadx= 15, ipady=15, side = 'right', fill = 'x')



# raiz.mainloop()



window = tk.Tk ()
from tkinter import ttk

#USUARIO
window.columnconfigure (0, weight=1)
window.columnconfigure (1, weight=3)

#ETIQUETA USUARIO
username_label = ttk.Label(window, text = "Username:")
username_label.grid (row=0, column=0, sticky=tk.W, padx=5, pady=5)

#CAMPO USUARIO
username_entry = ttk.Entry (window)
username_entry.grid (row=0, column=1, sticky=tk.E, padx=5, pady=5)

#ETIQUETA PASSWORD
password_label = ttk.Label(window, text = "Password:")
password_label.grid (row=1, column=0, sticky=tk.W, padx=5, pady=5)


#CAMPO PASSWORD
password_entry = ttk.Entry (window, show='*')
password_entry.grid (row=1, column=1, sticky=tk.E, padx=5, pady=5)

#BOTON
login_button = ttk.Button (window, text = 'Login')
login_button.grid (row=3, column=1, sticky=tk.E)

window.mainloop()

