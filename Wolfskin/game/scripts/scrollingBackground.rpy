# Test file for testing scrolling background
# Can be removed once it´s succesfully implemented.

label scrolling_bg_test:

    # The static bg
    scene bg valley sunset with fade

    show ilona_sunset blood:
        zoom 0.5 yoffset 0 xcenter 700
    show edwin_sunset blood at center behind ilona_sunset:
        zoom 0.5 xzoom -1
    with dissolve

    narrator "At the valley..."

    # The scrolling bg
    scene valley_scroll
    show ilona_sunset blood:
        zoom 0.5 yoffset 0 xcenter 700
    show edwin_sunset blood at center behind ilona_sunset:
        zoom 0.5 xzoom -1
    with fade

    narrator "Ilona and Edwin are walking rapidly..."

    # The static bg
    scene bg valley sunset
    show ilona_sunset blood:
        zoom 0.5 yoffset 0 xcenter 700
    show edwin_sunset blood at center behind ilona_sunset:
        zoom 0.5 xzoom -1
    with fade

    narrator "and stopped at their destination."

# keep the xalign values for the bg to scroll in the correct direction
# Increase linear value for slower scrolling
image valley_scroll:
    "images/bg/bg valley sunset long debug.png"
    xalign 0.0
    linear 10.0 xalign 1.0
    repeat
