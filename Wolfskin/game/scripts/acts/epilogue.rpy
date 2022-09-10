## The file for the epilogue.

label epilogue:

    # Stop the credits theme
    stop music fadeout 0.1

    scene bg black
    with fade

    $ quick_menu = False

    window hide

    # Toggle on the auto-play
    #$_preferences.afm_enable = True

    # Makes sure that the poem advances automatically. Still possible to instantly see a sentence though!
    # show screen disable_Lmouse()

    # NVL mode: The final poem - this is still being rewritten to have correct stanzas and structure. We are thinking part of this should be spoken in unison, and Edwin and Ilona should have separate parts.

#####   ALTERNATING LINES FOR THE LAST POEM  ########
#
#    Ilona & Edwin:
#       We are found.
#
#    Ilona:
#       Praying deep in dead of night,
#       You have found your path.
#
#    Edwin:
#       Praying still, no end in sight,
#       A pure heart perseveres.
#
#    Ilona:
#       Praying, no desire, delight,
#       A serene soul you see.
#
#    Ilona & Edwin:
#       Bring back those melancholy hearts,
#       Cleanse these with your soul unbound.
#
#    Edwin:
#       Out of sorts, but not far gone,
#       With you, nothing lost is found.
#
######################################################

    nvlNarrator """
    We are found,

    Praying deep in dead of night,

    You have found your path.

    {clear}

    \nPraying still, no end in sight,

    A pure heart perseveres.

    \nPraying, no desire, delight,

    A serene soul you see.

    {clear}

    Bring back those melancholy hearts,

    Cleanse these with your soul unbound.

    Out of sorts, but not far gone,

    With you, nothing lost is found.
    """

    hide screen disable_Lmouse

    nvl clear

    $ persistent.completed = True

    play music 'audio/sfx/birdsong.ogg' volume 0.7

    # Toggle off the auto-play
    #$_preferences.afm_enable = False

    scene no_cry_be_happy with longfade
    $ renpy.pause (6, hard=True)
    scene no_cry_be_end with longdissolve
    $ renpy.pause ()

    # This ends the game and returns you to the main menu.
    return
