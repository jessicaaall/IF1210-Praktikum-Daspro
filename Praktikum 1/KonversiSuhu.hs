module KonversiSuhu where

-- Konversi Suhu                    konversiSuhu(t,k)

-- DEFINISI DAN SPESIFIKASI
konversiSuhu :: Float -> Char -> Float
-- konversiSuhu(t,k) menghasilkan besaran suhu Celcius (t)
-- dalam satuan suhu konversi (k).

-- REALISASI
konversiSuhu t k
    | k=='R' = 4/5 * t
    | k=='F' = (9/5 * t) + 32
    | otherwise = t + 273.15

-- APLIKASI
-- konversiSuhu 37 'F'