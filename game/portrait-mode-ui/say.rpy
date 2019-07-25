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
    style_prefix "say"

    zorder 45
    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        add AlphaMask(SideImage(), "portrait-mode-ui/ui/say-side-mask.png") zoom pmui.scale xalign 0.0 yalign 0.0 alpha 0.2 xoffset pmui.scale_p(30) yoffset pmui.scale_p(-30)
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
    background "saybox foo"
    # background Solid("#fff", xysize=(1080, 375))

    # background Frame(im.MatrixColor("portrait-mode-ui/ui/bg-say.png", im.matrix.opacity(0.9)),
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

transform saybox_namebox_transform:
    zoom 1.0

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
    easein 0.2 rotate 15 yoffset pmui.scale_p(-180) xoffset pmui.scale_p(-20)

image saybox namebox:
    Composite(
        (pmui.scale_p(1080), pmui.scale_p(375)),
        (0,0), AlphaMask(Solid("#ff7777"),Frame("portrait-mode-ui/ui/say-alphamask.png")),
        (0,0), "portrait-mode-ui/ui/say-dropshadow.png",
        (pmui.scale_p(50),pmui.scale_p(50)), Text("Testing Name", color="#fff", size=50)
    )
    rotate_pad False
    rotate 0
    # This one worked
    easein 0.15 rotate 10 yoffset pmui.scale_p(-140) xoffset pmui.scale_p(-20)

    # rotate_pad True
    # xoffset -30
    # yoffset -375-15
    # alpha 0.8
    # xpos 0.5 xanchor 0.5
    # ypos 1.0 yanchor 0.6
    # transform_anchor True
    # xanchor  0.5
    # yanchor  0.5
    # transform_anchor True

image saybox foo:
    Composite(
        (pmui.scale_p(1080), pmui.scale_p(375)),
        (0,0), "saybox extra",
        # (-30, -int(375*0.6)), "saybox namebox",
        (0, 0), "saybox namebox",
        (0,0), AlphaMask(Solid("#ccffcc"),Frame("portrait-mode-ui/ui/say-alphamask.png")),
        (0,0), "portrait-mode-ui/ui/say-dropshadow.png"
    )
    alpha 0.8


style saybox_screen_window is empty

# style say_dialogue:
#     size pmui.text_size * pmui.scale
#     # yalign 1.0
#     xpos pmui.scale_p(70)
#     ypos pmui.scale_p(1500)
#     # yoffset int(-(1920-1500-50-50.0) * pmui.scale)
#     xsize int((1080 - 70 - 70) * pmui.scale)


style say_dialogue:
    color "#f00"
    size pmui.scale_p(60)
    xmargin pmui.scale_p(60)
    ymargin pmui.scale_p(60)
    xalign 0.0
    yalign 0.0
    xfill True
    yfill True

label saybox_test:
    scene bg cave
    hide window
    show screen saybox_screen
    pause
    c "test"
