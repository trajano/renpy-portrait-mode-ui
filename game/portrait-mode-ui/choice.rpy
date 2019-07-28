init offset = -1

################################################################################
## In-game screens
################################################################################

## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

image rect choice alphamask:
    "rect alphamask"
image rect choice dropshadow:
    "rect dropshadow"
image rect choice alphamask gradient:
    "rect alphamask gradient"

screen choice(items):

    if renpy.get_say_image_tag() == None:
        style_prefix "choice"
    else:
        style_prefix "choicesay"

    zorder 40
    frame:
        vbox:
            for i in items:
                textbutton i.caption action i.action

## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True

style choice_say_button is choice_button
style choice_button_text is button_text

image choice frame:
    Frame(
        Composite(
            (900, 375),
            (0,0), AlphaMask(Solid(pmui.choice_box_color), "rect choice alphamask"),
            (0,0), "rect choice dropshadow",
        ),
        60, 60, 60, 60
    )

image choice selected frame:
    Frame(
        Composite(
            (900, 375),
            (0,0), AlphaMask(Solid(pmui.choice_selected_box_color), "rect choice alphamask"),
            (0,0), "rect choice dropshadow",
        ),
        60, 60, 60, 60
    )

style choice_frame:
    background "choice frame"
    xalign 1.0
    xsize pmui.scale_p(648)
    yalign 0.5
    left_padding pmui.scale_p(25)
    top_padding pmui.scale_p(25)
    bottom_padding pmui.scale_p(25)

style choicesay_frame is choice_frame:
    yalign 1.0
    bottom_padding 75 + int(220 * pmui.scale)
    yoffset int(-240.0  * pmui.scale)

style choice_button is default:
    selected_background "choice selected frame"
    hover_background "choice selected frame"
    left_padding pmui.scale_p(50)
    top_padding pmui.scale_p(50)
    bottom_padding pmui.scale_p(50)
    yalign 0.5
    xfill True
    color pmui.choice_text_color
    hover_color "#ffff00"

style choicesay_button is choice_button

style choice_button_text is default:
    color pmui.choice_text_color
    hover_color "#000000"
    selected_color "#000000"
    size pmui.scale_p(50)

style choicesay_button_text is choice_button_text
