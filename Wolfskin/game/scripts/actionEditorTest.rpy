# Test file for testing ActionEditor.
# Can be removed once it´s succesfully implemented.

label action_editor_test:

    scene bg black

    show hd edwolf unchained onlayer middle:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            xpos 1.36
            easein 1.5 xpos 0.85 # face

            linear 1.5 xpos 0.63 # neck upper
            easeout_bounce 0.5 xpos 0.67 # neck lower

            linear 0.25 xpos 0.47 # full body
            linear 0.25 xpos 0.5 # full body
        parallel:
            ypos 2.8
            linear 1.5 ypos 2.5 # face

            easein 1.5 ypos 1.9 # neck upper
            linear 0.5 ypos 1.3 # neck lower

            linear 0.5 ypos 1.06 # full body
        parallel:
            zoom 1
            linear 1.5 zoom 0.9 # face

            linear 1.5 zoom 0.8 # neck upper
            linear 0.5 zoom 0.6 # neck lower

            linear 0.5 zoom 0.38 # full body

    $ renpy.pause(4)
    narrator "debug"
