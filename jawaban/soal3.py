def hitung_rata2(list_nilai):
    for i in range(len(list_nilai)):
        print(f"Nilai ke-{i+1}: {list_nilai[i]}")
    print(f"Rata-rata: {sum(list_nilai) / len(list_nilai):.1f}")

nilai_mhs = [80, 75, 90, 65, 88]
hitung_rata2(nilai_mhs)


