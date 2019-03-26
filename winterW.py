# Winter Wonderland by Akhi & Pauline
from graphics import*

WinterWin = GraphWin("Winter Wonderland",600,600)
WinterWin.setCoords(0,0,600,600)
WinterWin.setBackground("light blue")


circle = Circle(Point(100,100), 25)
circle.setFill("white")
circle.draw(WinterWin)

Rect = Rectangle(Point(0,0),Point (600,80))
Rect.setFill("light gray")
Rect.draw(WinterWin)
