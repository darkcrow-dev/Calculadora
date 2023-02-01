from tkinter import *

#Funciones para la calculadora
def botonClick(valor):
    global i
    texto.insert(i, valor)
    i += 1

def borrarClick():
    texto.delete(0, END)

def igualClick():
    valor = texto.get()
    resultado = eval(valor)
    texto.delete(0, END)
    texto.insert(0, resultado)

#Titulo de la aplicacion
ventana = Tk()
ventana.title("CALCULADORA")
ventana.geometry('294x306')

#Ventana para los calculos ingresados
i = 0
texto = Entry(ventana, font = ("Calibri 20"))
texto.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5)

#Botones
boton1 = Button(ventana, text = "1", width = 5, height = 2, command = lambda: botonClick(1))
boton2 = Button(ventana, text = "2", width = 5, height = 2, command = lambda: botonClick(2))
boton3 = Button(ventana, text = "3", width = 5, height = 2, command = lambda: botonClick(3))
boton4 = Button(ventana, text = "4", width = 5, height = 2, command = lambda: botonClick(4))
boton5 = Button(ventana, text = "5", width = 5, height = 2, command = lambda: botonClick(5))
boton6 = Button(ventana, text = "6", width = 5, height = 2, command = lambda: botonClick(6))
boton7 = Button(ventana, text = "7", width = 5, height = 2, command = lambda: botonClick(7))
boton8 = Button(ventana, text = "8", width = 5, height = 2, command = lambda: botonClick(8))
boton9 = Button(ventana, text = "9", width = 5, height = 2, command = lambda: botonClick(9))
boton0 = Button(ventana, text = "0", width = 15, height = 2, command = lambda: botonClick(0))

botonBorrar = Button(ventana, text = "AC", width = 5, height = 2, command = lambda: borrarClick())
botonParentesis1 = Button(ventana, text = "(", width = 5, height = 2, command = lambda: botonClick("("))
botonParentesis2 = Button(ventana, text = ")", width = 5, height = 2, command = lambda: botonClick(")"))
botonPunto = Button(ventana, text = ".", width = 5, height = 2, command = lambda: botonClick("."))

botonDivision = Button(ventana, text = "/", width = 5, height = 2, command = lambda: botonClick("/"))
botonMultiplicacion = Button(ventana, text = "X", width = 5, height = 2, command = lambda: botonClick("*"))
botonSuma = Button(ventana, text = "+", width = 5, height = 2, command = lambda: botonClick("+"))
botonResta = Button(ventana, text = "-", width = 5, height = 2, command = lambda: botonClick("-"))
botonIgual = Button(ventana, text = "=", width = 5, height = 2, command = lambda: igualClick())

#Botones en pantalla
botonBorrar.grid(row = 1, column = 0, padx = 5, pady = 5)
botonParentesis1.grid(row = 1, column = 1, padx = 5, pady = 5)
botonParentesis2.grid(row = 1, column = 2, padx = 5, pady = 5)
botonDivision.grid(row = 1, column = 3, padx = 5, pady = 5)

boton7.grid(row = 2, column = 0, padx = 5, pady = 5)
boton8.grid(row = 2, column = 1, padx = 5, pady = 5)
boton9.grid(row = 2, column = 2, padx = 5, pady = 5)
botonMultiplicacion.grid(row = 2, column = 3, padx = 5, pady = 5)

boton4.grid(row = 3, column = 0, padx = 5, pady = 5)
boton5.grid(row = 3, column = 1, padx = 5, pady = 5)
boton6.grid(row = 3, column = 2, padx = 5, pady = 5)
botonResta.grid(row = 3, column = 3, padx = 5, pady = 5)

boton1.grid(row = 4, column = 0, padx = 5, pady = 5)
boton2.grid(row = 4, column = 1, padx = 5, pady = 5)
boton3.grid(row = 4, column = 2, padx = 5, pady = 5)
botonSuma.grid(row = 4, column = 3, padx = 5, pady = 5)

boton0.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)
botonPunto.grid(row = 5, column = 2, padx = 5, pady = 5)
botonIgual.grid(row = 5, column = 3, padx = 5, pady = 5)

#Iniciar la aplicacion
ventana.mainloop()