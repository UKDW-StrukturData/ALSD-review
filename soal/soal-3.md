# Soal 03 — Perulangan & Fungsi

## Tujuan
Melatih penggunaan perulangan (`for`, `while`) dan pembuatan fungsi (`def`) di Python.

## Soal
Buatlah program Python yang:

1. Membuat fungsi `hitung_rata2(list_nilai)` yang:
Menerima parameter berupa `list` berisi nilai-nilai mahasiswa.
   - Menggunaka   - n perulangan `for` untuk mencetak setiap nilai dalam list.
   - Mengembalikan (`return`) nilai rata-rata dari semua nilai dalam list.
2. Memanggil fungsi tersebut dengan data contoh, misalnya:
   ```python
   nilai_mhs = [80, 75, 90, 65, 88]
   ```
3. Menampilkan nilai rata-rata yang dikembalikan fungsi.
4.  Modifikasi fungsi agar nilai yang **kurang dari 0 dan lebih dari 100** (data tidak valid) dilewati menggunakan `continue`, dan tidak dihitung dalam rata-rata.
   - Tambahkan `break` pada skenario: hentikan pencetakan nilai jika ditemukan nilai `-1` (dianggap sebagai tanda akhir data).

## Contoh Output
```
Nilai ke-1: 80
Nilai ke-2: 75
Nilai ke-3: 90
Nilai ke-4: 65
Nilai ke-5: 88
Rata-rata: 79.6
```
