#creamos una clase llamada animal, este sera el molde que definira los objetos que creemos, como una buena practica, el nombre de la clase siempre va en mayuscula.
class Animal:
  #el contructor __init__ es el que nos permite inicializar los atributos que son tipo y peso
  def __init__(self,tipo,peso):
    #usamos el parametro self para referirnos a cada atributo, este lo que hace es referenciar el atributo para que este se reconozca asi mismo y sew pueda manipular.
    self.tipo=tipo
    self.peso=peso

#aqui creamos el objeto "objeto" el cual lo instanciamos a la clase principal que es animal.
objeto=Animal("perro","30kg")

#ahora imprimimos el resultado y como ese resultado esta en el objeto, se refererncia a este primero y luego el atributo del mismo.
print(objeto.tipo, objeto.peso)
