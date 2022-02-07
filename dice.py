# dice.py
# this imports the random module
import random
DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "
# The job of the parse_input function is to take the user's input and check
# if it is a valid integer number
# This line defines parse_input
def parse_input(input_string):
    # This is a docstring- infomative and wellformatted- a best practice
    """Return input string as an integer between 1 and 6.

     Check if input_string is an integer number between 1 and 6.
     If so, return an integer with the same value. Otherwise, tell the user to
     enter a valid number and quit the program.
     """
     # This line checks if user input is valid number, strips unwanted
     # spaces, and uses the in operator to see if the input falls
     #within the number of accepted dice to roll
    if input_string.strip() in {"1", "2", "3", "4", "5", "6"}:
         # this line converts the input into an integer and returns it
        return int(input_string)
    else:
         # This prints a message to the screen if input is invalid
        print("Please enter a number from 1 to 6.")
         # this exits the app
        raise SystemExit(1)
# Defines roll_dice
def roll_dice(num_dice):
    """Return a list of integers with length `num_dice`.

    Each integer in the returned list is a random number between
    1 and 6, inclusive.
    """
    # Creates an empty list to store results
    roll_results = []
    # sets up a for loop to iterate through the num_dice
    for _ in range(num_dice):
        #calls randint to generate a random number from 1 to 6
        roll = random.randint(1, 6)
        # adds the number to roll_results
        roll_results.append(roll)
    #returns the list
    return roll_results

def generate_dice_faces_diagram(dice_values):
    """Return an ASCII diagram of dice faces from `dice_values`.

    The string returned contains an ASCII representation of each die.
    For example, if `dice_values = [4,1,3,2]` then the string representation
    looks like this:
     ~~~~~~~~~~~~~~~~~~~ RESULTS ~~~~~~~~~~~~~~~~~~~
    ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
    │  ●   ●  │ │         │ │  ●      │ │  ●      │
    │         │ │    ●    │ │    ●    │ │         │
    │  ●   ●  │ │         │ │      ●  │ │      ●  │
    └─────────┘ └─────────┘ └─────────┘ └─────────┘
    """
    # Generate a list of dice faces from DICE_ART
    dice_faces = []
    for value in dice_values:
        dice_faces.append(DICE_ART[value])

    # Generate a list containing the dice faces rows
    dice_faces_rows = []
    for row_idx in range(DIE_HEIGHT):
        row_components = []
        for die in dice_faces:
            row_components.append(die[row_idx])
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)

    # Generate a header with the word "RESULTS" centered
    width = len(dice_faces_rows[0])
    diagram_header = " RESULTS ".center(width, "~")

    dice_faces_diagram = "\n".join([diagram_header]+ dice_faces_rows)
    return dice_faces_diagram



# App's main code block
# 1. get and validate information from the user
# This asks the user how many dice they want to role.
num_dice_input = input("How many dice do you want to role? [1-6]: ")
# This calls parse_input and stores the return value in num_dice
num_dice = parse_input(num_dice_input)
# 2. Roll the dice
roll_results = roll_dice(num_dice)
print(roll_results)# remove after test
# 3. Generate the ASCII diagram of the dice faces
dice_faces_diagram = generate_dice_faces_diagram(roll_results)
# 4. display the diagram
print(f"\n{dice_faces_diagram}")
