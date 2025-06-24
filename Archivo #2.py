#numeros primos
print("Este programa descompone un numero en sus factores primos")

#declaramos la clase FactoresPrimos, la cual se encargará de descomponer un número en sus factores primos
class FactoresPrimos:
  #definimos el constructor, que recibirá el número que se quiere descomponer
  def __init__(self, numero):
    #este es el único atributo que necesitamos, el número que ingresara el usuario
    self.numero = numero

  #definimos el primer metodo, que se encargara de obtener los factores primos
  def obtener_factores(self):
    #creamos una variable local n que será una copia del número ingresado para irlo dividiendo
    n = self.numero
    #creamos una lista vacía donde almacenaremos los factores primos encontrados
    factores = []
    #inicializamos el divisor en 2, que es el primer número primo
    divisor = 2

    #creamos un ciclo que se repetirá mientras n sea mayor que 1
    while n > 1:
      #si el número es divisible entre el divisor actual, agregamos ese divisor a la lista
      while n % divisor == 0:
        #agregamos el divisor a la lista de factores
        factores.append(divisor)
        #dividimos n por ese divisor y actualizamos su valor   
        n = n // divisor           
        #si ya no es divisible, incrementamos el divisor en 1 para probar el siguiente número
        divisor += 1
    
    #retornamos la lista de factores primos
    return factores

  #definimos el segundo método, que imprimirá el resultado
  def mostrar_resultado(self):
    #llamamos al método obtener_factores_primos para descomponer el número
    factores = self.obtener_factores()
    #mostramos la lista con los factores encontrados
    print(f"Los factores primos de {self.numero} son: {factores}")

#ahora pedimos los datos al usuario
numero = int(input("Ingrese el numero que desea descomponer: "))

#verificamos que el número sea válido
if numero > 1:
  #creamos un objeto de la clase Factorizador
  fact = FactoresPrimos(numero)
  #llamamos al método que muestra los factores primos
  fact.mostrar_resultado()
else:
  #si el número no es mayor que 1, mostramos un mensaje de error
  print("El numero debe ser mayor que 1.")
