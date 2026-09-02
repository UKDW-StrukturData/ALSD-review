def hitung_rata2(list_nilai):
    panjang = len(list_nilai)
    total = 0
    urutan = 1
    for i in list_nilai:
        print(f"Nilai ke-{urutan}: {i}")
        urutan += 1
        if i >= 0 and i <=100:
            total += i
        elif i == -1:
            break
        else:
            panjang -= 1
            continue
    total /= panjang
    print(total)

hitung_rata2([101, 103, 29, 30])
hitung_rata2([11, 30, 29, 30])