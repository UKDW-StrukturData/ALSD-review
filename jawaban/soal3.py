def hitung_rata2(list_nilai):
    data_valid = 0 
    total_nilai = 0
    for nilai in list_nilai:
        if nilai == -1 :
            break
        if nilai < 0 or nilai > 100:
            continue
        data_valid += 1
        total_nilai += nilai
        print(f"Nilai ke-{data_valid}: {nilai}")
    rata_rata = total_nilai/data_valid
    print(f"Rata-rata: {rata_rata:.1f}")

data = eval(input("Masukkan semua nilai yang ada: "))
hitung_rata2(data)