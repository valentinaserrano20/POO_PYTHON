#conversion de numero entero a numero romano
print("Este programa convierte un numero entero (entre 1 y 1000) en su equivalente en numero romano")

#creamos la clase que hara la conversion, llamada ConversorRomano
class ConversorRomano:

    #no necesitamos guardar ningun dato en el constructor, asi que no usamos __init__

    #este metodo hara la conversion de entero a romano
    def convertir_a_romano(self, numero):
        #creamos una lista con pares ordenados de valores arabigos y sus romanos correspondientes
        valores = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]

        #inicializamos una cadena vacia para guardar el resultado
        romano = ""

        #usamos un ciclo para recorrer todos los pares de valores
        for valor, simbolo in valores:
            #mientras el numero sea mayor o igual al valor actual
            while numero >= valor:
                #agregamos el simbolo romano al resultado
                romano = romano + simbolo
                #restamos ese valor al numero original
                numero = numero - valor
        
        #devolvemos la cadena final con el numero romano completo
        return romano

#pedimos al usuario que escriba un numero
numero = int(input("Ingrese un numero entero entre 1 y 1000: "))

#verificamos que el numero este dentro del rango valido
if numero >= 1 and numero <= 1000:
    #creamos un objeto de la clase ConversorRomano
    conversor = ConversorRomano()

    #llamamos al metodo que convierte el numero
    romano = conversor.convertir_a_romano(numero)

    #mostramos el resultado final
    print("El numero", numero, "en romano es:", romano)

else:
    #si el numero no esta en el rango, mostramos un mensaje de error
    print("El numero ingresado no esta en el rango permitido (1 a 1000)")
