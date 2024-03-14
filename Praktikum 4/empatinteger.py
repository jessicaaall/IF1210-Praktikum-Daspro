# Tuliskan identitas di sini
# Nama : Jessica
# NIM : 16521024
# Tanggal : 18 Maret 2022

# Program EmpatInteger
# Input: 4 integer: A, B, C, D
# Output: Sifat integer dari A, B, C, D (positif/negatif/nol) 
#         Jika semua integer positif, tampilkan:
#         nilai maksimum, minimum, dan mean olympic 

# KAMUS
# variabel
#    A, B, C, D : int
#    mo : real

# PROCEDURE DAN FUNCTION
def CekInteger (x):
# I.S.: x terdefinisi, bertype int
# F.S.: Jika x positif, maka tertulis di layar: POSITIF
#       Jika x negatif, maka tertulis di layar: NEGATIF
#       Jika x nol, maka tertulis di layar: NOL
# Tuliskan realisasi prosedur CekInteger di bawah ini
    if x == 0 :
        print("NOL")
    elif x>0 :
        print("POSITIF")
    else :
        print("NEGATIF")
    return

def Max (a, b, c, d):
# menghasilkan nilai terbesar di antara a, b, c, d (integer)
# Tuliskan realisasi fungsi Max di bawah ini
    if a > b :
        if a > c :
            if a > d :
                max = a
            else :
                max = d
        else :
            if c > d :
                max = c
            else :
                max = d
    else :
        if b > c :
            if b > d :
                max = b
            else :
                max = d
        else :
            if c > d :
                max = c
            else :
                max = d
    return max

def Min (a, b, c, d):
# menghasilkan nilai terkecil di antara a, b, c, d (integer)
# Tuliskan realisasi fungsi Min di bawah ini
    if a < b :
        if a < c :
            if a < d :
                min = a
            else :
                min = d
        else :
            if c < d :
                min = c
            else :
                min = d
    else :
        if b < c :
            if b < d :
                min = b
            else :
                min = d
        else :
            if c < d :
                min = c
            else :
                min = d
    return min

def IsAllPositif (a, b, c, d):
# menghasilkan true jika a, b, c, d seluruhnya positif
# false jika tidak
# Tuliskan realisasi fungsi IsAllPositif di bawah ini
    if a>0 and b>0 and c>0 and d>0 :
        return True
    else :
        return False 

# PROGRAM UTAMA
# Tidak boleh diubah-ubah
# Input
A = int(input())
B = int(input())
C = int(input())
D = int(input())

# Menuliskan sifat integer
CekInteger(A)
CekInteger(B)
CekInteger(C)
CekInteger(D)

# Penulisan maksimum, minimum, dan mean olympic
if (IsAllPositif(A,B,C,D)):
    print(Max(A,B,C,D))
    print(Min(A,B,C,D))
    mo = (A + B + C + D - Max(A,B,C,D) - Min(A,B,C,D)) / 2
    print("%.2f" % mo)