# Program NilaiEkstrim
# Mencetak apakah masukan X merupakan nilai maksimum, nilai minimum, atau keduanya dari masukan array of integer

# KAMUS
# N, i, maks, min, X : int
# arr : array [0..N] of int
# found : bool

# ALGORITMA
N = int(input())

arr = [0 for i in range(N)]

for i in range(N) :
    arr[i] = int(input())

maks = arr[0]
min = arr[0]

for i in range(1,N) :
    if (arr[i] > maks) :
        maks = arr[i]
    if (arr[i] < min) :
        min = arr[i]

X = int(input())

if (X == maks) and (X == min) :
    print("maksimum")
    print("minimum")
elif (X == maks) and (X != min):
    print("maksimum")
elif (X == min) and (X != maks):
    print("minimum")
else :
    found = False
    for i in range(N) :
        if found == False :
            if (X == arr[i]) :
                found = True
    if found == True :
        print("N#A")
    else :
        print(X, "tidak ada")