# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define notVisited = False
define counter = 0


# The game starts here.

label start:

    play music "field_of_hopes.ogg"

    scene bg depan_tc
    with dissolve

    "Anda adalah mahasiswa baru yang baru saja masuk ke Teknik Informatika ITS."
    "Anda akan diberikan sebuah quiz yang berisi tentang Teknik Informatika ITS"
    "Sebagai Mahasiswa yang rajin. Anda mengunjungi kampus untuk melihat-lihat."

    show fsm: 
        align (.5, .5) zoom 1
    with dissolve
    pause

    menu:
        "Halaman Depan":
            "Anda menuju ke Halaman Depan."
            jump halaman
        "Keliling Lantai 1":
            "Anda ke Lantai 1."
            jump lantai_1
        "Pulang":
            "Anda Pulang."
            $ notVisited = True
            jump end_sequence

label depan_tc:
    scene bg depan_tc
    with dissolve

    "Anda di Depan Teknik Informatika ITS"

    menu:
        "Halaman Depan":
            "Anda menuju ke Halaman Depan."
            jump halaman
        "Keliling Lantai 1":
            "Anda ke Lantai 1."
            jump lantai_1
        "Pulang":
            "Anda Pulang."
            jump end_sequence

label halaman:
    scene bg yard
    with dissolve

    "Ini adalah halaman depan Informatika"

    menu:
        "Keliling Lantai 1":
            "Kamu Berkeliling di Lantai 1"
            jump lantai_1
        "Depan Infomatika":
            "Anda menu ke Depan Informatika ITS."
            jump depan_tc

label lantai_1:
    scene bg lt1
    with dissolve

    "Ini adalah lantai 1 Informatika"
    
    menu:
        "Lantai 2":
            jump lantai_2
        "Halaman":
            "You chose halaman."
            jump halaman
        "Depan Infomatika":
            "You chose depan Informatika."
            jump depan_tc
        "Pulang":
            "Anda Pulang."
            jump end_sequence

label lantai_2:
    scene bg lt_2
    with dissolve

    menu:
        "Naik Ke Lantai 3":
            jump lantai_3
        "Keliling Lantai 2":
            jump lt2_explore
        "Turun ke Lantai 1":
            scene bg tangga_turun_lt2
            "Anda Turun ke Lantai 1."
            jump lantai_1

label lt2_explore:
    scene bg lt2_1
    with dissolve
    scene bg lt2_2
    with dissolve
    scene bg lt2_3
    with dissolve

    jump lantai_2

label lantai_3:
    scene bg tangga_naik_lt3
    with dissolve

    "Anda naik ke Lantai 3."

    menu:
        "Koridor Utara":
            "Anda ke Koridor Utara."
            jump koridor_utara
        "Koridor Selatan":
            "Anda ke Koridor Selatan."
            jump koridor_selatan
        "Lantai 2":
            scene bg tangga_turun_lt2
            with dissolve
            "Anda Turun ke Lantai 2."
            jump lantai_2

label koridor_utara:
    scene bg lt3_utara
    with dissolve

    "Anda menuju ke Koridor Utara."

    menu:
        "Lihat Lab":
            "Anda melihat-melihat lab."
            jump lab_utara
        "Koridor Selatan":
            "Anda ke Koridor Selatan."
            jump koridor_selatan
        "Lantai 2":
            scene bg tangga_turun_lt2
            with dissolve
            "Anda Turun ke Lantai 2"
            jump lantai_2

label lab_utara:
    scene bg lt3_rpl
    with dissolve

    "Ini adalah Lab Rekayasa Perangkat Lunak."
    "Laboratorium menawarkan bidang minat yang berfokus pada keahlian melakukan 
    pengujian perangkat lunak."

    scene bg lt3_kcv
    with dissolve

    "Ini adalah Lab Komputasi Cerdas dan Visi."
    "Laboratorium menawarkan bidang keahlian yang ditekankan pada kemampuan 
    lulusan dalam memanipulasi dan menganalisis data citra pada berbagai bidang aplikasi"

    scene bg lt3_lp2
    with dissolve

    "Ini adalah Lab Pemrograman 2"

    jump koridor_utara

label koridor_selatan:
    scene bg lt3_selatan
    with dissolve

    "Anda menuju ke Koridor Selatan."

    menu:
        "Lihat Lab":
            "Anda melihat-melihat lab."
            jump lab_selatan
        "Koridor Utara":
            "Anda ke Koridor Utara."
            jump koridor_utara
        "Lantai 2":
            scene bg tangga_turun_lt2
            with dissolve
            "Anda Turun ke Lantai 2"
            jump lantai_2

label lab_selatan:
    scene bg lt3_kbj
    with dissolve

    "Ini adalah Lab Komputasi Berbasis Jaringan"
    "Laboratorium ini menawarkan bidang keahlian yang ditekankan pada Kemampuan 
    lulusan dalam membangun infrastruktur jaringan yang aman,"

    scene bg lt3_giga
    with dissolve

    "Ini adalah lab Grafika, Interaksi, Game dan Analitik."
    "Laboratorium ini di bidang minat ini menawarkan bidang keahlian yang 
    ditekankan pada kemampuan lulusan dalam mendesain, mengembangkan dan 
    mendokumentasikan proses pembuatan game sesuai dengan standar."

    scene bg lt3_ajk
    with dissolve
    "Ini adalah Laboratorium Teknologi Jaringan dan Keamanan Siber Cerdas."
    "Laboratorium ini menawarkan bidang keahlian yang ditekankan pada Kemampuan 
    lulusan dalam membangun berbagai macam arsitektur jaringan sesuai 
    standar teknologi terkini dan menerapkan keamanan jaringan."

    scene bg lt3_lp1
    with dissolve

    "Ini adalah Lab Pemrograman 1"

    scene bg lt3_alpro
    with dissolve

    "Ini adalah Laboratorium Algoritma dan Pemrograman"
    "Laboratorium ini menawarkan bidang keahlian yang ditekankan pada kemampuan 
    lulusan dalam merancang dan menganalisa algoritma"

    scene bg lt3_mci
    with dissolve

    "ini adalah Laboratorium Manajemen Cerdas Informasi"
    "Laboratorium di bidang minat ini menawarkan bidang keahlian yang ditekankan 
    pada kemampuan lulusan dalam menganalisis, mensintesa dan mengevaluasi proses 
    bisnis dan sistem informasi pada sistem Enterprise"

    "Dan disebelahnya adalah Laboratorium Pemodelan dan Komputasi Terapan"
    "Laboratorium ini mewadahi riset dan kerjasama industri di bidang pemodelan 
    & simulasi, peramalan sains, optimasi, serta komputasional saintifik."

    jump koridor_selatan

label end_sequence:
    scene bg black
    with dissolve

    if notVisited == True:
        "Sebelum anda menginjakkan kaki di Informatika, Anda sudah pulang."
        "Sehingga anda tidak tahu jawaban dari quiz yang diberikan."
        "{b}Anda tidak lulus quiz yang diberikan.{/b}"
        return
    else:
        "Ketika anda pulang. Anda langsung mengerjakan quiz yang diberikan."
    
    "Ada berapa Lab Di Teknik Informatika ITS?"

    menu:
        "8":
            $ counter += 1
        "7":
            $ counter += 0
        "10":
            $ counter += 0

    "Pada lantai berapa kelas kelas terdapat?"

    menu:
        "3":
            $ counter += 0
        "1":
            $ counter += 1
        "2":
            $ counter += 0

    "Lab apa yang mendalami dibidang game dan 3D modelling?"

    menu:
        "Lab Rekayasa Perangkat Lunak":
            $ counter += 0
        "Lab Algoritma dan Pemrograman":
            $ counter += 0
        "Lab Grafika, Interaksi, Game dan Analitik":
            $ counter += 1

    "Lab apa yang mendalami dibidang jaringan dan keamanan?"

    menu:
        "Laboratorium Teknologi Jaringan dan Keamanan Siber Cerdas":
            $ counter += 1
        "Laboratorium Manajemen Cerdas Informasi":
            $ counter += 0
        "Laboratorium Pemodelan dan Komputasi Terapan":
            $ counter += 0

    "Apa nama plaza yang ada di Teknik Informatika ITS?"

    menu:
        "Plaza Prof Supeno Djanali":
            $ counter += 1
        "Plaza Informatika":
            $ counter += 0
        "Plaza Djikstra":
            $ counter += 0

    if counter >= 3:
        "Selamat Anda Lulus Quiz yang diberikan."
        "Anda mendapatkan nilai [counter] dari 5."
    else:
        "Maaf Anda tidak lulus quiz yang diberikan."
        "Anda mendapatkan nilai [counter] dari 5."

    "Game ini dibuat oleh\nMuhammad Ariandra Dwiratama - 5025221010\nAbyan Bismar Alfayed - 5025221026"

    return