import tkinter as tk
from tkinter import ttk
import random
import string

# ==================
#   region Variables
TITLE = "pywdGenerator"
WINDOW_SIZE = "400x300"

#endregion
# ============================
#   region Funciones

def generar_password():
    longitud = int(slider_longitud.get())
    caracteres = ""

    if var_mayus.get():
        caracteres += string.ascii_uppercase
    if var_minus.get():
        caracteres += string.ascii_lowercase
    if var_numeros.get():
        caracteres += string.digits
    if var_simbolos.get():
        caracteres += string.punctuation

    if not caracteres:
        resultado.set("Selecciona al menos una opción")
        return

    password = "".join(random.choice(caracteres) for _ in range(longitud))
    resultado.set(password)

# =====================
#   region Interfaz 
root = tk.Tk()
root.title(TITLE)
root.geometry(WINDOW_SIZE)

# variables
var_mayus = tk.BooleanVar()
var_minus = tk.BooleanVar()
var_numeros = tk.BooleanVar()
var_simbolos = tk.BooleanVar()
resultado = tk.StringVar()

# checkboxes
ttk.Checkbutton(root, text="Mayúsculas (A-Z)", variable=var_mayus).pack(anchor="w", padx=20)
ttk.Checkbutton(root, text="Minúsculas (a-z)", variable=var_minus).pack(anchor="w", padx=20)
ttk.Checkbutton(root, text="Números (0-9)", variable=var_numeros).pack(anchor="w", padx=20)
ttk.Checkbutton(root, text="Símbolos (!@#$%)", variable=var_simbolos).pack(anchor="w", padx=20)

# slider longitud
tk.Label(root, text="Longitud de la contraseña:").pack()
slider_longitud = tk.Scale(root, from_=8, to=25, orient="horizontal")
slider_longitud.set(15)
slider_longitud.pack()

# botón generar
ttk.Button(root, text="Generar", command=generar_password).pack(pady=10)

# text esultado
tk.Entry(root, textvariable=resultado, width=40).pack(pady=5)

#endregion

#region Main

root.mainloop()
