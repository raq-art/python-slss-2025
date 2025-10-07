# (String) Methods
# #Auther: Rachel Yip
# 6 October 2025

# Ask the user what the weather is like
weather = input("what's the weather like today?")

if weather.lower().strip("!.?,") == "rainy":
    # Rainy, RAINY, RAiny
    # Rainy!
    # Rainy.
    print("You should bring an umbrella.")
else:
    print("I see...")
