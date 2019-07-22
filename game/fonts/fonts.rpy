init python:
    config.font_replacement_map["Lato.ttf", False, False] = ("fonts/Lato-Light.ttf", False, False)
    config.font_replacement_map["Lato.ttf", True, False] = ("fonts/Lato-Bold.ttf", False, False)
    config.font_replacement_map["Lato.ttf", True, True] = ("fonts/Lato-BoldItalic.ttf", False, False)
    config.font_replacement_map["Lato.ttf", False, True] = ("fonts/Lato-LightItalic.ttf", False, False)
    # Default font which supports CJK.
    config.font_replacement_map["SourceHanSans.ttf", False, False] = ("fonts/SourceHanSans-Light.ttf", False, False)
    config.font_replacement_map["SourceHanSans.ttf", True, False] = ("fonts/SourceHanSans-Bold.otf", False, False)

    # Coder font.  Trigged by {tt} tag.
    def coder_font(tag, argument, contents):

        return [ (renpy.TEXT_TAG, u"font=fonts/Inconsolata-Regular.ttf") ] + contents + [ (renpy.TEXT_TAG, u"/font") ]

    config.custom_text_tags["tt"] = coder_font
    config.custom_text_tags["code"] = coder_font

style default:
    font FontGroup().add("Lato.ttf", 0x0020, 0x007f).add("SourceHanSans.ttf", 0x0000, 0xffff)
