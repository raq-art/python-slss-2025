# functions
# Author: Rachel
# 8 October
# function to print "hello" to the consol
def say_hello():
    print("Hello")


# function to print a persoalized hello
# our example from notes-3-functions.py
# defauult name -> "Tiger"
def say_hello_personal(name="Tiger": str):
	print(f"hello {name}")

say_hello_personal("David")
say_hello_personal()


def normalized_input():
    """Clean up the user's input"""
    output = input()
    output.strip(".,?!").lower
    return output


def some_fun():
    print("hello")


def some_fun_return() -> str:
    print("hello!")
    return "purple monkey dishwasher!"
    print("does this run?")  # this does't


#return_val = some_fun_return()
#print(return_val)
