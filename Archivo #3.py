#conversion de binario a decimal
print("Este programa convierte un numero binario a decimal y de decimal a binario")
class ConversorNumerico:
    # En este caso, nuestro conversor no necesita "recordar" ningun numero especifico, asi que no guardamos nada en memoria o en nuestro constructor init, empezamos ocn el primer metodo directamenten que sera el encargado de convertir de decimal a binario
    def convertir_a_binario(self, numero):
        #creamos una lista vacia donde guardaremos los residuos de cada division
        binario = []
        
        # Hacemos una copia del numero original para no perderlo durante el proceso
        n = numero
        
        #Si el numero es cero, el resultado en binario tambien es cero
        if n == 0:
            # Agregamos un 0 a nuestra lista
            binario.append(0)  
        
        #Dividimos entre 2 repetidamente hasta que no se pueda mas
        while n > 0:
            # Calculamos el residuo cuando dividimos entre 2, el cual nos dira si es 0 o 1
            resto = n % 2
            
            #agregamos con el metodo insert el residuo al inicio de la lista porque ira # al reves, es decir, el primer residuo sera el ultimo en aparecer
            binario.insert(0, resto)
            
            #creamos una nueva variable n que sera el resultado de la division entera del numero original entre 2
            n = n // 2
        
        # Devolvemos nuestra lista con todos los 0s y 1s en el orden correcto
        return binario
    
    #creamos el segundo metodo que se encargara de convertir de binario a decimal
    def convertir_a_decimal(self, binario):
        # Empezamos los contadores en 0 lo que nos ayudara a sumar el valor total
        decimal = 0
        longitud = 0
        
        #contamos cuantos digitos tiene el numero binario
        for dig in binario:
            longitud = longitud + 1
        
        #usamos un for para contar desde 0 hasta la longitud del numero binario
        for i in range(0, longitud):
            # calculamos la potencia de 2 que corresponde a cada digito dependiendo de su posicion
            potencia = longitud - 1 - i
            
            #sumamos el valor del digito (0 o 1) multiplicado por 2 elevado a la potencia
            decimal = decimal + (binario[i] * (2 ** potencia))
        
        # Devolvemos el numero ya convertido a decimal
        return decimal
    
    #este metodo es el encargado de mostrar el menu de opciones al usuario
    def mostrar_menu(self):
        print("Menu de opciones de conversion:")
        print("1. Convertir de decimal a binario")
        print("2. Convertir de binario a decimal")
    
    #este metodo es el encargado de mostrar el resultado de la conversion de decimal a binario
    def mostrar_binario(self, numero, binario):
        # Imprimimos el inicio del mensaje SIN saltar a la siguiente linea
        print("El numero", numero, "en binario es:", end=" ")
        
        # Imprimimos cada 0 o 1 SIN espacios entre ellos y SIN saltar linea
        for bit in binario:
            print(bit, end="")
        
        # Al final, saltamos a la siguiente linea para que se vea ordenado
        print()


#aqui creamos un objeto de la clase ConversorNumerico, ya que no se uso un constructor __init__ porque no necesitamos guardar ningun dato especifico se referencia a la clase directamente
conversor = ConversorNumerico()

#le mostramos el menu de opciones al usuario
conversor.mostrar_menu()

#le pedimos al usuario que seleccione una opcion
opcion = input("Seleccione una opcion (1 o 2): ")

#si el usuario selecciona la opcion 1, convertiremos de decimal a binario
if opcion == "1":
    # Le pedimos al usuario que escriba el numero que quiere convertir
    numero = int(input("Ingrese un numero decimal: "))
    
    #llamamos al metodo convertir_a_binario desde el objeto conversor
    binario = conversor.convertir_a_binario(numero)
    
    #luego llamamos al metodo mostrar_binario para mostrar el resultado
    conversor.mostrar_binario(numero, binario)

#si el usuario selecciona la opcion 2, convertiremos de binario a decimal
elif opcion == "2":
    # Preguntamos cuantos digitos tiene el numero binario
    cantidad = int(input("Cuantos digitos tiene el numero binario: "))
    
    # Creamos una lista vacia que sera nuestra "caja" para guardar los digitos binarios
    binario = []
    
    # Esta variable nos ayudara a recordar si todos los digitos son validos, ya que un numero binario solo puede tener 0 y 1
    valido = True
    
    
    #usamos un for para que recorra las veces que el usuario nos diga que digitos tiene el numero binario
    for i in range(cantidad):
        # Pedimos el digito numero i+1 (sumamos 1 porque empezamos contando desde 0)
        digito = int(input("Ingrese el digito " + str(i+1) + ": "))
        
        #Verificamos que el digito sea 0 o 1
        if digito == 0 or digito == 1:
            # Si es valido, lo agregamos a nuestra lista
            binario.append(digito)
        else:
            # Si no es valido, marcamos que algo salio mal
            valido = False
    
    # RESULTADO: Solo hacemos la conversion si todos los digitos fueron validos
    if valido:
        # Usamos nuestro traductor para convertir a decimal
        decimal = conversor.convertir_a_decimal(binario)
        print("El numero binario ingresado en decimal es:", decimal)
    else:
        # Si hubo digitos invalidos, le decimos al usuario que hubo un error
        print("El numero ingresado no es binario valido.")

#si no es ninguna de las opciones anteriores, mostramos un mensaje de error
else:
    print("Opcion no valida. Por favor seleccione 1 o 2.")