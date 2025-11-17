# Boilerplate
# Question 1
#  Age after 31 years
# def age_31(x: int):
#     return x + 24


# def main():
#     print("I can calculate the age of you in 2049")
#     x = int(input("how old are you right now?"))
#     print(f"Your age in 2049 will be {age_31(x + 24)}")


# if __name__ == "__main__":
#     main()


# Question 2
#  Oympic scoring


# def average(
#     a: float,
#     b: float,
#     c: float,
#     d: float,
#     e: float,
# ) -> float:
#     return (a + b + c + d + e) / 5


# def main():
#     a = float(input("judge 1:"))
#     b = float(input("judge 2:"))
#     c = float(input("judge 3:"))
#     d = float(input("judge 4:"))
#     e = float(input("judge 5:"))
#     print("Do you want to know your score average from 5 judges?")
#     print(f" Your average score is {average(a, b, c, d, e)}.")


# if __name__ == "__main__":
#     main()


# Question 3
# McDoland program


def taxed(x: int, y: int):
    return ((x + y) * 0.14) + (x + y)


def main():
    x = 0
    y = 0

    burgers = (
        input("Hello! would you like a burger for $5?(yes/no)").lower().strip(",. !?")
    )
    if burgers == "yes":
        x += 5
        fries = (
            input("Would you also like fries for an extra $3?(yes/no)")
            .lower()
            .strip(",. ?!")
        )
        if fries == "yes":
            y += 3
        print(f"Your total is {taxed(x + y) + (x + y)}")
        else:
            print(f"your total is {")
    elif burgers == "no":
        print("Aww man... ok")
        x = 0
        y = 0
    if x + y > 1:
        print(f"Your total is {taxed(x + y) + (x + y)}")


if __name__ == "__main__":
    main()
