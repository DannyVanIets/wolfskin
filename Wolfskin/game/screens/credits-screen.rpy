## You can find the label in "scripts/credits-script.rpy".

## In here is the screen, to show the text and disable key bindings, so no one can open the quick menu while it's happening. Also adds a skip button.
## After the screne we have styling for the credits text.

## End Credits Scroll ############################################################
## ATL for scrolling screen object. In this case, credits roll.
## Speed is the time for object to move up from initial ypos to finish ypos.
## Code Source: https://lemmasoft.renai.us/forums/viewtopic.php?t=42667
transform credits_scroll(speed):
    ypos 1100  # This is the space between the top of the screen and the text 'credits'.
    linear speed ypos -5500  # This is how far down the screen will scroll, with the speed for how fast it will scroll.

screen credits():
    # Make a menu of this, so you do not have main menu in the background while the credits are rolling.
    tag menu

    ## Ensure that the game_menu screens don't appear and interrupt the credits.
    key "K_ESCAPE" action NullAction()
    key "K_MENU" action NullAction()
    key "mouseup_3" action NullAction()

    style_prefix "credits"

    ## Make the player always able to skip the credits, going straight back to the main menu.
    ## The reason 'action Return()' is used, is because of a weird bug if you want to go from the main menu to the credits.
    ## If you then want to skip, it will instead start a new game for you. This fixes it!
    textbutton _("Skip") action Return() xalign 1.0 yalign 1.0

    ## Adjust this number to control when the Credits screen is hidden and the game
    ## returns to its normal flow.
    ## Ideally, there is some wait time after the the credits reaches the end.
    ## If you make the credits longer or shorter, you need to adjust this timer!
    timer 33.0 action Return()

    ## Adjust this number to control the speed at which the credits scroll.
    ## Needs to be adjusted if you make the credits longer or shorter.
    frame at credits_scroll(30.0):
        background None
        xalign 0.5

        # In here is all the text for the credits.
        vbox:
            # This "Credits" label is the hbox.
            label "Credits" xalign 0.5

            null height 300

            text "Director, lead arist & writer" size 100
            null height 50
            text "Tamafry"

            null height 300

            text "Co-writers" size 100
            null height 50
            text "Ahkmin"

            null height 50
            text "PotatoLays"

            null height 300

            text "Editor" size 100
            null height 50
            text "Billie"

            null height 300

            text "Music & sound designers" size 100
            null height 50

            hbox:
                xalign 0.5
                spacing 250

                vbox:
                    text "Luis \"RunnerGuitar\" Guerrero"

                vbox:
                    text "Patrick Intallura"

            null height 200

            text "Programming" size 100
            null height 50
            text "Vygan"

            null height 300

            text "Voice acting" size 100
            null height 50
            text "??? as Ilona"

            null height 50
            text "??? as Edwin"

            null height 300

            text "Special Thanks" size 100
            null height 50
            text "Remort Studios for hosting this Visual Novel Jam."

            null height 300

            text "Made with Ren'Py [renpy.version_only]." size 100

            null height 300

            text "Made for the Spooktober 3rd Annual Visual Novel Jam by DevTalk." size 100

            null height 600

            text "And thank you, the player, for playing this game!" size 100

# The styling for all the credit text.
style credits_hbox:
    spacing 40
    ysize 30

style credits_label_text:
    xalign 0.5
    size 200
    text_align 0.5

style credits_text:
    xalign 0.5
    size 80
    justify True
    text_align 0.5
    color "#ffffff"
