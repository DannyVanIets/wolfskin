## You can find the label in "scripts/credits-script.rpy".

## In here is the screen, to show the text and disable key bindings, so no one can open the quick menu while it's happening. Also adds a skip button.
## After the screne we have styling for the credits text.

## End Credits Scroll ############################################################
## ATL for scrolling screen object. In this case, credits roll.
## Speed is the time for object to move up from initial ypos to finish ypos.
## Code Source: https://lemmasoft.renai.us/forums/viewtopic.php?t=42667

transform credits_scroll(speed):
    ypos 1100  # This is the space between the top of the screen and the text 'credits'.
    linear speed ypos -24600 # This is how far down the screen will scroll, with the speed for how fast it will scroll.

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
            label _("Credits") xalign 0.5

            null height 400

            text _("Voice Cast") size 100
            null height 100
            text _("Lasli Tran as Ilona")

            null height 100
            text _("Conner Howard as Edwin")

            null height 100
            text _("Elissa Park as Anari")

            null height 100
            text _("Shakyra Dunn as Eisleigh")

            null height 100
            text _("Daniel Walton as Kellac")

            null height 100
            text _("Trent Martin as Uldin")

            null height 100
            text _("Lisa-Marie Lee as Salome")

            null height 100
            text _("and")

            null height 100
            text _("Bindy Coda as Fleur")

            null height 400

            text _("Creative Director") size 100
            null height 80
            text _("Tamafry")

            null height 400

            text _("Lead Writer") size 100
            null height 80
            text _("Abhishek")

            null height 400

            text _("Editor and Proofreader") size 100
            null height 80
            text _("Billie (thelof9)")

            null height 400

            text _("Casting and Voice Director") size 100
            null height 80
            text _("Maxi Molina (SandraMJ)")

            null height 400

            text _("Script Editors") size 100
            null height 80
            text _("Jordan K. Brown")
            null height 80
            text _("Maxi Molina (SandraMJ)")

            null height 400

            text _("Voice Audio Editing Team") size 100
            null height 80
            text _("Jordan K. Brown")
            null height 80
            text _("Luis \"RunnerGuitar\" Guerrero")
            null height 80
            text _("J-Der")
            null height 80
            text _("ObsidianWasp")
            null height 80
            text _("Andrew Rella")
            null height 80
            text _("Amemarteau")

            null height 400

            text _("Voice Mastering") size 100
            null height 80
            text _("Luke Ford")

            null height 400

            text _("Quality Assurance Tester") size 100
            null height 80
            text _("Gaming Variety Potato")

            null height 400

            text _("Programmers") size 100
            null height 80
            text _("Gaming Variety Potato")
            null height 80
            text _("Vygan")

            null height 400

            text _("Lead Artist") size 100
            null height 80
            text _("Tamafry")

            null height 400

            text _("CG Assistance") size 100
            null height 80
            text _("Luis \"RunnerGuitar\" Guerrero")

            null height 400

            text _("Assistant BG Artist & Colours") size 100
            null height 80
            text _("Jason \"Helrouis\" Cheng")

            null height 400

            text _("GUI & Graphic Designer") size 100
            null height 80
            text _("Kaya")

            null height 400

            text _("Logo Designer") size 100
            null height 80
            text _("Puchi")

            null height 400

            text _("Music Composers") size 100
            null height 80
            text _("Luis \"RunnerGuitar\" Guerrero")
            null height 80
            text _("Octavio Savinelli")
            null height 80
            text _("Luke Ford")

            null height 400

            text _("Music Arranger and Mixer") size 100
            null height 80
            text _("Luis \"RunnerGuitar\" Guerrero")

            null height 400

            text _("Sound Designer") size 100
            null height 80
            text _("Luke Ford")

            null height 400

            text _("French Translator") size 100
            null height 80
            text _("Jean-Yves Chasle")

            null height 400

            text _("Wikicommons: Background Resources") size 100
            null height 80
            text _("Ľuboš Repta")
            null height 80
            text _("Daniel Thornton")
            null height 80
            text _("Zidikai1")
            null height 80
            text _("Leonid Evdokimov")
            null height 80
            text _("Александр Байдуков")
            null height 80
            text _("Horia Varlan")
            null height 80
            text _("Gary Todd")
            null height 80
            text _("Monyesz")

            null height 400

            text _("Freepik: Graphic Resources") size 100
            null height 80
            text _("Racool Studio")
            null height 80
            text _("Jannoon028")
            null height 80
            text _("GaryKillian")

            null height 200

            text _("FreeSound: Sound Resources") size 100
            null height 80
            text _("PatrickLieberkind")
            null height 80
            text _("InspectorK")
            null height 80
            text _("Tim Kahn")
            null height 80
            text _("nhaudio")
            null height 80
            text _("Volivieri")
            null height 80
            text _("Gynation")
            null height 80
            text _("Reinsamba")

            null height 200

            text _("Additional Sounds from") size 100
            null height 80
            text _("Zapsplat")
            null height 80
            text _("Pro Sound Effects")

            null height 400

            text _("Special Thanks") size 100
            null height 80
            text _("Amemarteau")
            null height 80
            text _("Adam, Sam, Selene and Chase")
            null height 80
            text _("Jessica and Jacob Elalouf of Exigent")
            null height 80
            text _("Remort Studios \nfor hosting\n Spooktober VN Game Jam 2021")
            null height 250

            null height 80
            text _("Thank you for playing this game. \n\nWe hope you enjoyed it.")

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
