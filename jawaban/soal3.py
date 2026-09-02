def hitung_rata2(list_nilai):
    total = 0
    for i in range (len(list_nilai)):
        hitung += list_nilai [i]
        nilai_mhs = total / len(list_nilai)
        print(f"(Nilai ke {i +1}: {list_nilai[i]})")
        

    print(f"{"Rata2:":12}: {nilai_mhs:.1f}")
    return nilai_mhs

avg = hitung_rata2([90, 85, 76])