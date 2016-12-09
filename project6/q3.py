#!/usr/bin/env python3

import unittest
from Crypto import Random
from Crypto.Util.number import getPrime
from Crypto.PublicKey import RSA

# problem 3 parameters
PADDED_MSG_LEN_BITS     = 256
PADDED_MSG_LEN_BYTES    = PADDED_MSG_LEN_BITS // 8
MOD_LEN_BITS            = 1024
MOD_LEN_BYTES           = MOD_LEN_BITS // 8

random = Random.new() # set up new RNG

class PublicKey():
    def __init__(self, n, e):
        self.n = n
        self.e = e

class PrivateKey():
    def __init__(self, n, d):
        self.n = n
        self.d = d

class PaddedRSA():
    """
    Implements padded RSA as introduced in class.

    Public methods:
    .enc()      Encrypt a message
    .dec()      Decrypt a message

    Private methods:
    ._gen()     Generate a public key and private key
    ._pad()     Pad a message prior to encryption
    ._unpad()   Unpad a message after decryption
    """

    def __init__(self, msglen, modlen):
        """
        .msglen Final message `m` length in bits
        .modlen Product of primes `N` length in bits
        .kpub   Public key
        .kprv   Private key
        """
        self.msglen = msglen
        self.modlen = modlen
        self.kpub, self.kprv = self._gen()
    
    def enc(self, pt):
        padpt = self._pad(pt)
        return pow(padpt, self.kpub.e, self.kpub.n)

    def dec(self, ct):
        padpt = pow(ct, self.kprv.d, self.kprv.n)
        return self._unpad(padpt)

    def _mod_mult_inv(self, x, modulo):
        def _div(n, d):
            return (-1 if (n < 0) != (d < 0) else 1) * (n // abs(d))
        t1, t2, r1, r2 = 0, 1, modulo, x
        while r2 != 0:
            q = _div(r1, r2)
            t1, t2, r1, r2 = t2, t1-q*t2, r2, r1-q*r2
        if r1 > 1:
            raise ValueError('Not invertible')
        if t1 < 0:
            t1 += modulo
        return t1

    def _gen(self):
        p = getPrime(self.modlen // 2, random.read)
        q = getPrime(self.modlen // 2, random.read)
        n = p*q
        e = 2**16 + 1 # assume phi > e, usually
        d = self._mod_mult_inv(e, (p-1)*(q-1))
        return PublicKey(n, e), PrivateKey(n, d)

    def _pad(self, msg):
        padlen = self.modlen // 8 - len(msg)
        return int.from_bytes(random.read(padlen) + msg, 'big')

    def _unpad(self, msg):
        return msg.to_bytes(self.modlen // 8 + 1, 'big')[-self.msglen // 8:]

class Tests(unittest.TestCase):
    def _rand_msg(self): # TODO fix to return messages of diff lengths
        #return random.read(256 // 8)
        return random.read(30)

    def test_enc_and_dec(self):
        """Encrypt and decrypt using own RSA"""
        msg = self._rand_msg()          # generate random message
        rsa = PaddedRSA(256,1024)       # initialize RSA class
        ct = rsa.enc(msg)               # encrypt the message
        pt = rsa.dec(ct)                # decrypt the message
        self.assertEqual(msg, pt)       # message should be unchanged

    def test_pad_and_unpad(self):
        """Pad then unpad the message"""
        msg = self._rand_msg()          # generate random message
        rsa = PaddedRSA(256,1024)       # initialize RSA class
        self.assertEqual(msg, rsa._unpad(rsa._pad(msg))) # message should be unchanged

if __name__ == '__main__':
    unittest.main()
