init offset = -2

define pmui.quick_menu_icon_size = 108
define pmui.quick_menu_bar_size = 140
define pmui.quick_menu_bar_dropshadow_size = 28
define pmui.game_menu_quick_menu_gap_size = 25
define pmui.game_menu_button_bar_icon_size = 72
define pmui.game_menu_button_bar_text_size = 30
define pmui.game_menu_bar_size = 140

define pmui.text_size = 60
define pmui.name_text_size = 50

## The width and height of thumbnails used by the save slots.
define config.thumbnail_width = int((1080 - 50 - 50 * pmui.save_columns - pmui.scrollbar_size)/pmui.save_columns)
define config.thumbnail_height = int(config.thumbnail_width * 16/9)

# define gui.slot_button_borders = Borders(9, 9, 9, 9)
# define gui.slot_button_text_size = 30
# define gui.slot_button_text_xalign = 0.5
# define gui.slot_button_text_idle_color = gui.idle_small_color
# define gui.slot_button_text_selected_idle_color = gui.selected_color
# define gui.slot_button_text_selected_hover_color = gui.hover_color
# define gui.slot_button_width = config.thumbnail_width + 18
# define gui.slot_button_height = config.thumbnail_height + 18 * 2 + gui.slot_button_text_size * 3
