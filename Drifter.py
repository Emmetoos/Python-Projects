import turtle
import keyboard
import math

#Variables
shipVelocityX = 0
shipVelocityY = 0
shipRotateSpeed = 0

movementAccelerationMultiplier = 5
movementDecayMultiplier = 0.9

rotationalAccelerationMultiplier = 0.1
rotationDecayMultiplier = 0.9

penTimePassed = 0
shapeTimePassed = 0

#Turtles
ship = turtle.Turtle()
ship.radians()
ship.penup()
turtleShapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
currentShape = 0
ship.shape(turtleShapes[currentShape])

screen = turtle.Screen()

#Loop
while True:
    if (keyboard.is_pressed("up")):
        shipVelocityX += (math.cos(ship.heading()) * movementAccelerationMultiplier)
        shipVelocityY += (math.sin(ship.heading()) * movementAccelerationMultiplier)
    
    if (keyboard.is_pressed("left")):
        shipRotateSpeed += rotationalAccelerationMultiplier

    if (keyboard.is_pressed("right")):
        shipRotateSpeed -= rotationalAccelerationMultiplier

    if keyboard.is_pressed("enter"):
        screen.bye()
        break

    if keyboard.is_pressed("space") & (ship.isdown() == True) & (penTimePassed >= 5):
        ship.penup()
        penTimePassed = 0

    if keyboard.is_pressed("space") & (ship.isdown() == False) & (penTimePassed >= 5):
        ship.pendown()
        penTimePassed = 0

    if keyboard.is_pressed("shift") & (shapeTimePassed >= 5):
        currentShape += 1
        ship.shape(turtleShapes[currentShape % len(turtleShapes)])
        shapeTimePassed = 0

    shipVelocityX *= movementDecayMultiplier
    shipVelocityY *= movementDecayMultiplier

    shipRotateSpeed *= rotationDecayMultiplier

    shipVelocities = (shipVelocityX, shipVelocityY)

    ship.goto(ship.pos() + shipVelocities)

    ship.setheading(ship.heading() + shipRotateSpeed)

    penTimePassed += 1
    shapeTimePassed += 1