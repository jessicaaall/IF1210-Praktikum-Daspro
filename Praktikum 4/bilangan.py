# Program Bilangan
# Menghasilkan urutan ditemukannya suatu bilangan dari masukan beberapa bilangan

# KAMUS
# masukan, find : bool
# N, X, i, urutan : int
# arraynilai : array of int

# ALGORITMA
masukan = False
while masukan == False :
    N = int(input())
    if 0 < N <= 100 :
        arraynilai = [0 for i in range(N)]
        for i in range(N) :
            arraynilai[i] = int(input())
        masukan = True
    else :
        print("Masukan salah. Ulangi!")

X = int(input())

find = False
for i in range(N) :
    if find == False :
        if X == 0 :
            if arraynilai[i] == 0 :
                urutan = i+1
                find = True
            else :
                urutan = 0
        elif X == -1 :
            if arraynilai[i] < 0 :
                urutan = i+1
                nilai = arraynilai[i]
                find = True
            else :
                urutan = 0
        elif X == 1 :
            if arraynilai[i] > 0 :
                urutan = i+1
                nilai = arraynilai[i]
                find = True
            else :
                urutan = 0
        else :
            find = True

if X == 0 :
    if urutan == 0 :
        print("Tidak ada 0")
    else :
        print(urutan)
elif X == -1 :
    if urutan == 0 :
        print("Tidak ada negatif")
    else :
        print(urutan, nilai)
elif X == 1 :
    if urutan == 0 :
        print("Tidak ada positif")
    else :
        print(urutan, nilai)
else :
    print("Tidak diproses")