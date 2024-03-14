module Kinerja where

-- KINERJA                              kinerja(j,m,d)

-- DEFINISI DAN SPESIFIKASI
kinerja :: Int -> Int -> Int -> (Int,Int,Int,Int)
{- kinerja(j,m,d) menghasilkan durasi antara jam selesainya pekerjaan
    karyawan dengan standar jam selesai berupa nilai dalam jam, menit,
    dan detik, serta keterangan status kinerja karyawan apakah lebih awal 
    (1), tepat waktu (0), atau terlambat (-1), dari masukan jam selesainya
    pekerjaan karyawan dalam jam (j), menit(m), dan detik(d). -}

-- REALISASI
kinerja j m d =
    let detikKaryawan = j*3600 + m*60 + d
        detikStandar = 17*3600 + 30*60
    in
        let selisih =
                if detikKaryawan<detikStandar then
                    detikStandar - detikKaryawan
                else if detikKaryawan>detikStandar then
                    detikKaryawan - detikStandar
                else
                    0
        in
            if detikKaryawan<detikStandar then
                (div selisih 3600,
                div (mod selisih 3600) 60,
                mod (mod selisih 3600) 60,
                1)
            else if detikKaryawan>detikStandar then
                (div selisih 3600,
                div (mod selisih 3600) 60,
                mod (mod selisih 3600) 60,
                -1)
            else
                (0,0,0,0)

-- APLIKASI
-- kinerja 17 0 0