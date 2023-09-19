#Autor:Heidy Leon
#Programacion avanzada
# definimos el constructor 
def run():

    # solicitaremos al usuario por medio de la maquina que ingrese las palabras
    word_1= input('digite una palabra: ')
    word_2= input('digite la segunda palabra: ')
    
    # imprimira en consola al evaluar las dos palabras mediante la entrada 
    print(f'¿la palabra "{word_1}" es anagrama de "{word_2}? {set(word_1) == set(word_2)}"')




if __name__=='__main__':
    run()

