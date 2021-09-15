## You can find the label in "scripts/credits-script.rpy".

## In here is the screen, to show the text and disable key bindings, so no one can open the quick menu while it's happening. Also adds a skip button.
## After the screne we have styling for the credits text.

## End Credits Scroll ############################################################
## ATL for scrolling screen object. In this case, credits roll.
## Speed is the time for object to move up from initial ypos to finish ypos.
## Code Source: https://lemmasoft.renai.us/forums/viewtopic.php?t=42667
transform credits_scroll(speed):
    ypos 1100  # This is the space between the top of the screen and the text 'credits'.
    linear speed ypos -5800  # This is how far down the screen will scroll, with the speed for how fast it will scroll.

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
    timer 1000.0 action Return()

    ## Adjust this number to control the speed at which the credits scroll.
    ## Needs to be adjusted if you make the credits longer or shorter.
    frame at credits_scroll(30.0):
        background None
        xalign 0.5

        # In here is all the text for the credits.
        vbox:
            # This "Credits" label is the hbox.
            label "Credits" xalign 0.5

            null height 400

            text "Voice Cast" size 100
            null height 100
            text "Lasli Tran as Ilona"

            null height 100
            text "Connor Howard as Edwin"

            null height 100
            text "Elissa Park as Anari"

            null height 100
            text "Shakyra Dunn as Eisleigh"

            null height 100
            text "Daniel Walton as Kellac"

            null height 100
            text "Trent Martin as Uldin"

            null height 100
            text "Lisa-Marie Lee as Salome"

            null height 100
            text "and"

            null height 100
            text "Bindy Coda as Fleur"

            null height 400

            text "Creative Director" size 100
            null height 80
            text "Tamafry"

            null height 400

            text "Lead writer" size 100
            null height 80
            text "Abhishek"

            null height 400

            text "Story Consultant, Quality Assurance Tester" size 100
            null height 80
            text "Gaming Variety Potato"

            null height 400

            text "Editor & Proofreader" size 100
            null height 80
            text "Billie"

            null height 400

            text "Casting and Voice Direction, Script Editing" size 100
            null height 80
            text "Maxi Molina (SandraMJ)"

            null height 400

            text "Music & sound designers" size 100
            null height 80
            text "Luis \"RunnerGuitar\" Guerrero"
            null height 80

            hbox:
                xalign 0.5
                spacing 280

                vbox:
                    text "Octavio Savinelli"

                vbox:
                    text "Luke Ford"

            null height 400

            text "Audio Engineer" size 100
            null height 80
            text "Luke Ford"

            text "Lead Artist & Sprites" size 100
            null height 80
            text "Tamafry"

            text "Backgrounds & Cleanup" size 100
            null height 80
            text "Jason"

            null height 400

            text "Backgrounds & Cleanup" size 100
            null height 80
            text "Jason"

            null height 400

            text "GUI design" size 100
            null height 80
            text "Kaya"

            null height 400

            text "Logo design by" size 100
            null height 80
            text "Puchi"

            null height 400

            text "Programming" size 100
            null height 80
            text "Vygan"

            null height 400

            text "Special Thanks to" size 100
            null height 80
            text "Remort Studios for hosting this Visual Novel Jam."

            null height 400

            text "Made with Ren'Py [renpy.version_only]." size 100

            null height 400

            text "Made for the Spooktober 3rd Annual Visual Novel Jam by DevTalk." size 100

            null height 600

            text "And thank you, the player, for playing this game!" size 100

# The styling for all the credit text.
style credits_hbox:
    spacing 40
    ysize 30

style credits_label_text:
    xalign 0.5
    size 140
    text_align 0.5

style credits_text:
    xalign 0.5
    size 80
    justify True
    text_align 0.5
    color "#ffffff"
