# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

# Gambar Background
image bg bandung = im.Scale("images/overview-stages/bandung_bg.png", 1920, 1080)
image bg jogja = im.Scale("images/overview-stages/jogja_bg.png", 1920, 1080)
image bg bali = im.Scale("images/overview-stages/bali_bg.png", 1920, 1080)
image bg aceh = im.Scale("images/overview-stages/aceh_bg.png", 1920, 1080)

# Bandung Overview
label bandung:
    scene bg bandung
    call screen bandungview

screen bandungview():

    imagebutton:
        activate_sound klick
        idle im.Scale("images/overview-stages/button_idle_mulaistage.png", 400, 135)
        xalign 0.63
        yalign 0.7
        action Jump("bandungplay")

    imagebutton:
        top_margin 25
        left_margin 25
        idle im.Scale("images/stages/back.png", 100, 120)
        xalign 0.0
        yalign 0.0
        action Jump("stage")
        activate_sound klick

# Jogja Overview
label jogja:
    scene bg jogja
    call screen jogjaview

screen jogjaview():

    imagebutton:
        activate_sound klick
        idle im.Scale("images/overview-stages/button_idle_mulaistage.png", 400, 135)
        xalign 0.63
        yalign 0.7
        action Jump("jogjaplay")

    imagebutton:
        top_margin 25
        left_margin 25
        idle im.Scale("images/stages/back.png", 100, 120)
        xalign 0.0
        yalign 0.0
        action Jump("stage")
        activate_sound klick

# Bali Overview
label bali:
    scene bg bali
    call screen baliview

screen baliview():

    imagebutton:
        activate_sound klick
        idle im.Scale("images/overview-stages/button_idle_mulaistage.png", 400, 135)
        xalign 0.7
        yalign 0.8
        action Jump("baliplay")

    imagebutton:
        top_margin 25
        left_margin 25
        idle im.Scale("images/stages/back.png", 100, 120)
        xalign 0.0
        yalign 0.0
        action Jump("stage")
        activate_sound klick

# Aceh Overview
label aceh:
    scene bg aceh
    call screen acehview

screen acehview():

    imagebutton:
        activate_sound klick
        idle im.Scale("images/overview-stages/button_idle_mulaistage.png", 400, 135)
        xalign 0.63
        yalign 0.7
        action Jump("acehplay")

    imagebutton:
        top_margin 25
        left_margin 25
        idle im.Scale("images/stages/back.png", 100, 120)
        xalign 0.0
        yalign 0.0
        action Jump("stage")
        activate_sound klick
