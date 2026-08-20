##Funciones de script
import tkinter as tk
from tkinter import messagebox

##Funciones secundarias 
def enviar_msjbox():
    nombre = tbNombre.get()
    messagebox.showinfo("Programacion Avanzada", f"Bienvenido, {nombre}!")


 
ventana = tk.Tk()
ventana.title("Actividad 02- Pantallaa EN Blaco")
ventana.geometry("450x250")
ventana .configure(bg="#663E78")
## Elementos graficos
lbNombre =tk.Label(ventana, text="Nombre:", bg="#663E78", fg="Black")
lbNombre.place (x=60, y=60)
tbNombre=tk.Entry()
tbNombre .place(x=120, y=60)
btnAceptar= tk.Button(ventana, text="Aceptar", command=enviar_msjbox)
btnAceptar.place(x=120, y=120)
btnCancelar= tk.Button(ventana, text="Cancelar", command= ventana.quit)
btnCancelar.place(x=180, y=120)

ventana.mainloop()

