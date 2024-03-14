# Program HitungVokal
# Membaca masukan sejumlah karakter dan menyimpannya ke file data.txt
# Membaca isi file data.txt, menghitung dan menampilkan ada berapa
# banyak karakter huruf hidup dalam file

# KAMUS
# constant mark : character = '.'
# huruf vokal : array of char
# file : SEQFILE of char
# karakter : char
# count, i : int

def TulisTeks():
# Membaca kalimat (kumpulan karakter) diakhiri mark dari keyboard
# dan menyimpannya ke file data.txt
    # KAMUS LOKAL
    # f : SEQFILE of char
    # kalimat
    # ALGORITMA
    f = open("dataku.txt",'w')
    kalimat = input() # Baca sebuah kalimat dari keyboard
                      # diakhiri mark '.'
                      # Kalimat kosong hanya ada mark
    f.write(kalimat)  # Menuliskan kalimat ke file
    f.close()


# ALGORITMA PROGRAM UTAMA
mark = '.'
hurufvokal = ['A', 'a', 'I', 'i', 'U', 'u', 'E', 'e', 'O', 'o']

TulisTeks()

file = open('dataku.txt', 'r')
karakter = file.read(1)

count = 0
while (karakter != mark) :
    for i in range(10) :
        if (hurufvokal[i] == karakter) :
            count += 1
            break
    karakter = file.read(1)

file.close()

print(count)