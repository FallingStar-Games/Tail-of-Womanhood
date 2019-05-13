#First scene after cw

define cg = Character("Pat", who_color="#006400")
define dw = Character("Emily")
define dw_post = Character("Dustin")

label wolf:
    scene bg eantioch
    show wolf before at right
    show catgirl young at left

    cg "See ya next year, Emily."

    dw "See ya then."

    show bg eantioch
    with fade
    show wolf after at right

    dw_post "Hey, Pat."

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
