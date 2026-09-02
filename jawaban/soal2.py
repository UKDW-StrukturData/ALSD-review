from soal1 import nilai_akhir

nilaiAkhir = nilai_akhir(100,100,100)

if 85 <= nilaiAkhir <= 100:
    print(f"Nilai {nilaiAkhir} -> Grade A")

elif 70 <= nilaiAkhir < 85:
    print(f"Nilai {nilaiAkhir} -> Grade B")

elif 60 <= nilaiAkhir < 70:
    print(f"Nilai {nilaiAkhir} -> Grade C")

elif 50 <= nilaiAkhir < 60:
    print(f"Nilai {nilaiAkhir} -> Grade D")

elif nilaiAkhir < 50:
    print(f"Nilai {nilaiAkhir} -> Grade E")