#Este es un registro de entradas para cualquier evento en general, donde se podrá ingresar el nombre y apellido de las personas que adquirieron su entrada.
#Con un límite pre-establecido y modificable solamente antes de ejecutar el programa
print("=====================================================================")
print("BIENVENIDO AL REGISTRO DE ENTRADAS ANTICIPADAS DE [Nombre de evento]")
print("=====================================================================")
#Área de definiciones
anticipadas = []#Lista vacia donde guardará los datos de la persona

limite_registros = 150 #Límite de entradas adquiribles
#Área de funciones
#Registro de personas: Number String List(String)-> List(String)
#Si la cantidad de datos ingresados no supera al límite, se ingresará el nombre y apellido de la persona que adquirió la entrada o, escribir salir para dejar de agregar personas.
while len(anticipadas) < limite_registros:
    
    nuevo_dato = input(f"Ingresa el nombre y apellido de la persona que compró su anticipada ({len(anticipadas) + 1}/{limite_registros}) o escribe 'salir' para terminar: ") #Ingrese el nombre en minusculas y sin tildes

    if nuevo_dato.lower() == 'salir':
        break 
    anticipadas.append(nuevo_dato)
#Área de comprobación de existencia de los datos en la lista
print("=====================================================================")
print("CENTRO DE COMPROBACION DE ENTRADAS ADQUIRIDAS")
print("=====================================================================")
#Comprobacion: String List(String) -> Boolean String
#Comprueba la igualdad de datos ingresados con la existencia de alguno en la lista, devuelve true en caso de coincidir, false en caso contrario.
#Ingresando "TODOS" se imprimirá en pantalla la lista completa.
opcion_3 = input("Desea comprobar quien adquirió la entrada ? si o no: ")
opcion_3 = opcion_3.lower()
while opcion_3 == "si":
        comprobar = input("Inserte el nombre y apellido de la persona a verificar, en caso de adquirir la lista completa, escribir TODOS: ")
        if comprobar == "TODOS":
             print(f"{anticipadas}")
        print(comprobar in anticipadas)          
        opcion_3 = input("Desea seguir comprobando ? si o no: ")
        opcion_3 = opcion_3.lower()
        if not opcion_3 == "si":
            break

input("Presiona enter para salir del programa")#Finalización del programa.