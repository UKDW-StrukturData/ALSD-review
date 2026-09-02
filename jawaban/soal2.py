import soal1

def hitungGrade(hasil):
    
    if hasil >= 85:
        print (f"Nilai{hasil} -> Grade A")
    elif hasil >= 70 and hasil <= 84:
        print (f"Nilai{hasil} -> Grade B")
    elif hasil >= 60 and hasil <= 69:
        print (f"Nilai{hasil} -> Grade C")
    elif hasil >= 50 and hasil <= 59:
        print (f"Nilai{hasil} -> Grade D")
    else:
        print (f"Nilai{hasil} -> Grade E")
hitungGrade(soal1.hasil)