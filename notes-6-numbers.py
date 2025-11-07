# Numbers and Operations
# Author: Rachel
#  5 November 2025

# Create an algorithm to gather
# data to find the most popular
# bubble ttea place around us

# Version 1
def vote_listed_choices():
    """Display all voting choices
    5 users vote for their choice
    Results will be printed"""
    CHOICES = [
        "A, Coco",
        "B, Chatime",
        "C, BUBBLE WAFFLE",
        "D, gong cha",
        "E, suntea",
    ]

    # Buckets to hold all the votes
    coco = 0
    chatime = 0
    bubble_waffel = 0
    gong_cha = 0
    suntea = 0

    # Show all the Bbt choices
    print("Vote for your favorite from the list.")
    print("Give the letter of yor choice")
    for choice in CHOICES:
        print(choice)
    # Ask the user for their choice
    vote = input("Your vote: ").lower().strip(",.!? ")
    # Add their vote to a running tally
    if vote == "a":
        coco = coco + 1  # incremetation
    elif vote == "b":
        chatime += 1
    elif vote == "c":
        bubble_waffel += 1
    elif vote == "c":
        gong_cha += 1
    elif vote == "e":
        suntea += 1
    # Give some raw scores
    # give score as a percentage


# Version 2
# ask the user what their favorite bbt place
# Add their vote to a running tally
# Give the raw scores
# give score as a perentage


def main():
    vote_listed_choices()


if __name__ == "__main__":
    main()
