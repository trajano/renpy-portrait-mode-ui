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

transform pmui_scale:
    zoom pmui.scale

image rect say alphamask = At(Frame("portrait-mode-ui/ui/say-alphamask.png", 60, 60, 60, 60, xysize=(1080, pmui.say_dialog_box_height)), pmui_scale)
image rect say dropshadow = At(Frame("portrait-mode-ui/ui/say-dropshadow.png", 60, 60, 60, 60, xysize=(1080, pmui.say_dialog_box_height)), pmui_scale)
image rect say alphamask gradient = At(Frame("portrait-mode-ui/ui/say-alphamask-gradient.png", 60, 60, 60, 60, xysize=(1080, pmui.say_dialog_box_height)), pmui_scale)

screen say(who, what):
    zorder 45
    vbox:
        yalign 1.0
        use say_dialogue(who, what)

screen say_dialogue(who, what):
    # style_prefix "say"

    window:
        id "window"
        style "say_window"
        background DynamicDisplayable(pmui.dialogbox, who=Text(who, style = "say_label"))
        text what id "what"

# ## Make the namebox available for styling through the Character object.
# init python:
#     config.character_id_prefixes.append('namebox')

style window is empty
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style say_window:
    xfill True
    yalign 1.0
    xpadding pmui.scale_p(pmui.say_dialog_box_offset)
    ypadding pmui.scale_p(pmui.say_dialog_box_offset)
    ysize pmui.scale_p(pmui.say_dialog_box_height - 30 * pmui.say_dialog_box_height/375 + pmui.say_dialog_box_bottom_offset)

style say_label:
    color pmui.say_name_text_color
    size pmui.scale_p(pmui.say_name_text_size)
    bold pmui.say_name_text_bold
    kerning pmui.say_name_text_kerning

screen saybox:
    style_prefix "saybox"
    window:
        text "Xyz" size 90 color "#000"

screen saybox_screen:
    style_prefix "saybox_screen"
    window:
        yalign 1.0
        use saybox

init python in pmui:
    from math import sqrt
    from renpy.store import At, SideImage
    from renpy.display.core import absolute
    from renpy.display.imagelike import Frame, Solid
    from renpy.display.layout import AlphaMask, Composite

    def dialogbox(st, at, who=None):
        w = 1080
        h = 375
        z = sqrt(w*w + h*h)
        xoffset = absolute(-((z - w) /2.0 ))
        yoffset = absolute(-((z - h) /2.0 ))
        rect_dimensions = (scale_p(w), scale_p(h))
        transform_function = renpy.store.saybox_namebox_transform_fixed
        return Composite(
            rect_dimensions,
            (0,0), At(
                Composite(
                    rect_dimensions,
                    (0,0), AlphaMask(Solid(say_extra_box_color), "rect say alphamask"),
                    (0,0), "rect say dropshadow",
                ),
                transform_function(
                    xoffset=xoffset,
                    yoffset=yoffset,
                    yoffset_transform=say_extra_box_yoffset_transform,
                    degs = say_extra_box_rotation,
                    easein = 0.20)
                ),
            (0, 0), At(
                Composite(
                    rect_dimensions,
                    (0,0), AlphaMask(Solid(say_name_box_color), "rect say alphamask"),
                    (0,0), "rect say dropshadow",
                    (scale_p(say_name_box_offset), scale_p(say_name_box_offset)), who
                ),
                transform_function(
                    xoffset=xoffset,
                    yoffset=yoffset,
                    yoffset_transform=say_name_box_yoffset_transform,
                    degs = say_name_box_rotation)
                ),
            (0,0), AlphaMask(Solid(say_dialog_box_color_1), "rect say alphamask"),
            (0,0), AlphaMask(Solid(say_dialog_box_color_2), "rect say alphamask gradient"),
            (0,0), At(AlphaMask(SideImage(), "rect say alphamask gradient"), renpy.store.saybox_side_image_transform),
            (0,0), "rect say dropshadow",
        ), None

transform saybox_side_image_transform:
    alpha 0.2

transform saybox_namebox_transform(xoffset, yoffset, degs, yoffset_transform = 40, easein = 0.15):
    rotate_pad True
    rotate 0
    xoffset pmui.scale_p(xoffset)
    yoffset pmui.scale_p(yoffset)
    easein easein rotate degs yoffset pmui.scale_p(yoffset-yoffset_transform)

transform saybox_namebox_transform_fixed(xoffset, yoffset, degs, yoffset_transform = 40):
    rotate_pad True
    rotate 0
    xoffset pmui.scale_p(xoffset)
    rotate degs yoffset pmui.scale_p(yoffset-yoffset_transform)

transform saybox_namebox_transform2(xoffset=0, yoffset=0, degs = 10, yoffset_transform = 40, easein = 0.15):
    rotate_pad True
    xoffset pmui.scale_p(xoffset)
    on show:
        rotate 0
        yoffset pmui.scale_p(yoffset)
        easein easein rotate degs yoffset pmui.scale_p(yoffset-yoffset_transform)
    on replace:
        yoffset pmui.scale_p(yoffset-yoffset_transform)
        rotate degs
    on hide:
        rotate degs
        yoffset pmui.scale_p(yoffset-yoffset_transform)
        easein easein rotate 0 yoffset pmui.scale_p(yoffset)

transform saybox_namebox_transform_fixed(xoffset=0, yoffset=0, degs = 10, yoffset_transform = 40, easein = None):
    rotate_pad True
    xoffset pmui.scale_p(xoffset)
    yoffset pmui.scale_p(yoffset-yoffset_transform)
    rotate degs

style saybox_screen_window is empty

style say_dialogue:
    color pmui.say_dialog_text_color
    size pmui.scale_p(pmui.say_dialog_text_size)
    xmargin pmui.scale_p(pmui.say_dialog_box_offset)
    ymargin pmui.scale_p(pmui.say_dialog_box_offset)
    xalign 0.0
    yalign 0.0
    xfill True
    yfill True
