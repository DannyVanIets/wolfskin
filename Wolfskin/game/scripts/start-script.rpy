# The script of the game goes in this file.

#config auto voice

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define il = Character("Ilona", ctc="ctc_anchored", ctc_position="fixed", namebox_background = "gui/ribbons/ilona_ribbon.png")
define ed = Character("Edwin", ctc="ctc_anchored", ctc_position="fixed", namebox_background = "gui/ribbons/edwin_ribbon.png")
define an = Character("Anari", ctc="ctc_anchored", ctc_position="fixed", namebox_background = "gui/ribbons/anari_ribbon.png")
define fl = Character("Fleur", ctc="ctc_anchored", ctc_position="fixed", namebox_background = "gui/ribbons/fleur_ribbon.png")
define ke = Character("Kellac", ctc="ctc_anchored", ctc_position="fixed", namebox_background = "gui/ribbons/kellac_ribbon.png")
define ei = Character("Eisleigh", ctc="ctc_anchored", ctc_position="fixed", namebox_background = "gui/ribbons/eisleigh_ribbon.png")
define sa = Character("Salome", ctc="ctc_anchored", ctc_position="fixed", namebox_background = "gui/ribbons/salome_ribbon.png")
define ul = Character("Uldin", ctc="ctc_anchored", ctc_position="fixed", namebox_background = "gui/ribbons/uldin_ribbon.png")
define unk = Character("???", ctc="ctc_anchored", ctc_position="fixed", namebox_background = "gui/ribbons/default_ribbon.png")
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

## Commonly used sprite positions

# variations of left
transform extra_left:
    xcenter 250

transform less_left:
    xcenter 540

# variations of right
transform extra_right:
    xcenter 1670

transform less_right:
    xcenter 1380

# to put two characters in the center
transform left_center:
    xcenter 640

transform right_center:
    xcenter 1280


## TINT MATRICES

# I'm going bob ross over Here

define dark_matrix = (
    TintMatrix(Color(rgb=(0.46, 0.7, 1.2)))*BrightnessMatrix(-0.02)
    )

define sunset_matrix = (
    TintMatrix(Color(rgb=(1.00, 0.80, 0.95)))*BrightnessMatrix(-0.06)
    )

define dim_matrix = (
    TintMatrix(Color(rgb=(0.9, 0.9, 1)))*BrightnessMatrix(-0.1)
    )

define bw_matrix = (
    TintMatrix("#EDFAFF") * SaturationMatrix(0.0, (0.39, 0.39, 0.39))
    )

define twilight_matrix = (
    TintMatrix(Color(rgb=(0.9, 1.0, 1.2)))*BrightnessMatrix(-0.08)
    )

define sil_matrix = (
    TintMatrix(Color(rgb=(0.9, 1.0, 1.2)))*BrightnessMatrix(-1.0)
    )

# sprites with night shading (weak)
image edwin_twilight = LayeredImageProxy("edwin", Transform(matrixcolor=twilight_matrix))
image ilona_twilight = LayeredImageProxy("ilona", Transform(matrixcolor=twilight_matrix))
image anari_twilight = LayeredImageProxy("anari", Transform(matrixcolor=twilight_matrix))
image kellac_twilight = LayeredImageProxy("kellac", Transform(matrixcolor=twilight_matrix))
image eisleigh_twilight = LayeredImageProxy("eisleigh", Transform(matrixcolor=twilight_matrix))
image salome_twilight = LayeredImageProxy("salome", Transform(matrixcolor=twilight_matrix))
image uldin_twilight = LayeredImageProxy("uldin", Transform(matrixcolor=twilight_matrix))

# sprites with night shading (strong)
image edwin_night = LayeredImageProxy("edwin", Transform(matrixcolor=dark_matrix))
image ilona_night = LayeredImageProxy("ilona", Transform(matrixcolor=dark_matrix))
image anari_night = LayeredImageProxy("anari", Transform(matrixcolor=dark_matrix))
image kellac_night = LayeredImageProxy("kellac", Transform(matrixcolor=dark_matrix))
image eisleigh_night = LayeredImageProxy("eisleigh", Transform(matrixcolor=dark_matrix))
image salome_night = LayeredImageProxy("salome", Transform(matrixcolor=dark_matrix))
image uldin_night = LayeredImageProxy("uldin", Transform(matrixcolor=dark_matrix))

# sprites with sunset shading
image edwin_sunset = LayeredImageProxy("edwin", Transform(matrixcolor=sunset_matrix))
image ilona_sunset = LayeredImageProxy("ilona", Transform(matrixcolor=sunset_matrix))
image anari_sunset = LayeredImageProxy("anari", Transform(matrixcolor=sunset_matrix))
image kellac_sunset = LayeredImageProxy("kellac", Transform(matrixcolor=sunset_matrix))
image eisleigh_sunset = LayeredImageProxy("eisleigh", Transform(matrixcolor=sunset_matrix))

# sprites with dim shading
image edwin_dim = LayeredImageProxy("edwin", Transform(matrixcolor=dim_matrix))
image ilona_dim = LayeredImageProxy("ilona", Transform(matrixcolor=dim_matrix))
image anari_dim = LayeredImageProxy("anari", Transform(matrixcolor=dim_matrix))
image kellac_dim = LayeredImageProxy("kellac", Transform(matrixcolor=dim_matrix))
image eisleigh_dim = LayeredImageProxy("eisleigh", Transform(matrixcolor=dim_matrix))
image salome_dim = LayeredImageProxy("salome", Transform(matrixcolor=dim_matrix))
image uldin_dim = LayeredImageProxy("uldin", Transform(matrixcolor=dim_matrix))
image fleur_dim = LayeredImageProxy("fleur", Transform(matrixcolor=dim_matrix))

# sprites with bw shading
image salome_bw = LayeredImageProxy("salome", Transform(matrixcolor=bw_matrix))
image uldin_bw = LayeredImageProxy("uldin", Transform(matrixcolor=bw_matrix))
image fleur_bw = LayeredImageProxy("fleur", Transform(matrixcolor=bw_matrix))
image edwin_bw = LayeredImageProxy("edwin", Transform(matrixcolor=bw_matrix))

# sprites black silhouette
image salome_sil = LayeredImageProxy("salome", Transform(matrixcolor=sil_matrix))
image uldin_sil = LayeredImageProxy("uldin", Transform(matrixcolor=sil_matrix))
image fleur_sil = LayeredImageProxy("fleur", Transform(matrixcolor=sil_matrix))
image edwin_sil = LayeredImageProxy("edwin", Transform(matrixcolor=sil_matrix))

## LAYERED IMAGES

# begin auto_layeredimage for Edwin

layeredimage edwin:

    always:
        "edwin_base"

    group outfit:
        attribute wolf
        attribute blood

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

    group outfit:
        attribute blood

    group emotion auto

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

# begin auto_layeredimage for eisleigh

layeredimage eisleigh:

    always:
        "eisleigh_base"

    group eyes auto:
        attribute look default

    group eyebrows auto:
        attribute relaxed default

    group mouth auto:
        attribute smile default

    group glasses auto:
        attribute regular default

    group emotion auto

# begin auto_layeredimage for Fleur

layeredimage fleur:

    always:
        "fleur_base"

    group eyes auto:
        attribute look default

    group mouth auto:
        attribute smile default

# begin auto_layeredimage for Salome

layeredimage salome:

    always:
        "salome_base"

    group eyes auto:
        attribute open default

    group eyebrows auto:
        attribute relaxed default

    group mouth auto:
        attribute smallgrin default

    group emotion auto

# begin auto_layeredimage for Uldin

layeredimage uldin:

    always:
        "uldin_base"

    group eyes auto:
        attribute open default

    group eyebrows auto:
        attribute relaxed default

    group mouth auto:
        attribute smile default

    group emotion auto

## BACKGROUNDS

image bg_repeating_town_plaza_blurry:
    "bg town plaza morning" with dissolve
    pause 1
    "bg town plaza morning blurry" with dissolve
    pause 1
    repeat

image bg_repeating_town_plaza_kellac_blurry:
    "bg town plaza morning kellac" with dissolve
    pause 0.3
    "bg town plaza morning kellac blurry" with dissolve
    pause 2
    repeat

image bg_transition_blurry_kellac_extreme:
    "bg town plaza morning kellac blurry" with dissolve
    pause 0.3
    "bg town plaza morning kellac blurry extreme" with dissolve

image cg_repeating_edwolf_edgewolf_blurry:
    "hd edwolf final" with dissolve
    pause 2
    "hd edwolf final blurry" with dissolve
    pause 1
    repeat

## FILTER IMAGES

# Overlay a black bg with alpha value changed, on top of a scene to simulate slow eyeblinking.
image slow_eyeblink_filter:
    "bg black"
    alpha 0
    linear 2 alpha 0.85
    pause 1.5 alpha 0.85
    linear 1.8 alpha 0

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

# long dissolve for suspenseful introductions of characters
define longdissolve = Dissolve(3.0)


# logo transition

define logodissolve = MultipleTransition([
    False, Dissolve(0.7),
    "logo.png", Pause(4.0),
    "logo.png", dissolve,
    True])

# drop shadows for dialogue box

style say_label:
    outlines [ ( 0, "#000000", 1, 1) ]

style say_dialogue:
    outlines [ ( 0, "#000000", 1, 1) ]

# The game starts here.
label start:

    scene bg forest night

    # Stop the main menu music
    stop music fadeout 0.1

    # Start the game from the first act
    jump act1

    # menu:
    #     "Click the act you want to go to!"
    #
    #     "Act 1":
    #         jump act1
    #
    #     "Act 2":
    #         jump act2
    #
    #     "Act 3":
    #         jump act3
    #
    #     "Blurry and shaking":
    #         jump blurry_shake
    #
    #     "Action Editor Test":
    #         jump action_editor_test
    #
    #     "Scrolling Background Test":
    #         jump scrolling_bg_test
    #
    #     "Credits":
    #         jump credits_from_script
    #
    #     "Epilogue":
    #         jump epilogue
