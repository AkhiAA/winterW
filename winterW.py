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


WinterWin = GraphWin("Winter Wonderland",600,600)
WinterWin.setCoords(0,0,600,600)
WinterWin.setBackground("light blue")


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
