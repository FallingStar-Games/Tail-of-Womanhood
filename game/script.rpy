# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define cw = Character("Developer", who_color="#1f8b4c", what_color="#ff0000")


# The game starts here.

label start:

# Opening content warning message.

    cw "Hey."

    cw "Welcome to {i}A Tail of Womanhood{/i}."

    cw "Please note that this experience contains likely triggering elements."

    cw "It includes online sexual abuse, self-doubt, and transgender feels."

    cw "It is my hope that by not shying away from these elements, this experience will have the ability to help you."

    cw "What you're about to experience is the story of how I realized I was a transgender woman."

    cw "Everything in this story is true, except for the part about realizing you're transgender turning you into a furry."

    cw "That's false, obviously."

    cw "Please feel free to take breaks while experiencing this if you get overwhelmed or to return this game if it sets your PTSD off to the point of being unable to play it."

    cw "Thank you for listening to my story."
    #jump to wolf.rpy, the scene with Dustin.
    jump wolf
