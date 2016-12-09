#!/usr/bin/env python3

import unittest
from Crypto.Random import random
from Crypto.Random.random import randint
from Crypto.PublicKey import RSA

MLEN = 256
NLEN = 1024
RLEN = NLEN-MLEN-1

def _mod_mult_inv(x, modulo):
    t1, t2, r1, r2 = 0, 1, modulo, x
    while r2 != 0:
        q = (-1 if (r1<0)!=(r2<0) else 1) * (r1 // abs(r2))
        t1, t2, r1, r2 = t2, t1-q*t2, r2, r1-q*r2
    return (t1 if t1>0 else t1+modulo)

class PaddedRSA():
    def __init__(self):
        self.N, self.e, self.d = self.gen()
    
    def gen(self):
        rsa = RSA.generate(1024)
        p = getattr(rsa.key, 'p')
        q = getattr(rsa.key, 'q')
        N = p*q
        e = 2**16 + 1 # assume phi > e, usually
        d = _mod_mult_inv(e, (p-1)*(q-1))
        return N, e, d

    def enc(self, m):
        r = randint(0, 2**RLEN)
        m2 = (r << MLEN) | m
        return pow(m2, self.e, self.N)

    def dec(self, c):
        m2 = pow(c, self.d, self.N)
        return m2 & (2**MLEN - 1)

class Tests(unittest.TestCase):
    def _rand_msg(self):
        return randint(0, 2**(MLEN//8))

    def test_enc_and_dec(self):
        """Encrypt and decrypt using own RSA"""
        m = self._rand_msg()    # generate random message
        rsa = PaddedRSA()       # initialize RSA class
        c = rsa.enc(m)          # encrypt the message
        m2 = rsa.dec(c)         # decrypt the message
        self.assertEqual(m, m2) # message should be unchanged

if __name__ == '__main__':
    unittest.main()
