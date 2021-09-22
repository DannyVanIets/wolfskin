# File for the intro of an act screen. It will show the act number and the title of that act.

# actNumber is used to check which act this is.
screen intro(actNumber):

    # After 5 seconds, it will return to the act label.
    timer 5.0 action Return()

    # Make sure it uses the correct styling for the labels and text inside the vbox.
    # You can find those at the bottom of this file.
    style_prefix "intro"

    # Used to make all the labels and text use the correct positions and that there's no background.
    frame at:
        ypos 350
        background None
        xalign 0.5

        vbox:
            if actNumber == 1:
                label "Act I" xalign 0.5

                null height 50

                text "All Hallows' Eve - Sanctuary"

            elif actNumber == 2:
                label "Act II" xalign 0.5

                null height 50

                text "All Hallows' Day - The Curse"

            elif actNumber == 3:
                label "Act III" xalign 0.5

                null height 50

                text "All Hallow's Day - Warmth Combined"

            # In case we want to make it clear that it is the epilogue.
            else:
                label "Epilogue" xalign 0.5

style intro_label_text:
    xalign 0.5
    size 140
    text_align 0.5
    font "BluuNext-Bolditalic.otf"

style intro_text:
    xalign 0.5
    size 80
    text_align 0.5
    color "#ffffff"
    font "BluuNext-Bolditalic.otf"
