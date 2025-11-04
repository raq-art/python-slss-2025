# Recursion
# Author: Rachel
# 20 October

# Create a function that draws trees recursively

import turtle

# set up the environment
wn = turtle.Screen()
t = turtle.Turtle()
t.left(90)  # point turtle up
t.penup()  # move the turtle a bit lower
t.goto(0, -200)
t.color("brown")
t.width(5)
t.speed(3)
t.shape("arrow")  # leaf shape

# Create a dictioary of leaf colors
LEAF_COLOURS = {
    "spring": "#ECCBD9",
    "summer": "#A1C181",
    "fall": "#B36A5E",
    "winter": "#E1EFF6",
}


def draw_tree(level: int, branch_length: float):
    """Draw a tree recursively at a given level
    level - the level of branches
    branch_length - length of branch in pixels
    """

    t.pendown()

    # if the level is greater than zero
    if level > 0:
        # 1. Move forward branch_legth
        t.forward(branch_length)
        # 2. turn left and draw a "smaller tree"
        t.left(47)
        draw_tree(level - 1, branch_length * 0.8)
        # 3. go to the middle nd add another tree
        t.right(47)
        draw_tree(level - 1, branch_length * 0.8)
        # 4. Turn right and draw a "smaller tree"
        t.right(47)
        draw_tree(level - 1, branch_length * 0.8)
        # 5. return to the beginning
        t.left(47)
        t.backward(branch_length)
    else:
        # create a leaf
        t.color(LEAF_COLOURS["spring"])
        t.stamp()
        t.color("brown")


# def fibonacci(num: int) -> int:
# """retrns the nth fibonaci num calculated recursively"""
# if num > 2:
# return fibonacci(num - 1) + fibonacci(
# num - 2)  # add the num before it with the num before that
# else:
# return 1


# print(fibonacci(6))
# print(fibonacci(8))

draw_tree(4, 225)

wn.exitonclick()
