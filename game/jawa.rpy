# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bgjogja  = "images/jogja/bgjogja.png"
image awaljogja = "images/jogja/awal-jogja.png"
image jogja1 = "images/jogja/1.png"
image jogja1 = "images/jogja/1.png"
image jogja2 = "images/jogja/2.png"
image jogja3 = "images/jogja/3.png"
image jogja4 = "images/jogja/4.png"
image jogja5 = "images/jogja/5.png"
image jogja6 = "images/jogja/6.png"
image jogja7 = "images/jogja/7.png"
image jogja8 = "images/jogja/8.png"
image jogja9 = "images/jogja/9.png"

# Deklarasikan karakter yang digunakan di game.
define a = Character('Rayeh', color="#FFFAD7")
define b = Character('Pak Slamet', color="#FFFAD7")

# Game dimulai disini.
label jogjaplay:

    scene awaljogja
    "Sang anak muda tiba di Kota Jogja dengan harapan dapat mencari informasi tentang orang tuanya di sini."
    "Sambil berjalan-jalan di sekitar, anak muda itu melihat beberapa tempat yang menarik. Dia melewati Malioboro, jalan utama yang terkenal dengan toko-toko, pedagang kaki lima, dan keramaian wisatawan. dia bertemu seorang pria bernama Pak Slamet"

    scene jogja1
    a "Permisi pak, saya ada di daerah mana ya?"

    scene jogja5
    b "Sampeyan sekarang di daerah malioboro mas"

    scene jogja3
    a "Oh begitu pak? Mengapa Jogja disebut daerah istimewa? Apa yang membuatnya begitu istimewa?"

    scene jogja4
    b "Jogja disebut daerah istimewa karena memiliki status khusus di Indonesia."

    scene jogja5
    a "Jadi begitu pak,"

    scene jogja6
    b "Iya mas, Status istimewa ini diberikan karena Jogja memiliki tradisi dan kebudayaan yang sangat kaya serta memiliki hubungan historis dengan Kerajaan Mataram Islam."

    scene jogja7
    a "Apa yang membuat Jogja begitu istimewa dari segi budaya, Pak?"

    scene jogja8
    b "Budaya Jogja sangat kental dan terasa dalam setiap aspek kehidupan masyarakatnya. Jogja dikenal dengan kearifan lokal, seni, dan tradisi yang masih dijaga dengan baik."

    scene jogja9
    a "Itu sangat menarik, Pak. Bagaimana dengan pariwisata di Jogja?"

    scene jogja3
    b "Pariwisata di Jogja juga menjadi salah satu daya tarik utama. Jogja memiliki banyak destinasi wisata yang menarik, seperti Candi Prambanan, Candi Borobudur, Pantai Parangtritis, Taman Sari, dan masih banyak lagi."

    scene jogja1
    a "Terima kasih banyak, Pak Slamet, atas penjelasannya. Saya semakin tertarik untuk menjelajahi Jogja dan menikmati keindahan dan keistimewaannya."

    scene jogja4
    b "Sama sama mas, tetapi sebelum itu bantu saya menyelesaikan teka teki kartu ini, saya kebingungan untuk menyelesaikannya."

    scene jogja3
    a "tentu saja pak"
    jump minigame_memory

label jogjaplay2:
    scene jogja6
    "Terimakasih mas telah membantu saya menyelesaikan teka teki kartu ini, siapa namamu mas?"
    scene jogja8
    "Nama saya Rayeh pak"
    scene jogja3
    "Terimakasih bantuannya mas Rayeh. Semoga Anda menikmati waktu Anda di Jogja dan dapat mengalami keunikan serta keindahan budaya yang ada di sini. Selamat menjelajah!"
    $ persistent.stage = 4
    jump stage
# label start_jogja1:
#     scene bgjogja
#     # Pertanyaan
#     $ question = "Apa yang membuat pantai Kuta di jogja terkenal?"
#
#     # Opsi jogjaban
#     $ choices = ["Pasir putih", " Air tawar", "Batu-batuan", "Salju"]
#
#     # Tampilkan pertanyaan dan opsi jogjaban
#     call screen quiz(question, choices)
#
#     # Lanjut ke label penanganan jogjaban
#     jump handle_jogja1
#
# label start_jogja2:
#     scene bgjogja
#     # Pertanyaan
#     $ question = "Apa tujuan dari Upacara Melasti di jogja?"
#
#     # Opsi jogjaban
#     $ choices = ["Membersihkan rohani", "Memancing ikan", "Merayakan ulang tahun", "Menggambar seni"]
#
#     # Tampilkan pertanyaan dan opsi jogjaban
#     call screen quiz(question, choices)
#
#     # Lanjut ke label penanganan jogjaban
#     jump handle_jogja2
#
# label start_jogja3:
#     scene bgjogja
#     # Pertanyaan
#     $ question = "Di mana biasanya dilakukan Upacara Melasti? "
#
#     # Opsi jogjaban
#     $ choices = ["Di pantai", "Di taman bermain", "Di sekolah", "Di pusat perbelanjaan"]
#
#     # Tampilkan pertanyaan dan opsi jogjaban
#     call screen quiz(question, choices)
#
#     # Lanjut ke label penanganan jogjaban
#     jump handle_jogja3
#
# label start_jogja4:
#     scene bgjogja
#     # Pertanyaan
#     $ question = "Apa yang membuat budaya jogja terkenal? "
#
#     # Opsi jogjaban
#     $ choices = ["Makanan lezat", "Tarian tradisional", "Musik rock", "Pakaian modern"]
#
#     # Tampilkan pertanyaan dan opsi jogjaban
#     call screen quiz(question, choices)
#
#     # Lanjut ke label penanganan jogjaban
#     jump handle_jogja4
#
# label start_jogja5:
#     scene bgjogja
#     # Pertanyaan
#     $ question = "Apa yang dilakukan dalam Upacara Melasti di jogja?"
#
#     # Opsi jogjaban
#     $ choices = ["Membaca buku", "Bermain sepak bola", "Menari ballet", "Membersihkan patung-patung "]
#
#     # Tampilkan pertanyaan dan opsi jogjaban
#     call screen quiz(question, choices)
#
#     # Lanjut ke label penanganan jogjaban
#     jump handle_jogja5
#
#
# screen quiz(question, choices):
#     frame:
#         background "#FFFFFF88"
#         xalign 0.5
#         yalign 0.5
#
#     vbox:
#         spacing 20
#         xalign 0.5
#         yalign 0.5
#
#         # Tampilkan pertanyaan
#         text question:
#             color "#000000"
#
#         for choice in choices:
#             # Tampilkan setiap opsi jogjaban sebagai tombol
#             textbutton choice action [SetVariable("selected_jogja", choice), Return()]
#
#
# label handle_jogja1:
#     # Cek jogjaban yang dipilih
#     if selected_jogja == "Sayuran dengan saus kacang":
#         $ poinjogja += 20
#         jump start_jogja2
#     else:
#         jump start_jogja2
#
# label handle_jogja2:
#     # Cek jogjaban yang dipilih
#     if selected_jogja == "jogja":
#         $ poinjogja += 20
#         jump start_jogja3
#     else:
#         jump start_jogja3
#
# label handle_jogja3:
#     # Cek jogjaban yang dipilih
#     if selected_jogja == "A'a":
#         $ poinjogja += 20
#         jump start_jogja4
#     else:
#         jump start_jogja4
#
# label handle_jogja4:
#     # Cek jogjaban yang dipilih
#     if selected_jogja == "Sunda":
#         $ poinjogja += 20
#         jump start_jogja5
#     else:
#         jump start_jogja5
#
# label handle_jogja5:
#     # Cek jogjaban yang dipilih
#     if selected_jogja == "A'a":
#         $ poinjogja += 20
#         jump scorejogja
#     else:
#         jump scorejogja
#
# # jogja Overview
# label scorejogja:
#     scene bgjogja
#     call screen scorejogja
#
# screen scorejogja():
#
#     imagebutton:
#         xalign 0.5
#         yalign 0.5
#         if poinjogja <= 30:
#             idle im.Scale("images/quiz/lumayan.png", 1602, 800)
#         if poinjogja == 60:
#             idle im.Scale("images/quiz/bagus.png", 1602, 800)
#         if poinjogja >= 80:
#             idle im.Scale("images/quiz/sempurna.png", 1602, 800)
#
#     imagebutton:
#         idle im.Scale("images/quiz/next.png", 684, 200)
#         xalign 0.8
#         yalign 0.9
#         action Jump("jogjaplay2")
#         activate_sound klick
#
#     imagebutton:
#         idle im.Scale("images/quiz/ulang.png", 684, 200)
#         xalign 0.2
#         yalign 0.9
#         action Jump("start_jogja1")
#         activate_sound klick
