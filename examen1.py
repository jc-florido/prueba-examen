
import json
import random

# Diccionario para almacenar canciones
diccionario_canciones = {}

# Clase para definir una canción
class Cancion:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

# Función para crear una canción y agregarla al diccionario
def crear_cancion():
    titulo = input("Ingrese el titulo de la cancion: ")
    autor = input("Ingrese el autor de la cancion: ")

    if titulo in diccionario_canciones:
        print("La canción ya existe")
        return

    cancion_nueva = Cancion(titulo, autor)
    diccionario_canciones[titulo] = cancion_nueva

# Función para mostrar la información de una canción
def mostrar_informacion_cancion():
    titulo = input("Ingrese el titulo de la cancion: ")

    if titulo in diccionario_canciones:
        print(diccionario_canciones[titulo])
    else:
        print("La canción no existe")

# Función para cargar canciones desde un archivo JSON
def cargar_lista_Json():
    global diccionario_canciones
    with open("canciones.json", "r") as archivo:
        canciones_json = json.load(archivo)
        diccionario_canciones = {titulo: Cancion(titulo, datos['autor']) for titulo, datos in canciones_json.items()}

# Función para guardar canciones en un archivo JSON
def guardar_lista_Json():
    canciones_json = {titulo: {"titulo": cancion.titulo, "autor": cancion.autor} for titulo, cancion in diccionario_canciones.items()}
    with open("canciones.json", "w") as archivo:
        json.dump(canciones_json, archivo)

# Función para contar el número de canciones
def contar_canciones():
    print("El número de canciones en la lista es:", len(diccionario_canciones))

# Función para buscar canciones de un autor
def buscar_canciones_artista():
    autor = input("Ingrese el autor de la cancion: ")
    canciones_encontradas = [str(cancion) for cancion in diccionario_canciones.values() if cancion.autor == autor]
    
    if canciones_encontradas:
        print("\n".join(canciones_encontradas))
    else:
        print("No se encontraron canciones de ese autor o el autor no existe")

# Función para ordenar canciones alfabéticamente
def ordenar_alfabeticamente():
    lista_ordenada = sorted(diccionario_canciones.keys())
    print("Canciones ordenadas alfabéticamente:")
    for titulo in lista_ordenada:
        print(diccionario_canciones[titulo])

# Función para crear una lista aleatoria de canciones
def crear_lista_aleatoria():
    numero_canciones = int(input("Ingrese el numero de canciones que desea en la lista: "))
    if numero_canciones > len(diccionario_canciones):
        print("No hay suficientes canciones en la lista.")
        return

    lista_canciones = random.sample(list(diccionario_canciones.values()), numero_canciones)
    for cancion in lista_canciones:
        print(cancion)
    return lista_canciones

# Función para guardar una lista de reproducción en un archivo de texto
def guardar_lista_txt():
    lista_canciones = crear_lista_aleatoria()
    if lista_canciones:
        with open("canciones.txt", "w") as archivo:
            for cancion in lista_canciones:
                archivo.write(f"{cancion}\n")

# Menú para ejecutar el programa
def menu():
    while True:
        print("\n1. Crear canción")
        print("2. Mostrar información de canción")
        print("3. Cargar lista de canciones")
        print("4. Guardar lista de canciones")
        print("5. Contar canciones")
        print("6. Buscar canciones por autor")
        print("7. Ordenar canciones alfabéticamente")
        print("8. Crear lista aleatoria")
        print("9. Guardar lista en txt")
        print("10. Salir")
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            crear_cancion()
        elif opcion == 2:
            mostrar_informacion_cancion()
        elif opcion == 3:
            cargar_lista_Json()
        elif opcion == 4:
            guardar_lista_Json()
        elif opcion == 5:
            contar_canciones()
        elif opcion == 6:
            buscar_canciones_artista()
        elif opcion == 7:
            ordenar_alfabeticamente()
        elif opcion == 8:
            crear_lista_aleatoria()
        elif opcion == 9:
            guardar_lista_txt()
        elif opcion == 10:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida")

# Ejecutar el menú
menu()
