init offset = -1

## Quick Game Menu screen ######################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.
screen side_test():
    side "c tl br t":
        text "Center" size 40
        text "Top-Left" size 40
        text "Bottom-Right" size 40
        text "Top" size 40

screen portrait_game_menu(title=None, scroll=None, yinitial=0.0):
    tag menu
    side "c t":
        viewport:
            mousewheel True
            draggable True
            pagekeys True
            scrollbars "vertical"
            side_yfill True
            xfill True
            yinitial yinitial
            transclude
        frame style "gamemenu_frame":
            has vbox
            style_prefix "gamemenu"
            hbox:
                ysize pmui.quick_menu_bar_size
                xfill True

                # yoffset int((pmui.quick_menu_bar_size - pmui.quick_menu_icon_size)/2 * pmui.scale)
                # add Solid("#cccccc", xysize=(50, 50)) yalign 0.5
                # add Solid("#cccccc", xysize=(100, pmui.quick_menu_bar_size)) yalign 0.5
                hbox yalign 0.5 xoffset int(50 * pmui.scale):
                    spacing int(100 * pmui.scale)
                    imagebutton auto "button big exit_to_game %s" action Return()

                hbox yalign 0.5 xalign 1.0 xoffset int(-50 * pmui.scale):
                    spacing int(100 * pmui.scale)
                    imagebutton auto "button big show_menu %s" action Return()

            null height int((pmui.game_menu_quick_menu_gap_size) * pmui.scale)

            grid 5 1 xalign 0.5 xfill True:

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
                vbox xalign 0.5:
                    imagebutton auto "button load %s" xalign 0.5 action ShowMenu("load")
                    textbutton _("Load") action ShowMenu("load")
                vbox xalign 0.5:
                    imagebutton auto "button settings %s" xalign 0.5 action ShowMenu("preferences")
                    textbutton _("Settings") action ShowMenu("preferences")
            null height int((pmui.game_menu_quick_menu_gap_size) * pmui.scale)

style gamemenu_frame:
    background Solid("#000000cc", xysize=(config.screen_width, config.screen_height))
    xfill True
    yfill True

# style gamemenu_viewport:
#     yoffset int((pmui.game_menu_quick_menu_gap_size) * pmui.scale)
#     ysize int((1920 - pmui.quick_menu_bar_size - pmui.game_menu_quick_menu_gap_size - pmui.game_menu_button_bar_icon_size - pmui.game_menu_button_bar_text_size) * pmui.scale)
#     # yoffset ((pmui.quick_menu_ba1r_size + pmui.game_menu_quick_menu_gap_size + pmui.game_menu_button_bar_icon_size + pmui.game_menu_button_bar_text_size + 28) * pmui.scale)

# style gamemenux_vbox:
#     xsize int((1080 - 50 - 50) * pmui.scale)
# # style gamemenu_frame is quick_frame:
# #     yfill True
#     # ysize int((pmui.quick_menu_bar_size + pmui.game_menu_quick_menu_gap_size + pmui.game_menu_button_bar_icon_size + pmui.game_menu_button_bar_text_size + 28) * pmui.scale)

style gamemenu_button_text:
    idle_color pmui.idle_color
    selected_color pmui.selected_color
    selected_idle_color pmui.selected_color
    insensitive_color pmui.insensitive_color
    hover_color pmui.hover_color
    xalign 0.5
    size pmui.game_menu_button_bar_text_size * pmui.scale
    selected_bold True
    selected_idle_bold True
