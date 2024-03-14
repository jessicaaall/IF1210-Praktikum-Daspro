module KlasifikasiKomputer where

-- KLASIFIKASI KOMPUTER                     klasifikasi(c,g,h)

-- DEFINISI DAN SPESIFIKASI
klasifikasi :: Int -> Int -> Int -> Int
{- klasifikasi(c,g,h) mengklasifikasikan komputer pengguna ke salah
    satu dari 5 kelompok, yaitu 1,2,3,4, dan 5 berdasarkan kemampuan CPU (c),
    kemampuan GPU (g), dan kemampuan harddisk (h). -}

-- REALISASI
klasifikasi c g h =
    if c<2 || g<2 || h<2 then
        1
    else if c<5 || g<5 then
        2
    else if c<=7 && g<=7 && h<=7 then
        3
    else if c<=7 || g<=7 || h<=7 then
        4
    else
        5

-- APLIKASI
-- klasifikasi 8 9 4