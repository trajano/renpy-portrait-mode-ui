################################################################################
## Customizations
################################################################################

# This file controls the customizable values for the portrait-mode-ui

## The init offset statement causes the initialization statements in this file
## to run before init statements in any other file.
init offset = -2

## Calling gui.init resets the styles to sensible default values, and sets the
## width and height of the game.
init python:
    # gui.init(1080, 1920)
    gui.init(720, 1280)

## Colors ######################################################################
##
## The colors of text in the interface.

## Color for the name in the dialogue
define pmui.name_color = '#101010'

## Color for choice action
define pmui.choice_color = '#efefef'

## An accent color used throughout the interface to label and highlight text.
define pmui.accent_color = '#0099cc'

## The color used for a text button when it is neither selected nor hovered.
define pmui.idle_color = '#888888'

## The small color is used for small text, which needs to be brighter/darker to
## achieve the same effect.
define pmui.idle_small_color = '#aaaaaa'

## The color that is used for buttons and bars that are hovered.
define pmui.hover_color = '#66c1e0'

## The color used for a text button when it is selected but not focused. A
## button is selected if it is the current screen or preference value.
define pmui.selected_color = '#ffffff'

## The color used for a text button when it cannot be selected.
define pmui.insensitive_color = '#8888887f'

## Colors used for the portions of bars that are not filled in. These are not
## used directly, but are used when re-generating bar image files.
define pmui.muted_color = '#003d51'
define pmui.hover_muted_color = '#005b7a'

## The colors used for dialogue and menu choice text.
define pmui.text_color = '#ffffff'
define pmui.interface_text_color = '#ffffff'

## Localization ################################################################

## This controls where a line break is permitted. The default is suitable
## for most languages. A list of available values can be found at https://
## www.renpy.org/doc/html/style_properties.html#style-property-language

define pmui.language = "unicode"
