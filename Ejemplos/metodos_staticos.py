#creamos una clase llamada matematicas
class Matematicas:

  #usamos el decorador que se reconcoe por la '@' para definir el metodo statico, esto signiofica que no tenemos que crear un constructor si no que podemos crarer directamente metodos de la clase, esto se usa solo si no queremos tener objetos en nuestra clase o acceder a ellos por ese medio ya que simplemente el valor del atributo se pondria en el print
  @staticmethod
  #creamos un metodo: sumar
  def sumar(num1,num2):
    #en este guardamos el resultado de la suma de dos numeros
    return num1+num2
  
  @staticmethod
  #creamos un metodo: restar
  def restar(num1, num2):
    #en este guardamos el resultado de la resta de dos numeros
    return num1-num2
  
#imprimimos nuestro resultado, dandole valor a los num o las variables puestas en los metodos.
print(Matematicas.sumar(5,7))
print(Matematicas.restar(9,7))