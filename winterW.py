# Winter Wonderland by Akhi & Pauline
from graphics import*

WinterWin = GraphWin("Winter Wonderland",600,600)
WinterWin.setCoords(0,0,600,600)
WinterWin.setBackground("light blue")

#bottom cirlce
circle = Circle(Point(100,100), 34)
circle.setFill("white")
circle.setOutline("white")
circle.draw(WinterWin)
#middle circle 
circle = Circle(Point(100,140), 28)
circle.setFill("white")
circle.setOutline("white")
circle.draw(WinterWin)
#top circle
circle = Circle(Point(100,175), 23)
circle.setFill("white")
circle.setOutline("white")
circle.draw(WinterWin)

#snowman eyes
circle = Circle(Point(90,175), 3)
circle.setFill("black")
circle.draw(WinterWin)
#----------------
circle = Circle(Point(110,175), 3)
circle.setFill("black")
circle.draw(WinterWin)
#nose
nose = Line(Point(100,170), Point(120,160))
nose.setFill("orange")
nose.draw(WinterWin)
#Bottom snow 
Rect = Rectangle(Point(0,0),Point (600,78))
Rect.setFill("light gray")
Rect.draw(WinterWin)
