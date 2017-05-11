# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define bscreen = Character(None,
                          what_size=50, #Font size
                          what_xalign=0.5, #Centers text within the window
                          window_xalign=0.5, #Centers the window horizontally
                          window_yalign=0.5, #Centers the window vertically
                          what_text_align=0.5, #Centers text within the window, just in case
                          window_background=None,#Removes the window, so only the text shows
                          #what_outlines=[(3, "#000000", 2, 2), (3, "#282", 0, 0)],
                          #Gives an outline
                          what_slow_cps=20 #Speed at which the text appears (slow)
                          )


# The game starts here.

label start:


    jump prologue

    return


label prologue:

    show black with fade

    bscreen ""

    return
