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

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    add AlphaMask(SideImage(), "portrait-mode-ui/ui/say-side-mask.png") zoom pmui.scale xalign 0.0 yalign 1.0 alpha 0.2 xoffset int(40.0 * pmui.scale) yoffset int(-125.0 * pmui.scale)


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xfill True
    yalign 1.0

    background Frame("portrait-mode-ui/ui/say.png",
        xysize=(config.screen_width, int(591.0 * pmui.scale)),
        yoffset=int((-125.0 + (591-495)) * pmui.scale),
        yalign=1.0)

style namebox:
    xpos int(75.0 * pmui.scale)
    xalign 0.0
    ypos int(1475.0 * pmui.scale)
    yalign 1.0

style say_label:
    yalign 1.0
    size 50 * pmui.scale
    color pmui.name_color
    kerning -1
    bold True

style say_dialogue:
    size 60 * pmui.scale
    xpos int(70.0 * pmui.scale)
    ypos int(1500.0 * pmui.scale)
    xsize int((1080 - 70 - 70) * pmui.scale)
