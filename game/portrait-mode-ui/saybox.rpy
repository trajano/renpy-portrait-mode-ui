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
    xpos 0.5 xanchor 0.5
    ypos 0.5 yanchor 0.6
    easein 0.2 rotate 15

image saybox namebox:
    Composite(
        (1080,375),
        (0,0), AlphaMask(Solid("#ff7777"),"portrait-mode-ui/ui/say-alphamask.png"),
        (0,0), "portrait-mode-ui/ui/say-dropshadow.png",
        (50,50), Text("Testing Name", color="#fff", size=50)
    )
    # xpos 0.5 xanchor 0.5
    # ypos 0.5 yanchor 0.6
    # transform_anchor True
    xcenter 0.6
    ycenter 0.5
    easein 0.15 rotate 7.5 # yoffset -440+int(375*0.6)

image saybox foo:
    Composite(
        (1080, 400),
        (-20, -440), "saybox extra",
        # (-30, -int(375*0.6)), "saybox namebox",
        (-30, -440), "saybox namebox",
        (0,0), AlphaMask(Solid("#ccffcc"),"portrait-mode-ui/ui/say-alphamask.png"),
        (0,0), "portrait-mode-ui/ui/say-dropshadow.png"
    )

style saybox_window is empty
style saybox_window:
    xsize 1080
    ysize 375+125-30
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
