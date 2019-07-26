# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Candace", image="candace")
define narrator = Character("Me")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg cave

    show candace happy

    # These display lines of dialogue.

    c "You've created a new Ren'Py game."
    "This is the narrator."
    c "This is {b}Candace{/b} again.  It should animate. last_who"
    c "This is {b}Candace{/b} again.  It should not animate. last_who"
    "This is the narrator. It should animate last_who"
    "This is the narrator. It should not animate last_who"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    python:
        povname = renpy.input("What is your name?")
        povname = povname.strip()

    c "Hi [povname]!"

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

    c "Some {b}random{/b} {i}dialog{/i} to make {b}{i}history{/i}{/b} scroll. じーっ・{b}じっ~~{/b}"
    c "Though history is working, I actually don't really like the way it is rendered."
    c "Maybe have a background... in fact make each menu screen have its own background."
    c "The next few remaining bits are the history, save/load, preferences and main menu."
    c "I'm leaving it up to the developer to add additional rows to the game menu."
    c "I'm also thinking just make it full screen blackout when in the game menu, just to simply a few things."
    c "Maybe put this up on github on the weekend."
    c "I did find that the icons on top are a bit difficult to press though so something to check in a bit."
    c "Some random dialog to make history scroll."
    c "I think I want the confirmation dialogs to be stlyized like Persona 5 but with blocks of Persona 4."
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
