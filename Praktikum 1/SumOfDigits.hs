module SumOfDigits where

-- SUM OF DIGITS                                        sumOfDigits(n)

-- DEFINISI DAN SPESIFIKASI 
sumOfDigits :: Int -> Int 
{- sumOfDigits(n) menghasilkan hasil penjumlahan dari setiap bilangan
    tunggal yang terdapat di dalam sebuah bilangan integer positif (n),
    prekondisi n>=0. -}

-- REALISASI
sumOfDigits n =
    if n == 0 then                          -- Basis
        0
    else                                    -- Rekurens
        mod n 10 + sumOfDigits (div n 10)

-- APLIKASI
-- sumOfDigits 123