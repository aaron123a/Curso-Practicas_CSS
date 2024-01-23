import tkinter as tk
from tkinter import ttk
import mysql.connector
from datetime import datetime


try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Empleados",
        port=3308
    )
    cursor = conn.cursor()
except mysql.connector.Error as e:
    print(f"Error conectando a MySQL: {e}")


def actualizar_hora_fecha():
    now = datetime.now()
    fecha_hora_actual = now.strftime("%Y-%m-%d %H:%M:%S")
    etiqueta_fecha_hora.config(text=fecha_hora_actual)
    root.after(1000, actualizar_hora_fecha)  


def buscar_cliente():
    
    pass


def mostrar_contenido_base_datos():
    
    for row in tree.get_children():
        tree.delete(row)

    
    query = "SELECT * FROM facturacion"
    cursor.execute(query)
    result = cursor.fetchall()

    
    for row in result:
        tree.insert("", "end", values=row)


def calcular_total():
    
    pass

def generar_factura():
    
    pass

def limpiar_facturacion():
    
    categoria.set("")
    sub_categoria.set("")
    articulo.set("")
    cantidad.set("")
    precio.set("")

    
    for row in tree.get_children():
        tree.delete(row)

    


def eliminar_registro():
    
    selected_item = tree.selection()
    if not selected_item:
        return  

    
    factura_id = tree.item(selected_item, "values")[0]

   
    query = f"DELETE FROM facturacion WHERE N_Factura = {factura_id}"
    cursor.execute(query)
    conn.commit()

    
    tree.delete(selected_item)


def salir():
    root.destroy()


root = tk.Tk()
root.title("Facturación")


etiqueta_titulo = tk.Label(root, text="Sistema de Facturación", font=("Helvetica", 16))
etiqueta_titulo.grid(row=0, column=0, columnspan=4, sticky="nsew")


frame_cliente = tk.LabelFrame(root, text="Información de Cliente")
frame_facturacion = tk.LabelFrame(root, text="FACTURACIÓN")


tk.Label(frame_cliente, text="Factura No.").grid(row=0, column=0)
factura_no = tk.Entry(frame_cliente)
factura_no.grid(row=0, column=1)

tk.Label(frame_cliente, text="Nombre del Cliente:").grid(row=1, column=0)
nombre_cliente = tk.Entry(frame_cliente)
nombre_cliente.grid(row=1, column=1)

tk.Label(frame_cliente, text="Teléfono:").grid(row=2, column=0)
telefono = tk.Entry(frame_cliente)
telefono.grid(row=2, column=1)


boton_buscar = tk.Button(frame_cliente, text="Buscar", command=buscar_cliente)
boton_buscar.grid(row=3, column=0, columnspan=2)


tk.Label(frame_facturacion, text="Seleccionar Categoría").grid(row=0, column=0)
categoria = ttk.Combobox(frame_facturacion)
categoria.grid(row=0, column=1)

tk.Label(frame_facturacion, text="Sub-Categoría:").grid(row=1, column=0)
sub_categoria = ttk.Combobox(frame_facturacion)
sub_categoria.grid(row=1, column=1)

tk.Label(frame_facturacion, text="Artículo:").grid(row=2, column=0)
articulo = ttk.Combobox(frame_facturacion)
articulo.grid(row=2, column=1)

tk.Label(frame_facturacion, text="Cantidad:").grid(row=3, column=0)
cantidad = ttk.Combobox(frame_facturacion)
cantidad.grid(row=3, column=1)

tk.Label(frame_facturacion, text="Precio:").grid(row=4, column=0)
precio = tk.Entry(frame_facturacion)
precio.grid(row=4, column=1)

opciones_categoria = ["Tecnologia", "Alimentos", "Calzados"]
opciones_sub_categoria = ["Ninguno", "Enlatados", "Panes", "Zapatillas", "Zapatos"]
opciones_articulo = ["Durasno", "Atun", "sardina", "baget", "croissant", "Nike", "Adidas", "Puma", "Gucci"]
opciones_cantidad = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

def generar_factura():
    
    factura_no_valor = factura_no.get()
    nombre_cliente_valor = nombre_cliente.get()
    telefono_valor = telefono.get()
    categoria_valor = categoria.get()
    sub_categoria_valor = sub_categoria.get()
    articulo_valor = articulo.get()
    cantidad_valor = cantidad.get()
    precio_valor = precio.get()

   
    query_cliente = "INSERT INTO facturacion (Nombre, Telefono, Categoria, Sub_categoria, Articulo, Cantidad, Precio) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values_cliente = (nombre_cliente_valor, telefono_valor, categoria_valor, sub_categoria_valor, articulo_valor, cantidad_valor, precio_valor)
    cursor.execute(query_cliente, values_cliente)
    conn.commit()

    
    tree.insert("", "end", values=(factura_no_valor, nombre_cliente_valor, telefono_valor, categoria_valor, sub_categoria_valor, articulo_valor, cantidad_valor, precio_valor))

    
    limpiar_facturacion()

def salir():
    conn.close()  
    root.destroy()


boton_salir = tk.Button(root, text="Salir", command=salir)
boton_salir.grid(row=3, column=3, padx=10, pady=10, sticky="se")
    

categoria['values'] = opciones_categoria
sub_categoria['values'] = opciones_sub_categoria
articulo['values'] = opciones_articulo
cantidad['values'] = opciones_cantidad


boton_total = tk.Button(frame_facturacion, text="Total", command=mostrar_contenido_base_datos)
boton_total.grid(row=5, column=0)

boton_generar = tk.Button(frame_facturacion, text="Generar", command=generar_factura)
boton_generar.grid(row=5, column=1)

boton_limpiar_facturacion = tk.Button(frame_facturacion, text="Limpiar", command=limpiar_facturacion)
boton_limpiar_facturacion.grid(row=5, column=2)


boton_eliminar_facturacion = tk.Button(frame_facturacion, text="Eliminar", command=eliminar_registro)
boton_eliminar_facturacion.grid(row=5, column=3)


tree_frame = ttk.Frame(root)
tree_frame.grid(row=1, column=3, padx=10, pady=10, sticky="nsew")

tree = ttk.Treeview(tree_frame, columns=("N_Factura", "Nombre", "Teléfono", "Categoría", "Sub_Categoría", "Artículo", "Cantidad", "Precio"), show="headings", height=15)
tree.heading("N_Factura", text="N_Factura")
tree.heading("Nombre", text="Nombre")
tree.heading("Teléfono", text="Teléfono")
tree.heading("Categoría", text="Categoría")
tree.heading("Sub_Categoría", text="Sub_Categoría")
tree.heading("Artículo", text="Artículo")
tree.heading("Cantidad", text="Cantidad")
tree.heading("Precio", text="Precio")


column_widths = [100, 100, 100, 100, 100, 100, 100, 100]  
for i, width in enumerate(column_widths):
    tree.column(tree["columns"][i], width=width, anchor="center")

tree.pack(fill=tk.BOTH, expand=1)  


frame_cliente.grid(row=1, column=0, columnspan=2, sticky="nsew")
frame_facturacion.grid(row=1, column=2, sticky="nsew")


etiqueta_fecha_hora = tk.Label(root, text="", font=("Helvetica", 12))
etiqueta_fecha_hora.grid(row=2, column=3, padx=10, pady=10, sticky="e")


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=2)
root.columnconfigure(3, weight=2)
root.rowconfigure(0, weight=0)  
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=0)  


actualizar_hora_fecha()


root.mainloop()