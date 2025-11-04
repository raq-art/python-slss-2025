# Drawin and Loops
# Auther: Rachel
# 14 October 2025

import random
import turtle

window = turtle.Screen()  # Set up the window and its attributes
window.bgcolor("lightblue")

# TMNT - turtles
# create a turtle called mike
mike = turtle.Turtle()
mike.turtlesize(1)  # set size
# mike.shape("turtle")  # set shape
# mike.color("white")  # set color

# move mike around
mike.speed(1.5)
mike.width(3)


# snowman code
# mike.circle(100)
# mike.penup()
# mike.goto(0, 200)
# mike.pendown()
# mike.circle(90)
# mike.penup()
# mike.goto(50, 290)
# mike.pendown()
# mike.circle(10)
# mike.penup()
# mike.goto(-50, 290)
# mike.pendown()
# mike.circle(10)
# mike.penup()
# mike.goto(500, 500)
# Create a function to make cookies
def make_cookies(x: int, y: int):
    # Cookie Making
    # Set the colour of our choco chip cookie
    mike.color("brown")
    # Draw a circle to represent our cookie
    mike.pu()
    mike.setheading(0)  # to make sure mike points east

    mike.goto(-5 + x, -30 + y)
    mike.pd()
    mike.circle(30)
    # Put a choco chip ar the top-right
    mike.pu()
    mike.goto(10 + x, 10 + y)
    mike.pd()
    mike.stamp()
    # Put a choc chip at the bottom-right
    mike.pu()
    mike.goto(10 + x, -10 + y)
    mike.pd()
    mike.stamp()
    # put a choc chi at the botton-left
    mike.pu()
    mike.goto(-10 + x, -10 + y)
    mike.pd()
    mike.stamp()
    # Put a choc chip at the top-left
    mike.pu()
    mike.goto(-10 + x, 10 + y)
    mike.pd()
    mike.stamp()
    # choc chip in mid
    mike.pu()
    mike.goto(0 + x, 0 + y)
    mike.pd()
    mike.stamp()


# Make cookies randomly on the screen
# Make 500 of them
for _ in range(500):
    x = random.randrange(-500, 500)
    y = random.randrange(-500, 500)
    mike.speed(0)
    make_cookies(x, y)

window.exitonclick()
