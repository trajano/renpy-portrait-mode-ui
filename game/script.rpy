# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Candace", image="candace")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg cave

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    python:
        povname = renpy.input("What is your name?")
        povname = povname.strip()

    show candace happy

    # These display lines of dialogue.

    c "You've created a new Ren'Py game."

    c "Once you add a story, pictures, and music, you can release it to the world!"

    c "I like {code}coding{/code}!"

    c "Making sure that the {tt}xsize{/tt} of theiii dialogue is correct by putting iniiiii extra {tt}i{/tt}s."

    menu:
        "yES, I'd like that very very much":
            c "You said yes"
        "NO":
            c "You said no"

    menu:
        c "This time with caption"
        "YES":
            c "You said yes"
        "NO":
            c "You said no"

    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."
    c "Some random dialog to make history scroll."

    # This ends the game.

    return
