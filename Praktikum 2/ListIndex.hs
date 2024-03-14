module ListIndex where

-- LIST INDEX               listIndex(l,f)

-- DEFINISI DAN SPESIFIKASI
listIndex :: [Int] -> (Int -> Char) -> [Char]
{- listIndex(l,f) menerima masukan sebuah list of integer l dan sebuah
    fungsi f yang menerima masukan sebuah integer dan menghasilkan sebuah 
    char, listIndex akan menghasilkan sebuah list of character yang melambangkan 
    nilai-nilai indeks dari suatu list nilai integer. -}

-- REALISASI
listIndex l f =
    if null l then
        []
    else if length l == 1 then
        [f(head l)]
    else
        [f(head l)] ++ (listIndex (tail l) f)