#!/usr/bin/env python3

from timeit import default_timer as timer
from binascii import hexlify
from hashlib import sha512

ENABLE_TIMING = False # global; if enabled, print crack time for each password

WORDLIST = [] # global; lines in dictionary.txt
HASHLIST = [] # global; hashes for dictionary.txt

class PasswordDetails:
    """Class that describes password policy as fields."""
    def __init__(self, rounds, salt, hash_data):
        self.rounds     = rounds
        self.salt       = salt
        self.hash_data  = hash_data

def crack_passwords(passwords_from_file):
    """Return plaintext passwords recovered from `passwords.txt`."""
    global WORDLIST, HASHLIST
    with open('dictionary.txt', 'r') as fh:
        WORDLIST = [line.rstrip('\r\n') for line in fh.readlines()]
    HASHLIST = [my_hash(word, 5000, '') for word in WORDLIST]
    print('\n'.join(HASHLIST))
    plaintexts = [brute(password) for password in passwords_from_file]
    return plaintexts

def my_hash(message, rounds, salt):
    """SHA-512 hash with rounds and salt parameters."""
    digest = sha512((salt + message).encode('utf-8')).hexdigest() # first round
    for _ in range(rounds-1): # remaining rounds
        digest = sha512(digest.encode('utf-8')).hexdigest()
    return digest # potential speed-up without .encode() and .hexdigest()?

def parse(line):
    """Parse the password line into a PasswordDetails class."""
    fields = line.split('$')
    # Custom rounds with salt
    if line.count('$') == 4:
        (_, _, rounds, salt, hash_data) = fields
        rounds = int(rounds.strip('rounds='))
    # Default rounds without salt
    elif '$$' in line:
        (_, _, _, hash_data) = fields
        rounds, salt = 5000, ''
    # Default rounds with salt
    else:
        (_, _, salt, hash_data) = fields
        rounds = 5000
    return PasswordDetails(rounds, salt, hash_data)

def brute(line):
    """Return the plaintext that generates the given `password_line`."""
    global ENABLE_TIMING
    start = timer()
    ################## Start timed block
    detals = parse(line) # minor speed-up by fetching fields only once
    salt, rounds, hash_data = details.salt, details.rounds, details.hash_data
    if salt == '': # weakest policy
        pt = '{:12}'.format(WORDLIST[HASHLIST.index(hash_data)])
    else: # either salted policy
        for word in WORDLIST:
            if my_hash(word, rounds, salt) == hash_data:
                pt = '{:12}'.format(word); break
    ################## End timed block
    end = timer()
    if ENABLE_TIMING: pt += '\t{} sec'.format(end - start)
    return pt

def main():
    with open('passwords.txt', 'r') as fh:
        plaintexts = \
            crack_passwords([line.rstrip('\r\n') for line in fh.readlines()])
        print('\n'.join(plaintexts))
    return

if __name__ == '__main__':
    main()
