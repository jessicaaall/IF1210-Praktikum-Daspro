# Program CariKarakter
# Mencari karakter yang muncul pertama kali dalam array of character berdasarkan masukan jenis karakter 

# KAMUS
# N, i, indeks : int
# charr : array [0..N] of char
# CC, karakter : char
# found : bool

# ALGORITMA
N = int(input())

while not(0 < N <= 100) :
    print("Masukan salah. Ulangi!")
    N = int(input())

charr = [0 for i in range(N)]

for i in range(N) :
    charr[i] = input()

CC = input()

found = False
for i in range(N) :
    if found == False :
        if CC == "S" or CC == "s" :
            if 97 <= ord(charr[i]) <= 122 :
                indeks = i+1
                karakter = charr[i]
                found = True
        elif CC == "L" or CC == "l" :
            if 65 <= ord(charr[i]) <= 90 :
                indeks = i+1
                karakter = charr[i]
                found = True
        elif CC == "X" or CC == "x" :
            if not((97 <= ord(charr[i]) <= 122) or (65 <= ord(charr[i]) <= 90)) :
                indeks = i+1
                karakter = charr[i]
                found = True

if CC == "S" or CC == "s" :
    if found == True :
        print(indeks, karakter)
    else :
        print("Tidak ada huruf kecil")
elif CC == "L" or CC == "l" :
    if found == True :
        print(indeks, karakter)
    else :
        print("Tidak ada huruf besar")
elif CC == "X" or CC == "x" :
    if found == True :
        print(indeks, karakter)
    else :
        print("Semua huruf")
else :
    print("Tidak diproses")