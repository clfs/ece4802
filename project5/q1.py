#!/usr/bin/env python3

from fractions import gcd

def multGroup(n):
    return {x for x in range(n) if gcd(x, n) == 1}

def totient(n):
    return len(multGroup(n))

def yieldGen(bound, n):
    z_n = multGroup(n)
    for a in range(bound, n):
        if {pow(a, p, n) for p in z_n} == z_n:
            yield a

p841 = totient(4968) 
p842 = p841 / 4969
p843 = next(yieldGen(1000,4969))

print("8.4.1\t{}".format(p841))
print("8.4.2\t{}".format(p842))
print("8.4.3\t{}".format(p843))
