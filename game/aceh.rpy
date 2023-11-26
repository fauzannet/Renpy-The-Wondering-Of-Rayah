# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image aceh0 = im.Scale("images/aceh/aceh 0.png", 1920, 1080)
image aceh1 = im.Scale("images/aceh/aceh 1.png", 1920, 1080)
image aceh2 = im.Scale("images/aceh/aceh 2.png", 1920, 1080)
image aceh3 = im.Scale("images/aceh/aceh 3.png", 1920, 1080)
image aceh4 = im.Scale("images/aceh/aceh 4.png", 1920, 1080)
image aceh5 = im.Scale("images/aceh/aceh 5.png", 1920, 1080)
image aceh6 = im.Scale("images/aceh/aceh 6.png", 1920, 1080)
image aceh7 = im.Scale("images/aceh/aceh 7.png", 1920, 1080)
image aceh8 = im.Scale("images/aceh/aceh 8.png", 1920, 1080)
image aceh9 = im.Scale("images/aceh/aceh 9.png", 1920, 1080)
image aceh10 = im.Scale("images/aceh/aceh 10.png", 1920, 1080)
image aceh11 = im.Scale("images/aceh/aceh 11.png", 1920, 1080)
image aceh12 = im.Scale("images/aceh/aceh 12.png", 1920, 1080)
image aceh13 = im.Scale("images/aceh/aceh 13.png", 1920, 1080)
image aceh14 = im.Scale("images/aceh/aceh 14.png", 1920, 1080)
image aceh15 = im.Scale("images/aceh/aceh 15.png", 1920, 1080)
image aceh16 = im.Scale("images/aceh/aceh 16.png", 1920, 1080)
image aceh17 = im.Scale("images/aceh/aceh 17.png", 1920, 1080)
image aceh18 = im.Scale("images/aceh/aceh 18.png", 1920, 1080)

style pilihan:
    color "#EAB2A0"
    hover_color "#000000"
    background "#435B66"

define selected_choice = None
# Deklarasikan karakter yang digunakan di game.
default poinaceh = 0
define t = Character('Jamal', color="#FFFAD7")
define y = Character('Orang Asing', color="#FFFAD7")

# Game dimulai disini.s
label acehplay:

    scene aceh0
    a "akhirnya aku sampai di Aceh! Aku benar-benar bersemangat untuk menemui orang tua asliku yang kabarnya berada di sini."

    scene aceh1
    t "Selamat datang di Aceh, Bung! Apa yang membawamu ke sini?"

    scene aceh2
    a "Terima kasih! Aku mencari orang tua asliku yang konon berada di Aceh. diriku pun belum terlalu mengenal tentang Aceh"

    scene aceh3
    t "Ah, sangat menarik! Aceh memang kaya akan budaya dan sejarah. Di sini, kamu akan menemukan warisan yang kental dari kebudayaan Islam, yang memberikan identitas yang kuat bagi masyarakat Aceh."

    scene aceh4
    a "Benar sekali. Aku juga mendengar bahwa seni dan musik tradisional sangat penting di Aceh."

    scene aceh5
    t "Ya, betul sekali. Salah satu seni tradisional terkenal di Aceh adalah tari Saman, yang biasanya dilakukan oleh sekelompok pemuda dengan gerakan yang serasi dan dinamis. Musik tradisional seperti gendang, serune kalee (serunai), dan rapai juga sangat populer di sini."

    scene aceh6
    a "Itu terdengar menarik! Aku sangat berharap bisa menyaksikan pertunjukan seni dan mendengarkan musik tradisional Aceh."

    scene aceh7
    t "Tentu, aku akan membantumu menemukan tempat-tempat yang tepat untuk menikmati seni dan musik tradisional Aceh."

    scene aceh8
    a "Wow, terdengar spektakuler! Aku sungguh beruntung bisa menjelajahi kekayaan budaya dan sejarah Aceh."

    scene aceh9
    t "Kamu pasti akan menemukan banyak hal menarik di Aceh. Budaya dan keramahan penduduk setempat akan membuatmu merasa diterima dengan hangat. Jangan ragu untuk bertanya jika kamu membutuhkan bantuan apa pun."

    scene aceh6
    a "Terima kasih banyak, Jamal! Aku benar-benar bersemangat untuk memulai petualangan ini dan mengenal lebih dekat budaya Aceh."

    scene aceh7
    t "Tetapi sebelumnya, apakah kamu bisa membantuku menyelesaikan teka teki ini ?"

    scene aceh8
    a "tentu saja !"
    jump start_aceh1

label acehplay2:
    scene aceh7
    t "terimakasih telah membantuku"
    scene aceh9
    a "terimakasih kembali"
    scene aceh10
    y "Ah, kamu datang! Aku telah mendengar tentangmu. Aku tahu mengenai orang tuamu."
    scene aceh11
    a "Benarkah? Apa kamu bisa memberiku informasi tentang mereka? Aku telah mencari mereka begitu lama."
    scene aceh12
    y "Sebenarnya,...."
    y "aku adalah orang tuamu."
    scene aceh13
    a "Bagaimana mungkin?"
    scene aceh14
    y "Ya, mungkin ini terdengar tidak masuk akal, tetapi aku memiliki alasan yang kuat untuk mengatakan itu."
    scene aceh15
    a "aku mengira dirimu sudah meninggal saat terjadi tsunami pada saat itu."
    scene aceh16
    y "Peristiwa tsunami yang mengerikan itu telah menciptakan banyak kebingungan dan kehilangan di antara keluarga-keluarga di Aceh. Namun, dalam kasusku, aku berhasil selamat dan berada di tempat yang jauh."
    scene aceh17
    a "Tapi bagaimana kamu bisa tahu tentangku? Aku tidak pernah mendengar berita tentang ayah selamat dari tsunami."
    scene aceh18
    y "Setelah peristiwa itu, Aku berjuang untuk membangun kembali hidupku seorang diri."
    scene aceh11
    a "Aku tidak tahu apa yang harus kukatakan. Semua ini terasa begitu tak terduga."
    scene aceh12
    y "Aku memahami bahwa ini adalah berita yang mengejutkan bagimu. Aku ingin memberimu waktu untuk memproses semuanya. kamu masih ingat benda ini ?"
    scene aceh13
    a "potongan foto yang terakhir! terimakasih ayah"
    y "Sama - sama Rayeh"

    $ persistent.stage = 6
    jump stage

label start_aceh1:
    $ poinaceh = 0
    scene aceh0
    # Pertanyaan
    $ question = "Apa yang membuat tari Saman di Aceh sangat khas?"

    # Opsi Jawaban
    $ choices = ["Gerakan yang serasi dan dinamis", "Penggunaan alat musik modern", "Kostum yang berwarna-warni", "Penari tunggal yang menarikan tari tersebut"]

    # Tampilkan pertanyaan dan opsi jawaban
    call screen quiz(question, choices)

    # Lanjut ke label penanganan jawaban
    jump handle_aceh1

label start_aceh2:
    scene aceh0
    # Pertanyaan
    $ question = "Alat musik tradisional yang populer di Aceh adalah"

    # Opsi Jawaban
    $ choices = ["Serunai", "Gitar", "Biola", "Piano"]

    # Tampilkan pertanyaan dan opsi jawaban
    call screen quiz(question, choices)

    # Lanjut ke label penanganan jawaban
    jump handle_aceh2

label start_aceh3:
    scene aceh0
    # Pertanyaan
    $ question = "Apa nama masjid terkenal di Aceh?"

    # Opsi Jawaban
    $ choices = ["Masjid Istiqlal", "Masjid Raya Baiturrahman", "Masjid Agung Jawa Tengah", "Masjid Nabawi"]

    # Tampilkan pertanyaan dan opsi jawaban
    call screen quiz(question, choices)

    # Lanjut ke label penanganan jawaban
    jump handle_aceh3

label start_aceh4:
    scene aceh0
    # Pertanyaan
    $ question = "Apa yang membuat budaya Aceh begitu istimewa?"

    # Opsi Jawaban
    $ choices = ["Keanekaragaman kuliner", "Seni lukis yang terkenal", "Kekayaan budaya Islam", "Tradisi perburuan yang unik"]

    # Tampilkan pertanyaan dan opsi jawaban
    call screen quiz(question, choices)

    # Lanjut ke label penanganan jawaban
    jump handle_aceh4

label start_aceh5:
    scene aceh0
    # Pertanyaan
    $ question = "Apa yang membuat budaya Aceh begitu istimewa?"

    # Opsi Jawaban
    $ choices = ["Keanekaragaman kuliner", "Seni lukis yang terkenal", "Kekayaan budaya Islam", "Tradisi perburuan yang unik"]

    # Tampilkan pertanyaan dan opsi jawaban
    call screen quiz(question, choices)

    # Lanjut ke label penanganan jawaban
    jump handle_aceh5

screen quiz(question, choices):
    frame:
        background "#FFFFFF88"
        xalign 0.5
        yalign 0.5

    vbox:
        spacing 20
        xalign 0.5
        yalign 0.5

        # Tampilkan pertanyaan
        text question:
            color "#000000"

        for choice in choices:
            # Tampilkan setiap opsi jawaban sebagai tombol
            textbutton choice action [SetVariable("selected_choice", choice), Return()] style "pilihan" text_size 35


label handle_aceh1:
    # Cek jawaban yang dipilih
    if selected_choice == "Gerakan yang serasi dan dinamis":
        $ poinaceh += 25
        jump start_aceh2
    else:
        jump start_aceh2

label handle_aceh2:
    # Cek jawaban yang dipilih
    if selected_choice == "Serunai":
        $ poinaceh += 25
        jump start_aceh3
    else:
        jump start_aceh3

label handle_aceh3:
    # Cek jawaban yang dipilih
    if selected_choice == "Masjid Raya Baiturrahman":
        $ poinaceh += 25
        jump start_aceh4
    else:
        jump start_aceh4

label handle_aceh4:
    # Cek jawaban yang dipilih
    if selected_choice == "Masjid Raya Baiturrahman":
        $ poinaceh += 25
        jump start_aceh5
    else:
        jump start_aceh5

label handle_aceh5:
    # Cek jawaban yang dipilih
    if selected_choice == "Kekayaan budaya Islam":
        $ poinaceh += 25
        jump scoreaceh
    else:
        jump scoreaceh

# aceh Overview
label scoreaceh:
    scene aceh0
    call screen scoreaceh
    return

screen scoreaceh():

    text "Score [poinaceh]" xalign 0.5 yalign 0.5

    imagebutton:
        xalign 0.5
        yalign 0.5
        if poinaceh <= 50:
            idle im.Scale("images/quiz/lumayan.png", 1602, 800)
        elif poinaceh == 75:
            idle im.Scale("images/quiz/bagus.png", 1602, 800)
        elif poinaceh >= 100:
            idle im.Scale("images/quiz/sempurna.png", 1602, 800)

    imagebutton:
        idle im.Scale("images/quiz/next.png", 684, 200)
        xalign 0.8
        yalign 0.9
        action Jump("acehplay2")
        activate_sound klick

    imagebutton:
        idle im.Scale("images/quiz/ulang.png", 684, 200)
        xalign 0.2
        yalign 0.9
        action Jump("start_aceh1")
        activate_sound klick
