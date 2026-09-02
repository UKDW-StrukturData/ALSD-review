# Praktikum Struktur Data — Review Python & Git Workflow

Repo ini dipakai untuk latihan **Review Python** sekaligus latihan **Git workflow** (branch → commit → push → pull request → merge) yang dipakai di dunia kerja nyata.

## Struktur Folder

```
repo/
├── soal/
│   ├── soal01.md
│   ├── soal02.md
│   └── soal03.md
├── jawaban/
│   └── <NIM>/          <- folder jawaban milik masing-masing mahasiswa
├── .github/
│   └── PULL_REQUEST_TEMPLATE.md
└── README.md
```

## Aturan Main

1. **Jangan push langsung ke `main`.** Branch `main` diproteksi — semua perubahan wajib lewat Pull Request (PR).
2. Satu soal = satu branch = satu PR.
3. Nama branch wajib format: `soal0X-<NIM>` (contoh: `soal01-72210001`).
4. Jawaban ditaruh di folder `jawaban/<NIM>/soal0X.ipynb` (atau `.py` kalau diminta).
5. Commit message wajib pakai format **Conventional Commits**:
   - `feat: tambah fungsi hitung rata-rata`
   - `fix: perbaiki logika grade B`
   - Jangan commit dengan pesan `update`, `fix bug`, `asdf`, dsb.

## Langkah Kerja (per soal)

```bash
# 1. Pastikan main lokal up to date
git checkout main
git pull origin main

# 2. Buat branch baru dari main
git checkout -b soal01-<NIM>

# 3. Kerjakan soal, taruh file di jawaban/<NIM>/soal01.ipynb

# 4. Commit
git add jawaban/<NIM>/soal01.ipynb
git commit -m "feat: jawaban soal01 - variabel dan tipe data"

# 5. Push branch ke GitHub
git push origin soal01-<NIM>

# 6. Buka Pull Request di GitHub
#    base: main  <-  compare: soal01-<NIM>
#    Isi PR pakai template yang sudah disediakan

# 7. Tunggu review (asisten/dosen atau teman sekelompok)
#    Kalau ada "Request changes" → perbaiki di branch yang sama, commit lagi, push lagi (PR auto-update)

# 8. Setelah di-approve → merge pakai "Squash and merge"

# 9. Hapus branch setelah merge (opsional tapi disarankan)
git branch -d soal01-<NIM>
```

## Checklist Sebelum Buka PR

- [ ] Notebook/script bisa dijalankan dari atas ke bawah tanpa error (`Restart Kernel & Run All`)
- [ ] Nama file & folder sesuai format (`jawaban/<NIM>/soal0X.ipynb`)
- [ ] Commit message mengikuti Conventional Commits
- [ ] Tidak ada file sampah (`.ipynb_checkpoints`, `__pycache__`, dll — cek `.gitignore`)
- [ ] Constraint di soal terpenuhi (baca ulang `soal/soal0X.md`)

## Kenapa Pakai PR, Bukan Langsung Merge?

Di dunia kerja, kode tidak pernah langsung masuk `main` tanpa direview. PR memberi kesempatan:
- Orang lain (reviewer) mengecek kode sebelum jadi bagian resmi project
- Diskusi & feedback terekam di history, bukan cuma chat WA
- `main` selalu dalam kondisi jalan/stabil

Latihan ini simulasi kecil dari workflow tersebut.