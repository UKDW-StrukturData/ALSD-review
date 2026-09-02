def hitung_rata2(list_nilai):
    hitung = 0
    for n in range(len(list_nilai)):
        print(f"Nilai ke-{n + 1}: {list_nilai[n]}")
        hitung += list_nilai[n]
    rata_rata = hitung / len(list_nilai)
    return rata_rata

nilai_mhs = [80, 75, 90, 65, 88]
print(f"Rata-rata: {hitung_rata2(nilai_mhs)}")
#ketinggalan