def penilaian(nilai_tugas, nilai_uts, nilai_uas):
    nilai_akhir = 0.3 * nilai_tugas + 0.3 * nilai_uts + 0.4 * nilai_uas
    return nilai_akhir

nama = input("Masukkan nama mahasiswa: ")
nilai_tugas = float(input("Masukkan nilai tugas: "))
nilai_uts = float(input("Masukkan nilai UTS: "))
nilai_uas = float(input("Masukkan nilai UAS: "))
nilai_akhir = penilaian(nilai_tugas, nilai_uts, nilai_uas)
print(f"| {'Nama':11} :", nama, type(nama))
print(f"| {'Nilai Akhir':12}: {nilai_akhir:.2f}", type(nilai_akhir))