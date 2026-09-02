from soal1 import *
def abc(nilai):
    if nilai >= 85:
        print (f"Nilai {nilai} -> Grade A")
    elif nilai >= 70:
        print(f"Nilai {nilai} -> Grade B")
    elif nilai >= 60:
        print(f"Nilai {nilai} -> Grade C")
    elif nilai >= 50:
        print(f"Nilai {nilai} -> Grade D")
    else:
        print(f"Nilai {nilai} -> Grade E")

p = tes("anies",90,100,60)
abc(p)    