init python:
    # Default font which supports CJK.
    config.font_replacement_map["DejaVuSans.ttf", False, False] = ("fonts/SourceHanSans-Light.ttf", False, False)
    config.font_replacement_map["DejaVuSans.ttf", True, False] = ("fonts/SourceHanSans-Bold.otf", False, False)

    # Coder font.  Trigged by {tt} tag.
    def coder_font(tag, argument, contents):

        return [ (renpy.TEXT_TAG, u"font=fonts/Inconsolata-Regular.ttf") ] + contents + [ (renpy.TEXT_TAG, u"/font") ]

    config.custom_text_tags["tt"] = coder_font
