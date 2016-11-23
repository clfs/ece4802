import Data.Bits

modExp :: Integer -> Integer -> Integer -> Integer -> Integer
modExp b 0 m = 1
modExp b e m = t * modExp (b^2 `mod` m) (Data.Bits.shiftR e 1)  m `mod` m
    where t = if Data.Bits.testBit e 0 then b `mod` m else 1
