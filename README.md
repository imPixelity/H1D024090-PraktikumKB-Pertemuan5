# Sistem Pakar Diagnosa Penyakit THT

Sistem pakar berbasis Python untuk mendiagnosa penyakit THT (Telinga, Hidung, Tenggorokan) menggunakan metode pencocokan gejala.

## Cara Kerja

Program akan mengajukan serangkaian pertanyaan mengenai gejala yang dialami pengguna. Setiap jawaban dikumpulkan lalu dicocokkan dengan basis pengetahuan penyakit. Penyakit ditampilkan sebagai hasil diagnosa apabila tingkat kecocokan gejalanya mencapai minimal 60%.

## Penyakit yang Dapat Dideteksi

- Tonsilitis
- Sinusitis (Maksilaris, Frontalis, Edmoidalis, Sfenoidalis)
- Abses Peritonsiler
- Faringitis
- Kanker Laring
- Deviasi Septum
- Laringitis
- Kanker Leher & Kepala
- Otitis Media Akut
- Contact Ulcers
- Abses Parafaringeal
- Barotitis Media
- Kanker Nasofaring
- Kanker Tonsil
- Neuronitis Vestibularis
- Meniere
- Tumor Syaraf Pendengaran
- Kanker Leher Metastatik
- Osteosklerosis
- Vertigo Postular

## Cara Menjalankan

Pastikan Python 3 sudah terinstall, lalu jalankan:

```
python main.py
```

Jawab setiap pertanyaan gejala dengan `y` (ya) atau `t` (tidak).

## Contoh Output

```
>> Terdeteksi: Tonsilitis (kecocokan: 83.3%)
>> Terdeteksi: Faringitis (kecocokan: 60.0%)
```

## Catatan

Program ini bersifat informatif dan tidak menggantikan diagnosis dari tenaga medis profesional.
