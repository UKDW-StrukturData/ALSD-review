def hitung_rata2(nilai):
    valid = 0
    total = 0

    for i in nilai:
        if i == -1:
            break
        
        if i < 0 or i > 100:
            continue
        else:
            valid += 1
            total += i
            print(f"Nilai ke-{valid}: {i}")

    print(f"Rata-rata: {total/valid}")

nilai = eval(input("Masukkan Nilai: "))

hitung_rata2(nilai)