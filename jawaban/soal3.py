def hitung_rata2(list_nilai):
    total = 0
    for i in range (len(list_nilai)):
        total += list_nilai [i]
        nilai_mhs = total / len(list_nilai)
        print (f"Nilai ke {i+1}: {list_nilai[i]}")

    print(f"{'Rata-rata':12}: {nilai_mhs:.1f}")
    return nilai_mhs

rata = hitung_rata2([80, 75, 90, 65, 88, 80, 35, 78, 97])