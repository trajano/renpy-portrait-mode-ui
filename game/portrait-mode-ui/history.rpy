init offset = -1

################################################################################
## Main and Game Menu Screens
################################################################################

## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history_test():

    tag menu

    use portrait_game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):
        style_prefix "history"
        frame:
            # xpadding int(50 * pmui.scale)
            xpadding int(50 * pmui.scale)
            # xsize int((1080 - 50 - 50 - gui.scrollbar_size) * pmui.scale)
            xsize int((1080 - gui.scrollbar_size) * pmui.scale)
            has vbox
            # add Solid("#ffffcc", width=1000, height=30)
            # add Tile("bg grid")
            text "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam iaculis quam quis felis bibendum, sed condimentum felis vulputate. Ut non nisi malesuada, euismod eros imperdiet, varius ipsum. Nunc eu ligula et velit suscipit tempor ut sed dolor. Nullam gravida nulla ut enim lacinia, et porta velit pharetra. Vivamus leo lacus, vehicula nec tristique at, fringilla a mauris. Nulla at arcu vel est sodales venenatis. In egestas tempus consequat. Integer nec accumsan ipsum. Integer viverra, ipsum vitae posuere interdum, mauris justo cursus sem, sed ornare leo tellus non ipsum." size 50
            text "Pellentesque auctor tellus enim, vitae facilisis leo imperdiet non. Morbi malesuada nisl ut semper bibendum. Fusce eget erat varius, porta metus vitae, auctor dui. Nulla ullamcorper lectus quis tortor facilisis, eu ultricies massa cursus. Proin in pretium nibh. Sed sodales dictum magna, non viverra quam blandit finibus. Aliquam sit amet placerat odio. Maecenas tortor sem, ultricies vel lectus non, auctor viverra justo. Sed accumsan ullamcorper vehicula. Nam arcu arcu, condimentum at mollis quis, vestibulum vitae odio. Fusce et finibus ante, ac venenatis odio." size 50
            text "Vestibulum non sem blandit, auctor lorem eget, fermentum sem. Nullam lobortis orci ut vestibulum commodo. Nullam pulvinar, nisi eget dictum placerat, orci nisl efficitur lorem, egestas maximus sem tortor at velit. Vivamus efficitur congue erat vitae condimentum. Duis posuere nulla elit, ac commodo dolor molestie ac. Integer non fringilla sem, non efficitur elit. Etiam gravida lacinia felis sed dignissim. Morbi vulputate placerat lorem, vitae tempor dui. Donec velit velit, aliquam vitae maximus et, finibus id ante. Etiam tristique lacus in erat mattis malesuada." size 50
            text "Sed eu leo pellentesque, laoreet dui non, euismod velit. Suspendisse potenti. Sed malesuada eu velit vel mollis. Morbi at imperdiet augue. Fusce venenatis nisl sit amet euismod tempor. Donec auctor metus eros, dictum semper erat ultrices ac. Integer in lorem vitae mi pellentesque maximus non eget ligula." size 50
            text "Vestibulum id dignissim velit. Fusce efficitur vel mi nec efficitur. Nulla condimentum nisi nec tortor gravida, vitae sodales lacus suscipit. Sed tempor neque nec hendrerit venenatis. Proin non imperdiet arcu. Cras vitae tortor nec ligula vehicula semper. Pellentesque mauris magna, faucibus sed tristique vitae, facilisis eget dui." size 50


screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use portrait_game_menu(_("History"), scroll="viewport", yinitial=1.0):

        style_prefix "history"

        frame:
            xpadding int(50 * pmui.scale)
            xsize int((1080 - gui.scrollbar_size) * pmui.scale)
            has vbox
            for h in _history_list:
                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]
                else:
                    label "Me":
                        style "history_name"
                        text_color "#2222cc"
                        substitute False

                $ what = renpy.filter_text_tags(h.what, deny=["cps"])
                text what:
                    substitute False
                null height (pmui.text_size * pmui.scale)

            if not _history_list:
                label _("The dialogue history is empty.")

style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    size pmui.name_text_size

style history_text:
    color "#ffffff"
    size pmui.text_size

style history_label:
    xfill True

style history_label_text:
    xalign 0.5
