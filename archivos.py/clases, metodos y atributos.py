#Autor:Heidy Leon
#Programacion avanzada
# realizamos la definicion de la clase
class Automovil: 

    # Definicion de una variable que se reutilizara y los atributos
    
    # Definicion de metodos con sus atributos
    def __init__(self, marca, modelo):   
        self.marca = marca
        self.modelo = modelo
        self.usado = False

    def arrancar(self):      
        self.usado = True
        print("El", self.marca, self.modelo, "es usado")

    def parar(self):
        self.usado = False
        print("El", self.marca, self.modelo, "es cero kilometros")



# llamadas por instancias de los metodos

R = Automovil("Renault", "Duster")
M = Automovil("Mazda", "Miata")

# imprimir si al evaluar es verdadero
R.arrancar()
M.arrancar()

print(R.usado)
print(M.usado)

# imprimir si al evaluar es falso
R.parar()
M.parar()