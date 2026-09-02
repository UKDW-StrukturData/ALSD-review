from soal1 import nilai_akhir


nama_mahasiswa = "Kila"
nilaiakhir = nilai_akhir(nama_mahasiswa, 90, 80, 88)

if nilaiakhir >= 85:
  print(f"Nilai {nilaiakhir:.2f} -> Grade A")
elif nilaiakhir >= 70:
  print(f"Nilai {nilaiakhir:.2f} -> Grade B")
elif nilaiakhir >= 60:
  print(f"Nilai {nilaiakhir:.2f} -> Grade C")
elif nilaiakhir >= 50:
  print(f"Nilai {nilaiakhir:.2f} -> Grade D")
else:
  print(f"Nilai {nilaiakhir:.2f} -> Grade E")





