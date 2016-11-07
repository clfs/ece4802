#!/usr/bin/env python3

from Crypto.Cipher import DES
import binascii
import struct

pt = binascii.unhexlify('48656c6c6f212121')
ct = binascii.unhexlify('d52bd481f21e25a1')

print(pt)
print(ct)

upper_bound = 0x0000000100000000

for k in range(1000000):
    print(k, end='\r')
    if DES.new(struct.pack('>Q', k)).encrypt(pt) == ct:
        break
