
# Author: Micheala Jackson
# Username: jacksonmic
#

# Assignment: A02: Exploring Turtles in Python
# Purpose: Draws a 3D cube using turtles and nested for loops
######################################################################
# Acknowledgements: William Romano

# Original code by: Dr. Scott Heggen

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
######################################################################
import turtle   #imports turtle library

wn = turtle.Screen()  #graphic window
a_turtle = turtle.Turtle()
a_turtle.color('purple')   #turns the arrow purple
a_turtle.shape("arrow")    # turns the 'turtle' shape into an arrow

bturtle = turtle.Turtle()
bturtle.color('blue') #turns the bturtle blue
bturtle.shape('turtle') #makes bturtle shape a turtle

a_turtle.penup()
bturtle.penup()

size = 10   #sets the size of the pen to 10
for i in range(20):
    a_turtle.stamp()
    size = size + 8 #increases the pen size by 8
    a_turtle.forward(size) #moves the arrow foward by 8
    a_turtle.right(24) #turns the arrow right 24 degrees
    a_turtle.pendown()

size = 10  #Will helped by showing me how to reset the size variable
for i in range(20):
    bturtle.stamp()
    size = size + 4 #increases the pen size by 4
    bturtle.forward(size) #moves the arrow foward by 4
    bturtle.right(25) #turns the arrow right 24 degrees
    bturtle.pendown()






