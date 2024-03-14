# PROGRAM UKURAN BAJU
# Menentukan ukuran baju berdasarkan tinggi dan berat badan

# KAMUS 
# t, b, ukuran : int

# ALGORITMA
t = int(input())
b = int(input())

if (t <= 150) :
    ukuran = 1
elif (150 < t <= 170) :
    if (b <= 80) :
        ukuran = 2
    else :
        ukuran = 3
else :
    if (60 < b <= 80) :
        ukuran = 3
    else :
        ukuran = 4

print(ukuran)