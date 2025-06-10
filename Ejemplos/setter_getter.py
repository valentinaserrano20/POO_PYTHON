#definimos una clase llamada geeks
class Geeks:
  #declaramos el contsructor para inicializar los atributos
  def __init__(self):
    #creamos una variable protegida llamada _age y le damos el valor 0, 
    self._age=0

  #el decorador property lo que permite es que se pueda leer el valor de la variable protegida
  @property
  #creamos el metodo que nos permitira ver el valor de la edad, esto dando alusion al getter que permite controlar la visualizacion del atributo
  def age(self):
    print("getter method called")
    return self._age
  
  #este decorador define como se cambia el valor de un atributo, en este caso se valida que la persona tenga mas de 18 años
  @age.setter
  def age(self, a):
    if(a < 18):
      #el raise es una palabra clave para generar errores intencionales segun la sentencia, se usa el value error para ver si el dato que se recibe es valido o no
      raise ValueError("su edad no es elegible")
    print("setter method called")
    self._age=a

#creamos un objeto llamado mark, esto lo que hace es ejecutar el constructor init y que _age este en 0
mark=Geeks()

#aqui pedimos al usuario que ingrese una edad, y de aqui es donde actua el metodo setter validando segun la edad que el usuario digite.
mark.age=int(input("ingrese la edad"))

#ahora mostramos el valor de la edad y usamos el getter.
print(mark.age)