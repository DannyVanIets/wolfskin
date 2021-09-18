# Test file for making the background blurry and shaky.
# Can be removed once it´s succesfully implemented.

label blurry_shake:
    # If you only want to do the blurriness, uncomment the line under this.
    # show background_with_blurry with dissolve

    # Blurriness and shaking combined.
    # The shaking is more wobbling your head around, could change that if neccesary but would be a lot of work.
    scene background_with_blurry with vpunch:
        # Makes you able to use subpixels, handy for positioning.
        subpixel True
        # Keep this as it is, really annoying to change. It tells where to position the image and how far you want to zoom in.
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.02
        # Tells where you will circle around in the image and how far.
        alignaround(.5, .5)
        # Linear is how fast you want the circling to be, lower it to make it faster. yalign is the same as like xpos, don't bother changing that. Circles is the amount of circles it will do before repeating.
        linear 10.0 yalign 1.0 clockwise circles 1
        repeat

    narrator "I am feeling shaky... My vision... Is clearing..."

    narrator "I need new glasses..."

# This image makes the screen go from blurry to clear to blurry endlessly.
# The pauses here are how long it will stay that partiular background, change that if needed.
image background_with_blurry:
    "bg forest night blurry" with dissolve
    pause 1
    "bg forest night" with dissolve
    pause 1
    repeat
