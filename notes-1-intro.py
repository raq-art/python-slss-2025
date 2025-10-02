# Notes - Introduction
# 16 September
# Raachel Yip

# Create an algorithm to solve a problem
# Problem: Create our own chatbot
#          MeGPT

# 1. Greet the user with a predetermined statement
greeting = "Hello! I am a chatbot."

# 1a. Print the greeting
print(greeting)

# 2. Introduce the bot
print("My name is MeGPT.")
print("I'm not like the other guy.")
print("I am completely deterministic.")

# 3. Wow the user with some maths
print("I bet you don't know what 8*8 is.")
print("I can do it.")
print(f"8*8 is actually {8*8}")

print("What is pi squared?")
print("I'm smart, I can do it too.")
print(f"It is {3.14159265359 ** 2}")

# 4. Make the bot crash out a little bit.
print("The quick brown fox jumps over the lazy dog." * 10)

# 5. Get the name of the user, store it and use it
user_name = input("What's your name? ")
print(f"It's nice to meet you, {user_name}!")

# 6. ask what's their favorite food
favorite_food = input("What's your favorite food? ")
print(f"I like {favorite_food} too {user_name}!")

# 7. find where the user is from
where_user_is_from = input(f"Where are you from {user_name}?")
print(f"Wow, I heard {where_user_is_from} is beautiful!")
print("Wish I can see...")

# 8. find out what the user likes to do in their free time
user_hobby = input(f"What do you like to do in your free time {user_name}?")
print(f"Wow, {user_hobby} sounds so fun!")

# 9. See if the user is someone specific.
# 9a. If they're someone specific, tell them a secret.
if user_name == "Coco":
    print("I know you like to drink water.")
    print("Don't worry, I won't tell anyone. Shhhhhhhhh.....")
else:
    print("I don't have any secrets for you.")

    favourite_book = input("What's your favourite book?")

    if favourite_book== "Harry Potter":
        print("I like Harry Potter too!")
