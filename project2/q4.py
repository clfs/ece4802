#!/usr/bin/env python3

from Crypto.Cipher import DES
from joblib import Parallel, delayed  
import binascii
import struct

pt = binascii.unhexlify('48656c6c6f212121')
ct = binascii.unhexlify('d52bd481f21e25a1')

keyspace = 1 << 32
n_cpus = 8
chunk_size = int(keyspace/n_cpus)

def check(cpu):
    for k in range(chunk_size * cpu, chunk_size * (cpu+1)):
        if DES.new(struct.pack('>Q',k), DES.MODE_ECB).encrypt(pt) == ct:
            return k

keys = Parallel(n_jobs=n_cpus)(delayed(check)(cpu) for cpu in range(n_cpus))

for k in keys:
    if k is not None:
        with open('answer.txt', 'w') as f:
            f.write(str(hex(k))+'\n')
        break
