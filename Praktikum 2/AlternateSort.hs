module AlternateSort where

-- ALTERNATE SORT                                           alternateSort(l)

-- DEFINISI DAN SPESIFIKASI
alternateSort :: [Int] -> [Int]
{- alternateSort(l) mengurutkan list l, lalu membagi list tersebut menjadi 2 sama 
    besar, misal l1 dan l2, dimana jika panjang list ganjil, maka l1 memiliki 1 elemen
    yang lebih bayak dibanding l2, kemudian elemen terkecil l1 dimasukkan ke akhir l3
    dan elemen terbesar l2 dimasukkan ke akhir l3, yang dilakukan terus-menerus hingga
    list l1 dan l2 kosong.-}
getSmallest :: [Int] -> Int
{- getSmallest(l) menghasilkan elemen list l yang merupakan nilai terkecil. -}
delElement :: [Int] -> Int -> [Int]
{- delElement(l,x) membuang elemen x pada list l. -}
sortList :: [Int] -> [Int]
{- sortList(l) mengurutkan elemen list l dari yang terkecil ke yang terbesar. -}

-- REALISASI
getSmallest l = 
    if length l == 1 then       -- Basis
        head l
    else                        -- Rekurens
        if head l > getSmallest (tail l) then
            getSmallest (tail l)
        else
            head l

delElement l x =
    if null l then          -- Basis
        l
    else                    -- Rekurens
        if head l == x then
            tail l
        else
            [head l] ++ delElement (tail l) x

sortList l =
    if length l == 1 then       -- Basis
        l
    else                        -- Rekurens
        [getSmallest l] ++ sortList (delElement l (getSmallest l))

alternateSort l =
    if null l || (length l == 1) then       -- Basis
        l
    else                                    -- Rekurens
        [head (sortList l)] ++ [last (sortList l)] ++ alternateSort (init (tail (sortList l)))

-- APLIKASI
-- alternateSort [9,10,11,12]