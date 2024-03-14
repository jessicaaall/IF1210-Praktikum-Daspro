module LuasSegitiga where

-- Luas Segitiga                    luasSegitiga(a,t)

-- DEFINISI DAN SPESIFIKASI
luasSegitiga :: Float -> Float -> Float 
-- luasSegitiga(a,t) menghasilkan luas segitiga dari masukan 
-- dua buah bilangan real, yaitu alas segitiga (a) dan tinggi 
-- segitiga (t), dengan asumsi a dan t lebih besar dari 0.

-- REALISASI
luasSegitiga a t = (1/2) * a * t

-- APLIKASI
-- luasSegitiga 3 4