init offset = -1

## Quick Game Menu screen ######################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.
screen portrait_game_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    style_prefix "gamemenu"
    frame:
        xpadding int(50 * pmui.scale)
        vbox:
            hbox:
                xfill True
                yoffset int((100.0-72)/2 * pmui.scale)
                hbox:
                    spacing int(100 * pmui.scale)
                    imagebutton auto "button exit_to_game %s" action Return()

                hbox:
                    xalign 1.0
                    spacing int(100 * pmui.scale)
                    imagebutton auto "button show_menu %s" action Return()
            grid 5 1:
                xfill True
                yoffset int((100.0-72)/2 * 3 * pmui.scale)
                style_prefix "gamemenuitems"
                vbox:
                    xalign 0.5
                    imagebutton auto "button show_main_menu %s" xalign 0.5 action MainMenu()
                    textbutton "Main" text_size 30 * pmui.scale text_kerning -1 text_color "#ffffff" xalign 0.5 action MainMenu()
                vbox:
                    xalign 0.5
                    imagebutton auto "button history %s"  xalign 0.5 action ShowMenu("history")
                    textbutton "History" text_size 30 * pmui.scale text_kerning -1 text_color "#ffffff" xalign 0.5 action ShowMenu("history")
                vbox:
                    xalign 0.5
                    imagebutton auto "button save %s" xalign 0.5 action ShowMenu("save")
                    textbutton "Save" text_size 30 * pmui.scale text_kerning -1 text_color "#ffffff" xalign 0.5 action ShowMenu("save")
                vbox:
                    xalign 0.5
                    imagebutton auto "button load %s" xalign 0.5 action ShowMenu("load")
                    textbutton "Load" text_size 30 * pmui.scale text_kerning -1 text_color "#ffffff" xalign 0.5 action ShowMenu("load")
                vbox:
                    xalign 0.5
                    imagebutton auto "button settings %s" xalign 0.5 action ShowMenu("preferences")
                    textbutton "Settings" text_size 30 * pmui.scale text_kerning -1 text_color "#ffffff" xalign 0.5 action ShowMenu("preferences")

style gamemenu_frame is quick_frame:
    ysize int((128 + 100 + 12 + 28) * pmui.scale)
