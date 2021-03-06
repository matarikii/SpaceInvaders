# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 01:09:03 2020

@author: Marta1
"""

#Space Invaders tuto

#The Screen

import turtle
import os
 #Set up the screen
 
wn= turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
 
 #Draw border
border_pen= turtle.Turtle()
border_pen.speed(0)

border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.down()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Create player
player= turtle.Turtle()
player.color("red")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed= 15

#Create the enemy
enemy= turtle.Turtle()
enemy.color("blue")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

enemyspeed= 2

#Move the player left and right
def move_left():
    x= player.xcor()
    x-= playerspeed
    if x< -280:
        x= -280
    player.setx(x)

def move_right():
    x= player.xcor()
    x+= playerspeed
    if x> 280:
       x= 280
    player.setx(x)
    
#Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")

