init offset = -1

## Quick Game Menu screen ######################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.
screen portrait_game_menu(title = None):

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
                vbox:
                    xalign 0.5
                    imagebutton auto "button show_main_menu %s" xalign 0.5 action MainMenu()
                    textbutton "Main" action MainMenu()
                vbox:
                    xalign 0.5
                    imagebutton auto "button history %s"  xalign 0.5 action ShowMenu("history")
                    textbutton _("History") action ShowMenu("history")
                vbox:
                    xalign 0.5
                    imagebutton auto "button save %s" xalign 0.5 action ShowMenu("save")
                    textbutton _("Save") action ShowMenu("save")
                vbox:
                    xalign 0.5
                    imagebutton auto "button load %s" xalign 0.5 action ShowMenu("load")
                    textbutton _("Load") action ShowMenu("load")
                vbox:
                    xalign 0.5
                    imagebutton auto "button settings %s" xalign 0.5 action ShowMenu("preferences")
                    textbutton "Settings" action ShowMenu("preferences")

style gamemenu_frame is quick_frame:
    ysize int((128 + 100 + 12 + 28) * pmui.scale)

style gamemenu_button_text:
    idle_color pmui.idle_color
    selected_color pmui.selected_color
    selected_idle_color pmui.selected_color
    insensitive_color pmui.insensitive_color
    hover_color pmui.hover_color
    kerning -1
    xalign 0.5
    size 30 * pmui.scale
    selected_bold True
    hover_bold True
