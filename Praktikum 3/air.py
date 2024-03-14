# PROGRAM KONDISI AIR
# Menentukan kondisi air berdasarkan temperatur air

# KAMUS
# T : int

# ALGORITMA
T = int(input())

if T < 0 :
    print("PADAT")
elif T == 0 :
    print("ANTARA PADAT-CAIR")
elif 0 < T < 100 :
    print("CAIR")
elif T == 100 :
    print("ANTARA CAIR-GAS")
else :
    print("GAS")