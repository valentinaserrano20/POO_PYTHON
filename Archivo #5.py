#juego de adivinanza de numero
print("Este programa intenta adivinar el numero que estas pensando")

#creamos la clase llamada Adivinador
class Adivinador:
    #el constructor recibe el limite inferior y superior del rango
    def __init__(self, minimo, maximo):
        #guardamos esos limites como atributos
        self.minimo = minimo
        self.maximo = maximo
        #inicializamos el contador de intentos
        self.intentos = 0

    #este metodo se encarga de hacer una suposicion basada en el rango actual
    def suponer(self):
        #calculamos el punto medio entre minimo y maximo
        self.supuesto = (self.minimo + self.maximo) // 2
        #incrementamos el contador de intentos
        self.intentos = self.intentos + 1
        #devolvemos el numero que vamos a suponer
        return self.supuesto

    #este metodo recibe la respuesta del usuario y ajusta el rango segun sea necesario
    def procesar_respuesta(self, respuesta):
        if respuesta == "A":
            #si el numero adivinado fue muy alto, bajamos el limite superior
            self.maximo = self.supuesto - 1
        elif respuesta == "B":
            #si el numero adivinado fue muy bajo, subimos el limite inferior
            self.minimo = self.supuesto + 1
        #si fue "S" no hacemos nada porque el numero fue correcto

    #este metodo muestra la cantidad de intentos al final
    def mostrar_resultado(self):
        print("¡He adivinado tu numero en", self.intentos, "intentos!")

#pedimos al usuario los limites del rango
print("Piensa en un numero dentro de un rango y yo lo adivinare")
minimo = int(input("Ingrese el limite inferior del rango: "))
maximo = int(input("Ingrese el limite superior del rango: "))

#creamos el objeto de la clase Adivinador
juego = Adivinador(minimo, maximo)

#usamos un ciclo hasta que adivinemos correctamente
while True:
    #el programa hace una suposicion
    intento = juego.suponer()
    #preguntamos al usuario si el numero es correcto, mayor o menor
    print("¿Es", intento, "tu numero?")
    print("Responde con: S (si es correcto), A (si es muy alto), B (si es muy bajo)")
    respuesta = input("Respuesta: ")

    #si el numero es correcto, terminamos
    if respuesta == "S":
        juego.mostrar_resultado()
        break
    #si no es correcto, ajustamos los limites
    else:
        juego.procesar_respuesta(respuesta)
