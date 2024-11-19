import json
import random

diccionario_inventario = {}

class Producto:
    def __init__(self,codigo,nombre,precio,cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def __str__(self):
        return f"{self.codigo}-{self.nombre}-{self.precio}-{self.cantidad}"

def caragar_inventario():
    global diccionario_inventario
    try:
        with open("inventario.json","r")as archivo:
            inventario_json = json.load(archivo)
            diccionario_inventario = {producto: Producto(producto,datos['nombre'],datos['precio'],datos['cantidad']) for producto,datos in inventario_json.items()}
    except:
        print("Error al cargar el archivo o archivo no encontrado, se creará un inventario vacio")
        diccionario_inventario = {}

def mostrar_inventario():
    for producto in diccionario_inventario.values():
        print(producto)

def agregar_producto():
    codigo=input("Ingrese el codigo del producto: ")
    
    for codigo1 in diccionario_inventario:
        if codigo1 == codigo:
            print("El codigo ya existe ,no se puede agregar")
            return
    
    nombre=input("Ingrese el nombre del producto: ")

    try:
        cantidad=int(input("Ingrese la cantidad del producto: "))
    except:
        print("Error al ingresar la cantidad,no puede ser una cadena de texto")
        return
    
    try:
        precio=float(input("Ingrese el precio del producto: "))
    except:
        print("Error al ingresar el precio,no puede ser una cadena de texto")
        return
    
    Producto1 = Producto(codigo,nombre,precio,cantidad)
    diccionario_inventario[codigo] = Producto1

def actualizar_producto():
    codigo=input("Ingrese el codigo del producto: ")
    if codigo in diccionario_inventario:
        try:
            cantidad=int(input("Ingrese la cantidad del producto: "))
        except:
            print("Error al ingresar la cantidad,no puede ser una cadena de texto")
            return
        
        try:
            precio=float(input("Ingrese el precio del producto: "))
        except:
            print("Error al ingresar el precio,no puede ser una cadena de texto")
            return
        
        Producto1 = Producto(codigo,diccionario_inventario[codigo].nombre,precio,cantidad)
        diccionario_inventario[codigo] = Producto1
    else:
        print("El codigo no existe")


def guardar_inventario():
    inventario_json = {producto_id:{"nombre":producto.nombre,"precio":producto.precio,"cantidad":producto.cantidad} for producto_id,producto in diccionario_inventario.items()}
    with open("inventario.json","w") as archivo:
        json.dump(inventario_json,archivo,indent=4)
        

           


caragar_inventario()
mostrar_inventario()
agregar_producto()
mostrar_inventario()
actualizar_producto()
mostrar_inventario()
guardar_inventario()