from soal1 import nilaiAkhir


def grade(nilai):
    if nilai >= 85:
        print(f"Nilai {nilai} -> Grade A")
    elif nilai >= 70:
        print(f"Nilai {nilai} -> Grade B")
    elif nilai >= 60:
        print(f"Nilai {nilai} -> Grade C")
    elif nilai >= 50:
        print(f"Nilai {nilai} -> Grade D")
    elif nilai < 50:
        print(f"Nilai {nilai} -> Grade E")
    else:
        print("Nilai tidak valid")
nilai = nilaiAkhir("Anton", 81, 15, 72)
grade(nilai)