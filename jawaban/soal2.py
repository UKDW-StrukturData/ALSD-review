from soal1 import nilai

nilai_akhir = nilai("mikey", 90, 80, 85)
if nilai >= 85:
    print(f"Nilai {nilai} -> Grade A")
elif nilai >= 70:
    print(f"Nilai {nilai} -> Grade B")
elif nilai >= 60:
    print(f"Nilai {nilai} -> Grade C")
elif nilai >= 50:
    print(f"Nilai {nilai} -> Grade D")
else:
    print(f"Nilai {nilai} -> Grade E")

