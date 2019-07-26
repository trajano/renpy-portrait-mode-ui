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
    window:
        yalign 1.0
        use say_dialogue(who, what)

screen say_dialogue(who, what):
    # style_prefix "say"

    zorder 45

    window:
        id "window"
        background DynamicDisplayable(dialogbox, who=
            Text(who,
                color = pmui.say_name_text_color,
                size = pmui.scale_p(pmui.say_name_text_size),
                bold = pmui.say_name_text_bold,
                kerning = pmui.say_name_text_kerning
            )
        )

        # add AlphaMask(SideImage(), "portrait-mode-ui/ui/say-side-mask.png") zoom pmui.scale xalign 0.0 yalign 0.0 alpha 0.2 xoffset pmui.scale_p(30) yoffset pmui.scale_p(-30)
        text what id "what"



# ## Make the namebox available for styling through the Character object.
# init python:
#     config.character_id_prefixes.append('namebox')

style window is default
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
    ysize pmui.scale_p(375 - 30 + 120)
    # background "saybox foo"
    # background Solid("#fff", xysize=(1080, 375))

    # background Frame(im.MatrixColor("portrait-mode-ui/ui/bg-say.png", im.matrix.opacity(0.9)),
    #     xysize=(config.screen_width, int(591.0 * pmui.scale)),
    #     yoffset=int((-125.0 + (591-495)) * pmui.scale),
    #     yalign=1.0)

# style namebox:
#     xalign 0.0
#     yalign 1.0
#     xpos int(75.0 * pmui.scale)
#     ypos int(1475.0 * pmui.scale)

style say_label:
    yalign 1.0
    size pmui.name_text_size * pmui.scale
    color pmui.name_color
    kerning -1
    bold True


screen saybox:
    style_prefix "saybox"
    window:
        text "Xyz" size 90 color "#000"

screen saybox_screen:
    style_prefix "saybox_screen"
    window:
        yalign 1.0
        use saybox

image saybox dialogbox:
    Composite(
        (1080,375),
        (0,0), AlphaMask(Solid("#ccffcc"),"portrait-mode-ui/ui/say-alphamask.png"),
        (0,0), "portrait-mode-ui/ui/say-dropshadow.png"
    )

image saybox extra:
    Composite(
        (pmui.scale_p(1080), pmui.scale_p(375)),
        (0,0), AlphaMask(Solid("#77ffff"), Frame("portrait-mode-ui/ui/say-alphamask.png")),
        (0,0), "portrait-mode-ui/ui/say-dropshadow.png"
    )
    xcenter 0.6
    ycenter 0.5
    rotate_pad False
    # alpha 0.7
    easein 0.2 rotate 15 yoffset pmui.scale_p(-180) xoffset pmui.scale_p(-pmui.say_name_box_offset)

init -1 python:
    from math import sqrt
    def dialogbox(st, at, who=None):
        w = 1080
        h = 375
        z = sqrt(w*w + h*h)
        xoffset = absolute(-((z - w) / 2))
        yoffset = absolute(-((z - h) / 2))

        return Composite(
            (pmui.scale_p(w), pmui.scale_p(h)),
            (0,0), At(
                Composite(
                    (pmui.scale_p(1080), pmui.scale_p(375)),
                    (0,0), AlphaMask(Solid(pmui.say_extra_box_color),Frame("portrait-mode-ui/ui/say-alphamask.png")),
                    (0,0), "portrait-mode-ui/ui/say-dropshadow.png",
                    (pmui.scale_p(50), pmui.scale_p(50)), who
                ),
                saybox_namebox_transform(
                    xoffset = xoffset,
                    yoffset = yoffset,
                    yoffset_transform = pmui.say_extra_box_offset,
                    degs = 15,
                    easein = pmui.say_extra_box_easein)),
            (0, 0), At(
                Composite(
                    (pmui.scale_p(1080), pmui.scale_p(375)),
                    (0,0), AlphaMask(Solid(pmui.say_name_box_color),Frame("portrait-mode-ui/ui/say-alphamask.png")),
                    (0,0), "portrait-mode-ui/ui/say-dropshadow.png",
                    (pmui.scale_p(50), pmui.scale_p(50)), who
                ),
                saybox_namebox_transform(
                    xoffset = xoffset,
                    yoffset = yoffset,
                    yoffset_transform = pmui.say_name_box_offset,
                    degs = 10,
                    easein = pmui.say_name_box_easein)
                ),
            (0,0), AlphaMask(Solid(pmui.say_dialog_box_color_1), Frame("portrait-mode-ui/ui/say-alphamask.png")),
            (0,0), AlphaMask(Solid(pmui.say_dialog_box_color_2), Frame("portrait-mode-ui/ui/say-alphamask-gradient.png")),
            (0,0), At(AlphaMask(SideImage(), Frame("portrait-mode-ui/ui/say-alphamask-gradient.png")), saybox_side_image_transform),
            (0,0), "portrait-mode-ui/ui/say-dropshadow.png"
        ), None

transform saybox_side_image_transform:
    alpha 0.2

transform saybox_namebox_transform(xoffset, yoffset, degs, yoffset_transform = 40, easein = 0.15):
    rotate_pad True
    rotate 0
    xoffset pmui.scale_p(xoffset)
    yoffset pmui.scale_p(yoffset)
    easein easein rotate degs yoffset pmui.scale_p(yoffset-yoffset_transform)

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
