# Save the Turkey 🦃
# SBiC GBM: Thanksgiving Code Along (STARTER)
# Fill in the code under each comment! Delete each "pass" once you write that function.

# Import the random module so we can roll random numbers


# Create a variable called STARTING_LIVES and set it to 3


# The story is already written for you!
# Each scene has a description and two choices.
# Each choice has a chance of success (0.0 to 1.0) and a message for each outcome.
scenes = [
    {
        "description": "It's the night before Thanksgiving. You hear Farmer Fred sharpening the carving knife...",
        "choices": [
            {"text": "Hide in the haystack", "chance": 0.7,
             "success": "Fred walks right past you. Smooth.",
             "fail": "You sneeze. Hay fever. Fred spots you and you barely get away!"},
            {"text": "Make a run for the barn door", "chance": 0.5,
             "success": "You waddle out the door at top speed!",
             "fail": "The door is locked and you bonk your beak. Ouch!"},
        ],
    },
    {
        "description": "You made it outside, but there's a tall fence around the whole farm.",
        "choices": [
            {"text": "Dig under the fence", "chance": 0.6,
             "success": "You dig like never before and squeeze right through!",
             "fail": "You hit a rock. Your claws are sore, but you eventually wiggle under."},
            {"text": "Try to fly over it", "chance": 0.4,
             "success": "Turns out turkeys CAN fly (a little)! You clear the fence!",
             "fail": "Turkeys... can't really fly. You faceplant into the mud."},
        ],
    },
    {
        "description": "You reach a busy road. A pumpkin truck is parked nearby.",
        "choices": [
            {"text": "Hop in the back of the pumpkin truck", "chance": 0.6,
             "success": "You blend right in with the pumpkins and ride into town!",
             "fail": "The truck hits a pothole and you go flying out the back!"},
            {"text": "Cut through the cornfield", "chance": 0.7,
             "success": "The corn is tall enough to hide you completely.",
             "fail": "You get stuck in a corn maze for three hours. Exhausting."},
        ],
    },
    {
        "description": "A neighborhood dog spots you and starts barking!",
        "choices": [
            {"text": "Distract it with cranberry sauce", "chance": 0.6,
             "success": "The dog forgets you exist. Cranberry sauce wins again.",
             "fail": "The dog eats the sauce AND keeps chasing you!"},
            {"text": "Play dead", "chance": 0.5,
             "success": "The dog sniffs you, gets bored, and walks away.",
             "fail": "The dog thinks it's a game and drags you around the yard!"},
        ],
    },
    {
        "description": "You made it to town, but every house is cooking Thanksgiving dinner. You need a disguise!",
        "choices": [
            {"text": "Disguise yourself as a ham", "chance": 0.5,
             "success": "Nobody suspects a thing. You are now a ham.",
             "fail": "A family almost puts you in the oven. You escape, but it was close!"},
            {"text": "Join the Thanksgiving parade", "chance": 0.6,
             "success": "You march in the parade and everyone thinks you're a costume!",
             "fail": "A kid points and yells 'REAL TURKEY!' You flee the parade."},
        ],
    },
]


def show_lives(lives):
    # Make a string of hearts, one for each life (hint: you can multiply a string by a number!)

    # Print the hearts and the number of lives, like "Lives: ❤️ ❤️ ❤️ (3)"

    pass


def get_choice(choices):
    # Loop through the choices with enumerate (start counting at 1)

        # Print the number and the choice's text, like "  1. Hide in the haystack"


    # Write a while True loop so we keep asking until we get a valid answer

        # Use input() to ask the room for 1 or 2, and .strip() off extra spaces

        # If the answer is "1" or "2"...

            # Return the matching choice from the list (lists start at 0, so subtract 1!)

        # Otherwise, print a message telling them to pick 1 or 2

    pass


def play_scene(scene, lives):
    # Print a blank line, then print the scene's description


    # Call get_choice() with this scene's choices and save the result in a variable

    # Use random.random() to roll a number between 0 and 1 and save it in a variable

    # If the roll is less than the choice's chance, it worked...

        # Print a ✅ and the choice's success message

    # Otherwise, it failed...

        # Print a ❌ and the choice's fail message

        # Take away one life

    # Call show_lives() to show the updated lives

    # Return the updated lives

    pass


def main():
    # Print the title of the game and a one-line intro


    # Create a lives variable and set it to STARTING_LIVES

    # Call show_lives() to show the starting lives


    # Write a for loop that goes through every scene in scenes

        # Call play_scene() and save the result back into lives

        # If lives is 0 or less, break out of the loop early



    # Print a blank line before the ending

    # If the turkey still has more than 0 lives...

        # Print a win message that says how many lives are left

    # Otherwise...

        # Print a lose message (the turkey is dinner!)

    pass


# Call main() to start the game