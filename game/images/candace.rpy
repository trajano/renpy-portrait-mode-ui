# Ren'py default: the side image should be 20% of the screen width to align well with the
# image side candace = Crop((318, 149, 565, 565), "candace happy", zoom=(gui.name_xpos/565))

# The side image for portrait mode should be 1020 x 315 to match the alpha mask.
# The alpha mask and scaling will be applied by the library.
image side candace = Composite(
    (1020, 315),
    #(1020-800, 0), Crop((0, 300, 800, 315), "candace happy", yoffset=-200)
    (0, 0), Crop((0, 400, 800, 315), "candace happy", zoom=2.0, xoffset=-300)
)
