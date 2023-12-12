#Alex Santiago Carrero Salazar/ Jean Sebastian Vigoya / 2749613 / ejercicio 4 y 5
from ast import While
from pickle import TRUE

#se hace una lista desocupada para guardar las palabras y con un bucle pedimos al usuario ingrese 20 palabras
palabras=[]
for i in range(20):
    palabra=input(f"Igrese la palabra {i+1}: ")
    palabras.append(palabra)
#se utiliza una funcion que ordene la lista de palabras por su tamñano de la mas larga a la mas corta  
def ordenar_por_tamaño(palabras):
    return sorted(palabras, key=len, reverse=True)
#se muestra un menu con opciones al usuario 
while True:
    print("\n Seleccione una opcion: ")
    print("1.Orden alfabetico")
    print("2.Orden de tamaño, de la mas larga a la mas corta")
    print("3.Orden aleatorio")
    print("4.orden inverso al ingresado")
    print("5.Orden igual al ingresado")
    print("6.Salir")
    seleccion=input("Elija una opcion:")
    match seleccion:
            case "1":
                palabras_ordenadas=sorted(palabras)
            case "2":
                palabras_ordenadas=ordenar_por_tamaño(palabras)
            case "3":
                import random
                random.shuffle(palabras)
                palabras_ordenadas=palabras
            case "4":
                palabras_ordenadas=list(reversed(palabras))
            case "5":
                palabras_ordenadas=palabras
            case "6":
                print("salir")
            case "_":
                print("Opcion no valida. Elija una opcion del 1 al 6.")
                continue
#se observa la lista de palabras segun la opcion elegida por el usuario 
    print("\nPalabras ordenadas")
    for palabra in palabras_ordenadas:
            print(palabra)