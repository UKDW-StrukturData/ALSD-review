def hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas):
    nilai_akhir = 0.3*nilai_tugas + 0.3*nilai_uts + 0.4*nilai_uas
    return (nilai_akhir)

def grade_nilai(nilai):
    if nilai > 84:
        hasil = "A"
    elif nilai > 69:
        hasil = "B"
    elif nilai > 59:
        hasil = "C"
    elif nilai > 49:
        hasil = "D"
    else:
        hasil = "E"
    return(hasil)

