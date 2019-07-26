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
    zorder 45
    fixed:
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
    xpadding pmui.scale_p(60)
    ypadding pmui.scale_p(60)
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

    alphamask = Frame(
        "portrait-mode-ui/ui/say-alphamask.png",
        60,
        60,
        60,
        60,
    )
    # alphamask2 = Frame(
    #     Frame("portrait-mode-ui/ui/say-alphamask.png", xysize=(200.0 / 375 * 1080,200)),
    #     # pmui.say_dialog_box_height / 375.0 * 1080.0
    #     60.0 * say_dialog_box_height / 375,
    #     60.0 * say_dialog_box_height / 375,
    #     60.0 * say_dialog_box_height / 375,
    #     60.0 * say_dialog_box_height / 375,
    # )
    # alphamask = Frame("portrait-mode-ui/ui/say-alphamask.png", xysize=(200.0 / 375 * 1080,200))
    alphamask_gradient = Frame(
        "portrait-mode-ui/ui/say-alphamask-gradient.png",
        60,
        60,
        60,
        60,
    )

    def dialogbox_l(st, at, who=None):
        w = 1080
        h = say_dialog_box_height
        z = sqrt(w*w + h*h)
        xoffset = absolute(-((z - w) /2.0 ))
        yoffset = absolute(-((z - h) /2.0 ))
        rect_dimensions = (scale_p(w), scale_p(h))
        transform_function = renpy.store.saybox_namebox_transform
        return Composite(
            rect_dimensions,
            (0,0), At(
                Composite(
                    rect_dimensions,
                    (0,0), AlphaMask(Solid(say_extra_box_color), alphamask),
                    # (0,0), Frame("portrait-mode-ui/ui/say-dropshadow.png"),
                ),
                transform_function(
                    xoffset=xoffset,
                    yoffset=yoffset,
                    yoffset_transform=30,
                    degs = 7.5,
                    easein = 0.20)
                ),
            (0, 0), At(
                Composite(
                    rect_dimensions,
                    (0,0), AlphaMask(Solid(say_name_box_color), alphamask),
                    # (0,0), Frame("portrait-mode-ui/ui/say-dropshadow.png"),
                    (scale_p(40), scale_p(40)), who
                ),
                transform_function(
                    xoffset=xoffset,
                    yoffset=yoffset,
                    yoffset_transform=30,
                    degs = 5)
                ),
            (0,0), AlphaMask(Solid(say_dialog_box_color_1), alphamask),
            (0,0), AlphaMask(Solid(say_dialog_box_color_2), alphamask_gradient),
            # (0,0), At(AlphaMask(SideImage(),  alphamask_gradient), renpy.store.saybox_side_image_transform),
            # (0,0), Frame("portrait-mode-ui/ui/say-dropshadow.png")
        ), None
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
                    (0,0), AlphaMask(Solid(say_extra_box_color), Frame("portrait-mode-ui/ui/say-alphamask.png")),
                    (0,0), Frame("portrait-mode-ui/ui/say-dropshadow.png"),
                ),
                transform_function(
                    xoffset=xoffset,
                    yoffset=yoffset,
                    yoffset_transform=40,
                    degs = 15,
                    easein = 0.20)
                ),
            (0, 0), At(
                Composite(
                    rect_dimensions,
                    (0,0), AlphaMask(Solid(say_name_box_color), Frame("portrait-mode-ui/ui/say-alphamask.png")),
                    (0,0), Frame("portrait-mode-ui/ui/say-dropshadow.png"),
                    (scale_p(50), scale_p(50)), who
                ),
                transform_function(
                    xoffset=xoffset,
                    yoffset=yoffset,
                    yoffset_transform=40,
                    degs = 10)
                ),
            (0,0), AlphaMask(Solid(say_dialog_box_color_1), Frame("portrait-mode-ui/ui/say-alphamask.png")),
            (0,0), AlphaMask(Solid(say_dialog_box_color_2), Frame("portrait-mode-ui/ui/say-alphamask-gradient.png")),
            (0,0), At(AlphaMask(SideImage(), Frame("portrait-mode-ui/ui/say-alphamask-gradient.png")), renpy.store.saybox_side_image_transform),
            (0,0), Frame("portrait-mode-ui/ui/say-dropshadow.png")
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

image saybox namebox:
    Composite(
        (pmui.scale_p(1080), pmui.scale_p(375)),
        (0,0), AlphaMask(Solid("#ff7777"),Frame("portrait-mode-ui/ui/say-alphamask.png")),
        (0,0), "portrait-mode-ui/ui/say-dropshadow.png",
        (pmui.scale_p(50),pmui.scale_p(50)), Text("Testing Name", color="#fff", size=50)
    )
    # offset (pmui.scale_p(1080 * 2), pmui.scale_p(375 * 2))
    saybox_namebox_transform

style saybox_screen_window is empty

style say_dialogue:
    color pmui.say_dialog_text_color
    size pmui.scale_p(pmui.say_dialog_text_size)
    xmargin pmui.scale_p(60)
    ymargin pmui.scale_p(60)
    xalign 0.0
    yalign 0.0
    xfill True
    yfill True
