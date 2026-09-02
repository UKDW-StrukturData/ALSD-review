<<<<<<< Updated upstream
def nilai_akhir(*data):
    nama, nilai_tugas, nilai_uts, nilai_uas = data
    nilai_akhir = 0.3 * nilai_tugas + 0.3 * nilai_uts + 0.4 * nilai_uas
    
    print(f"| {'Nama':11} :", nama, type(nama))
    print(f"| {'Nilai Akhir':12}: {nilai_akhir:.2f}", type(nilai_akhir))
    
nilai_akhir("Anton", 100, 100, 100)
=======
def nilai_akhir(nama, nilai_tugas, nilai_uts, nilai_uas):
    nilai_akhir = nilai_tugas * 0.3 + nilai_uts * 0.3 + nilai_uas * 0.4

    print(f"| {'Nama':11} :", nama, type(nama))
    print(f"| {'Nilai Akhir':12}: {nilai_akhir:.2f}", type(nilai_akhir))

nilai_akhir("anton", 100, 70, 80)
>>>>>>> Stashed changes
