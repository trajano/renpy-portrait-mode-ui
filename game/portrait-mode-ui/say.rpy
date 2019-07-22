init offset = -1

################################################################################
## In-game screens
################################################################################

## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    zorder 45
    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    add AlphaMask(SideImage(), "portrait-mode-ui/ui/say-side-mask.png") zoom pmui.scale xalign 0.0 yalign 1.0 alpha 0.2 xoffset pmui.scale_p(40) yoffset pmui.scale_p(-125)


# ## Make the namebox available for styling through the Character object.
# init python:
#     config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xfill True
    yalign 1.0

    # background im.FactorScale(
    #         im.MatrixColor("portrait-mode-ui/ui/bg-say.png",
    #             im.matrix.opacity(0.9)),
    #         pmui.scale) yoffset int(1080 -125.0 - 591 * pmui.scale)

    background Frame(im.MatrixColor("portrait-mode-ui/ui/bg-say.png", im.matrix.opacity(0.9)),
        xysize=(config.screen_width, int(591.0 * pmui.scale)),
        yoffset=int((-125.0 + (591-495)) * pmui.scale),
        yalign=1.0)

    # background Frame("portrait-mode-ui/ui/bg-say.png",
    #     xysize=(config.screen_width, int(591.0 * pmui.scale)),
    #     yoffset=int((-125.0 + (591-495)) * pmui.scale),
    #     yalign=1.0)

style namebox:
    xalign 0.0
    yalign 1.0
    xpos int(75.0 * pmui.scale)
    ypos int(1475.0 * pmui.scale)

style say_label:
    yalign 1.0
    size pmui.name_text_size * pmui.scale
    color pmui.name_color
    kerning -1
    bold True

style say_dialogue:
    size pmui.text_size * pmui.scale
    # yalign 1.0
    xpos pmui.scale_p(70)
    ypos pmui.scale_p(1500)
    # yoffset int(-(1920-1500-50-50.0) * pmui.scale)
    xsize int((1080 - 70 - 70) * pmui.scale)
