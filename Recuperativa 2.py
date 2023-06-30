# hacer rut de españa 03.03.45.67 (-xxy -rtx -ccu -03f)

datos_nombres = []
datos_edad = []
datos_nif = []
datos_digito_verificdor = []
menu = []
opc = 0

nombre = str(input("Ingrese su nombre:"))
edad = int(input("Ingrese su edad: "))
nif = int(input("Ingrese los digitos de su nif: "))

def datos_personales ():
    datos_nombres.append(nombre)
    datos_edad.append(edad)
    datos_nif.append(nif)

def ingresar_datos ():
    try:
        if len(datos_nombres) < 8 and len(datos_nombres) > 8 :
            print("Su nombre es valido 👍")
        else:
            print("Su nombre no es valido😢")


        if len(datos_edad) < 8:
            print("Su edad es valida")
        else:
            print("Su edad no es valida😢")
    except ValueError:
        print("Su opcion no es valida😢")

while True:
    print("")
    print("Escoja su digito verificador: ")
    print("[1] -xxy")
    print("[2] -rtx")
    print("[3] -ccu")
    print("[4] -03f")
    print("[5] salir")


    try:
        datos_digito_verificdor = int(input("Cual es su digito verificador: "))
        if opc == 1:
            print("escojio -xxy")
        elif opc == 2:
            print("escojio -rtx")
        elif opc == 3:
            print("escojio -ccu")
        elif opc == 4:
            print("escojio -03f")
        elif opc == 5:
            print("reinicie nuevamente 👍")
        break
        
    except ValueError:
        print("Ingrese un digito valido")

def certificado():
    print(f"El NIF de nombre: " + datos_nombres, "y edad: " + datos_edad)
