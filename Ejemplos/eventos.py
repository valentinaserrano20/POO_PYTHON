#para crear un evento en POO es neecsario importar una libreria, en este caso estaremso importando la libreria tkinter que permite  craer interfaces visuales, en este caso sera una ventana emergente.
import tkinter as tk

#creamos una clase Boton que nos permitira crear un boton personalizado
class Boton:
	
  #aqui declaramos el constructor init que inicializara el atributo text, el cual contendra el texto del boton
	def __init__(self,text):
		self.text=text
		#aunque no se haya declarado antes, python puede crear atributos en cualquier momento solo con la palabra self, aqui usamos la clase button de tkinter para crearlo y le decimos que este atributo va a tomar el de arriba y juntarse, ene ste caso con el atributo de texto. el parametro 'command' lo que hace aqui es referenciar la funcion que se va a aplicar.
		self.boton=tk.Button(text=self.text, command=self.on_click)

	#definimos un metodo, en este caso es que este se ejecute cuando hace click en el boton y imprima un mesnaje avisandole al usuario que el boton ha sido clickeado
	def on_click(self):
		print(f'¡El boton "{self.text}" ha sido clickeado!')

#se crea la ventana principal de la interfaz
ventana= tk.Tk()

#creamos el objeto instanciando la clase y dandole al atributo d etexto su valor en este caso click me
boton=Boton("Click me")

#agregamos el boton a una ventana emergente con el metodo .pack que hace es que este sea visible en la ventana, se referencia al objeto en donde esta creado el boton.
boton.boton.pack()

#ejecutamos el bucle principal de la interfaz, que mantiene la ventana abierta esperando a ser clickeado.
ventana.mainloop()