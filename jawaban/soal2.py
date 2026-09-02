#from soal1 import *

def point(nama,pa, pi, pu):
    isi =(0.3 * pa) + (0.3 * pi) + (0.4*pu)
    if isi >=85:
        print(f"nilai {isi}-> Grade A")
    elif isi >=75:
        print(f"nilai {isi}-> Grade B")
    elif isi >=60:
        print(f"nilai {isi}-> Grade C")
    elif isi >=50:
        print(f"nilai {isi}-> Grade D")
    else:
         print(f"nilai {isi}-> Grade E")
        
point("piji", 95, 95, 100)