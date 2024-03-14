module NbKelipatanX where

-- KELIPATAN BILANGAN                       nbKelipatanX(m,n,x)

-- DEFINISI DAN SPESIFIKASI
nbKelipatanX :: Int -> Int -> Int -> Int
{- nbKelipatanX(m,n,x) menghasilkan banyaknya bilangan kelipatan x
    di antara m dan n. -}


-- REALISASI

nbKelipatanX m n x =
    if m == n then                  -- Basis
        if mod n x == 0 then
            1
        else 
            0
    else                            -- Rekurens
        if mod n x == 0 then
            nbKelipatanX m (n-1) x + 1
        else
            nbKelipatanX m (n-1) x

-- APLIKASI
-- nbKelipatanX 1 10 2