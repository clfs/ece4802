#!/usr/bin/env python3

from timeit import default_timer as timer
from hashlib import sha512

ENABLE_TIMING = True # global; if enabled, print crack time for each password

WORDLIST = [] # global; lines in dictionary.txt
HASHLIST = [] # global; hashes for dictionary.txt

class PasswordDetails:
    def __init__(self, rounds, salt, hash_data):
        self.rounds     = rounds
        self.salt       = salt
        self.hash_data  = hash_data

def crack_passwords(passwords_from_file):
    """Return plaintext passwords recovered from `passwords.txt`."""
    global WORDLIST
    global HASHLIST
    with open('dictionary.txt', 'r') as fh:
        WORDLIST = [line.rstrip('\r\n') for line in fh.readlines()]
    HASHLIST = [my_hash(word, 5000, '') for word in WORDLIST]
    plaintexts = [crack(password) for password in passwords_from_file]
    return plaintexts

def my_hash(message, rounds, salt):
    """SHA-512 hash with rounds and salt parameters."""
    # first round
    digest = sha512((salt + message).encode('utf-8')).hexdigest()
    # remaining rounds
    for _ in range(rounds-1):
        digest = sha512(digest.encode('utf-8')).hexdigest()
    return digest

def parse(password_line):
    """Parse the password line into a PasswordDetails class."""
    fields = password_line.split('$')
    # Custom rounds with salt
    if password_line.count('$') == 4:
        (_, _, rounds, salt, hash_data) = fields
        rounds = int(rounds.strip('rounds='))
    # Default rounds without salt
    elif '$$' in password_line:
        (_, _, _, hash_data) = fields
        rounds, salt = 5000, ''
    # Default rounds with salt
    else:
        (_, _, salt, hash_data) = fields
        rounds = 5000
    return PasswordDetails(rounds, salt, hash_data)

def crack(password_line):
    global ENABLE_TIMING
    start = timer()
    ################## Start timed block
    details = parse(password_line)
    if details.salt == '' and details.rounds == 5000: # weakest policy
        pt = '{:12}'.format(WORDLIST[HASHLIST.index(details.hash_data)])
    else: # either salted policy
        for word in WORDLIST:
            hash_attempt = my_hash(word, details.rounds, details.salt)
            if hash_attempt == details.hash_data:
                pt = '{:12}'.format(word); break
    ################## End timed block
    end = timer()
    if ENABLE_TIMING: pt += '\t{} sec'.format(end - start)
    return pt

with open('passwords.txt', 'r') as fh:
    plaintexts = \
        crack_passwords([line.rstrip('\r\n') for line in fh.readlines()])
    print('\n'.join(plaintexts))

