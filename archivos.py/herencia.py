# se crea la clase que utilizaremos la cual es la clase padre
class vehiculo():

    # es nuestro constructor con los atributos
    def __init__(self, color, ruedas):

        # Estos son los atributos de la clase 
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color {}, {} ruedas".format(self.color, self.ruedas)
    
# se crea esta clase que sera nuestra clase hija
class automovil(vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindraje):
        self.color = color
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindraje = cilindraje

    def __str__(self):
        cad = "color {}, {} km/h, {} ruedas, {} cc"
        return cad.format( self.color, self.velocidad, self.ruedas, self.cilindraje)
    

# imprimira la clase padre
V = vehiculo("Negro Mate", 4)
print(V)

# imprimira la clase hija
A = automovil("azul", 4, 160, 1800)
print(A)