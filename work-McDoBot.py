# McDoBot
# Author: Rachel
# 6 October 2025

# Write a McDonald's bot that asks if you want fries with your meal.
# Call it  work-mcdobot.py .
# appropriately depending on the answer.
# If the user inputs anything else, it should repeat back their answer
# and say that it does not understand.

fries = input("Do you wat fries with your meal?")
if fries.lower().strip("!?., ") == "yes":
    print("Here is your meal with fries!")
elif fries.lower().strip("?!.,") == "no":
    print("Here is your fries-less meal.")
else:
    print("I don't know what you are saying")
