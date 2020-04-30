# -*- coding: utf-8 -*-
import turtle
import math
wn=turtle.Screen()
wn.bgcolor("white")
turt=turtle.Turtle()
turt.speed(0)
turt.shape("turtle")

turt.color("green") #background circle
turt.up()
turt.goto(0,-200)
turt.down()
turt.width(4)
turt.begin_fill()
turt.circle(200)
turt.end_fill()

turt.color("black") #black square
turt.width(3)
turt.up()
turt.goto(-100,-100)
turt.down()
turt.begin_fill()
for j in range(0,4):
    turt.forward(200)
    turt.left(90)
turt.end_fill()
turt.width(1)
turt.left(90)

turt.up()
turt.goto(0,0)
turt.down()
turt.color("light blue")
for i in range(0,120): #blue lines thing
    turt.forward(100)
    turt.goto(0,0)
    turt.left(3)

turt.color("dark blue") #right triangle
turt.up()
turt.goto(100,-100)
turt.down()
turt.width(4)
turt.right(45)
turt.begin_fill()
turt.forward((200/math.sqrt(2)))
turt.left(90)
turt.forward((200/math.sqrt(2)))
turt.left(135)
turt.width(1)
turt.forward(200)
turt.end_fill()

turt.width(4)
turt.left(180) #upper triangle
turt.up()
turt.goto(100,100)
turt.down()
turt.width(4)
turt.left(45)
turt.begin_fill()
turt.forward((200/math.sqrt(2)))
turt.left(90)
turt.forward((200/math.sqrt(2)))
turt.left(135)
turt.width(1)
turt.forward(200)
turt.end_fill()
turt.left(90)

turt.width(4) #left triangle
turt.up()
turt.goto(-100,100)
turt.down()
turt.width(4)
turt.left(135)
turt.begin_fill()
turt.forward((200/math.sqrt(2)))
turt.left(90)
turt.forward((200/math.sqrt(2)))
turt.left(135)
turt.width(1)
turt.forward(200)
turt.end_fill()

turt.width(4) #lower triangle
turt.up()
turt.goto(-100,-100)
turt.down()
turt.width(4)
turt.right(135)
turt.begin_fill()
turt.forward((200/math.sqrt(2))) 
turt.left(90)
turt.forward((200/math.sqrt(2)))  #after writing all the code for the triangles,
turt.left(135)                    #I know realize I could have used .goto() for less math
turt.width(1)                     #I'm not going to change it now though.
turt.forward(200)    #At least the triangles were mostly copy and paste from the first one
turt.end_fill()
turt.right(90)  #I also now realize I could have just made these a square in the background
                #But apparently I just like to complicate things
                
turt.up() #white quadrilateral
turt.goto(-100,0)
turt.color("white")
turt.down()
turt.begin_fill()
turt.goto(0,30)
turt.goto(100,00)
turt.goto(0,-30)
turt.goto(-100,0)
turt.end_fill()

turt.up() #text
turt.color("black")
turt.goto(-60,-15)
turt.write("Britton Inc.",font=("Arial",18,"bold"))
turt.goto(-300,-300)

wn.exitonclick()

