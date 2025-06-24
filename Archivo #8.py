#gestion de una cuenta bancaria con clase y metodos
print("Este programa permite crear una cuenta bancaria y gestionar ingresos y retiros")

#creamos la clase llamada Cuenta
class Cuenta:
    #definimos el constructor que puede recibir el nombre del titular y una cantidad inicial opcional
    def __init__(self, titular, cantidad=0.0):
        #guardamos el nombre del titular
        self.__titular = titular
        #guardamos la cantidad inicial, que puede ser 0 por defecto
        self.__cantidad = cantidad

    #creamos el metodo getter para el titular
    def get_titular(self):
        return self.__titular

    #creamos el metodo setter para el titular
    def set_titular(self, nuevo_titular):
        self.__titular = nuevo_titular

    #creamos el metodo getter para la cantidad
    def get_cantidad(self):
        return self.__cantidad

    #no hay setter directo para la cantidad, ya que esta se modifica solo con ingresar o retirar

    #este metodo muestra los datos de la cuenta
    def mostrar(self):
        print("Titular:", self.__titular)
        print("Cantidad actual en la cuenta:", self.__cantidad)

    #este metodo permite ingresar dinero a la cuenta, solo si es un valor positivo
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad + cantidad
        else:
            print("No se puede ingresar una cantidad negativa")

    #este metodo permite retirar dinero de la cuenta, puede quedar en saldo negativo
    def retirar(self, cantidad):
        self.__cantidad = self.__cantidad - cantidad


#solicitamos al usuario que cree su cuenta
nombre = input("Ingrese el nombre del titular de la cuenta: ")

#preguntamos si desea ingresar una cantidad inicial
opcion = input("¿Desea ingresar una cantidad inicial? (s/n): ")

if opcion == "s":
    cantidad_inicial = float(input("Ingrese la cantidad inicial: "))
    cuenta = Cuenta(nombre, cantidad_inicial)
else:
    cuenta = Cuenta(nombre)

#mostramos la cuenta creada
cuenta.mostrar()

#menu de operaciones
print("\nSeleccione una operacion:")
print("1. Ingresar dinero")
print("2. Retirar dinero")
print("3. Mostrar cuenta")
op = input("Opcion: ")

if op == "1":
    ingreso = float(input("Ingrese la cantidad a ingresar: "))
    cuenta.ingresar(ingreso)
    cuenta.mostrar()
elif op == "2":
    retiro = float(input("Ingrese la cantidad a retirar: "))
    cuenta.retirar(retiro)
    cuenta.mostrar()
elif op == "3":
    cuenta.mostrar()
else:
    print("Opcion no valida.")
