Project 1
===============================================================================

Calvin Figuereo-Supraner, ECE 4802, 11/1/16

Problem 1
-------------------------------------------------------------------------------

The script `q1.rb`  uses brute force to test all 26 keys. The output eventually
gives the key and plaintext.

```
19
THEENEMYKNOWSTHESYSTEM
```

Problem 2
-------------------------------------------------------------------------------

### Part 2a

The script `q2.rb` prints a sorted hash of letter counts in the ciphertext. The
letters J, K, and X are unused.

```
{"E"=>29, "N"=>28, "F"=>25, "P"=>24, "G"=>23, "I"=>23, "B"=>17, "V"=>14,
"W"=>13, "M"=>12, "L"=>11, "Q"=>10, "A"=>10, "Y"=>9, "C"=>8, "T"=>7, "H"=>3,
"R"=>2, "S"=>2, "U"=>2, "O"=>2, "Z"=>1, "D"=>1}
```

### Part 2b

The script `q2.rb` then replaces the characters by letter frequency. The
letters J, K, and X are placed on the end, since they are unused. This outputs:

```
THNAUSE THNAUSE SNTTSE DTRL ...
```

This is still unsolved, but could be `TWINKLE TWINKLE LITTLE STAR`. The script
`q2.rb` then replaces letters under that assumption. The output reads:

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

### Part 2c

The text is from a poem by Jane Taylor, and the missing words are below.

```
In the dark blue sky you keep,
And often through my curtains peep,
For you never shut your eye
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveller in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.
```

Problem 3
-------------------------------------------------------------------------------

### Part 3b

- Gen(kw, pt) outputs a keystream containing the keyword and plaintext.
- Enc(kw, pt) encrypts a message `pt` using the keyword `kw`; (p + k) % 26
- Dec(kw, ct) decrypts a message `ct` using the keyword `kw`; (c - k) % 26

### Part 3c

The script `q3.py` implements the autokey cipher. As verification, it outputs:

```
> enc('WPI', 'LEHRUNDKUNST')
HTPCYUUEHQCN
> dec('WPI', 'HTPCYUUEHQCN')
LEHRUNDKUNST
```

### Part 3d

```
> dec('PLATO', 'CZGHCQRKSRJRIWXTDYFCFWYQ')
NOGOODDEEDGOESUNPUNISHED
```

Problem 4
-------------------------------------------------------------------------------

> Another autokey cipher by Vigenere uses the letters of the ciphertext instead
> of the plaintext to form new key letters:
>
> ```
> plaintext     l e h r u n d k u n s t
> key           w p i h t p y n c b x w
> ciphertext    H T P Y N C B X W O P P
> ```

### Part 4a

> Show that this is a much weaker cipher than the other: Explain a brute force
> attack that can recover most of the plaintext quickly.

### Part 4b

> Decrypt the following ciphertext that has been encrypted with the above
> method. It is ok to miss the first few letters.

```
NEASJFINVCMMZJPQKSQXIKXJBZXLXO
```

