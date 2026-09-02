from soal1 import hitung

nilai_akhir = hitung("Okky", 100, 100, 100)

if nilai_akhir >= 85:
    print(f"Nilai {nilai_akhir} -> Grade: A")
elif nilai_akhir >= 70:
    print(f"Nilai {nilai_akhir} -> Grade: B")
elif nilai_akhir >= 60:
    print(f"Nilai {nilai_akhir} -> Grade: C")
elif nilai_akhir >= 50:
    print(f"Nilai {nilai_akhir} -> Grade: D")
else:
    print(f"Nilai {nilai_akhir} -> Grade: E")


