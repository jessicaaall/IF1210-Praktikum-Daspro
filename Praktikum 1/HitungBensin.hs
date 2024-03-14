module HitungBensin where

-- HITUNG BENSIN                    hitungBensin(a,b)

-- DEFINISI DAN SPESIFIKASI
hitungBensin :: Int -> Int -> Int
{- hitungBensin(a,b) menghasilkan total biaya bensin yang dibutuhkan oleh 
    seluruh kendaraan dari posisi a sampai kendaraan pada posisi b. -}
hitungBiaya :: Int -> Int
{- hitungBiaya(n) menghasilkan biaya bensin yang dibutuhkan oleh suatu kendaraan
    yang berada pada posisi n. -}

hitungBiaya n =
    if n == 1 then 0
    else if mod n 2 /= 0 then hitungBiaya (n*3 + 1) + 1
    else hitungBiaya (div n 2) + 1

hitungBensin a b =
    if a == b then hitungBiaya a
    else hitungBiaya a + hitungBensin (a+1) b

main :: IO ()
main = do
    putStrLn "Hasil : "
    print (hitungBensin 11 11) 