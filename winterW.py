# Winter Wonderland by Akhi & Pauline
from graphics import*
import random

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
    
def draw_sm(sX, sY, sRad,sCol,sWin):
    draw_circ(sX, sY - sRad * 1.2, sRad * 1.21, "white", sWin)     #bottonm
    draw_circ(sX, sY, sRad, "white", sWin)                  #middle
    draw_circ(sX, sY + sRad * 1.2, sRad * .82, "white", sWin)     #top
    
    draw_circ(sX - sRad / 4, sY + sRad * 1.5 , sRad * .11, "black", sWin)  #left eye 
    draw_circ(sX + sRad / 4, sY + sRad * 1.5 , sRad * .11, "black", sWin)  #right eye
    
##    nose = Polygon(Point(sX, sY+ sRad), Point(sX * 1.05, sY + sRad * 1.25), Point(sX * 1.2, sY + sRad*.71))
##    nose.setOutline("orange")
##    nose.setFill("orange")
##    nose.draw(sWin)



WinterWin = GraphWin("Winter Wonderland",600,600)
WinterWin.setCoords(0,0,600,600)
WinterWin.setBackground("light blue")

draw_rect(0, 0, 600, 80, "light gray", WinterWin)

anchX = 100      
anchY = 140
anchR = 28

for i in range (4):
    draw_sm(anchX, anchY, anchR, "white",WinterWin)

##-------- Snow code--------
###bottom cirlce
##draw_circ(anchX, anchY * .71, anchR * 1.21, "white", WinterWin)
##
###middle circle
##draw_circ(anchX, anchY, anchR, "white", WinterWin)
##
###top circle
##draw_circ(anchX, anchY * 1.25, anchR * .82, "white", WinterWin)
##
###snowman eyes
##draw_circ(anchX - anchR / 3, 180, anchR * .11, "black", WinterWin)
##
###----------------
##draw_circ(anchX + anchR / 3, 180, anchR * .11, "black", WinterWin)
##
###nose
