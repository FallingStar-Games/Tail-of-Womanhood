#First scene after cw
label wolf:
    scene bg eantioch
    show wolf before at right
    show catgirl young at left
    $ say_textbox = "textbox_paper"

    cg "See ya next year, Emily."

    dw "See ya then."

    scene bg black
    with dissolve
    $ say_textbox = "textbox"

    "At the start of the next school year."

    scene bg eantioch
    with dissolve
    show wolf after at right
    show catgirl young at left
    $ say_textbox = "textbox_paper"

    dw_post "Hey, Alan."

    cg "Woah, you look different Emi-"

    show wolf after upset at right

    dw_post "It's Dustin now. I'm a boy."

    show catgirl young apologetic at left

    cg "Oh, I'm sorry Dustin."

    show wolf after at right

    dw_post "It's alright, just try to remember that from now on, okay?"

    show catgirl young smiling at left

    cg "Sure thing."

    return
