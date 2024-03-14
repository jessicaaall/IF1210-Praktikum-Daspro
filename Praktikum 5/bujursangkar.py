# Program BujurSangkar
# Menghitung luas bujur sangkar berdasarkan masukan sisi yang divalidasi sehingga selalu > 0

# KAMUS
# sisi : int

# ALGORITMA
sisi = int(input())

if (sisi > 0) :
    print(sisi*sisi)
else :
    print("Sisi harus > 0")