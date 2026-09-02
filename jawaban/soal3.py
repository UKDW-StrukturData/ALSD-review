def hitung_rata2(list_nilai):
    xyz= 0
    abc =0
    for i in list_nilai:
        xyz +=1
        abc += 1
        print(f"Nilai ke-{abc}:{i}")
    ratarata = xyz / len(list_nilai)
    return f"rata-rata:{ratarata}"

print(hitung_rata2(list_nilai= [90, 78, 80, 85, 95]))