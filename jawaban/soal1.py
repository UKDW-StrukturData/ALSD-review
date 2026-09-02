def nilai_siswa(nama, nilai_tugas, nilai_uts, nilai_uas):
    
    nilai_akhir = (0.3 * nilai_tugas) + (0.3 * nilai_uts) + (0.4 * nilai_uas)

    print(f"| {'Nama':11} :", nama, type(nama))
    print(f"| {'Nilai Akhir':12}: {nilai_akhir:.2f}", type(nilai_akhir))
    
    return nilai_akhir

#nilai_siswa("Mikael", 100, 100, 100)