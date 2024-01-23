
import tkinter as tk
from tkinter import ttk
import mysql.connector
from datetime import datetime


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Empleados",
    port=3308
)
cursor = conn.cursor()


def mostrar_empleados():
    cursor.execute("SELECT * FROM ControlDeEmpleados")
    empleados = cursor.fetchall()
    limpiar_tabla()
    for empleado in empleados:
        tree.insert("", tk.END, values=empleado)

def agregar_empleado():
    
    nombre = entry_nombre.get()
    telefono = entry_telefono.get()
    domicilio = entry_domicilio.get()
    dni = entry_dni.get()
    contraseña = entry_contraseña.get()
    designacion = entry_designacion.get()

    query = "INSERT INTO ControlDeEmpleados (Nombre, Telefono, Domicilio, DNI, Contraseña, Designacion) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (nombre, telefono, domicilio, dni, contraseña, designacion)

    cursor.execute(query, values)
    conn.commit()
    limpiar_formulario()
    mostrar_empleados()

def actualizar_empleado():
    
    item = tree.selection()
    if item:
        id_empleado = tree.item(item, "values")[0]
        nombre = entry_nombre.get()
        telefono = entry_telefono.get()
        domicilio = entry_domicilio.get()
        dni = entry_dni.get()
        contraseña = entry_contraseña.get()
        designacion = entry_designacion.get()

        query = "UPDATE ControlDeEmpleados SET Nombre=%s, Telefono=%s, Domicilio=%s, DNI=%s, Contraseña=%s, Designacion=%s WHERE ID=%s"
        values = (nombre, telefono, domicilio, dni, contraseña, designacion, id_empleado)

        cursor.execute(query, values)
        conn.commit()
        limpiar_formulario()
        mostrar_empleados()

def eliminar_empleado():
    
    item = tree.selection()
    if item:
        id_empleado = tree.item(item, "values")[0]
        query = "DELETE FROM ControlDeEmpleados WHERE ID=%s"
        cursor.execute(query, (id_empleado,))
        conn.commit()
        limpiar_formulario()
        mostrar_empleados()

def limpiar_formulario():
    entry_nombre.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    entry_domicilio.delete(0, tk.END)
    entry_dni.delete(0, tk.END)
    entry_contraseña.delete(0, tk.END)
    entry_designacion.delete(0, tk.END)

def limpiar_tabla():
    for row in tree.get_children():
        tree.delete(row)


root = tk.Tk()
root.title("Control de Empleados")


titulo_frame = ttk.Frame(root)
titulo_frame.grid(row=0, column=0, columnspan=2, pady=10)


ttk.Label(titulo_frame, text="Mantenimiento de Empleados", font=("Helvetica", 16)).grid(row=0, column=0, padx=5, pady=5)


label_fecha_hora = ttk.Label(titulo_frame, text="", font=("Helvetica", 12))
label_fecha_hora.grid(row=0, column=1, padx=5, pady=5, sticky="e")


def actualizar_fecha_hora():
    fecha_hora_str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    label_fecha_hora.config(text=fecha_hora_str)
    root.after(1000, actualizar_fecha_hora)

actualizar_fecha_hora()


form_frame = ttk.Frame(root)
form_frame.grid(row=1, column=0, padx=10, pady=10)

ttk.Label(form_frame, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
entry_nombre = ttk.Entry(form_frame)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(form_frame, text="Teléfono:").grid(row=1, column=0, padx=5, pady=5)
entry_telefono = ttk.Entry(form_frame)
entry_telefono.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(form_frame, text="Domicilio:").grid(row=2, column=0, padx=5, pady=5)
entry_domicilio = ttk.Entry(form_frame)
entry_domicilio.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(form_frame, text="DNI:").grid(row=3, column=0, padx=5, pady=5)
entry_dni = ttk.Entry(form_frame)
entry_dni.grid(row=3, column=1, padx=5, pady=5)

ttk.Label(form_frame, text="Contraseña:").grid(row=4, column=0, padx=5, pady=5)
entry_contraseña = ttk.Entry(form_frame)
entry_contraseña.grid(row=4, column=1, padx=5, pady=5)

ttk.Label(form_frame, text="Designación:").grid(row=5, column=0, padx=5, pady=5)
entry_designacion = ttk.Entry(form_frame)
entry_designacion.grid(row=5, column=1, padx=5, pady=5)

ttk.Button(form_frame, text="Agregar", command=agregar_empleado).grid(row=6, column=0, columnspan=2, pady=10)
ttk.Button(form_frame, text="Actualizar", command=actualizar_empleado).grid(row=7, column=0, columnspan=2, pady=10)
ttk.Button(form_frame, text="Eliminar", command=eliminar_empleado).grid(row=8, column=0, columnspan=2, pady=10)


tree_frame = ttk.Frame(root)
tree_frame.grid(row=1, column=1, padx=10, pady=10)

tree = ttk.Treeview(tree_frame, columns=("ID", "Nombre", "Teléfono", "Domicilio", "DNI", "Contraseña", "Designación"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Nombre", text="Nombre")
tree.heading("Teléfono", text="Teléfono")
tree.heading("Domicilio", text="Domicilio")
tree.heading("DNI", text="DNI")
tree.heading("Contraseña", text="Contraseña")
tree.heading("Designación", text="Designación")
tree.pack(fill=tk.BOTH, expand=1)


ttk.Button(root, text="Mostrar Empleados", command=mostrar_empleados).grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()