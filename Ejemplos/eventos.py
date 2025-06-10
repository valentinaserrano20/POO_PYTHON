#para crear un evento en POO es neecsario importar una libreria, en este caso estaremso importando la libreria tkinter que permite  craer interfaces visuales, en este caso sera una ventana emergente.
import tkinter as tk

#creamos una clase Boton que nos permitira crear un boton personalizado
class Boton:
	
  #aqui declaramos el constructor init que inicializara el atributo text
	def __init__(self,text):
		self.text=text
		
		self.boton=tk.Button(text=self.text, command=self.on_click)

	def on_click(self):
		print(f'¡El boton "{self.text}" ha sido clickeado!')

ventana= tk.Tk()

boton=Boton("Click me")

boton.boton.pack()

ventana.mainloop()