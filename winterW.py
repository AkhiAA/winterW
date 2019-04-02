# Winter Wonderland by Akhi & Pauline
from graphics import*
import random

def draw_sf(sX, sY, size, color, WinterWin):
    sf = Circle(Point(sX, sY), size)
    sf.setFill(color)
    sf.setOutline(color)
    sf.draw(WinterWin)

sX=550
sY=550
size=5
color="white"

WinterWin = GraphWin("Winter Wonderland",600,600)
WinterWin.setCoords(0,0,600,600)
WinterWin.setBackground("light blue")

for i in range(50):
    draw_sf(random.randint(1,600),random.randint(300,600) , size, color, WinterWin)



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
