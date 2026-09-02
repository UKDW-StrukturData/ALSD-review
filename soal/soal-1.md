# Soal 01 — Variabel & Tipe Data

## Tujuan
Melatih penggunaan variabel dan pemahaman tipe data dasar Python (`int`, `float`, `str`, `bool`).

## Soal
Buatlah program Python yang:

1. Mendeklarasikan variabel berikut:
   - `nama` (nama mahasiswa, tipe `str`)
   - `nilai_tugas` (tipe `int` atau `float`)
   - `nilai_uts` (tipe `int` atau `float`)
   - `nilai_uas` (tipe `int` atau `float`)
2. Menghitung `nilai_akhir` dengan bobot:
   - Tugas 30%, UTS 30%, UAS 40%
3. Menampilkan nama, nilai_akhir, dan **tipe data** dari 2 variabel diatas.
HINT: 
'''
   print(f"| {'Nama':11} :", nama, type(nama))
   print(f"| {'Nilai Akhir':12}: {nilai_akhir:.2f}", type(nilai_akhir))
'''

## Contoh Output
```
| Nama        : Anton <class 'str'>
| Nilai Akhir : 100.00 <class 'float'>
```

## Kriteria Penilaian
| Kriteria | Bobot |
|---|---|
| Variabel & perhitungan benar | 40% |
| Tipe data ditampilkan | 30% |
| Penamaan variabel tidak asal | 20% |
| Commit message jelas | 10% |