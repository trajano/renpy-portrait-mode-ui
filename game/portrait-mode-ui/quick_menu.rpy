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
            hbox yalign 0.5:
                xfill True
                hbox:
                    spacing int(100 * pmui.scale * pmui.big_button_scale)
                    imagebutton auto "button big back %s" action Rollback()
                    imagebutton auto "button big auto_forward %s" action Skip() alternate Skip(fast=True, confirm=True)
                hbox:
                    xalign 1.0
                    spacing int(100 * pmui.scale * pmui.big_button_scale)
                    imagebutton auto "button big history %s" action ShowMenu("history_test")
                    imagebutton auto "button big show_menu %s" action ShowMenu()

## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default pmui.show_quick_menu = True

style quick_button is default
style quick_button_text is button_text

image ui bg quick_menu = Composite(
    (60, 75),
    (0, 0), Solid(pmui.quick_menu_box_color, ysize=60),
    (0, 61), im.Crop("portrait-mode-ui/ui/rect-dropshadow.png", 45, 135, 60, 15)
)


style quick_frame:
    background Frame("ui bg quick_menu", 0, 0, 0, 15)
    xfill True
    xpadding pmui.scale_p(50 * pmui.big_button_scale)
    bottom_padding pmui.scale_p(pmui.quick_menu_bar_dropshadow_size  / pmui.scale)
    ysize pmui.scale_p(pmui.quick_menu_bar_size * pmui.big_button_scale) + int(pmui.quick_menu_bar_dropshadow_size / pmui.scale)
    yalign 0.0

style quick_hbox:
    background "color #ff0000"
    spacing 0
