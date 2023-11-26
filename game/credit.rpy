# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

# Gambar Background
image bg foto = im.Scale("images/stages/bg.png", 1920, 1080)


label credit:
    scene bg foto
    call screen creditscreen

screen creditscreen(scroll="viewport"):

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
        action Jump("foto")

    frame:
        background None
        left_margin 400
        top_margin 200
        bottom_margin 50

        viewport:
            mousewheel True
            draggable True
            scrollbars "vertical"

            vbox:
                spacing 10

                #stageawal
                imagebutton:
                    idle im.Scale("images/credit/total.png", 1080, 1776)

    label _(""):
        xalign 0.5
        yalign 0.26
