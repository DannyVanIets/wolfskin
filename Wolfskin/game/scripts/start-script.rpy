# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define test = Character("Remove") # Remove any text from this character before uploading and remove the character too!
define il = Character("Ilona")
define ed = Character("Edwin")
define an = Character("Anari")
define fl = Character("Fleur")
define ke = Character("Kellac")
define ei = Character("Eisleigh")
define sa = Character("Salome")
define ul = Character("Uldin")

# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg forest night

    menu:
        "Click the act you want to go to!"

        "Act 1":
            jump act1

        "Act 2":
            jump act2

        "Act 3":
            jump act3

        "Credits":
            jump credits_from_script
