#FUNCIONES AUXILIARES
def diccionario(s): #Diccionario crea un diccionario en donde cada key será una letra sin repetir y los values serán las posiciones de las letras de la cadena ingresada
    dic={}
    for i in range(len(s)):
        if s[i] not in dic:
            dic[s[i]]=[i]
        else:
            dic[s[i]]=dic[s[i]]+[i]
    return dic

def encriptar(s): #Encriptar crea una lista de "_" en cada posicion de la cadena ingresada
    palabraoculta=[]
    for elemento in s:
        palabraoculta.append("_")
    return palabraoculta

#////////////////////////////////////////////////////////////////////

#PROGRAMA PRINCIPAL
def main(vidas=6):
    palabra=input("Ingrese la palabra a adivinar: ")
    palabra= palabra.lower()
    palabra_encriptada=encriptar(palabra)
    for i in range(20):
        print("")
    dic=diccionario(palabra)
    
    letras=[]
    
    print(palabra_encriptada)
    
    print(letras)
    
    while vidas!=0 and len(dic)!=0:
        intento=input("Ingrese la letra posible (sin tildes o mayúsculas): ")

        if len(intento)== 1 and intento.isalpha() and intento not in letras:
            if intento in dic:
                for elemento in dic[intento]:
                    palabra_encriptada[elemento]=[intento]
                dic.pop(intento)
                letras.append(intento)
                print(letras)
                print(palabra_encriptada)
            else:
                letras.append(intento)
                print(letras)
                print(palabra_encriptada)
                vidas=vidas-1
        else:
            print("El valor ingresado no es una letra válida")

    if vidas!=0:
        print(f"Felicidades adivinaste la palabra: {palabra}")
    else:
        print(f"No adivinó la palabra, aquella era: {palabra}")

#EJECUCIÓN
if __name__ == "__main__":

    main()