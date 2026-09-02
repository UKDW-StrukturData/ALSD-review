def hitung_rata2(list_nilai):
    for i in range (len(list_nilai)):
        print(f"Nilai ke-{i+1}: {list_nilai[i]}")
    
    hasil = 0
    for j in list_nilai:
        hasil += j
    
    rata = hasil / len(list_nilai)
    print (f"Rata-rata: {rata}")
    
list_nilai = [80, 90, 80]
hitung_rata2(list_nilai)