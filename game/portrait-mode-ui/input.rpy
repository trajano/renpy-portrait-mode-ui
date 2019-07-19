init offset = -1

################################################################################
## In-game screens
################################################################################

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    zorder 100
    window:
        vbox:
            # yalign 1.0
            xalign 0.0
            xpos int(70.0 * pmui.scale)
            ypos 0
            ycenter 0.0
            # ypos int(1500.0 * pmui.scale)
            text prompt style "input_prompt"
            frame:
                background "#fff"
                xsize int((1080 - 70 - 70) * pmui.scale)
                input id "input" style "input_text"

style input_prompt is default

style input_prompt:
    size 60 * pmui.scale
    xsize int((1080 - 70 - 70) * pmui.scale)

# style input:
#     xsize int((1080 - 70 - 70) * pmui.scale)
#     size 30

style input_text:
    size 60

style _console_text:
    size 40
