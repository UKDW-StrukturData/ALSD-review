from soal1 import hitung

nilai_akhir = hitung("Okky", 100, 100, 100)

if nilai_akhir >= 85:
    print("Grade: A")
elif nilai_akhir >= 70:
    print("Grade: B")
elif nilai_akhir >= 60:
    print("Grade: C")
elif nilai_akhir >= 50:
    print("Grade: D")
else:
    print("Grade: E")


