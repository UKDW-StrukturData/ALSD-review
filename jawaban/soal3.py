def rata(nilai_mhs):
    n = 0
    x=0
    for i in nilai_mhs:
        n += i
        x += 1
        print(f"Nilai ke-{x}: {i}")
    rata = n/len(nilai_mhs)
    return f"Rata-rata: {rata}"
        
print(rata(nilai_mhs = [80, 75, 90, 65, 88]))