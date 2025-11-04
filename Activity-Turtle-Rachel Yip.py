# Turtle Artist
# Author: Rachel Yip
# 28 October

import turtle
import random

# A one-of-a-kind drawing

wn = turtle.Screen()
Co = turtle.Turtle()
Co.speed(9)
# dictionary for all colors
FLOWER_COLOURS = {
    "grass": "#73bf75",
    "lavender": "#DFC5FE",
    "pink": "#FFC0CB",
    "yellow": "#FFEE8C",
    "brown": "#8C5311",
    "blue": "#BFDAF7",
    "dark_blue": "#6876c4",
}


# set up background
wn.bgcolor("#E2FDFF")
Co.pencolor(FLOWER_COLOURS["grass"])
Co.penup()
Co.goto(-800, 20)
Co.pendown()

# make grass field
Co.fillcolor(FLOWER_COLOURS["grass"])
Co.begin_fill()
Co.forward(1500)
Co.right(90)
Co.forward(600)
Co.right(90)
Co.forward(1500)
Co.right(90)
Co.forward(600)
Co.end_fill()

# make the sun
Co.penup()
Co.color(FLOWER_COLOURS["yellow"])
Co.goto(-300, 260)
Co.fillcolor(FLOWER_COLOURS["yellow"])
Co.begin_fill()
Co.pendown()
Co.circle(30)
Co.end_fill()


# make sun glow reursively 😏
def sun_glow(inner_size: int, outer_size: int):
    if outer_size > 0:
        Co.width(2)
        Co.pendown()
        Co.circle(inner_size)
        Co.penup()
        Co.right(90)
        Co.forward(10)
        Co.left(90)
        sun_glow(inner_size + 10, outer_size - 1)


sun_glow(30, 4)

Co.width(1)
# build a mountain
Co.speed(2)
Co.pu()
Co.goto(0, 20)
Co.right(45)
Co.begin_fill()
Co.color("#578f59")
Co.pd()
Co.forward(500)
Co.right(90)
Co.forward(500)
Co.right(135)
Co.forward(707)
Co.end_fill()


# make big sunflowers
def draw_sunflower(x: int, y: int):
    Co.pu()
    Co.goto(x, y)
    Co.color("orange")
    Co.pd()
    Co.speed(11)
    Co.setheading(0)
    Co.fillcolor(FLOWER_COLOURS["yellow"])
    Co.begin_fill()
    for _ in range(11):
        # point east
        Co.forward(70)
        Co.right(131)
    Co.end_fill()
    Co.pu()
    Co.right(48)
    Co.forward(35)
    Co.pd()
    Co.color(FLOWER_COLOURS["brown"])
    Co.fillcolor(FLOWER_COLOURS["brown"])
    Co.begin_fill()
    Co.circle(15)
    Co.end_fill()


for _ in range(15):
    x = random.randrange(-600, 600)
    y = random.randrange(-500, -50)
    draw_sunflower(x, y)


# make a pink flower
def draw_pink_flower(x: int, y: int):
    Co.pu()
    Co.goto(x, y)
    Co.color("#ff99df")
    Co.pd()
    Co.speed(11)
    Co.setheading(0)
    Co.fillcolor(FLOWER_COLOURS["pink"])
    Co.begin_fill()
    for _ in range(11):
        # point east
        Co.forward(50)
        Co.right(131)
    Co.end_fill()
    Co.pu()
    Co.right(48)
    Co.forward(25)
    Co.pd()
    Co.color(FLOWER_COLOURS["yellow"])
    Co.fillcolor(FLOWER_COLOURS["yellow"])
    Co.begin_fill()
    Co.circle(11.5)
    Co.end_fill()


for _ in range(15):
    x = random.randrange(-600, 600)
    y = random.randrange(-500, -50)
    draw_pink_flower(x, y)


# draw a purple flower
def draw_purple_flower(x: int, y: int):
    Co.pu()
    Co.goto(x, y)
    Co.color("#ad97c9")
    Co.pd()
    Co.speed(11)
    Co.setheading(0)
    Co.fillcolor(FLOWER_COLOURS["lavender"])
    Co.begin_fill()
    for _ in range(11):
        # point east
        Co.forward(25)
        Co.right(131)
    Co.end_fill()
    Co.pu()
    Co.right(48)
    Co.forward(12.5)
    Co.pd()
    Co.color(FLOWER_COLOURS["yellow"])
    Co.fillcolor(FLOWER_COLOURS["yellow"])
    Co.begin_fill()
    Co.circle(5.5)
    Co.end_fill()


for _ in range(15):
    x = random.randrange(-600, 600)
    y = random.randrange(-500, -50)
    draw_purple_flower(x, y)


# make blue flowers
def draw_blue_flowers(x: int, y: int):
    Co.pu()
    Co.goto(x, y)
    Co.color(FLOWER_COLOURS["blue"])
    Co.pd()
    Co.speed(11)
    Co.setheading(0)
    Co.fillcolor(FLOWER_COLOURS["blue"])
    Co.begin_fill()
    for _ in range(11):
        # point east
        Co.forward(35)
        Co.right(131)
    Co.end_fill()
    Co.pu()
    Co.right(48)
    Co.forward(17.5)
    Co.pd()
    Co.color("white")
    Co.fillcolor("white")
    Co.begin_fill()
    Co.circle(7)
    Co.end_fill()


for _ in range(15):
    x = random.randrange(-600, 600)
    y = random.randrange(-500, -50)
    draw_blue_flowers(x, y)


# draw daisies flowers
def draw_daisies(x: int, y: int):
    Co.pu()
    Co.goto(x, y)
    Co.color("white")
    Co.pd()
    Co.speed(11)
    Co.setheading(0)
    Co.fillcolor("white")
    Co.begin_fill()
    for _ in range(11):
        # point east
        Co.forward(50)
        Co.right(131)
    Co.end_fill()
    Co.pu()
    Co.right(48)
    Co.forward(25)
    Co.pd()
    Co.color("orange")
    Co.fillcolor(FLOWER_COLOURS["yellow"])
    Co.begin_fill()
    Co.circle(11.5)
    Co.end_fill()


for _ in range(20):
    x = random.randrange(-600, 600)
    y = random.randrange(-500, -50)
    draw_daisies(x, y)


wn.exitonclick()
