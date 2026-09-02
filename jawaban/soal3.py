
def hitung(list_nilai):
    panjang = len(list_nilai)
    total = 0
    for i in list_nilai:
        print(f"Nilai ke-{list_nilai.index(i)+1}: {i}")
        if i >= 0 and i <= 100:
            total += i
        elif i == -1:
            break
        else:
            panjang -= 1
            continue
    total /= panjang
    print(f"Rata-rata: {total:.2f}")
hitung([81, 80, 90, 100, 70, 60, 50, 40, 30, 20])
