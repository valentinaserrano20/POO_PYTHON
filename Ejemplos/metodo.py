#definimos la clase coche que contendra los atrtibutos y metodos de la misma.
class Coche:
  #en el contructor incializamos los atributos marca, modelo, año, siendo 2 datos de texto(marca,modelo) y uno entero(año)
  def __init__(self,marca,modelo,año):
    #como ya hablabamos en el principal, els elf es una referencia hacia el objeto mismo, e sun parametro que se usa para que este pueda acceder a sus propios atributos o metodos.
    self.marca= marca
    self.modelo=modelo
    self.año=año

  #agreagmos el primer metodo, este lo que hace es juntar los 3 atributos y imprimirlos, en este caso el return guarda este dato y lo muetsra al llamar al metodo
  def descripcion(self):
      return f'{self.marca} {self.modelo} de {self.año}'

  #aqui definimos el segundo metodo que lo que nos dice es que si el carro tiene mas de veinte años, desde la fecha de referencia, este coche es antiguo y guarda un valor verdadero o falso. 
  def es_antiguo(self):
      return 2023-self.año > 20

#creamos el objeto dodge, instanciandolo a la clasee coche y dandole valor a los atributos de marca, modelo y año    
dodge=Coche("dodge","hellcat",2021)

#aqui llamamos al metodo descripcion referenciandolo desde el objeto e imprimiendolo al igual que el metodo es_antiguo el cual nos dara un valor false ya que el año de creacion del vehiculo es del 2021, dos años antes de la fecha de referencia.
print(dodge.descripcion())
print(dodge.es_antiguo())

