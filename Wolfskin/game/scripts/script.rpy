# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

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

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    ed "Will you please stay with me?"

    il "What? Edwin, please, calm down-"

    ed "... Ilona I-I can’t. Not in a situation like this..."

    il "You’re right, but I need you to slow down. I can’t keep up with you. Moreover, it’s imperative that we don’t look suspicious."

    ed "..."

    il "We have only each other to rely on. Please, excuse me..."

    # Go to the credits.
    jump credits_from_script
