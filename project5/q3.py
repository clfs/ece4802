#!/usr/bin/env python3

import gensafeprime
import hashlib
import random
import binascii

random.seed(12345)              # Seed the PRNG
p = gensafeprime.generate(1024) # Generate a safe prime `p`
g = random.randint(2,p-2)       # Alice and Bob agree on a base `g`
a = random.randint(1,2**1024)   # Alice selects their `a`
b = random.randint(1,2**1024)   # Bob selects their `b`
ga = pow(g,a,p)                 # Alice computes g^a mod p
gb = pow(g,b,p)                 # Bob computes g^b mod p
ka = pow(gb,a,p)                # Alice uses Bob's `gb` to compute the key
kb = pow(ga,b,p)                # Bob uses Alice's `ga` to compute the key
assert ka == kb                 # Alice and Bob now have the same key!

# no .decode() method in python3, so weird .to_bytes() instead
key = hashlib.sha224(ka.to_bytes((ka.bit_length() + 7) // 8, 'big')).hexdigest()
print(key)
