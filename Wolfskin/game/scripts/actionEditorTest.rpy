# Test file for testing ActionEditor.
# Can be removed once it´s succesfully implemented.

label action_editor_test:

    # Show CG wolf
    #scene edwolf unleashed with vpunch
    #$ renpy.pause(1.5, hard=True)

    $all_moves(camera_check_points={'y': [(-122, 0, 'linear'), (-3533, 3.19, 'linear')], 'x': [(5606, 0, 'linear'), (187, 3.19, 'linear')]})
    show hd edwolf unchained onlayer middle:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            zoom 0.61
            linear 3.19 zoom 0.46

#    scene hd edwolf unchained:
#        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
#        parallel:
#            xpos 1.36
#            easein 1.5 xpos 0.85 # face
#            linear 1.5 xpos 0.63 # neck upper
#            easeout_bounce 0.5 xpos 0.67 # neck lower
#            linear 0.5 xpos 0.5 # full body
#        parallel:
#            ypos 2.8
#            linear 1.5 ypos 2.5 # face
#            easein 1.5 ypos 1.9 # neck upper
#            linear 0.5 ypos 1.3 # neck lower
#            linear 0.5 ypos 1.06 # full body
#        parallel:
#            zoom 1
#            linear 1.5 zoom 0.9 # face
#            linear 1.5 zoom 0.8 # neck upper
#            linear 0.5 zoom 0.6 # neck lower
#            linear 0.5 zoom 0.38 # full body
#    $ renpy.pause(4, hard=True)

    "The chains snap off him as he transforms into a massive wolf-man."

    "He rushes at the guards with a growl. He throws them off, prying Ilona away from them."

    hide hd edwolf unchained onlayer middle
    show bg black
    scene bg town plaza sunset
    show anari_sunset fury glance grin kill at center:
        zoom 0.7 yoffset 220
    with fade

    "Anari strings her bow, and takes an arrow from her quiver. She trains it on the monster."

    an "I won't let you escape."

    hide anari_sunset with dissolve

    play sound 'audio/sfx/arrow whistle.mp3'

    "When she releases the bowstring, her arrow whistles as it flies. Edwin transforms from half-man, half-wolf, into an enormous grey wolf, and the shot grazes him."

    ## TOWN WALL
    scene bg black with fade

    "Ilona and Edwin make their escape. Anari scowls, and then goes to climb a tower to gain a higher vantage point."

    il "The gates will be already closed by now. There's a part of the wall that was hastily patched up. You should be able to climb through there."

    "Edwin takes a running leap, and latches his claws into the stone wall. He shifts back into his half-wolf form and starts climbing."

# SCENE 44
    play sound 'audio/sfx/Gravel Floor Fall 1.mp3' volume 0.3

    with vpunch

    "The looming stone wall in front of them is a substantial hurdle to overcome. The town guards mobilise, firing arrows that torrent Edwin and Ilona. Edwin does his best to throw off their aim."

    hide hd edwolf protecc
    $ renpy.pause(2, hard=True)

    show bg belorov sunset
    show anari_sunset fury scary neutral kill at center:
        zoom 0.85 yoffset 420
    with fade

    "There is one he cannot escape from. Anari's skill with a bow is frightening, her gaze ever calm and steady."

    scene bg wound1
    play sound 'audio/sfx/arrow whistle.mp3'

    $ renpy.pause(0.6, hard=True)
    stop sound

    scene bg wound2
    play sound 'audio/sfx/zap arrow.mp3'

    "Two arrows finally meet its target. They pierce his side, fired in rapid succession."

    scene bg wound3
    play sound 'audio/sfx/arrow whistle.mp3'

    $ renpy.pause(0.4, hard=True)
    stop sound

    scene bg wound4
    play sound 'audio/sfx/zap arrow.mp3'

    $ renpy.pause(0.2, hard=True)
    stop sound

    scene bg wound5
    play sound 'audio/sfx/zap arrow.mp3'

    extend " Then three more pierce his ribs. This isn’t a problem for the werewolf, as he brushes aside the pain. He’s taken greater beatings than this."

    scene edwolf claws with longfade:
        xzoom -1

    "However, he’s not invincible; a few more well placed shots and he’s down, along with Ilona."

    show ilona_sunset closed aaaa talk at center:
        zoom 0.5
    with dissolve

    il "Stay with me Edwin! Don’t lose sight of our escape. I’ll do my best to heal your wounds with- Ah!"

    play sound 'audio/sfx/arrow whistle.mp3'

    $ renpy.pause(0.5, hard=True)

    play sound 'audio/sfx/zap bone break.mp3' volume 0.7

    scene bg blood
    with hpunch

    "An arrow pierces the hand with which Ilona was trying to use to heal. Her hand twists and contorts, reflexingly convulsing due to the writhing pain."

    ed "Ilona! Ho-hold on, we’re almost there!"



    "Time seems to move too slowly. How much more pain can they accept? Edwin grimaces past the pain of his sustained wounds."

    "There’s no question about it - Ilona knows Anari could never miss her mark, not with a target so large. She’s missing their vitals on purpose."

    "A good look at Anari leaves nothing more than questions. Does she want to let them leave? Or capture and burn them at the stake alive?"
    $ renpy.pause(0.3)
    play sound 'audio/sfx/arrow whistle.mp3'

    $ renpy.pause(0.5, hard=True)

    play sound 'audio/sfx/zap bone break.mp3' volume 0.7

    scene bg gore with hpunch
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
