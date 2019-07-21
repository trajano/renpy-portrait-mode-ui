init offset = -1

## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    style_prefix "quick"
    if pmui.show_quick_menu:
        frame:
            xpadding int(50 * pmui.scale)
            hbox:
                xfill True
                yoffset int((pmui.quick_menu_bar_size - pmui.quick_menu_icon_size)/2 * pmui.scale)
                hbox:
                    spacing int(100 * pmui.scale)
                    imagebutton auto "button big back %s" action Rollback()
                    imagebutton auto "button big auto_forward %s" action Skip() alternate Skip(fast=True, confirm=True)

                hbox:
                    xalign 1.0
                    spacing int(100 * pmui.scale)
                    imagebutton auto "button big history %s" action ShowMenu("history_test")
                    imagebutton auto "button big show_menu %s" action ShowMenu()

## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default pmui.show_quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_frame:
    background Frame("portrait-mode-ui/ui/bg-quick-menu.png", 0, 0, 0, int(28 * pmui.scale))
    xfill True
    ysize int(pmui.quick_menu_bar_size + 28 * pmui.scale)
    yalign 0.0

style quick_hbox:
    background "color #ff0000"
    spacing 0
