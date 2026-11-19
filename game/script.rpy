#######################
#        Main         #
#######################



define a = Character("Adelaine", callback = name_callback, cb_name = "adel")
define m = Character("Miruna", callback = name_callback, cb_name = "miru")
define narrator = Character(callback = name_callback, cb_name = None)

transform scale(ratio):
    zoom ratio

label start:

    play music crash

    scene black

    "What was that{space=0.1}? 2 spaceships crashing into eachother{space=0.1}??"

    scene bg explosion at truecenter, scale(4)

    "What a coincidence{space=0.1}!!!"

    jump act_one
    
    show adel pose2 smug blush

    a "Hi."