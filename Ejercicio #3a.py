#conversion de binario a decimal y de decimal a binario
print("Este programa convierte un numero binario a decimal y de decimal a binario")

#creamos una clase llamada ConversorNumerico que tendra los metodos necesarios para realizar ambas conversiones
class ConversorNumerico:

    #en este caso no definimos un constructor __init__ porque no necesitamos guardar ningun dato en memoria
    
    #este es el primer metodo, encargado de convertir un numero decimal en una lista que representa su equivalente en binario
    def convertir_a_binario(self, numero):
        #creamos una lista vacia donde guardaremos los residuos de cada division entre 2
        binario = []
        
        #hacemos una copia del numero original para no modificar el valor recibido directamente
        n = numero
        
        #si el numero es 0, su representacion binaria tambien es 0, asi que lo agregamos directamente
        if n == 0:
            binario.append(0)
        
        #usamos un ciclo while que seguira mientras el numero sea mayor que 0
        while n > 0:
            #obtenemos el residuo de dividir entre 2, que sera 0 o 1
            resto = n % 2
            
            #agregamos el residuo al inicio de la lista porque el binario se forma de atras hacia adelante
            binario.insert(0, resto)
            
            #dividimos el numero por 2 de forma entera para continuar con la conversion
            n = n // 2
        
        #al final devolvemos la lista con los digitos binarios ya ordenados
        return binario

    #este es el segundo metodo, que convierte una lista de digitos binarios (0 y 1) en su equivalente decimal
    def convertir_a_decimal(self, binario):
        #inicializamos la variable decimal donde sumaremos el valor final
        decimal = 0
        
        #calculamos la cantidad de digitos binarios que tiene la lista
        longitud = 0
        for dig in binario:
            longitud = longitud + 1
        
        #usamos un ciclo para recorrer cada digito de izquierda a derecha
        for i in range(longitud):
            #calculamos la potencia correspondiente de 2 segun la posicion del digito
            potencia = longitud - 1 - i
            
            #sumamos el digito multiplicado por 2 elevado a la potencia a nuestro total
            decimal = decimal + (binario[i] * (2 ** potencia))
        
        #devolvemos el numero decimal resultante
        return decimal

    #este metodo muestra al usuario el menu de opciones de conversion
    def mostrar_menu(self):
        print("Menu de opciones de conversion:")
        print("1. Convertir de decimal a binario")
        print("2. Convertir de binario a decimal")

    #este metodo muestra el resultado de la conversion de decimal a binario
    def mostrar_binario(self, numero, binario):
        #imprimimos el mensaje inicial sin saltar de linea
        print("El numero", numero, "en binario es:", end=" ")
        
        #recorremos la lista de digitos binarios y los imprimimos uno por uno sin espacios
        for bit in binario:
            print(bit, end="")
        
        #al final agregamos un salto de linea
        print()


#creamos un objeto de la clase ConversorNumerico
conversor = ConversorNumerico()

#mostramos el menu al usuario
conversor.mostrar_menu()

#pedimos al usuario que elija una opcion
opcion = input("Seleccione una opcion (1 o 2): ")

#si elige la opcion 1, haremos la conversion de decimal a binario
if opcion == "1":
    #pedimos el numero decimal
    numero = int(input("Ingrese un numero decimal: "))
    
    #llamamos al metodo para convertir el numero a binario
    binario = conversor.convertir_a_binario(numero)
    
    #mostramos el resultado llamando al metodo mostrar_binario
    conversor.mostrar_binario(numero, binario)

#si elige la opcion 2, haremos la conversion de binario a decimal
elif opcion == "2":
    #pedimos cuantos digitos tiene el numero binario
    cantidad = int(input("Cuantos digitos tiene el numero binario: "))
    
    #creamos una lista vacia donde guardaremos los digitos
    binario = []
    
    #esta variable nos permitira saber si todos los digitos son validos (solo 0 o 1)
    valido = True

    #usamos un ciclo para pedir cada digito binario
    for i in range(cantidad):
        #pedimos el digito numero i+1 (para que el conteo sea desde 1)
        digito = int(input("Ingrese el digito " + str(i+1) + ": "))
        
        #verificamos que el digito sea valido
        if digito == 0 or digito == 1:
            #si es valido, lo agregamos a la lista
            binario.append(digito)
        else:
            #si no es valido, marcamos que hay error
            valido = False

    #si todos los digitos fueron validos, hacemos la conversion
    if valido:
        #llamamos al metodo para convertir a decimal
        decimal = conversor.convertir_a_decimal(binario)
        
        #mostramos el resultado
        print("El numero binario ingresado en decimal es:", decimal)
    else:
        #si hubo algun digito invalido, mostramos un mensaje de error
        print("El numero ingresado no es binario valido.")

#si la opcion ingresada no es ni 1 ni 2, mostramos un mensaje de error
else:
    print("Opcion no valida. Por favor seleccione 1 o 2.")
