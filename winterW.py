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

anchX = 100
anchY = 140
anchR = 28

#bottom cirlce
draw_circ(anchX, anchY * .71, anchR * 1.21, "white", WinterWin)

#middle circle
draw_circ(anchX, anchY, anchR, "white", WinterWin)

#top circle
draw_circ(anchX, anchY * 1.25, anchR * .82, "white", WinterWin)

#snowman eyes
draw_circ(anchX - anchR / 3, 180, anchR * .11, "black", WinterWin)

#----------------
draw_circ(anchX + anchR / 3, 180, anchR * .11, "black", WinterWin)

#nose
nose = Polygon(Point(100,170), Point(105,175), Point(120,160))
nose.setOutline("orange")
nose.setFill("orange")
nose.draw(WinterWin)

#Bottom snow 
Rect = Rectangle(Point(0,0),Point (600,78))
Rect.setFill("light gray")
Rect.draw(WinterWin)
