#En este gestor de entradas para el cine, se recopila y almacena las peliculas disponibles y sus entradas disponibles, incluso pudiendo interactuar con ellas
print("==============================================================")
print("GESTOR DE ENTRADAS PARA EL CINE")
print("==============================================================")
print()
#agregar_peliculas: Number String Number -> listof String Number
#Comenzando con una lista vacía, se ingresa la cantidad de peliculas a las cuales asignar entradas, luego el nombre de la pelicula y la cantidad de entradas disponibles para esta.
#En caso de no ingresar un valor númerico, se mostrará el except
def agregar_peliculas():
    movies = []#Lista Vacia
    while True:
        try: 
            cant_peliculas = int(input("Cuantas peliculas hay disponibles?: "))
            break
        except:
            print("ingrese un valor numérico")
    for i in range(cant_peliculas):

        nombre_pelicula = input("ingrese el nombre de la pelicula: ")

        cant_entradas= int(input("introduzca la cantidad de entradas disponibles para la pelicula ingresada: "))

        pelicula = (nombre_pelicula,cant_entradas)#Elemento completo que ingresará a la lista, conformado por el nombre de la pelicula y sus entradas disponibles

        movies.append(pelicula)  
    return movies

peliculas= agregar_peliculas()#Renombre de la funcion

print(f"Estas son las peliculas disponibles: {peliculas}")

pelicula_trj = int(input("ingrese el numero de la pelicula con la que quiere trabajar: ")) #"0" corresponde a la primer pelicula asignada, el numero "1" para la segunda

print(f"esta es la pelicula {pelicula_trj}: {peliculas[pelicula_trj]}")

