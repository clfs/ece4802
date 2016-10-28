from itertools import chain

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def alphabet_add(x, y):
    return ALPHABET[(ALPHABET.index(x) + ALPHABET.index(y)) % 26]

def alphabet_sub(x, y):
    return ALPHABET[(ALPHABET.index(x) - ALPHABET.index(y)) % 26]

def gen(kw, pt):
    return chain(kw, pt)

def enc(kw, pt):
    ct = []
    k = gen(kw, pt)
    for pt_char, k_char in zip(pt, k):
        ct.append(alphabet_add(pt_char, k_char))
    return ''.join(ct)

def dec(kw, ct):
    pt = []
    k = gen(kw, pt)
    for ct_char, k_char in zip(ct, k):
        pt.append(alphabet_sub(ct_char, k_char))
    return ''.join(pt)
