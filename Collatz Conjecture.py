import turtle
import random

#Variables
inputs = int(input("How many numbers? "))

y = []

while inputs > 0: 
    y.append(int(input("Input a number: ")))
    inputs -= 1

xMax = 1
yMax = 1
localYMax = 1

#Functions

#Turtle Things
screen = turtle.Screen()
pen = turtle.Turtle()
screen.colormode(255)

#The Collatz Conjecture
for item in y:

    x = 0
    localYMax = 0

    if(x > xMax): xMax = x
    if(item > yMax): yMax = item
    screen.setworldcoordinates(0, 0, xMax, yMax)

    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    pen.penup()
    pen.setpos(0, item)
    pen.pencolor(r, g, b)
    
    itemStart = item

    while item != 1:
        x += 1

        if(item % 2 == 1):
            item = (3 * item) + 1
        else:
           item = item / 2
    
        if(x > xMax): xMax = x
        if(item > yMax): yMax = item
        if(item > localYMax): localYMax = item
        screen.setworldcoordinates(0, 0, xMax, yMax)

        pen.pendown()

        pen.hideturtle()

        pen.setpos(x, item)
    
    print("Input: " + str(itemStart) + ", Iterations: " + str(x) + ", Max Output: " + str(int(localYMax)))

screen.exitonclick()