# Program SortSaham
# Membaca data kepemilikan sahan sebuah perusahaan
# Mengurutkan data tersebut berdasarkan IdPemilik secara terurut membesar
# Pengurutan menggunakan insertion sort
import tulisdata


# KAMUS
# namafile : string
# file : SEQFILE of string
# bacafile, kata, temp : string
# arr : array of tuple of str
# tuplearr : tuple
# i, j, Pass : int


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
        for Pass in range(1,len(arr)) :
            temp = arr[Pass]
            i = Pass-1
            while (int(temp[0]) < int(arr[i][0])) and (i > 0) :
                arr[i+1] = arr[i]
                i = i-1
            if (int(temp[0]) >= int(arr[i][0])) :
                arr[i+1] = temp
            else :
                arr[i+1] = arr[i]
                arr[i] = temp

    for i in range(len(arr)) :
        print(arr[i][0] + ',' + arr[i][1] + ',' + arr[i][2])