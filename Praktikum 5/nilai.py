# Program Nilai
# Mencetak banyak mahasiswa dengan nilai yang valid, banyak mahasiswa yang lulus, 
# banyak mahasiswa yang tidak lulus, dan rata-rata nilai yang valid

# KAMUS
# nilai, jumlahinput, count, sum, tidaklulus, lulus : int

# ALGORITMA
nilai = int(input())

jumlahinput = 0
count = 0
sum = 0
tidaklulus = 0
lulus = 0

while (nilai != -9999) :
    jumlahinput += 1
    if (0 <= nilai <= 100) :
        count += 1
        sum += nilai
        if (nilai < 40) :
            tidaklulus += 1
        elif (nilai >= 40) :
            lulus += 1
    nilai = int(input())

if (jumlahinput == 0) and (count == 0) :
    print("Data nilai kosong")
elif (jumlahinput != 0) and (count == 0) :
    print(count)
else :
    print(count)
    print(lulus)
    print(tidaklulus)
    print("%.2f"%(sum/count))