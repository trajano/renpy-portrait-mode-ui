init offset = -1

## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    style_prefix "quick"
    frame:
        xpadding int(50 * pmui.scale)
        hbox:
            xfill True
            yoffset int((100.0-72)/2 * pmui.scale)
            hbox:
                spacing int(100 * pmui.scale)
                imagebutton auto "button back %s" action Rollback()
                imagebutton auto "button auto_forward %s" action Skip() alternate Skip(fast=True, confirm=True)

            hbox:
                xalign 1.0
                spacing int(100 * pmui.scale)
                imagebutton auto "button history %s" action ShowMenu('history')
                imagebutton auto "button show_menu %s" action ShowMenu()

## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_frame:
    background Frame("portrait-mode-ui/ui/bg-quick-menu.png", 0, 0, 0, int(28 * pmui.scale))
    xfill True
    ysize int(128 * pmui.scale)
    yalign 0.0

style quick_hbox:
    background "color #ff0000"
    spacing 0
