#creamos una clase principal que se llama animal
class Animal:
  #definimos el metodo general, en este caso si el metodo no se sobre escribe, saldra un error de validacion, esa en la funcion del NotImplementedError
  def hacer_sonido(self):
    #el NotImplementedError lo que hace es validar el metodo
    raise NotImplementedError("las subclases deben implemntar este metodo")
#creamos mas subclases asociadas a la clase principal con un metodo9 general pero con acciones distintas, en este caso la oveja hace vee-ee
class Oveja(Animal):
    def hacer_sonido(self):
      return "La oveja hace veeee-eee!"

#en este caso la gallina hace co,co    
class Gallina(Animal):
    def hacer_sonido(self):
      return "La gallina hace Co, co, co!"
    
#y aqui es el sonido de la vaca que hace muu   
class Vaca(Animal):
    def hacer_sonido(self):
      return "La vaca hace MUUUUUU!"

#este caso lo usamos para validar o mostrar el error omitiendo el metodo general, aqui tenemos una clase perro que esta asociada con la principal pero no con el metodo general.   
class perro(Animal):
  pass

#aqui creamos el objeto aniamles que isntancia directamente a las clases en una lista eso se hace porque las subclases herendan la clase principal, ya estaria instanciada entre ellas y el estar en una lista permite que sea mas facil trabajar con ellos
animales=[Oveja(),Gallina(),Vaca(),perro()]

#recorremos la lista y llamamos al metodo hacer sonido para cada subclase, cada una de ellas se ejecutara su propia funcion.
for Animal in animales:
  print(Animal.hacer_sonido())

