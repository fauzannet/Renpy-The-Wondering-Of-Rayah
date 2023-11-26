# Gambar Background
image bg block = im.Scale("images/stages/bg.png", 1920, 1080)

init:
    define stagemusic = "audio/stage-music.mp3"

# Game dimulai disini.
label stage:
    play music stagemusic
    scene bg block
    call screen tips
    return

label reset:
    $ persistent.stage = 1
    return

label buka:
    $ persistent.stage = 6
    return

screen tips(scroll="viewport"):

    ## Ensure other screens do not get input while this screen is displayed.

    modal True

    ## Back Button
    imagebutton:
        activate_sound klick
        top_margin 25
        left_margin 25
        idle im.Scale("images/stages/back.png", 100, 120)
        xalign 0.0
        yalign 0.0
        action Return()

    ## Lanjut Button
    imagebutton:
        activate_sound klick
        left_margin 100
        idle im.Scale("images/stages/puzzle.png", 512, 265)
        xalign 0.0
        yalign 0.6
        action Jump("foto")

    frame:
        background None

        top_margin 200
        bottom_margin 50
        left_margin 700

        viewport:
            mousewheel True
            draggable True
            scrollbars "horizontal"

            hbox:
                xalign 0.4
                spacing 10

                #stageawal
                imagebutton:
                    if persistent.stage >= 1:
                        activate_sound klick
                        idle im.Scale("images/stages/btn_raya.png", 400, 780)
                        clicked im.Scale("images/stages/klik_raya.png", 400, 780)
                        action Jump("awal")

                #stage bandung
                imagebutton:
                    if persistent.stage >= 2:
                        activate_sound klick
                        idle im.Scale("images/stages/btn_bandung.png", 400, 780)
                        clicked im.Scale("images/stages/klik_bandung.png", 400, 780)
                        action Jump("bandung")
                    else:
                        idle im.Scale("images/stages/lock_bandung.png", 400, 780)

                #stage Jogja
                imagebutton:
                    if persistent.stage >= 3:
                        activate_sound klick
                        idle im.Scale("images/stages/btn_jogja.png", 400, 780)
                        clicked im.Scale("images/stages/klik_jogja.png", 400, 780)
                        action Jump("jogja")
                    else:
                        idle im.Scale("images/stages/lock_jogja.png", 400, 780)

                #stage bali
                imagebutton:
                    if persistent.stage >= 4:
                        activate_sound klick
                        idle im.Scale("images/stages/btn_bali.png", 400, 780)
                        clicked im.Scale("images/stages/klik_bali.png", 400, 780)
                        action Jump("bali")
                    else:
                        idle im.Scale("images/stages/lock_bali.png", 400, 780)

                #stage aceh
                imagebutton:
                    if persistent.stage >= 5:
                        activate_sound klick
                        idle im.Scale("images/stages/btn_aceh.png", 400, 780)
                        clicked im.Scale("images/stages/klik_aceh.png", 400, 780)
                        action Jump("aceh")
                    else:
                        idle im.Scale("images/stages/lock_aceh.png", 400, 780)

    label _(""):
        xalign 0.5
        yalign 0.26
