# Winter Wonderland by Akhi & Pauline
from graphics import*
import random

def draw_sf(sX, sY, size, color, sfWin):
    sf = Circle(Point(sX, sY), size)
    sf.setFill(color)
    sf.setOutline(color)
    sf.draw(WinterWin)
    
def draw_sfs(flkNum, xStart, xFin, yStart, yFin, size, color,sfsWin):
    for i in range(flkNum):
        draw_sf(random.randint(xStart,xFin),random.randint(yStart,yFin) , size , color ,sfsWin)


def draw_circ(cX, cY, cRad, cColor, cWin):
    circle = Circle(Point(cX,cY), cRad)
    circle.setFill(cColor)
    circle.setOutline(cColor)
    circle.draw(cWin)  
    

WinterWin = GraphWin("Winter Wonderland",600,600)
WinterWin.setCoords(0,0,600,600)
WinterWin.setBackground("light blue")

#bottom cirlce
draw_circ(100, 100, 34, "white", WinterWin)

#middle circle
draw_circ(100, 140, 28, "white", WinterWin)

#top circle
draw_circ(100, 175, 23, "white", WinterWin)

#snowman eyes
draw_circ(90, 180, 3, "black", WinterWin)


draw_sfs(370, 1, 600, 300, 600, 5, "white", WinterWin) 



## Snowflake
circle = Circle(Point(550,550), 5)
circle.setFill("white")
circle.setOutline("white")
circle.draw(WinterWin)
#SnowMan
circle = Circle(Point(100,100), 25)
circle.setFill("white")
circle.draw(WinterWin)

## Gray Snow
Rect = Rectangle(Point(0,0),Point (600,80))

Rect.setFill("light gray")
Rect.draw(WinterWin)



WinterWin.getMouse()
WinterWin.close()
