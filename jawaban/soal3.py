def hitung_rata2(list_nilai):
    kosong = 0
    total = 0
    for i in list_nilai:
        if i == -1:
            break
        elif i < 0 or i > 100:
            continue
        else:
            kosong += 1
            total += i
            print(f"Nilai ke-{kosong}: {i}")

    akhir = (total)/(len(list_nilai))
    print(f"Rata-rata: {akhir}")
    
hitung_rata2([80, 75, 90, 101, -1])   
        