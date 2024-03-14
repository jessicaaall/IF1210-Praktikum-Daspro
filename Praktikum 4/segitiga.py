# Tuliskan identitas di sini
# Nama : Jessica
# NIM : 16521024
# Tanggal : 18 Maret 2022

# Program GambarSegitiga
# Input: N : integer
# Output: Jika N > 0 dan ganjil, gambar segitiga sesuai dengan N
#         Jika tidak, tampilkan pesan kesalahan: 

# KAMUS
# Variabel
#    N : int

def GambarSegitiga(N):
# I.S. N > 0 dan N ganjil
# F.S. Gambar segitiga dengan tinggi sebesar N sesuai spesifikasi soal
# Lengkapilah kamus lokal dan algoritma prosedur di bawah ini
    # KAMUS LOKAL
    # baris, spasi, simbol : int
    # a, b, c : int
    # ALGORITMA
    a = N-1
    for baris in range(1,int((N+1)/2)+1) :
        for spasi in range(0,a) :
            print(end=" ")
        a = a-2
        for simbol in range(0,2*baris-1) :
            print("*", end="")
        print("")
    b = 2
    c = N-2
    for baris in range(1,int((N-1)/2)+1) :
        for spasi in range(0,b) :
            print(end=" ")
        b = b+2
        for simbol in range(c,0,-1) :
            print("*", end="")
        print("")
        c = c-2
    return

def IsValid(N):
# menghasilkan true jika N positif dan ganjil, false jika tidak
# Lengkapilah kamus lokal dan algoritma fungsi di bawah ini
    # KAMUS LOKAL
    # nilaiN : bool
    # ALGORITMA
    if (N>0) and ((N % 2) != 0) :
        nilaiN = True
    else :
        nilaiN = False
    return nilaiN

# ALGORITMA PROGRAM UTAMA
N = int(input())
if (IsValid(N) == True) :          # lengkapi dengan pemanggilan fungsi IsValid
    GambarSegitiga(N)   # lengkapi dengan pemanggilan prosedur GambarSegitiga
else : # N tidak positif atau N tidak ganjil
    print("Masukan tidak valid")