from soal1 import *

data = mahasiswa("anton", 100, 100, 100)

def grade(nilai_akhir):
    if nilai_akhir >= 85 and nilai_akhir <= 100:
        print(f"Nilai {nilai_akhir} -> Grade A")
    elif nilai_akhir >= 70 :
        print(f"Nilai {nilai_akhir} -> Grade B")
    elif nilai_akhir >= 60 :
        print(f"Nilai {nilai_akhir} -> Grade C")
    elif nilai_akhir >= 50 :
        print(f"Nilai {nilai_akhir} -> Grade D")
    elif nilai_akhir >= 0 :
        print(f"Nilai {nilai_akhir} -> Grade E")

grade(data)