def Hitung_nilai(nama, nilai_tugas, nilai_uts, nilai_uas):
    
    nilai_akhir = (nilai_tugas * 0.3) + (nilai_uts * 0.3) + (nilai_uas * 0.4)
    
    hasil1 = f"| {'Nama':11} : {nama} {type(nama)}"
    hasil2 = f"| {'nilai_akhir':12}: {nilai_akhir:.2f} {type(nilai_akhir)}"
    
    # return f"{hasil1}\n{hasil2}"
    return nilai_akhir

hasil = (Hitung_nilai("Edbert", 100, 95, 100))
print(hasil)