# Program Berat
# Mencetak banyak mahasiswa dengan berat badan yang valid, banyak mahasiswa dengan berat <= 50,
# banyak mahasiswa dengan berat >= 100, dan rata-rata berat badan

# KAMUS
# berat, count, sum, below50, above100 : int

# ALGORITMA
berat = int(input())

count = 0
sum = 0
below50 = 0
above100 = 0

while (berat != -999) :
    if (30 <= berat <= 200) :
        count += 1
        sum += berat
        if (berat <= 50) :
            below50 += 1
        elif (berat >= 100) :
            above100 += 1
    berat = int(input())

if (count == 0) :
    print("Data kosong")
else :
    print(count)
    print(below50)
    print(above100)
    print(round(sum/count))