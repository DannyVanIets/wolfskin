## You can find the screen in "screens/credits-script.rpy".

## End credits file.
## First we have the labels, which is only used to disable the quick menu, textbox and fade to the credits screen. This will also enable it once it's done with the credits screen.
## In the labels we also go to the screen credits.
## After that is the transform credits_scroll, used to scroll the screen and how far it will go down.

# This label is used after the script is done.
label credits_from_script:

    # Variable created to update if the preference Skip: After Choices is enabled.
    # We set it automatically here to False, so Ren'Py knows the variables is created and that it won't set the Skip: After Choices suddenly to enabled.
    $ skip_after_choices = False

    # If the preference Skip: After Choices is enabled, update the variable skip_after_choices to true.
    # Temporary disable the preference Skip: After Choices, to make sure that in the credits the "Skippign >>>" textbox is removed and that you can't skip the credits nor the epilogue.
    # Not needed for any other perferences you set for the skippin, $ renpy.choice_for_skipping() takes care of that.
    if preferences.skip_after_choices:
        $ skip_after_choices = True
        $ preferences.skip_after_choices = False

    # If the player is currently skipping text, this removes that textbox and disabled skipping. It also autosaves!
    # Does not work if Skip: After Choices is enabled! The "if preferences.skip_after_choices:" statement already takes care of that.
    $ renpy.choice_for_skipping()

    ## We hide the quickmenu for the End Credits so they don't appear at the bottom.
    $ quick_menu = False

    ## We hide the textbox as well so it doesn't mess with things.
    window hide

    ## The background of the credits: bg moon for in-game credits
    # a variant of fade is necessary to transition from Act 3 ending CG.
    scene cg_cry with longfade

    ## Play credits theme
    play music 'audio/music/mastered/Lost_No_More_Main_Theme.ogg' fadein 2.0 noloop

    ## Go to the credits screen, in here is the text for the credits.
    call screen credits

    # If the Skip: After Choices was enabled before starting the credits, make sure it's enabled again.
    if skip_after_choices:
        $ preferences.skip_after_choices = True

    # Go to the epilogue.
    jump epilogue

# This label is used to go to the credits from the main menu. Doesn't need a whole lot of fancy stuff, so I removed that.
# NOTE: We do not define a music theme here so it can use the same as main menu theme,
# because the main menu theme will not be played again when we leave this credits screen.
label credits_from_main_menu:

    ## The background of the credits: bg fluffies for main menu credits
    scene bg fluffies

    ## Go to the credits screen.
    call screen credits

    # NOTE: Unreachable code from this point
