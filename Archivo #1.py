#cajero
print("Este programa permite devolver dada una cantidad de dinero asignada, segun su pago el cambio con el menor numero de monedas y billetes")

#declaramos la clase cajero
class Cajero:
  #definimos la funcion  con su constructor
  def __init__(self,recibido,total):
    #aqui declaramos los atributos, en este tenemos el valor recibido, el total y tenemos otro atributo que no esta declarado en el init pero lo usamos como el inicializador o la base que es el diccionario de monedas y billetes 
    self.recibido=recibido
    self.total=total
    self.dinero= {
        100000: "Billete de 100000",
        50000: "Billete de 50000", 
        20000: "Billete de 20000",
        10000: "Billete de 10000",
        5000: "Billete de 5000",
        2000: "Billete de 2000",
        1000: "Moneda de 1000",
        500: "Moneda de 500",
        200: "Moneda de 200",
        100: "Moneda de 100",
        50: "Moneda de 50"
    }

  #definimnos el primer metodo que es validar si el valor recibido es mayor o igual al total
  def pago(self):
    if self.recibido >= self.total:
      print("su pago fue aceptado")
      return True
    else:
      print("su pago fue rechazado ya que el monto que dio es menor al que tiene que pagar")
      return False
  
  #definimos el segundo metodo que es calcular el cambio
  def calcular_cambio(self):
    cambio=self.recibido-self.total
    return cambio
  
  #definimos el tercer metodo que descompondra el cambio
  def descomponer_cambio(self):
    #creamos un diccionario llamado contador el cual almacenara los billetes o monedas que se vayan contando
    contador={}
    #aqui llamamos al metodo anterior que nos servira de guia para la descomposicion, a este lo llamamos refcambio
    refcambio=self.calcular_cambio()

    #hacemos un for que permitira que se recorra todo el diccionario tomando las claves y valor como estan escritas 
    for valor, nombre in self.dinero.items():
        #aqui hacemos un if diciendo que el cambio debe ser mayor o igual al valor para que se descomponga.
        if refcambio >= valor:
            #esta seria la primera secuencia que tomaria el cambio y lo redondearia al primer billete o moneda mas grande
            cantidad = refcambio // valor
            #luego este valor se agrega al diccionario vacio
            contador[valor]=cantidad
            #y se termina haciendo lo mismo que la primera secuencia pero el resultado que se agrego al diccionario
            refcambio = refcambio % valor
    return contador
  
  def mostrar_cambio(self):
    #aqui llamamos al metodo descomponer_cambio y lo guardamos en una variable llamada cambio
    cambio = self.descomponer_cambio()
    #luego hacemos un if que nos dira si el cambio es mayor a 0, si es asi se mostrara el cambio
    if cambio:
      print("El cambio a devolver es:")
      for valor, cantidad in cambio.items():
        print(f"{cantidad} - {self.dinero[valor]}")
    else:
      print("No hay cambio que devolver.")
  
#ahora pedimos los datos al usuario
total = int(input("Ingrese el monto total de la compra: "))
recibido = int(input("Ingrese el monto recibido: "))

#creamos un objeto de la clase cajero, que contendra los datos recibidos y el total
cajero = Cajero(recibido, total)

#llamamos al metodo pago para validar el pago
if cajero.pago():
    #si el pago es valido, llamamos al metodo mostrar_cambio para mostrar el cambio
    cajero.mostrar_cambio()
else:
    #si el pago no es valido, mostramos un mensaje de error
    print("No se puede procesar el cambio debido a un pago invalido.")