## You can find the label in "scripts/credits-script.rpy".

## In here is the screen, to show the text and disable key bindings, so no one can open the quick menu while it's happening. Also adds a skip button.
## After the screne we have styling for the credits text.

## End Credits Scroll ############################################################
## ATL for scrolling screen object. In this case, credits roll.
## Speed is the time for object to move up from initial ypos to finish ypos.
## Code Source: https://lemmasoft.renai.us/forums/viewtopic.php?t=42667

transform credits_scroll(speed):
    ypos 1100  # This is the space between the top of the screen and the text 'credits'.
    linear speed ypos -23500 # This is how far down the screen will scroll, with the speed for how fast it will scroll.

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
    timer 200.0 action Return()

    ## Adjust this number to control the speed at which the credits scroll.
    ## Needs to be adjusted if you make the credits longer or shorter.
    frame at credits_scroll(195.0):
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
            text "Conner Howard as Edwin"

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

            text "Lead Writer" size 100
            null height 80
            text "Abhishek"

            null height 400

            text "Editor and Proofreader" size 100
            null height 80
            text "Billie"

            null height 400

            text "Casting and Voice Director" size 100
            null height 80
            text "Maxi Molina (SandraMJ)"

            null height 400

            text "Script Editors" size 100
            null height 80
            text "Jordan K. Brown"
            null height 80
            text "Maxi Molina (SandraMJ)"

            null height 400

            text "Voice Audio Editing Team" size 100
            null height 80
            text "Jordan K. Brown"
            null height 80
            text "Luis \"RunnerGuitar\" Guerrero"
            null height 80
            text "J-Der"
            null height 80
            text "ObsidianWasp"
            null height 80
            text "ThatOneNerd"
            null height 80
            text "Amemarteau"

            null height 400

            text "Voice Mastering" size 100
            null height 80
            text "Luke Ford"

            null height 400

            text "Quality Assurance Tester" size 100
            null height 80
            text "Gaming Variety Potato"

            null height 400

            text "Programmers" size 100
            null height 80
            text "Gaming Variety Potato"
            null height 80
            text "Vygan"

            null height 400

            text "Lead Artist" size 100
            null height 80
            text "Tamafry"

            null height 400

            text "CG Assistance" size 100
            null height 80
            text "Luis \"RunnerGuitar\" Guerrero"

            null height 400

            text "Assistant BG Artist & Colours" size 100
            null height 80
            text "Jason"

            null height 400

            text "GUI & Graphic Designer" size 100
            null height 80
            text "Kaya"

            null height 400

            text "Logo Designer" size 100
            null height 80
            text "Puchi"

            null height 400

            text "Music Composers" size 100
            null height 80
            text "Luis \"RunnerGuitar\" Guerrero"
            null height 80
            text "Octavio Savinelli"
            null height 80
            text "Luke Ford"

            null height 400

            text "Music Arranger and Mixer" size 100
            null height 80
            text "Luis \"RunnerGuitar\" Guerrero"

            null height 400

            text "Sound Designer" size 100
            null height 80
            text "Luke Ford"

            null height 400

            text "Wikicommons: Background Resources" size 100
            null height 80
            text "Ľuboš Repta"
            null height 80
            text "Daniel Thornton"
            null height 80
            text "Zidikai1"
            null height 80
            text "Leonid Evdokimov"
            null height 80
            text "Александр Байдуков"
            null height 80
            text "Horia Varlan"
            null height 80
            text "Gary Todd"
            null height 80
            text "Monyesz"

            null height 400

            text "Freepik: Graphic Resources" size 100
            null height 80
            text "Racool Studio"
            null height 80
            text "Jannoon028"
            null height 80
            text "GaryKillian"

            null height 200

            text "FreeSound: Sound Resources" size 100
            null height 80
            text "PatrickLieberkind"
            null height 80
            text "InspectorK"
            null height 80
            text "Tim Kahn"
            null height 80
            text "nhaudio"
            null height 80
            text "Volivieri"
            null height 80
            text "Gynation"
            null height 80
            text "Reinsamba"

            null height 200

            text "Additional Sounds from" size 100
            null height 80
            text "Zapsplat"
            null height 80
            text "Pro Sound Effects"

            null height 400

            text "Special Thanks" size 100
            null height 80
            text "Amemarteau"
            null height 80
            text "Adam, Sam, Selene and Chase"
            null height 80
            text "Jessica and Jacob Elaouf of Exigent"
            null height 80
            text "Remort Studios \nfor hosting\n Spooktober VN Game Jam 2021"
            null height 250

            null height 80
            text "Thank you for playing this game. \n\nWe hope you enjoyed it."

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
