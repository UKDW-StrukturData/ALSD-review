def cari_grade (nilai):
    if nilai <50:
        print (f"Nilai {nilai} -> Grade E")
    elif nilai <= 59:
        print (f"Nilai {nilai} -> Grade D")
    elif nilai <= 69:
        print (f"Nilai {nilai} -> Grade C")
    elif nilai <= 84:
        print (f"Nilai {nilai} -> Grade B")
    elif nilai <= 100:
        print (f"Nilai {nilai} -> Grade A")

cari_grade (95.5)
cari_grade (80)
cari_grade (63)
cari_grade (55)
cari_grade (30)