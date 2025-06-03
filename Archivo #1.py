#cajero
print("Este programa permite devolver dada una cantidad de dinero asignada, segun su pago el cambio con el menor numero de monedas y billetes")

#declaramos la clase
class Cajero:
  #definimos la funcion con su constructor
  def __init__(self,recibido,total):
    #aqui declaramos los atributos, en este tenemos el valor recibido, el total y tenemos otro atributo que no esta declarado en el init pero lo usamos como el inicializador o la base que es la lista de monedas y billetes 
    self.recibido=recibido
    self.total=total
    self.monedas=[50,100,200,500,1000]
    self.billetes=[2000,5000,10000,20000,50000,100000]
