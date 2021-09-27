# Test file for testing ActionEditor.
# Can be removed once it´s succesfully implemented.

label action_editor_test:
    # Resets the camera and layers positions
    $ camera_reset()
    # Instantly sets layer distances from the camera
    $ layer_move("background", 2000)
    $ layer_move("middle", 1500)
    $ layer_move("forward", 1000)
    scene bg forest night onlayer background
    # WARNING: The 'scene' command will reset the depth of whatever layer the image
    # is displayed on. Make sure you reset the depth after you call the 'scene' command.
    $ layer_move("background", 2000)
    show A onlayer middle
    show B onlayer forward
    with dissolve

    # "Moves the camera to (1800, 0, 0) in 1 second."
    $ camera_move(1800, 0, 0, 0, 1)
    # "Moves the camera to (0, 0, 1600) in 5 seconds."
    $ camera_move(0, 0, 1600, 0, 5)
    # "Moves the camera to (0, 0, 0) instantaneously."
    $ camera_move(0, 0, 0)
    # "Rotates the camera 180 degrees in 1 second."
    $ camera_move(0, 0, 0, 180, 1)
    # 'Rotates the camera -180 degrees in 1 second and subsequently moves the camera to (-1800, 0, 500) in 1.5 seconds'
    $ camera_moves( ( (0, 0, 0, 0, 1, 'linear'), (-1800, 0, 500, 0, 1.5, 'linear') ) )
    # 'Continually moves the camera between (-1800, 0, 500) and (0, 0, 0), taking 0.5 seconds for the first move and 1 second for the second until the action is interrupted.'
    $ camera_moves( ( (0, 0, 0, 0, .5, 'linear'), (-1800, 0, 500, 0, 1, 'linear') ), loop=True)
