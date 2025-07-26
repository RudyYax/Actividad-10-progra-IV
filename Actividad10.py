def invertir(palabra):
    return palabra[::-1]
print(invertir('Palabra'))

opcion = 0
print("Bienvenidos Actividad 10")
while(opcion != 6):
    print("Bienvenidos menu iteracción")
    print("1.- Invertir una cadena de texto")
    print("2.- Calcular la suma de dos numeros ")
    print("3.- Imprimir una cuenta regresiva desde N números naturales hasta 1 ")
    print("4.- Sumar los digitos de un número")
    print("5.- Contar cuantos díjitos tiene un número")
    print("6.- Salir")
    opcion = int(input("Ingrese la opcion que desee: "))
    match(opcion):
        case 1:
            print("\n Bienvenido a escogido la opcion 1")
            print("Invertir Una cadena de texto")
            palabra = input("Ingrese la palabra que desea invertir: ")
            print(invertir(palabra))



