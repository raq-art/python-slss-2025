# Functions

8 October 2025

## Function *Friends*

```python
print("Hello!")
print(2.1)
```

Print is a **function** that outputs values to the console.

```python
user_information = input("Some Prompt:")
```

Input is a **function** that waits for a user to give some information, then it *returns* their input.

## What is a Function?

> A function is a **block of reusable code** with a **name**.

##  `def`ining your own Function

```python
def  <function_name>(<optional perameters>):
	<code block>
```

1. use the `def` keyword
2. give the function a good **name**
	1. convention - use lower case characters and underscores
	2. write your code in an **indented codeblock**
  
## Calling a Function

When we use a function, we say that we **call** it
We call a function by using its name followeed by parentheses. If there are any values the functon **needs**, we put those values inside the parentheses. 

```python
<function_name>(<optional arguments>)
```

## Practical Example

We can **normalize input**  so that our programs can be more robust.

```python
weather_reply = nput("what's the weather like?").lower().strip(",!? ")
```

To optimize the code above, we can use **functions**

```python
def normalized_input():
	"""Clean up the user's input"""
	output = input()
	otput.strip(".,?!").lower
	return output 

# Ask the user for the weather
print("What's the weather like?")
weather_reply = normalized_input()

if weather_reply == "rainy":
	print("you should briing an umbrella.")

```


## Parameters

**Parameters** are the **inputs** of the function.

```python
# Create a function that represents f(x) = x^2
def squared(num: float): 
	output = num ** 2
	print(output)

def power(num: float, exp: float):
	"""raise a number to a power."""
	output = num **exp
	print output

squared(2)   # 4
squared(6.5)  # 6.5 * 6.5'
power(2, 2)  # 4
```

## `return` values

The **return** keyword is used to give the function an **output values**.
In a function, the `return` keyword will stop the execution of the rest of the function.

```python
def some_fun():
	print("hello!")

def some_fun_return() -> str:
	print("hello!")
	return "hello"

return_val = some_fun()

print(return_val) # what's the difference?

return_val = some_fun_return()

print(return_val) # what's the difference?
```

## Default Arguments

**Parameters** are the *inputs* to a function.
**Arguments** are the *values* given as inputs.

```python
# our example from notes-3-functions.py
# defauult name -> "Tiger"
def say_hello_personal(name="Tiger": str):
	print(f"hello {name}")

say_hello_personal("David")
say_hello_persoal()
```