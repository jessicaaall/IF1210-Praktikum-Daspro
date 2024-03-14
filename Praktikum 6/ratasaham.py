# Program RataRataSaham
# Membaca data kepemilikan saham sebuah perusahaan
# Menuliskan nilai rata-rata kepemilikan sahan dalam keadaan terurut berdasarkan IdPemilik
import tulisdata


# KAMUS
# namafile : string
# file : SEQFILE of string
# bacafile, kata, temp, current : string
# arr : array of tuple of string
# tuplearr : tuple
# i, j, sumNilai, countNilai : int

# ALGORITMA PROGRAM UTAMA
namafile = input()
tulisdata.TulisDataSaham(namafile)

file = open(namafile, 'r')
bacafile = file.readline()

arr = []

while (bacafile != '99999999') :
    tuplearr = ()
    for i in range(3) :
        kata = ''
        for j in range(len(bacafile)-1) :
            kata += bacafile[j]
        tuplearr += (kata,)
        bacafile = file.readline()
    arr += [tuplearr]

file.close()


if (len(arr) == 0) :
    print('File kosong')
else :
    if (len(arr) > 1) :
        for i in range(len(arr)) :
            for j in range(len(arr)-1) :
                if (int(arr[j][0]) > int(arr[j+1][0])) :
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
       
    i = 0
    while (i < len(arr)) :
        current = arr[i][0]
        sumNilai = 0
        countNilai = 0
        while (i < len(arr)) and (arr[i][0] == current) :
            sumNilai += int(arr[i][2])
            countNilai += 1
            i += 1
        print(current + '=' + str("%.2f"%(sumNilai/countNilai)))