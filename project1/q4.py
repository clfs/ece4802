#!/usr/bin/env python3

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def alphabet_sub(x, y):
    return ALPHABET[(ALPHABET.index(x) - ALPHABET.index(y)) % 26]

def break_autokey2(ct):
    for kw_len in range(len(ct)):
        k = 'A'*kw_len + ct[:-kw_len]
        pt = ''.join(map(alphabet_sub, ct, k))
        print(pt)
    return

break_autokey2('NEASJFINVCMMZJPQKSQXIKXJBZXLXO')
