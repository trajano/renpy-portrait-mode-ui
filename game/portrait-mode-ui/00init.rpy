################################################################################
## Initialization
################################################################################

## The init offset statement causes the initialization statements in this file
## to run before init statements in any other file.
init offset = -2

init python in pmui:
    scale = renpy.config.screen_width / 1080.0
    def scale_p(x):
        if scale == 1.0:
            return int(x)
        else:
            return int(scale * x)
    def scale_f(x):
        if scale == 1.0:
            return x
        else:
            return scale * x
    if renpy.config.screen_width > renpy.config.screen_height:
        # landscape
        ctc_offset = 0
        ctc_scale = 0.5
        say_dialog_box_bottom_offset = 15
        say_dialog_box_height = 200
        say_dialog_box_offset = 45
        say_dialog_text_size = 20
        say_extra_box_offset = 20
        say_extra_box_rotation = 7.5
        say_extra_box_yoffset_transform = 0
        say_name_box_offset = 45
        say_name_box_rotation = 5
        say_name_box_yoffset_transform = 5
        say_name_text_size = 20

    else:
        # portrait
        ctc_offset = -60
        ctc_scale = 1
        say_dialog_box_bottom_offset = 120
        say_dialog_box_height = 375
        say_dialog_box_offset = 60
        say_dialog_text_size = 60
        say_extra_box_offset = 20
        say_extra_box_rotation = 15
        say_extra_box_yoffset_transform = 40
        say_name_box_offset = 50
        say_name_box_rotation = 10
        say_name_box_yoffset_transform = 40
        say_name_text_size = 40

## Colors ######################################################################
##
## The colors of text in the interface.

## An accent color used throughout the interface to label and highlight text.
#define gui.accent_color = "#0099cc" if hasattr(pmui, "accent_color") else pmui.accent_color
define gui.accent_color = pmui.accent_color

## The color used for a text button when it is neither selected nor hovered.
define gui.idle_color = pmui.idle_color

## The small color is used for small text, which needs to be brighter/darker to
## achieve the same effect.
define gui.idle_small_color = pmui.idle_small_color

## The color that is used for buttons and bars that are hovered.
define gui.hover_color = pmui.hover_color

## The color used for a text button when it is selected but not focused. A
## button is selected if it is the current screen or preference value.
define gui.selected_color = pmui.selected_color

## The color used for a text button when it cannot be selected.
define gui.insensitive_color = pmui.insensitive_color

## Colors used for the portions of bars that are not filled in. These are not
## used directly, but are used when re-generating bar image files.
define gui.muted_color = pmui.muted_color
define gui.hover_muted_color = pmui.hover_muted_color

## The colors used for dialogue and menu choice text.
define gui.text_color = pmui.text_color
define gui.interface_text_color = pmui.interface_text_color
