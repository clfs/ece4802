# Project 1

Calvin Figuereo-Supraner, ECE 4802 11/1/16

## Problem 1

> The following ciphertext has been encoded with a shift cipher:
>
> ```
> AOLLULTFRUVDZAOLZFZALT.
> ```

### 1a

> Perform an attack against the cipher using one of the attacks discussed in
> class. What is the key? What is the plaintext?

The Ruby script below uses brute force to test all 26 keys.

```ruby
m = 'AOLLULTFRUVDZAOLZFZALT'
a = *('A'..'Z')
for k in 0..25
    puts a[k], m.tr(a.join, a.rotate(k).join)
end
```

The output gives the key and plaintext.

```
...
T
THEENEMYKNOWSTHESYSTEM
...
```

## Problem 2

> The ciphertext printed below was encrypted using a substitution cipher. The
> objective is to decrypt the ciphertext without knowledge of the key.
>
> Ciphertext:
>
> ```
> NVIFABE NVIFABE BINNBE MNWL
> PGV I VGFCEL VPWN YGQ WLE
> QH WOGUE NPE VGLBC MG PITP
> BIAE W CIWDGFC IF NPE MAY
>
> VPEF NPE OBWZIFT MQF IM TGFE
> VPEF PE FGNPIFT MPIFEM QHGF
> NPEF YGQ MPGV YGQL BINNBE BITPN
> NVIFABE NVIFABE WBB NPE FITPN

> NPEF NPE NLWUEBEL IF NPE CWLA
> NPWFAM YGQ SGL YGQL NIFY MHWLA
> PE RGQBC FGN MEE VPIRP VWY NG TG
> IS YGQ CIC FGN NVIFABE MG
> ```
## 1a

> Provide the relative frequency of all letters A...Z in the ciphertext.

The Ruby script below
- creates a hash, mapping each character in A..Z to 0
- strips the ciphertext of non-letters
- increments a character's hash value when found
- prints the sorted hash

```ruby
ct = %{
NVIFABE NVIFABE BINNBE MNWL
PGV I VGFCEL VPWN YGQ WLE
QH WOGUE NPE VGLBC MG PITP
BIAE W CIWDGFC IF NPE MAY

VPEF NPE OBWZIFT MQF IM TGFE
VPEF PE FGNPIFT MPIFEM QHGF
NPEF YGQ MPGV YGQL BINNBE BITPN
NVIFABE NVIFABE WBB NPE FITPN

NPEF NPE NLWUEBEL IF NPE CWLA 
NPWFAM YGQ SGL YGQL NIFY MHWLA
PE RGQBC FGN MEE VPIRP VWY NG TG
IS YGQ CIC FGN NVIFABE MG
}

# create hash
h = Hash[('A'..'Z').to_a.product([0])]
# fill hash
ct.scan(/\w/).join.each_char{|c| h[c] += 1}
# print the sorted hash
puts h.sort_by{|k,v| v}.reverse.to_h

```

The output gives the characters in order of frequency as
"ENFPIGBVWMLQAYCTHUSROZDXKJ".

```
{"E"=>29, "N"=>28, "F"=>25, "P"=>24, "I"=>23, "G"=>23, "B"=>17, "V"=>14, "W"=>13, "M"=>12, "L"=>11, "Q"=>10, "A"=>10, "Y"=>9, "C"=>8, "T"=>7, "H"=>3, "U"=>2, "S"=>2, "R"=>2, "O"=>2, "Z"=>1, "D"=>1, "X"=>0, "K"=>0, "J"=>0}
```



## Problem 3

## Problem 4
