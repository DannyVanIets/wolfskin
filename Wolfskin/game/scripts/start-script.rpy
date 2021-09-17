# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define test = Character("Remove") # Remove any text from this character before uploading and remove the character too!
define il = Character("Ilona", ctc="ctc_anchored", ctc_position="fixed")
define ed = Character("Edwin", ctc="ctc_anchored", ctc_position="fixed")
define an = Character("Anari", ctc="ctc_anchored", ctc_position="fixed")
define fl = Character("Fleur", ctc="ctc_anchored", ctc_position="fixed")
define ke = Character("Kellac", ctc="ctc_anchored", ctc_position="fixed")
define ei = Character("Eisleigh", ctc="ctc_anchored", ctc_position="fixed")
define sa = Character("Salome", ctc="ctc_anchored", ctc_position="fixed")
define ul = Character("Uldin", ctc="ctc_anchored", ctc_position="fixed")
define unk = Character("???", ctc="ctc_anchored", ctc_position="fixed")
define narrator = Character(name=None, ctc="ctc_anchored", ctc_position="fixed")

# moving sprites.

transform easeinleft_transform:
     offscreenleft
     easein 1.0 left

transform easeinright_transform:
     offscreenright
     easein 1.0 right

transform gocenter_transform:
     easein 1.0 center

transform centertoleft_transform:
     center
     easein 1.0 left

transform centertoright_transform:
     center
     easein 1.0 right

transform alphascaleleft_transform:
    zoom 0.50 xpos 100

transform alphascaleright_transform:
    zoom 0.50 xpos 1900

# I'm going bob ross over Here

define dark_matrix = (
    TintMatrix(Color(rgb=(0.9, 1.0, 1.2)))*BrightnessMatrix(-0.08)
    )

image edwin_night = LayeredImageProxy("edwin", Transform(matrixcolor=dark_matrix))
image ilona_night = LayeredImageProxy("ilona", Transform(matrixcolor=dark_matrix))
image anari_night = LayeredImageProxy("anari", Transform(matrixcolor=dark_matrix))

# begin auto_layeredimage for Edwin

layeredimage edwin:

    always:
        "edwin_base"

    group outfit:
        attribute wolf

    group eyes auto:
        attribute open default

    group mouth auto:
        attribute neutral default

    group emotion auto

# begin auto_layeredimage for ilona

layeredimage ilona:

    always:
        "ilona_base"

    group eyes auto:
        attribute open default

    group eyebrows auto:
        attribute relaxed default

    group mouth auto:
        attribute neutral default

    group emotion auto

image ilona night = LayeredImageProxy("ilona", Transform(matrixcolor=BrightnessMatrix(-0.1)))

# begin auto_layeredimage for anari

layeredimage anari:

    always:
        "anari_base"

    group eyes auto:
        attribute open default

    group eyebrows auto:
        attribute relaxed default

    group mouth auto:
        attribute smile default

    group outfit auto:
        attribute unarmed default

    group emotion auto

# begin auto_layeredimage for kellac

layeredimage kellac:

    always:
        "kellac_base"

    group eyes auto:
        attribute open default

    group eyebrows auto:
        attribute relaxed default

    group mouth auto:
        attribute neutral default

    group emotion auto

# CTC SHENANIGANS

image ctc_anchored:
       "ctc.png"
       yalign 0.93 xalign 0.96 #Adjust these numbers to fit your own textbox
       linear 0.95 alpha 1.0
       linear 0.85 alpha 0.0
       repeat

# Hold at black for a bit.
define fadehold = Fade(0.5, 2.0, 0.5)

# long fade
define longfade = Fade(1.5, 0.0, 1.5)

## moving sprites are a pain
define midleft= Position(xpos=0.40)

# drop shadows for dialogue box

style say_label:
    outlines [ ( 0, "#000000", 2, 2) ]

style say_dialogue:
    outlines [ ( 0, "#000000", 2, 2) ]

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
