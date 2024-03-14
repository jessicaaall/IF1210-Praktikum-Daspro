# PROGRAM MAKSIMUM TIGA BILANGAN
# Menuliskan nilai tebesar di antara 3 buah bilangan integer

# KAMUS
# a, b, c : int

# ALGORITMA
a = int(input())
b = int(input())
c = int(input())

if a>=b :
    if a>=c :
        print(a)
    else :
        print(c)
else :
    if b>=c :
        print(b)
    else :
        print(c)