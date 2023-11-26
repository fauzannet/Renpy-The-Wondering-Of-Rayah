# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

# Gambar Background
image bg foto = im.Scale("images/stages/bg.png", 1920, 1080)


label foto:
    scene bg foto
    call screen fotoview

screen fotoview():

    ## Back Button
    imagebutton:
        top_margin 25
        left_margin 25
        idle im.Scale("images/stages/back.png", 100, 120)
        xalign 0.0
        yalign 0.0
        action Jump("stage")
        activate_sound klick


    imagebutton:
        xalign 0.5
        yalign 0.8

        if persistent.stage == 1:
            idle im.Scale("images/foto/1.png", 1387, 800)

        elif persistent.stage == 2:
            idle im.Scale("images/foto/1.png", 1387, 800)

        elif persistent.stage == 3:
            idle im.Scale("images/foto/2.png", 1387, 800)

        elif persistent.stage == 4:
            idle im.Scale("images/foto/3.png", 1387, 800)

        elif persistent.stage == 5:
            idle im.Scale("images/foto/4.png", 1387, 800)

        elif persistent.stage == 6:
            idle im.Scale("images/foto/5.png", 1387, 800)
            action Jump("credit")

    if persistent.stage == 6:
        text "TEKAN GAMBAR" xalign 0.5 yalign 0.2 color "#000000"
        # Tambahkan teks lainnya di sini sesuai kebutuhan
