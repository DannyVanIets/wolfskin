label extra:

    # For the gallery and music room screens, use these codes: 
    # http://www.renpy.org/doc/html/rooms.html
    # For the endings list, check out this topic:
    # http://lemmasoft.renai.us/forums/viewtopic.php?f=8&t=4309

    menu:
        
        "Trailer":
            
            $ renpy.movie_cutscene("images/movies/trailer.webm")
            
        "Blooper Reel":
            
            $ renpy.movie_cutscene("images/movies/blooper.webm")

        "Back to Main Menu":
            return