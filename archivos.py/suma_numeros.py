#Autor:Heidy Leon
#Programacion avanzada

print("Programa de suma de secuencia de una serie de numeros")
print()

# Definimos la variable a utilizar en el programa
def secuencia(numero):

    # Este bucle condicioonal nos evaluara los numeros y realizara la suma
    if(numero == 0 or numero == 1):
        return 1
    else:
        return secuencia(numero - 1) + secuencia(numero - 2)

# Este bucle evaluara los numeros ingresados por el usuario que no sean negativos
while True:
    n = int(input("ingrese un numero: "))
    
    # Este condicional nos cerrara el bucle al evaluar que el numero es positivo
    if(n >= 1):
        break

# Este bucle nos imprimira el resultado despues de ser evaludo y se guardara en la variable i
for i in range(n):
    print(secuencia(i))
    