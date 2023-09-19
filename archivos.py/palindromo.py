#Autor:Heidy Leon
#Programacion avanzada
# Definir la variable a utilizar
def palindromo(palabra):

    # con lower cambiaremos las mayusculas a minusculas de la palabra o frase
    palabra = palabra.lower()

    # con replace quitaremos los espacios que contenga la frace y las tildes
    palabra = palabra.replace(" ","")
    palabra = palabra.replace("á","a")
    palabra = palabra.replace("é","e")
    palabra = palabra.replace("í","i")
    palabra = palabra.replace("ó","o")
    palabra = palabra.replace("ú","u")

    # Evaluaremos cuanto tiene de longitud la palabra
    a = 0
    b = len(palabra) -1

    # Utilizaremos un bucle para verificar el largo de la palabra
    for i in range(0, len(palabra)):
        if palabra[a] == palabra[b]:
            a += 1
            b -= 1
        else:
            return False
        
    return True

# Con este Input pedimos al usuario que ingrese la palabra o la frase que el programa verificara
palabra = input("Ingrese una palabra o una frase: ")

# Con este bucle condicional evaluara a la variable palabra y le dira al usuario si es o no palindroma
if palindromo(palabra):
    print("Es una palabra o frase palindroma")
else:
    print("No es una frase o palabra palindroma")    