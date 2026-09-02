def nilai_akhir(nama, nilai_tugas, nilai_uts, nilai_uas):
    nilai_akhir = (nilai_tugas * 0.3) + (nilai_uts * 0.3) + (nilai_uas * 0.4)
    print(f"| {'Nama':11}: {nama} ({type(nama).__name__})")
    print(f"| {'Nilai Akhir':11}: {nilai_akhir:.2f} ({type(nilai_akhir).__name__})")
    return nilai_akhir
nama_mahasiswa = "Kila"
hasil_akhir = nilai_akhir(nama_mahasiswa, 90, 80, 88)

