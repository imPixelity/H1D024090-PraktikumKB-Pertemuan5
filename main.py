rules_penyakit = {
    "Tonsilitis": {
        "gejala": {"G37", "G12", "G5", "G27", "G6", "G21"},
    },
    "Sinusitis Maksilaris": {
        "gejala": {"G37", "G12", "G27", "G17", "G33", "G36", "G29"},
    },
    "Sinusitis Frontalis": {
        "gejala": {"G37", "G12", "G27", "G17", "G33", "G36", "G21", "G26"},
    },
    "Sinusitis Edmoidalis": {
        "gejala": {
            "G37",
            "G12",
            "G27",
            "G17",
            "G33",
            "G36",
            "G21",
            "G30",
            "G13",
            "G26",
        },
    },
    "Sinusitis Sfenoidalis": {
        "gejala": {"G37", "G12", "G27", "G17", "G33", "G36", "G29", "G7"},
    },
    "Abses Peritonsiler": {
        "gejala": {"G37", "G12", "G6", "G15", "G2", "G29", "G10"},
    },
    "Faringitis": {
        "gejala": {"G37", "G5", "G6", "G7", "G15"},
    },
    "Kanker Laring": {
        "gejala": {"G5", "G27", "G6", "G15", "G2", "G19", "G1"},
    },
    "Deviasi Septum": {
        "gejala": {"G37", "G17", "G20", "G8", "G18", "G25"},
    },
    "Laringitis": {
        "gejala": {"G37", "G5", "G15", "G16", "G32"},
    },
    "Kanker Leher & Kepala": {
        "gejala": {"G5", "G22", "G8", "G28", "G3", "G11"},
    },
    "Otitis Media Akut": {
        "gejala": {"G37", "G20", "G35", "G31"},
    },
    "Contact Ulcers": {
        "gejala": {"G5", "G2"},
    },
    "Abses Parafaringeal": {
        "gejala": {"G5", "G16"},
    },
    "Barotitis Media": {
        "gejala": {"G12", "G20"},
    },
    "Kanker Nasofaring": {
        "gejala": {"G17", "G8"},
    },
    "Kanker Tonsil": {
        "gejala": {"G6", "G29"},
    },
    "Neuronitis Vestibularis": {
        "gejala": {"G35", "G24"},
    },
    "Meniere": {
        "gejala": {"G20", "G35", "G14", "G4"},
    },
    "Tumor Syaraf Pendengaran": {
        "gejala": {"G12", "G34", "G23"},
    },
    "Kanker Leher Metastatik": {
        "gejala": {"G29"},
    },
    "Osteosklerosis": {
        "gejala": {"G34", "G9"},
    },
    "Vertigo Postular": {
        "gejala": {"G24"},
    },
}

daftar_gejala = {
    "G1": "Nafas abnormal",
    "G2": "Suara serak",
    "G3": "Perubahan kulit",
    "G4": "Telinga penuh",
    "G5": "Nyeri bicara menelan",
    "G6": "Nyeri tenggorokan",
    "G7": "Nyeri leher",
    "G8": "Pendarahan hidung",
    "G9": "Telinga berdenging",
    "G10": "Air liur menetes",
    "G11": "Perubahan suara",
    "G12": "Sakit kepala",
    "G13": "Nyeri pinggir hidung",
    "G14": "Serangan vertigo",
    "G15": "Getah bening",
    "G16": "Leher bengkak",
    "G17": "Hidung tersumbat",
    "G18": "Infeksi sinus",
    "G19": "Berat badan turun",
    "G20": "Nyeri telinga",
    "G21": "Selaput lendir merah",
    "G22": "Benjolan leher",
    "G23": "Tubuh tak seimbang",
    "G24": "Bola mata bergerak",
    "G25": "Nyeri wajah",
    "G26": "Dahi sakit",
    "G27": "Batuk",
    "G28": "Tumbuh di mulut",
    "G29": "Benjolan di leher",
    "G30": "Nyeri antara mata",
    "G31": "Radang gendang telinga",
    "G32": "Tenggorokan gatal",
    "G33": "Hidung meler",
    "G34": "Tuli",
    "G35": "Mual muntah",
    "G36": "Letih lesu",
    "G37": "Demam",
}

gejala_pasien = []


def tanya_gejala(kode_gejala):
    nama_gejala = daftar_gejala[kode_gejala]
    jawaban = input(f"Apakah Anda mengalami '{nama_gejala}'? (y/t): ").strip().lower()
    if jawaban == "y":
        gejala_pasien.append(kode_gejala)


def jalankan_diagnosa():
    print("\n--- Hasil Diagnosa Sistem ---")
    terdeteksi = False

    hasil = []
    for penyakit, data in rules_penyakit.items():
        gejala_syarat = data["gejala"]
        gejala_cocok = gejala_syarat.intersection(set(gejala_pasien))
        if len(gejala_cocok) > 0:
            skor = len(gejala_cocok) / len(gejala_syarat) * 100
            if skor >= 60:
                hasil.append((penyakit, skor))
                terdeteksi = True

    hasil.sort(key=lambda x: x[1], reverse=True)

    if terdeteksi:
        for penyakit, skor in hasil:
            print(f">> Terdeteksi: {penyakit} (kecocokan: {skor:.1f}%)")
    else:
        print(">> Tidak terdeteksi penyakit berdasarkan gejala yang Anda masukkan.")


def main():
    print("=== SISTEM PAKAR DIAGNOSA PENYAKIT THT ===")
    print("Jawablah pertanyaan berikut dengan 'y' untuk Ya atau 't' untuk Tidak.\n")

    print("[ GEJALA UMUM ]")
    tanya_gejala("G37")
    tanya_gejala("G36")
    tanya_gejala("G19")

    print("\n[ GEJALA KEPALA & WAJAH ]")
    tanya_gejala("G12")
    tanya_gejala("G25")
    tanya_gejala("G26")
    tanya_gejala("G30")

    print("\n[ GEJALA HIDUNG ]")
    tanya_gejala("G17")
    tanya_gejala("G33")
    tanya_gejala("G8")
    tanya_gejala("G13")
    tanya_gejala("G18")

    print("\n[ GEJALA TENGGOROKAN & MULUT ]")
    tanya_gejala("G6")
    tanya_gejala("G5")
    tanya_gejala("G27")
    tanya_gejala("G32")
    tanya_gejala("G10")
    tanya_gejala("G21")
    tanya_gejala("G28")

    print("\n[ GEJALA SUARA & PERNAFASAN ]")
    tanya_gejala("G2")
    tanya_gejala("G11")
    tanya_gejala("G1")

    print("\n[ GEJALA LEHER ]")
    tanya_gejala("G7")
    tanya_gejala("G16")
    tanya_gejala("G15")
    tanya_gejala("G22")
    tanya_gejala("G29")
    tanya_gejala("G3")

    print("\n[ GEJALA TELINGA ]")
    tanya_gejala("G20")
    tanya_gejala("G4")
    tanya_gejala("G9")
    tanya_gejala("G34")
    tanya_gejala("G31")

    print("\n[ GEJALA KESEIMBANGAN ]")
    tanya_gejala("G14")
    tanya_gejala("G23")
    tanya_gejala("G24")
    tanya_gejala("G35")

    jalankan_diagnosa()


main()
