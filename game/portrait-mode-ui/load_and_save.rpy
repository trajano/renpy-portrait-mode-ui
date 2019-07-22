init offset = -1

################################################################################
## Main and Game Menu Screens
################################################################################

## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu
    use file_slots(_("Save"))

screen load():

    tag menu
    use file_slots(_("Load"))

screen file_slots(title):
    use portrait_game_menu(title, scroll="vpgrid", cols = 3):
        style_prefix "slot"

        python:
            max_saves = int((FileUsedSlots()[0]-1) / pmui.save_columns + 1) * pmui.save_columns
            if title == _("Save"):
                max_saves = max_saves + pmui.save_columns

        for i in range(max_saves):
            $ slot = i + 1
            button:
                action FileAction(slot)

                has vbox

                add FileScreenshot(slot, empty="empty slot") xalign 0.5

                text FileTime(slot, format=_("{#file_time}%Y-%m-%d %H:%M"), empty="empty slot"):
                    style "slot_time_text"

                text FileSaveName(slot):
                    style "slot_name_text"

                key "save_delete" action FileDelete(slot)

image empty slot = Solid("#ffffff77", xysize=(config.thumbnail_width, config.thumbnail_height))

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 43
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    # properties gui.button_properties("slot_button")
    xalign 0.5
    xsize pmui.scale_p(config.thumbnail_width)
    ysize pmui.scale_p(config.thumbnail_height + 30 + 30)

style slot_button_text:
    size pmui.scale_p(30)
