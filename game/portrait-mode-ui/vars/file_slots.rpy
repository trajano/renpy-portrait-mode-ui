init offset = -2

## File Slot Buttons ###########################################################
##
## A file slot button is a special kind of button. It contains a thumbnail
## image, and text describing the contents of the save slot. A save slot uses
## image files in gui/button, like the other kinds of buttons.

## The save slot button.
define gui.slot_button_borders = Borders(9, 9, 9, 9)
define gui.slot_button_text_size = 30
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color
define gui.slot_button_width = config.thumbnail_width + 18
define gui.slot_button_height = config.thumbnail_height + 18 * 2 + gui.slot_button_text_size * 3

## The number of columns and rows in the grid of save slots.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2
