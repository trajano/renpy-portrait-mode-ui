init python in pmui:
    import renpy.display.im as im
    from renpy.display.imagelike import Solid
    import renpy.config as config
    from renpy.color import Color

    state_colors = {
        "idle" : Color(idle_color),
        "hover" : Color(hover_color),
        "selected" : Color(selected_color),
        "selected_idle" : Color(selected_color),
        "insensitive" : Color(insensitive_color),
    }

    buttons = {
        "back": "portrait-mode-ui/ui/twotone_skip_previous_white_24.png",
        "big back": "portrait-mode-ui/ui/twotone_skip_previous_white_36.png",
        "top": "portrait-mode-ui/ui/twotone_skip_previous_white_24.png",
        "bottom": "portrait-mode-ui/ui/twotone_skip_previous_white_24.png",
        "auto_forward": "portrait-mode-ui/ui/twotone_fast_forward_white_24.png",
        "big auto_forward": "portrait-mode-ui/ui/twotone_fast_forward_white_36.png",
        "show_menu": "portrait-mode-ui/ui/twotone_menu_white_24.png",
        "big show_menu": "portrait-mode-ui/ui/twotone_menu_white_36.png",
        "exit_to_game": "portrait-mode-ui/ui/twotone_exit_to_app_white_24.png",
        "big exit_to_game": "portrait-mode-ui/ui/twotone_exit_to_app_white_36.png",
        "history": "portrait-mode-ui/ui/twotone_history_white_24.png",
        "big history": "portrait-mode-ui/ui/twotone_history_white_36.png",
        "big rotate": "portrait-mode-ui/ui/twotone_rotate_90_degrees_ccw_white_36.png",
        "save": "portrait-mode-ui/ui/twotone_cloud_download_white_24.png",
        "load": "portrait-mode-ui/ui/twotone_cloud_upload_white_24.png",
        "settings": "portrait-mode-ui/ui/twotone_settings_white_24.png",
        "show_main_menu": "portrait-mode-ui/ui/twotone_home_white_24.png",
    }
    for key, file in buttons.iteritems():
        for state, color in state_colors.iteritems():
            renpy.image("button %s %s" % (key, state),
                im.FactorScale(
                    im.MatrixColor(file,
                        im.matrix.tint(color.rgb[0],color.rgb[1],color.rgb[2]) *
                        im.matrix.opacity(color.alpha)
                    ),
                    scale)
                )

    if renpy.variant("pc"):
        file = Solid("#ffffff", xysize=(72, 72))
        renpy.image("button test idle", file)
        renpy.image("button test insensitive", file)
        renpy.image("button test hover", file)
        renpy.image("button test selected_hover", file)

        file = Solid("#ffffff", xysize=(scale_p(quick_menu_icon_size), scale_p(quick_menu_icon_size)))
        renpy.image("button big test idle", file)
        renpy.image("button big test insensitive", file)
        renpy.image("button big test hover", file)
        renpy.image("button big test selected_hover", file)
