# create a function that calculates the average of three numbers. Here are the requirements in detail:
from doctest import OutputChecker


def average(num_one: float, num_two: float, num_three: float):
    output = (num_one + num_two + num_three) / 3
    return output


#  (num1, num2, num3)  ->  average ->
print(average(44, 45, 45))

# call it `average`
#  it should accept three parameters: `num_one`, `num_two`, and `num_three`
#  it should calculate the average value of the three numbers:
# recall that to calculate the average, you add the values then divide by the number of values you have
# return the result
# *Optional*: write another version that accepts a list and returns the average of all things inside the list


# Define a function called create_mood_message.
# It should accept two parameters: name and mood.
# Make the mood parameter optional by giving it a default value of "neutral".
# Inside the function, use an if/elif/else block to check the value of mood:
# If mood is "happy", return a cheerful message like f"Hey {name}, great to see you smiling!".
# If mood is "sad", return a supportive message like f"I hope your day gets better, {name}.".
# If mood  is "neutral", return a message like f"Sometimes you have average days, {name}." .
# For any other mood (the else case), return a neutral message like f"Hi {name}, hope you're having a good day.".
def create_mood_message(name: str, mood: str):
    if mood == "happy":
        return f"Hey {name}, great to see you smiling!"
    elif mood == "sad":
        return f"I hope your day gets better, {name}."
    elif mood == "neutral":
        return f"Sometimes you have average days, {name}."
    else:
        return f"Hi {name}, hope you're having a good day."


result = create_mood_message("Alicia", "happy")
print(result)
