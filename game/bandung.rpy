# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bandung0 = im.Scale("images/bandung/0.png", 1920, 1080)
image bandung1 = im.Scale("images/bandung/1.png", 1920, 1080)
image bandung2 = im.Scale("images/bandung/2.png", 1920, 1080)
image bandung3 = im.Scale("images/bandung/3.png", 1920, 1080)
image bandung4 = im.Scale("images/bandung/4.png", 1920, 1080)
image bandung5 = im.Scale("images/bandung/5.png", 1920, 1080)
image bandung6 = im.Scale("images/bandung/6.png", 1920, 1080)
image bandung7 = im.Scale("images/bandung/7.png", 1920, 1080)
image bandung8 = im.Scale("images/bandung/8.png", 1920, 1080)
image bandung9 = im.Scale("images/bandung/9.png", 1920, 1080)
image bandung10 = im.Scale("images/bandung/10.png", 1920, 1080)
image bandung11 = im.Scale("images/bandung/11.png", 1920, 1080)

init:
    define benar = "audio/benar.mp3"
    define salah = "audio/salah.mp3"
    define bintang1 = "audio/bintang 1.mp3"
    define bintang2 = "audio/bintang 2.mp3"
    define bintang3 = "audio/bintang 3.mp3"

style pilihan:
    color "#EAB2A0"
    hover_color "#000000"
    background "#435B66"

# Deklarasikan karakter yang digunakan di game.
$ selected_choice = None
default poinbandung = 0
define c = Character('kang Asep', color="#FFFAD7")

# Game dimulai disini.s
label bandungplay:

    scene bandung0
    "Setelah mendapatkan informasi sang anak muda pun sampai di kota bandung, namun langkah sang anak pun terhenti karena melihat keindahan dari kota bandung itu sendiri,"
    scene bandung11
    "ia berjalan melihat-lihat kota bandung tak lama berselang ia melihat ada keramaian di alun-alun kota dengan rasa penasaran ia pun ingin melihatnya, sang anak pun bertanya kepada warga sekitar"
    scene bandung1
    a "Punten aa, ini lagi ada acara apa yah aa?"
    scene bandung2
    c "Iya aa, ini teh lagi ada Festival Kuliner Bandung. festival makanan ini  bertujuan untuk memperkenalkan makanan khas jawa barat atau sunda, khusunya bandung. "
    scene bandung3
    c "makanan khas bandung pun beragam, contohnya seblak, lotek, batagor, cilok, cimol, colenak dan masih ada beberapa lagi. Anda bisa menikmati beragam hidangan lezat dan menarik di sini!"
    scene bandung4
    a "ohh saya begitu tertarik! kalau saya boleh tau, lotek itu makanan seperti apa ya?"
    scene bandung5
    c "lotek itu salad berbahan dasar sayuran dengan saus kacang. Meskipun bahan sausnya sama dengan pecel, saus lotek biasanya lebih manis rasanya."
    scene bandung6
    a "Wah, Saya sangat tertarik untuk mencoba makanan khas Bandung. Di mana lokasinya?"
    scene bandung7
    c "Lokasinya ada di alun-alun kota, aa. Anda bisa melihat berbagai stan yang menjajakan makanan tradisional dan kuliner khas Bandung."
    scene bandung8
    a "Terima kasih banyak, aa."
    scene bandung9
    c "Sama sama, tapi sebelumnya apakah kamu bisa membantuku menyelesaikan teka teki ini ?"
    scene bandung10
    a "Baik aa"

    jump start_quiz1
    return

label bandungplay2:
    scene bandung0
    "Dan anak muda pun mencari petunjuk untuk mencari informasi mengenai keberadaan orang tuanya, namun pencariannya belum mendapatkan titik terang, setelah itu sang anak muda pun melanjutkan pencarian ke kota selanjutnya berdasarkan dari informasi yang ia dapatkan"
    $ persistent.stage = 3
    jump stage

label start_quiz1:
    $ poinbandung = 0
    scene bandung0
    # Pertanyaan
    $ question = "Dari beberapa makanan khas bandung tadi, apa bahan dasar dari lotek?"

    # Opsi Jawaban
    $ choices = ["Daging-dagingan", "Sayuran dengan saus kacang", "Sayuran dengan mayonaise", "Buah dengan saus kacang"]

    # Tampilkan pertanyaan dan opsi jawaban
    call screen quiz(question, choices)

    # Lanjut ke label penanganan jawaban
    jump handle_answer1

label start_quiz2:
    scene bandung0
    # Pertanyaan
    $ question = "Kota apa yang Raden Rayeh pertama kali kunjungi untuk mencari orangtuanya?"

    # Opsi Jawaban
    $ choices = ["Cirebon", "Balikpapan", "Surabaya", "Bandung"]

    # Tampilkan pertanyaan dan opsi jawaban
    call screen quiz(question, choices)

    # Lanjut ke label penanganan jawaban
    jump handle_answer2

label start_quiz3:
    scene bandung0
    # Pertanyaan
    $ question = " Apa panggilan yang Raden Rayeh berikan saat berbicara dengan warga Bandung?"

    # Opsi Jawaban
    $ choices = ["Mas", "kakak", "aa", "Bli"]

    # Tampilkan pertanyaan dan opsi jawaban
    call screen quiz(question, choices)

    # Lanjut ke label penanganan jawaban
    jump handle_answer3

label start_quiz4:
    scene bandung0
    # Pertanyaan
    $ question = "Festival makanan tersebut dilaksanakan untuk tujuan memperkenalkan makanan dari?"

    # Opsi Jawaban
    $ choices = ["Sunda", "Jakarta", "Padang", "Papua"]

    # Tampilkan pertanyaan dan opsi jawaban
    call screen quiz(question, choices)

    # Lanjut ke label penanganan jawaban
    jump handle_answer4

label start_quiz5:
    scene bandung0
    # Pertanyaan
    $ question = " Dimana letak festival kuliner tersebut dilaksanakan??"

    # Opsi Jawaban
    $ choices = ["Trans Studio Bandung", "Braga City Walk", "Lembang Park Zoo", "Alun alun Kota"]

    # Tampilkan pertanyaan dan opsi jawaban
    call screen quiz(question, choices)

    # Lanjut ke label penanganan jawaban
    jump handle_answer5


screen quiz(question, choices):
    frame:
        background "#FFFFFF99"
        xalign 0.5
        yalign 0.5

    vbox:
        spacing 20
        xalign 0.5
        yalign 0.5

        # Tampilkan pertanyaan
        text question:
            color "#000000"
            size 35

        for choice in choices:
            # Tampilkan setiap opsi jawaban sebagai tombol
            textbutton choice action [SetVariable("selected_choice", choice), Return()] style "pilihan" text_size 35


label handle_answer1:
    # Cek jawaban yang dipilih
    if selected_choice == "Sayuran dengan saus kacang":
        $ poinbandung += 20
        play sound benar
        jump start_quiz2
    else:
        play sound salah
        jump start_quiz2

label handle_answer2:
    # Cek jawaban yang dipilih
    if selected_choice == "Bandung":
        $ poinbandung += 20
        play sound benar
        jump start_quiz3
    else:
        play sound salah
        jump start_quiz3

label handle_answer3:
    # Cek jawaban yang dipilih
    if selected_choice == "aa":
        $ poinbandung += 20
        play sound benar
        jump start_quiz4
    else:
        play sound salah
        jump start_quiz4

label handle_answer4:
    # Cek jawaban yang dipilih
    if selected_choice == "Sunda":
        $ poinbandung += 20
        play sound benar
        jump start_quiz5
    else:
        play sound salah
        jump start_quiz5

label handle_answer5:
    # Cek jawaban yang dipilih
    if selected_choice == "Alun alun Kota":
        $ poinbandung += 20
        play sound benar
        jump handle_lagubandung
    else:
        play sound salah
        jump handle_lagubandung

label handle_lagubandung:
        if poinbandung <= 40:
            play sound bintang1
        elif poinbandung == 60:
            play sound bintang2
        elif poinbandung >= 80:
            play sound bintang3
        jump scorebandung



# Bandung Overview
label scorebandung:
    scene bandung0
    call screen scorebandung

screen scorebandung():

    text "Score [poinbandung]" xalign 0.5 yalign 0.5

    imagebutton:
        xalign 0.5
        yalign 0.5
        if poinbandung <= 40:
            idle im.Scale("images/quiz/lumayan.png", 1602, 800)
        elif poinbandung == 60:
            idle im.Scale("images/quiz/bagus.png", 1602, 800)
        elif poinbandung >= 80:
            idle im.Scale("images/quiz/sempurna.png", 1602, 800)

    imagebutton:
        idle im.Scale("images/quiz/next.png", 684, 200)
        xalign 0.8
        yalign 0.9
        action Jump("bandungplay2")
        activate_sound klick

    imagebutton:
        idle im.Scale("images/quiz/ulang.png", 684, 200)
        xalign 0.2
        yalign 0.9
        action Jump("start_quiz1")
        activate_sound klick
