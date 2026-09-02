from soal1 import *

def grade_siswa(nilai):
    if nilai <= 100 and nilai >= 85:
        print(f"Nilai {nilai} -> Grade A")
    elif nilai < 85 and nilai >= 70:
        print(f"Nilai {nilai} -> Grade B")
    elif nilai < 70 and nilai >= 60:
        print(f"Nilai {nilai} -> Grade A")
    elif nilai < 60 and nilai >= 50:
        print(f"Nilai {nilai} -> Grade A")
    elif nilai < 50:
        print(f"Nilai {nilai} -> Grade E")

a = nilai_siswa("Adi", 80, 85, 90)
grade_siswa(a)

b = nilai_siswa("Mikael", 100, 100, 100)
grade_siswa(b)