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

# image rect choice alphamask = At(Frame(im.Crop("portrait-mode-ui/ui/say-alphamask.png",(0,0,900,375)), 60, 60, 60, 60), pmui_scale)
# image rect choice dropshadow = At(Frame(im.Crop("portrait-mode-ui/ui/say-dropshadow.png",(0,0,900,375)), left=60), pmui_scale)
# image rect choice select alphamask = At(Frame(im.Crop("portrait-mode-ui/ui/select-alphamask.png",(0,0,900,315)), 30, 30, 0, 30), pmui_scale)

# image rect choice alphamask = At(Frame("portrait-mode-ui/ui/say-alphamask.png", 60, 60, 60, 60), pmui_scale)
# image rect choice dropshadow = At(Frame("portrait-mode-ui/ui/say-dropshadow.png", left=60), pmui_scale)
# image rect choice select alphamask = At(Frame("portrait-mode-ui/ui/select-alphamask.png", 30, 30, 0, 30), pmui_scale)

# image rect choice alphamask = At(Frame("portrait-mode-ui/ui/rect-alphamask.png", 45, 45, 45, 45), pmui_scale)
# image rect choice dropshadow = At(Frame("portrait-mode-ui/ui/rect-dropshadow.png", 45, 45, 45, 45), pmui_scale)
# image rect choice select alphamask = At(Frame("portrait-mode-ui/ui/rect-alphamask-no-padding.png", 30, 30, 0, 30), pmui_scale)

image rect choice alphamask = At(Frame(im.Crop("portrait-mode-ui/ui/rect-alphamask.png", (0, 0, 105, 150)), top=45, left=45, bottom=45), pmui_scale)
image rect choice dropshadow = At(Frame(im.Crop("portrait-mode-ui/ui/rect-dropshadow.png", (0, 0, 105, 150)), top=45, left=45, bottom=45), pmui_scale)
image rect choice select alphamask = At(Frame(im.Crop("portrait-mode-ui/ui/rect-alphamask-no-padding.png", (0, 0, 90, 120)), top=30, left=30, bottom=30), pmui_scale)

screen choice(items):

    if renpy.get_say_image_tag() == None:
        style_prefix "choice"
    else:
        style_prefix "choicesay"

    zorder 40
    frame:
        vbox:
            # spacing pmui.scale_p(5)
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
            (900, 315),
            # (0,0), AlphaMask(Solid(pmui.choice_selected_box_color), "rect choice select alphamask"),
            (0,0), AlphaMask(Solid(pmui.choice_selected_box_color), "rect choice select alphamask"),
        ),
        30, 30, 30, 30
    )

style choice_frame:
    background "choice frame"
    xalign 1.0
    xsize pmui.scale_p(pmui.choice_width)
    yalign 0.5
    left_padding pmui.scale_p(pmui.choice_padding)
    top_padding pmui.scale_p(pmui.choice_padding)
    bottom_padding pmui.scale_p(pmui.choice_padding)

style choicesay_frame is choice_frame:
    yalign 1.0
    bottom_padding 75 + int(220 * pmui.scale)
    yoffset int(-240.0  * pmui.scale)

style choice_button is default:
    selected_background "choice selected frame"
    hover_background "choice selected frame"
    # left_padding pmui.scale_p(5)
    # top_padding pmui.scale_p(5)
    # bottom_padding pmui.scale_p(5)
    left_margin pmui.scale_p(pmui.choice_selected_padding)
    top_margin pmui.scale_p(pmui.choice_selected_padding)
    bottom_margin pmui.scale_p(pmui.choice_selected_padding)

    left_padding pmui.scale_p(pmui.choice_selected_padding)
    top_padding pmui.scale_p(pmui.choice_selected_padding)
    bottom_padding pmui.scale_p(pmui.choice_selected_padding)
    yalign 0.5
    xfill True
    color pmui.choice_text_color
    hover_color "#ffff00"

style choicesay_button is choice_button

style choice_button_text is default:
    color pmui.choice_text_color
    hover_color "#000000"
    selected_color "#000000"
    size pmui.scale_p(pmui.say_dialog_text_size)

style choicesay_button_text is choice_button_text
