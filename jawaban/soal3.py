def rata(list_nilai):
    n = 0
    x = 0
    for i in list_nilai:
        n += i
        x += 1
        print (f"nilai ke-{x}: {i}")
    rata_rata = n / len(list_nilai)
    return f"rata_rata: {rata_rata}"

print (rata(list_nilai=[80, 75, 90, 65, 88]))