# Program Tabungan
# Menghitung jumlah tabungan dari sejumlah siswa

# KAMUS 
# N, i, jumlah : int

# ALGORITMA
N = int(input())

jumlah = 0

for i in range(N) :
    jumlah = jumlah + int(input())

print(jumlah)