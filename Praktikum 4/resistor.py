# Program Resistor
# Menghitung nilai resistansi total dari 3 buah resistor

# KAMUS
# benar : bool
# R1,R2,R3,total : float
# pilihan : char

# ALGORITMA
benar = True

while benar == True :
    R1 = float(input())
    R2 = float(input())
    R3 = float(input())
    pilihan = input()[0]
    if (R1>0 and R2>0 and R3>0) :
        if pilihan == 's' or pilihan == 'S' :
            total = R1+R2+R3
            benar = False
        elif pilihan == 'p' or pilihan == 'P' :
            total = (R1*R2*R3)/(R2*R3 + R1*R2 + R1*R3)
            benar = False
        else :
            print("Masukan salah")
    else : 
        print("Masukan salah")
print(format(total, '.2f'))