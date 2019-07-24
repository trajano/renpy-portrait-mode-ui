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
        (1080,375),
        (0,0), AlphaMask(Solid("#77ffff"),"portrait-mode-ui/ui/say-alphamask.png"),
        (0,0), "portrait-mode-ui/ui/say-dropshadow.png"
    )
    xcenter 0.6
    ycenter 0.5
    rotate_pad False
    # alpha 0.7
    easein 0.2 rotate 15 yoffset -180 xoffset -20

image saybox namebox:
    Composite(
        (1080,375),
        (0,0), AlphaMask(Solid("#ff7777"),"portrait-mode-ui/ui/say-alphamask.png"),
        (0,0), "portrait-mode-ui/ui/say-dropshadow.png",
        (50,50), Text("Testing Name", color="#fff", size=50)
    )
    # alpha 0.8
    # xpos 0.5 xanchor 0.5
    # ypos 1.0 yanchor 0.6
    # transform_anchor True
    # xanchor  0.5
    # yanchor  0.5
    # transform_anchor True
    rotate_pad False
    # rotate_pad True
    rotate 0
    # xoffset -30
    # yoffset -375-15
    easein 0.15 rotate 10 yoffset -140 xoffset -20

image saybox foo:
    Composite(
        (1080, 375),
        (0,0), "saybox extra",
        # (-30, -int(375*0.6)), "saybox namebox",
        (0, 0), "saybox namebox",
        (0,0), AlphaMask(Solid("#ccffcc"),"portrait-mode-ui/ui/say-alphamask.png"),
        (0,0), "portrait-mode-ui/ui/say-dropshadow.png"
    )
    alpha 0.8

style saybox_window is empty
style saybox_window:
    xsize 1080
    ysize 375 - 30 + 120
#    ysize 375+120-30
    xpadding 60
    ypadding 60
    background "saybox foo"

style saybox_screen_window is empty

label saybox_test:
    scene bg cave
    hide window
    show screen saybox_screen
    pause
    c "test"
