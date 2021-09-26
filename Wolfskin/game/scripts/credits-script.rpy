## You can find the screen in "screens/credits-script.rpy".

## End credits file.
## First we have the labels, which is only used to disable the quick menu, textbox and fade to the credits screen. This will also enable it once it's done with the credits screen.
## In the labels we also go to the screen credits.
## After that is the transform credits_scroll, used to scroll the screen and how far it will go down.

# This label is used after the script is done.
label credits_from_script:
    # If the player is currently skipping text, this removes that textbox. It also autosaves!
    $ renpy.choice_for_skipping()

    ## We hide the quickmenu for the End Credits so they don't appear at the bottom.
    $ quick_menu = False

    ## We hide the textbox as well so it doesn't mess with things.
    window hide

    ## The background of the credits: bg moon for in-game credits
    # a variant of fade is necessary to transition from Act 3 ending CG.
    scene bg moon with longfade

    ## Play credits theme
    play music 'audio/music/Main Theme WIP.mp3' fadein 2.0 noloop

    ## Go to the credits screen, in here is the text for the credits.
    call screen credits

    # Go to the epilogue.
    jump epilogue

# This label is used to go to the credits from the main menu. Doesn't need a whole lot of fancy stuff, so I removed that.
label credits_from_main_menu:
    ## Play music (not the actual in-game credits theme to keep that as a surprise)
    play music 'audio/music/Wolfskin_Main_Theme_Piano_Lead.mp3' fadein 2.0 noloop

    ## The background of the credits: bg fluffies for main menu credits
    scene bg fluffies

    ## Go to the credits screen.
    call screen credits

    # This ends the game and returns you to the main menu.
    return
