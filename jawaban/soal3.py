def hitung_rata2(list_nilai):
    for i in range(len(list_nilai)):
        print(f"Nilai ke-{i+1}: {list_nilai[i]}")
    print(f"Rata-rata: {sum(list_nilai) / len(list_nilai):.1f}")

nilai_mhs = [80, 75, 90, 65, 88]
hitung_rata2(nilai_mhs)


# def hitung_rata2(list_nilai):
#     total = 0
#     count = 0
#     for index, nilai in enumerate(list_nilai, start=1):
#         if nilai == -1:
#             break
#         if nilai < 0 or nilai > 100:
#             continue    
#         print(f"Nilai ke-{index}: {nilai}")
#         total += nilai
#         count += 1   
#     if count == 0:
#         return 0     
#     return total / count
# nilai_mhs = [80, 75, 120, 90, -5, 65, 88, -1, 95]
# rata_rata = hitung_rata2(nilai_mhs)
# print(f"Rata-rata: {rata_rata:.1f}")