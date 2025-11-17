# Maths stuff with python
# Author: rachel
# 12 Nov 2025

import math

# # try to add
# def addition(x: int, y: int) -> int:
#     return x + y


# def main():
#     print("do you know how to do addition?")
#     print("let me show you")
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(f"the addition of these 2 numbers is {addition(x, y)}!")


# if __name__ == "__main__":
#     main()


def square(x: float, y: float) -> float:
    return x * y


def main():
    print("let me help you find the area of a rectangle")
    print("give me 2 numbers, it could have decimals!")
    x = float(input("x = "))
    y = float(input("y = "))
    print(f"The area of your rectangle is {square(x, y)}")


if __name__ == "__main__":
    main()
