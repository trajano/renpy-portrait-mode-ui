init offset = -1

## Quick Game Menu screen ######################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.
screen portrait_game_navigation(title):
    style_prefix "gamemenu"
    vbox:
        frame:
            xpadding pmui.scale_p(50)
            bottom_padding pmui.scale_p(pmui.quick_menu_bar_dropshadow_size  / pmui.scale)
            ysize pmui.scale_p(pmui.quick_menu_bar_size) + int(pmui.quick_menu_bar_dropshadow_size / pmui.scale)
            hbox yalign 0.5:
                xfill True
                hbox:
                    imagebutton auto "button big exit_to_game %s" action Return()

                hbox:
                    xalign 1.0
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

screen portrait_game_menu(title=None, scroll=None, yinitial=0.0, cols = 3):
    tag menu
    add Solid("#000000cc", xysize=(config.screen_width, config.screen_height))
    side "c t":
        if scroll == "viewport":
            viewport:
                mousewheel True
                draggable True
                pagekeys True
                scrollbars "vertical"
                side_yfill True
                child_size (pmui.scale_p(1080-pmui.scrollbar_size), None)
                yinitial yinitial
                transclude
        elif scroll == "vpgrid":
            frame:
                left_margin pmui.scale_p(50)
                vpgrid:
                    cols cols
                    spacing pmui.scale_p(50)
                    mousewheel True
                    draggable True
                    pagekeys True
                    scrollbars "vertical"
                    side_yfill True
                    xfill True
                    yinitial yinitial
                    transclude
        else:
            transclude
        use portrait_game_navigation(title)

style gamemenu_frame:

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
