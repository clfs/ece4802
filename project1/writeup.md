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

### 2a

> Provide the relative frequency of all letters A...Z in the ciphertext.

The Ruby code below prints a sorted hash of letter counts in the ciphertext.

```ruby
ct = %{
NVIFABE NVIFABE BINNBE MNWL
# ... omitted for brevity
IS YGQ CIC FGN NVIFABE MG
}

h = Hash.new(0)                         # create hash
ct.scan(/\w/).each{|c| h[c] += 1}       # fill hash; letters only
puts h.sort_by{|k,v| v}.reverse.to_h    # sort, print hash

```

The output gives the ciphertext character frequencies, from greatest to least,
as "ENFPGIBVWMLQAYCTHRSUOZD", with J, K, and X missing.

```
{"E"=>29, "N"=>28, "F"=>25, "P"=>24, "G"=>23, "I"=>23, "B"=>17, "V"=>14, "W"=>1
3, "M"=>12, "L"=>11, "Q"=>10, "A"=>10, "Y"=>9, "C"=>8, "T"=>7, "H"=>3, "R"=>2, 
"S"=>2, "U"=>2, "O"=>2, "Z"=>1, "D"=>1}
```

### 2b

> Decrypt the ciphertext with help of the relative letter frequency of the
> English language (e.g., search Wikipedia for letter frequency analysis). Note
> that the text is relatively short and might not completely fulfill the given
> frequencies from the table.

First, try replacing the characters by letter frequency only. Place J, K, and X
at the end, since they're unused. The code below is Ruby.

```
ct_freq = 'ENFPGIBVWMLQAYCTHRSUOZDJKX'
en_freq = 'ETAOINSHRDLCUMWFGYPBVKJXQZ' # via wikipedia
puts ct.tr(ct_freq, en_freq)
```

This outputs:

```
THNAUSE THNAUSE SNTTSE DTRL
OIH N HIAWEL HORT MIC RLE
CG RVIBE TOE HILSW DI ONFO
SNUE R WNRJIAW NA TOE DUM

HOEA TOE VSRKNAF DCA ND FIAE
HOEA OE AITONAF DONAED CGIA
TOEA MIC DOIH MICL SNTTSE SNFOT
THNAUSE THNAUSE RSS TOE ANFOT

TOEA TOE TLRBESEL NA TOE WRLU 
TORAUD MIC PIL MICL TNAM DGRLU
OE YICSW AIT DEE HONYO HRM TI FI
NP MIC WNW AIT THNAUSE DI
```

This is still unsolved. First, note that `N` (line 2, word 2) should have been
a single letter word, such as `I` or `A`. If we assume `N` here is `I`, then
`SNTTSE` (line 1, word 3) becomes `SITTSE`. This is nearly the word `LITTLE`,
so assume `S` here is actually `L`. The first two words of the ciphertext are
identical, so a possible plaintext is `TWINKLE TWINKLE LITTLE STAR`, and the
word lengths confirm this.

The solution is given by:

```
ct_alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
pt_alph = 'KLDMENOPI**RSTBHUCFGVWA*YZ'
puts ct.tr(ct_alph, pt_alph)
```

The output reads:

```
TWINKLE TWINKLE LITTLE STAR
HOW I WONDER WHAT YOU ARE
UP ABOVE THE WORLD SO HIGH
LIKE A DIAMOND IN THE SKY

WHEN THE BLAZING SUN IS GONE
WHEN HE NOTHING SHINES UPON
THEN YOU SHOW YOUR LITTLE LIGHT
TWINKLE TWINKLE ALL THE NIGHT

THEN THE TRAVELER IN THE DARK 
THANKS YOU FOR YOUR TINY SPARK
HE COULD NOT SEE WHICH WAY TO GO
IF YOU DID NOT TWINKLE SO
```

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

