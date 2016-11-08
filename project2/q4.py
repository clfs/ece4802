#!/usr/bin/env python3

from Crypto.Cipher import DES
from joblib import Parallel, delayed  
import binascii
import struct

pt = binascii.unhexlify('48656c6c6f212121')
#ct = binascii.unhexlify('d52bd481f21e25a1')
mykey = 0xee
ct = DES.new(struct.pack('>Q', mykey), DES.MODE_ECB).encrypt(pt)

keyspace = 1 << 32
cpus = 8
block_size = int(keyspace/cpus)

def check(cpu):
    for k in range(block_size * cpu, block_size * (cpu+1)):
        if DES.new(struct.pack('>Q',k), DES.MODE_ECB).encrypt(pt) == ct:
            return k

keys = Parallel(n_jobs=8)(delayed(check)(cpu) for cpu in range(cpus))

for k in keys:
    if k is not None:
        print(k)
        with open('answer.txt', 'w') as f:
            f.write(str(hex(k))+'\n')
        break
