# Rachel Yip
# sep29 2025
#
# Intro

import time

print(
    "You were banished by the king for not protecting the princes from a kidnapping as her personal knight"
)
time.sleep(1.5)

print(
    "You are now desserted with 2 coins and only a rusty sword and sheild, but you are determined save the princess and regain your honour."
)
time.sleep(1.5)
user_answer = input(
    "While wandering for a place to sleep at night, you see a faint blue light glowing from a distance. Do you want to check it out, find a place to stay or just sleep right where you are? (find a place to stay, sleep where I am, or check it out)"
)

if user_answer == "sleep where I am":
    print("you sleep wide in the open and get eaten by a dragon")
    print("THE END")


if user_answer == "check it out":
    print("you find a broken crystal ball on the ground.")
    time.sleep(1.5)
    print(
        "After reassembling it, it reveals a map. It shows a 5 star airbnb not far from where you are."
    )
    time.sleep(1.5)
    print(
        "You enter the airbnb and find an old man smiling at you in the empty living room"
    )
    yes_no = input(
        "Do you greet the old man and ask him for a room?(yes, no or anything else)"
    )
    if yes_no == "yes":
        print("Hello to you too and of course you can have a room!")
        user_name = input("I'm Bob Ubial. What's your name?")
        print(
            f"Well {user_name}, it is your lucky day. because I'm in a great mood so I'm not going to charge you for a room tonight!"
        )
        print("you continue inyour quest to save the princess full of energy.")

    elif yes_no == "no":
        print("Hey! You! Do you want a room or not?! It's 3 coins per night!")
        print("You only have 2 coins?! Get out.")
        print("you curl up outside and drifted to sleep.")
    else:
        print("The old mman got inpatient and killed you")
        print("THE END")


def kid_yes_no():
    kid_adventure = input("May I join your adventure?(yes or no)")
    if kid_adventure == "yes":
        print("the child has now joined your quest")
    if kid_adventure == "no":
        print("You left the child.")


def fire_path():
    print("you are now warm and continued finding the princess")
    print("You see a young boy getting robbed by bandits")
    help_yes_no = input("Do you go help defend the child?(help or don't help)")
    if help_yes_no == "help":
        print("You run to go help the kid and fought off the bandits.")
        user_name = input("Wow! You saved me! What's your name?")
        if user_name == "knight":
            print("Hey, aren't you the knight that let the princess get kidnapped")
        else:
            print(f"Thank you so much {user_name}!")
        kid_yes_no()
    elif help_yes_no == "don't help":
        print("You ignore the child and continued walking")


def tree_choice():
    print("you rest under a big tree and fell asleep")
    print(
        "after you woke up, you continue trying to find your way in this foreign land"
    )
    print(
        "Next morning, you were freezng because you slept outside. If you don't make or find a fire now you might freeze to death."
    )
    fire_no = input(
        "Are you going to try and find a fire or try and make a fire?(find a fire or make a fire)"
    )
    if fire_no == "find a fire":
        print("you search far and wide but was unable to find a house or fire.")
        print("you freeze to death.")
        print("THE END")
    if fire_no == "make a fire":
        print("you spend 2 hours trying to make a fire, but successfully made a fire!")
        fire_path()


def creepy_dialogue():
    in_out = input("Do you want to rest there?(yes or no)")
    if in_out == "yes":
        print(
            "You enter the hut and there was no one there. So you decide to sleep on an empty bed."
        )
        print("In the middle of the night you suddenly hear a sound.")
        print("A scary figure looms over your head.")
        user_name = input("Who are you and why are you in MY house?!")
        print(f"{user_name}, tonight you DIE")
        print("THE END")
    if in_out == "no":
        tree_choice()


if user_answer == "find a place to stay":
    print(
        "you continue walking even though you're exhausted. You discover a creepy hut infront of you"
    )
    creepy_dialogue()
