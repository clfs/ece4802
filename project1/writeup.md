# Project 1

Calvin Figuereo-Supraner, ECE 4802 11/1/16

## Problem 1

> The following ciphertext has been encoded with a shift cipher:
>
> ```
> AOLLULTFRUVDZAOLZFZALT.
> ```

> ### 1a

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

### 1a

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
{"E"=>29, "N"=>28, "F"=>25, "P"=>24, "I"=>23, "G"=>23, "B"=>17, "V"=>14,
"W"=>13, "M"=>12, "L"=>11, "Q"=>10, "A"=>10, "Y"=>9, "C"=>8, "T"=>7, "H"=>3,
"U"=>2, "S"=>2, "R"=>2, "O"=>2, "Z"=>1, "D"=>1, "X"=>0, "K"=>0, "J"=>0}
```

### 2b

> Decrypt the ciphertext with help of the relative letter frequency of the
> English language (e.g., search Wikipedia for letter frequency analysis). Note
> that the text is relatively short and might not completely fulfill the given
> frequencies from the table.

### 2c

> Who wrote the text? What are the missing words?

## Problem 3

> Vigenere proposed a stronger cipher than the Vigenere cipher. This cipher is
> an autokey cipher, where the plaintext itself is used as key. It works by
> starting with a keyword, and using plaintext characters after that.
>
> ```
> plaintext     l e h r u n d k u n s t
> key           w p i l e h r u n d k u
> ciphertext    H T P C Y U U E H Q C N
> ```

### 1a

> Check the above example.

### 1b

> Provide a formal definition of the `Gen`, `Enc`, and `Dec` algorithms for
> this cipher. Make sure to include the equation that defines the encryption
> and decryption operations.

### 1c

> Provide an implementation of this cipher. You may either use Python or sage,
> another common programming language, such as C.

### 1d

> Decrypt the following ciphertext using the key `plato`:
>
> ```
> CZGHCQRKSRJRIWXTDYFCFWYQ
> ```

## Problem 4

> Another autokey cipher by Vigenere uses the letters of the ciphertext instead
> of the plaintext to form new key letters:
>
> ```
> plaintext     l e h r u n d k u n s t
> key           w p i h t p y n c b x w
> ciphertext    H T P Y N C B X W O P P
> ```

### 4a

> Show that this is a much weaker cipher than the other: Explain a brute force
> attack that can recover most of the plaintext quickly.

### 4b

> Decrypt the following ciphertext that has been encrypted with the above
> method. It is ok to miss the first few letters.

```
NEASJFINVCMMZJPQKSQXIKXJBZXLXO
```

