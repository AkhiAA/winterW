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


def draw_rect(rX, rY, rW, rH, rCol, rWin):   #draws bottom snow
    Rect = Rectangle(Point(rX,rY),Point (rX + rW, rY + rH))
    Rect.setFill(rCol)
    Rect.setOutline(rCol)
    Rect.draw(rWin)

def draw_circ(cX, cY, cRad, cColor, cWin):  #draws the circle for the snowman 
    circle = Circle(Point(cX,cY), cRad)
    circle.setFill(cColor)
    circle.setOutline(cColor)
    circle.draw(cWin)
    
def draw_sm(sX, sY, sRad, sCol, sWin):
    draw_circ(sX, sY - sRad * 1.2, sRad * 1.21, "white", sWin)     #bottonm
    draw_circ(sX, sY, sRad, "white", sWin)                  #middle
    draw_circ(sX, sY + sRad * 1.2, sRad * .82, "white", sWin)     #top
    
    draw_circ(sX - sRad / 4, sY + sRad * 1.5 , sRad * .11, "black", sWin)  #left eye 
    draw_circ(sX + sRad / 4, sY + sRad * 1.5 , sRad * .11, "black", sWin)  #right eye
    
    nose = Polygon(Point(sX - sRad *.1, sY + sRad * 1.1), Point(sX, sY + sRad * 1.3), Point(sX + sRad *.82, sY + sRad))
    nose.setOutline("orange")
    nose.setFill("orange")
    nose.draw(sWin)



WinterWin = GraphWin("Winter Wonderland",600,600)
WinterWin.setCoords(0,0,600,600)
WinterWin.setBackground("light blue")


draw_rect(0, 0, 600, 80, "light gray", WinterWin)

anchX = 100      
anchY = 140
anchR = 58

for i in range (4):
    draw_sm(anchX, anchY, anchR, "white",WinterWin)

draw_sfs(370, 1, 600, 300, 600, 5, "white", WinterWin) 


## Gray Snow
Rect = Rectangle(Point(0,0),Point (600,80))

Rect.setFill("light gray")
Rect.draw(WinterWin)



WinterWin.getMouse()
WinterWin.close()
