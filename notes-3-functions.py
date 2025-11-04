# functions
# Author: Rachel
# 8 October
# function to print "hello" to the consol
def say_hello():
    print("Hello")


# function to print a persoalized hello
def say_hello_personal(name: str):
    print(f"hello {name}!")


say_hello_personal("Coco")
say_hello_personal("Alicia")


def normalized_input():
    """Clean up the user's input"""
    output = input()
    output = output.lower().strip(".,?!")
    return output


# Ask the user for the weather
print("What's the weather like?")
weather_reply = normalized_input()

if weather_reply == "rainy":
    print("you should briing an umbrella.")
