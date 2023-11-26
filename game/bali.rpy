# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bali0 = im.Scale("images/bali/pembuka.png", 1920, 1080)
image bali1 = im.Scale("images/bali/1.png", 1920, 1080)
image bali2 = im.Scale("images/bali/2.png", 1920, 1080)
image bali3 = im.Scale("images/bali/3.png", 1920, 1080)
image bali4 = im.Scale("images/bali/4.png", 1920, 1080)
image bali5 = im.Scale("images/bali/5.png", 1920, 1080)
image bali6 = im.Scale("images/bali/6.png", 1920, 1080)
image bali7 = im.Scale("images/bali/7.png", 1920, 1080)
image bali8 = im.Scale("images/bali/8.png", 1920, 1080)
image bali9 = im.Scale("images/bali/9.png", 1920, 1080)
image bgbali = im.Scale("images/bali/bg.png", 1920, 1080)

style pilihan:
    color "#EAB2A0"
    hover_color "#000000"
    background "#435B66"

# Deklarasikan karakter yang digunakan di game.
$ selected_choice = None
default poinbali = 0
define f = Character('Made Bagus', color="#FFFAD7")

# Game dimulai disini.
label baliplay:

    scene bali0
    "Rayeh tiba di pantai Kuta dengan pemandangan yang menakjubkan. Pasir putih yang lembut, ombak yang menggulung, dan langit yang cerah menciptakan suasana yang memikat. Dia merasa gembira karena telah sampai ke salah satu pantai paling terkenal di Bali."

    scene bali1
    a "Wow, pantai ini benar-benar indah! Pasir putih, ombak yang memukau, dan langit biru yang cerah. Sungguh luar biasa!"

    scene bali2
    f "Ya, betul sekali! Kuta Beach memang salah satu pantai yang terkenal di Bali. Terutama saat matahari terbenam, pemandangannya luar biasa romantis!"

    scene bali3
    a "Saya benar-benar terkesan dengan kekayaan budaya Bali."

    scene bali4
    f "Tentu saja! Bali sangat kaya akan tradisi dan budaya."

    scene bali5
    a "Itu akan sangat membantu! Saya ingin mengenal lebih dalam tentang tradisi dan kehidupan spiritual di Bali. "

    scene bali6
    f "Ya, benar sekali. Budaya Bali sangat unik dan kaya. Bali dikenal dengan tradisi dan upacara adatnya yang masih dijalankan hingga saat ini. Salah satu contohnya adalah upacara keagamaan seperti Upacara Melasti, Galungan, dan Nyepi."

    scene bali7
    a "Upacara tersebut pasti sangat menarik. Bisakah Anda memberi tahu saya lebih lanjut tentang Upacara Melasti?"

    scene bali8
    f "Tentu! Upacara Melasti adalah upacara pembersihan rohani yang dilakukan oleh umat Hindu Bali. Upacara ini biasanya dilakukan di pantai atau sumber air suci."

    scene bali3
    a "Bagaimana prosesinya dilakukan?"

    scene bali9
    f "Prosesi dimulai dengan para pemangku adat dan umat Hindu membawa patung-patung dan artefak suci menuju lokasi pembersihan. Mereka melakukan sembahyang (doa) dan membaca mantra selama upacara berlangsung."

    scene bali9
    f "Setelah itu, patung dan artefak akan dicuci dengan air laut atau air suci, yang dipercaya dapat membersihkan dan memurnikan energi negatif."

    scene bali3
    a "Terima kasih banyak atas penjelasannya, Made Bagus. Saya semakin bersemangat untuk menjelajahi kekayaan budaya dan tradisi Bali."

    scene bali4
    f "Sama-sama, Rayeh. Selamat menjelajahi keindahan Bali dan semoga Anda dapat merasakan kedamaian dan kekuatan spiritual yang khas dari pulau ini."

    scene bali3
    a "Made, sebenarnya ada hal lain yang ingin saya tanyakan. Saya datang ke Bali dengan harapan dapat mencari petunjuk tentang keberadaan orang tua saya."

    scene bali8
    f "Tentu, Rayeh. Saya akan membantu Anda. Untuk memulai pencarian ini, ada sesuatu yang bisa Anda lakukan."
    f "Di pantai-pantai Bali, terutama yang terpencil, sering kali terdapat objek-objek yang dianggap memiliki kekuatan mistis atau memiliki keterkaitan dengan cerita-cerita legendaris."
    f "Jika Anda dapat membantu saya mencari objek-objek tersebut, mungkin kita bisa menemukan petunjuk yang berguna."

    scene bali9
    a "Tentu, saya akan membantu dengan senang hati. Apa yang harus saya cari?"

    jump start_bali1

label baliplay2:

    scene bali6
    f "Terimakasih sudah membantuku menemukan objek objek ini di pantai, aku akan memberikan sesuatu untukmu"

    scene bali7
    a "Terima kasih banyak, Made Bagus. Saya sangat berterima kasih atas bantuannya selama ini. Saya tidak sabar untuk melanjutkan pencarian ini dan melacak jejak orang tua saya."

    scene bali9
    "sama-sama, Rayeh. Saya senang bisa membantu. Semoga pencarianmu berhasil dan kamu mendapatkan jawaban yang kamu cari."
    $ persistent.stage = 5
    jump stage

label start_bali1:
    $ poinbali = 0
    scene bgbali
    # Pertanyaan
    $ question = "Apa yang membuat pantai Kuta di Bali terkenal?"

    # Opsi Jawaban
    $ choices = ["Pasir putih", " Air tawar", "Batu-batuan", "Salju"]

    # Tampilkan pertanyaan dan opsi jawaban
    call screen quiz(question, choices)

    # Lanjut ke label penanganan jawaban
    jump handle_bali1

label start_bali2:
    scene bgbali
    # Pertanyaan
    $ question = "Apa tujuan dari Upacara Melasti di Bali?"

    # Opsi Jawaban
    $ choices = ["Membersihkan rohani", "Memancing ikan", "Merayakan ulang tahun", "Menggambar seni"]

    # Tampilkan pertanyaan dan opsi jawaban
    call screen quiz(question, choices)

    # Lanjut ke label penanganan jawaban
    jump handle_bali2

label start_bali3:
    scene bgbali
    # Pertanyaan
    $ question = "Di mana biasanya dilakukan Upacara Melasti? "

    # Opsi Jawaban
    $ choices = ["Di pantai", "Di taman bermain", "Di sekolah", "Di pusat perbelanjaan"]

    # Tampilkan pertanyaan dan opsi jawaban
    call screen quiz(question, choices)

    # Lanjut ke label penanganan jawaban
    jump handle_bali3

label start_bali4:
    scene bgbali
    # Pertanyaan
    $ question = "Apa yang membuat budaya Bali terkenal? "

    # Opsi Jawaban
    $ choices = ["Makanan lezat", "Tarian tradisional", "Musik rock", "Pakaian modern"]

    # Tampilkan pertanyaan dan opsi jawaban
    call screen quiz(question, choices)

    # Lanjut ke label penanganan jawaban
    jump handle_bali4

label start_bali5:
    scene bgbali
    # Pertanyaan
    $ question = "Apa yang dilakukan dalam Upacara Melasti di Bali?"

    # Opsi Jawaban
    $ choices = ["Membaca buku", "Bermain sepak bola", "Menari ballet", "Membersihkan patung-patung"]

    # Tampilkan pertanyaan dan opsi jawaban
    call screen quiz(question, choices)

    # Lanjut ke label penanganan jawaban
    jump handle_bali5


screen quiz(question, choices):
    # frame:
    #     background "#FFFFFF88"
    #     xalign 0.5
    #     yalign 0.5

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


label handle_bali1:
    # Cek jawaban yang dipilih
    if selected_choice == "Pasir putih":
        $ poinbali += 20
        jump start_bali2
    else:
        jump start_bali2

label handle_bali2:
    # Cek jawaban yang dipilih
    if selected_choice == "Membersihkan rohani":
        $ poinbali += 20
        jump start_bali3
    else:
        jump start_bali3

label handle_bali3:
    # Cek jawaban yang dipilih
    if selected_choice == "Di pantai":
        $ poinbali += 20
        jump start_bali4
    else:
        jump start_bali4

label handle_bali4:
    # Cek jawaban yang dipilih
    if selected_choice == "Tarian tradisional":
        $ poinbali += 20
        jump start_bali5
    else:
        jump start_bali5

label handle_bali5:
    # Cek jawaban yang dipilih
    if selected_choice == "Membersihkan patung-patung":
        $ poinbali += 20
        jump scorebali
    else:
        jump scorebali

# bali Overview
label scorebali:
    scene bgbali
    call screen scorebali
    return

screen scorebali():

    text "Score [poinbali]" xalign 0.5 yalign 0.5

    imagebutton:
        xalign 0.5
        yalign 0.5
        if poinbali <= 30:
            idle im.Scale("images/quiz/lumayan.png", 1602, 800)
        elif poinbali == 60:
            idle im.Scale("images/quiz/bagus.png", 1602, 800)
        elif poinbali >= 80:
            idle im.Scale("images/quiz/sempurna.png", 1602, 800)

    imagebutton:
        idle im.Scale("images/quiz/next.png", 684, 200)
        xalign 0.8
        yalign 0.9
        action Jump("baliplay2")
        activate_sound klick

    imagebutton:
        idle im.Scale("images/quiz/ulang.png", 684, 200)
        xalign 0.2
        yalign 0.9
        action Jump("start_bali1")
        activate_sound klick
