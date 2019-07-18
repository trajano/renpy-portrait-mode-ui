init python in pmui:
    import renpy.display.im as im
    from renpy.display.imagelike import Solid

    buttons = {
        "back": "portrait-mode-ui/ui/twotone_skip_previous_white_24.png",
        "top": "portrait-mode-ui/ui/twotone_skip_previous_white_24.png",
        "bottom": "portrait-mode-ui/ui/twotone_skip_previous_white_24.png",
        "auto_forward": "portrait-mode-ui/ui/twotone_fast_forward_white_24.png",
        "show_menu": "portrait-mode-ui/ui/twotone_menu_white_24.png",
        "exit_to_game": "portrait-mode-ui/ui/twotone_exit_to_app_white_24.png",
        "history": "portrait-mode-ui/ui/twotone_history_white_24.png",
    }
    for key, file in buttons.iteritems():
        renpy.image("button %s idle" % (key), file)
        renpy.image("button %s insensitive" % (key), im.MatrixColor(file, im.matrix.brightness(-0.5)))
        renpy.image("button %s hover" % (key), im.MatrixColor(file, im.matrix.tint(1.0, 1.0, 0.75)))
        renpy.image("button %s selected_hover" % (key), im.MatrixColor(file, im.matrix.tint(1.0, 1.0, 0.75)))

    file = Solid("#ffffff", xysize=(72, 72))
    renpy.image("button test idle", file)
    renpy.image("button test insensitive", file)
    renpy.image("button test hover", file)
    renpy.image("button test selected_hover", file)
