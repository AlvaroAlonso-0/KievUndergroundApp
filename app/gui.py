from tkinter.constants import *
import backend as bk
import database as db
import turtle as t

HEIGHT = 900
WIDTH = 1267

""" Resizer Imagen del metro """
#img = Image.open("./app/img/metrobien.png")
#img = img.resize((900,900),Image.ANTIALIAS)
#img.save("./app/img/metrobienresized.png")

""" Variables globales """
inicio = None
destino = None
buscaSegundaParada = False

# Dibujar camino dada una lista
def draw_path(path):
    if path == None:
        print("Can't draw an empty path")
        return
    a.penup()
    a.speed(0)
    a.goto((path[0].coords[0], path[0].coords[1]))
    a.speed(2.5)
    for parada in path:
        a.pendown()
        a.goto(parada.coords[0],parada.coords[1])
        a.penup()
    
    a.color('black')
    for parada in path:
        a.goto(parada.coords[0], parada.coords[1])
        a.showturtle()
        if parada is not path[-1]:
            a.dot(15)

    a.color('purple')
    a.hideturtle()
    a.stamp()
      
    
        

# Llama a A* con las dos paradas
def printcoords(x,y):
    global inicio, destino, buscaSegundaParada, a
    # Muestra las coordenadas del click por consola
    print (x,y)
    
    # Primera parada
    if buscaSegundaParada == False:
        inicio = db.which_stop(x, y)
        if inicio is None:
            return
        # Muestra el inicio por consola
        print("Inicio: " + str(inicio))
        buscaSegundaParada = True
    # Segunda parada
    else:
        destino = db.which_stop(x, y)
        if destino is None:
            return
        # Muestra el destino por consola y reinicia el buscador
        print("Destino: " + str(destino))
        print()
        buscaSegundaParada = False
        # Dibuja el camino
        path = bk.a_estrella(inicio,destino)
        draw_path(path) 
 
    
""" Ventanta principal """
win = t.Screen()
win.setup(width=WIDTH, height=HEIGHT, startx=None, starty=None)
# Background
win.bgpic("./app/img/metrobienresized2.png")
win.setup(height=HEIGHT, width=WIDTH)
win.title("Metro Kiev")
win.register_shape("./app/img/icono_metro.gif")
#Selecciona a una parada
win.onclick(printcoords,1)

#Pintar camino
a = t.RawTurtle(win)
a.speed(0)
a.penup()
a.goto((-455.0, 397.0))
a.pen(pensize=6)
a.write("AAaaaAAAAA",align=CENTER,font=("Arial",20,'normal'))
a.hideturtle()
a.pen(pensize=6)
a.color('purple')
a.shape("./app/img/icono_metro.gif")
# Llama en un bucle al programa
t.mainloop()
