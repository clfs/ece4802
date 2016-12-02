#!/usr/bin/env python3

def wrapper(a, b, c, d):
    print('{:>12} {:>12} {:>12} {:>12}'.format(a, b, c, d))
    return

def modexp(b, e, m):
    x = 1
    wrapper('x', 'b', 'e', 'm')
    wrapper(x, b, e, m)
    while e > 0:
        if e % 2: x = (x * b) % m
        b = (b * b) % m
        e >>= 1
        wrapper(x, b, e, m)
    return x

def main():
    tests = [{'a': 235973, 'e': 456789, 'p': 583903},
             {'a': 984327457683, 'e': 2153489582, 'p': 994348472629}]
    for t in tests:
        a, e, p = t['a'], t['e'], t['p']
        assert modexp(a, e, p) == pow(a, e, p)
    print("Success!")
    return

if __name__ == '__main__':
    main()
