# Test file for testing ActionEditor.
# Can be removed once it´s succesfully implemented.

label action_editor_test:

    scene bg black

    show hd edwolf unchained  onlayer middle:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            yzoom 1
            linear 3.5 yzoom 1.0
        parallel:
            xpos 1.36
            linear 0.5 xpos 0.85
            linear 0.5 xpos 0.63
            linear 1.0 xpos 0.67
            linear 1.0 xpos 0.49
            linear 0.5 xpos 0.5
        parallel:
            ypos 2.82
            linear 1.0 ypos 2.33
            linear 0.5 ypos 1.75
            linear 0.5 ypos 1.05
            linear 1.5 ypos 1.06
        parallel:
            zoom 1
            linear 1.5 zoom 0.8
            linear 1.0 zoom 0.5
            linear 0.5 zoom 0.4
            linear 0.5 zoom 0.38

    $ renpy.pause(5)
    narrator "debug"
