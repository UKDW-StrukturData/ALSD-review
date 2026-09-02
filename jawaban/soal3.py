def hitung_rata(list_nilai):
    total = 0
    for i in range(len(list_nilai)):
        total += list_nilai[i]
        nilai_mhs = total / len(list_nilai)
        print(f"Nilai ke-{i+1}: {list_nilai[i]}")
    print(f"{'Rata-rata':12}: {nilai_mhs:.2f}")
    return nilai_mhs

rata_rata = hitung_rata([81, 80, 90, 100, 70, 60, 50, 40, 30, 20])