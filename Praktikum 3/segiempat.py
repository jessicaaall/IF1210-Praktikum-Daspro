# PROGRAM SEGIEMPAT
# Membuat bentuk segiempat 

# KAMUS
#

# ALGORITMA
N = int(input())
C1 = input()[0]
C2 = input()[0]

if (N > 0) and (C1 != C2) :
    matriks = [[C1 for j in range(N)] for i in range(N)]
    
    if N>=3 :
        for i in range(1,N-1) :
            for j in range(1,N-1) :
                matriks[i][j] = C2
    
    for i in range(N) :
        for j in range(N) :
            print(matriks[i][j], end="")
        print()

else :
    print("Masukan tidak valid")