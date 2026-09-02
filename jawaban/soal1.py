def nilai_akhir(nilai_tugas, nilai_uts, nilai_uas):
    Akhir = 0.3 * nilai_tugas + 0.3 * nilai_uts + 0.4 * nilai_uas
    return Akhir


nilaiAkhir = nilai_akhir(100,100,100)
nama = "levi"

print(f"| {'Nama':11} :", nama, type(nama))
print(f"| {'Nilai Akhir':12}: {nilaiAkhir:.2f}", type(nilaiAkhir))