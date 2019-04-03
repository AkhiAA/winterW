# Winter Wonderland by Akhi & Pauline
from graphics import*

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

#----------------
draw_circ(110, 180, 3, "black", WinterWin)

#nose
nose = Line(Point(100,170), Point(120,160))
nose.setFill("orange")
nose.draw(WinterWin)
#Bottom snow 
Rect = Rectangle(Point(0,0),Point (600,78))
Rect.setFill("light gray")
Rect.draw(WinterWin)
