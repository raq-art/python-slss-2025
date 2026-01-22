# Drawing and Loops
 14 October 2025

 ## Turtles!

 Turtle is a library that helpes us visually interact with Pytho code.

 To draw on the screen, we create turtles. Turtles will be a new **type** of data.

 ## Turtle Boilerplate

**Boilerplate** is code that is freqently copied and pasted.

 ```python
import turtle

wn = turtle.Screen()  # Set up the window and its attributes
wn.bgcolor("lightgreen")

# TMNT - turtles


wn.exitonclick()
```

## Creating Turtles

> The names of the Teenage Mutant Ninja Turtles:
> Blue bandana - Leonardo (Leo)
> Red bandana - Raphael (Raph)
> Purple bandana - Donatello (Donnie)
> Orange bandana - Michaelangelo (Mike)

We need to create **turtle objects**

```python
#create a turtle named mike
mike = turtle.Turtle()
```

## Turtle Methods

```python
mikey = turtle.Turtle()  # creates a turtle object

# change attributes
mikey.size()
mikey.color()
mikey.width()
mikey.penup()    # mikey.pu()
mikey.pendown()  # mikey.pd()
mikey.shape()

# actions
mikey.forward()  # mikey.backward()
mikey.left()     # mikey.right()
mikey.circle()
mikey.goto()
```


## Loops / Iteration

**Iteration** is a word for repitition. 

If we ever want to repeat code, we can use a couple of methods. 

When we **know how many times** we want to repeat something.
we use a `for` loop.

```python
# Print "Hello" 10 times
for _ in rnge(10):
	print("Hello")

# A loop that uses a 'counter'
for counter in range(100)
	print(counter)	# 0, 1, ..., 99
```

## Functions and Turtles



