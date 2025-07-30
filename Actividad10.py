def invertir(palabra):
    return palabra[::-1]
print(invertir('Palabra'))
def sumar(numero):
    if numero == 0:
        return 0
    else:
         return numero + sumar(numero - 1)
def cuentaRegresiva(regresiva):
    if regresiva == 0:
        print("vamos")
    else:
        print(regresiva)
        return cuentaRegresiva(regresiva - 1)
def sumatoriaDigitos(digitos):
    if digitos < 10:
        return digitos
    else:
        n = digitos % 10
        e = digitos // 10
        return n + sumatoriaDigitos(e)
def ContarDigitos (n):
    if n < 10:
        return n
    else:
        e = n // 10
        return 1 + ContarDigitos(e)

opcion = 0
print("Bienvenidos Actividad 10")
while(opcion != 6):
    print("Bienvenidos menu iteracción")
    print("1.- Invertir una cadena de texto")
    print("2.- Calcular la suma de los  numeros ")
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
        case 2:
            print("\n Bienvenido a escogido la opcion 2")
            print("Calcular la suma de los numeros de 1 hasta N ")
            numero= int(input("Ingrese el numero hasta donde desea sumar"))
            print(sumar(numero))
        case 3:
            print("Imprimir una cuenta regresiva de numero N hasta 0")
            regresiva = int(input("Ingrese el numero desde donde desea iniciar la cuenta regresiva: "))
            print(cuentaRegresiva(regresiva))
        case 4:
            print("Suma de los digitos de un numero")
            digito = int(input("Ingrese un numero cualquiera entero"))
            print(sumatoriaDigitos(digito))
        case 5:
            print("Contar cuantos digitos tiene un numero")
            n = int(input("Ingrese un numero entero posirivo"))
            print(f"EL numero tiene :", ContarDigitos(n))
        case 6:
            print("Salir")
            break






