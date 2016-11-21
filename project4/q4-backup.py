#!/usr/bin/env python3

import time
from enum import Enum
from hashlib import sha512

WORDLIST = [] # global; lines in dictionary.txt
HASHLIST = [] # global; hashes for dictionary.txt

class Policy(Enum):
    default_rounds_no_salt      = 1
    default_rounds_with_salt    = 2
    custom_rounds_with_salt     = 3

class PasswordDetails:
    def __init__(self, policy, algid, rounds, salt, hash_data):
        self.policy     = policy
        self.algid      = algid
        self.rounds     = rounds
        self.salt       = salt
        self.hash_data  = hash_data

def crack_passwords(passwords_from_file):
    """Return plaintext passwords recovered from `passwords.txt`."""
    global WORDLIST
    global HASHLIST
    with open('dictionary.txt', 'r') as fh:
        WORDLIST = [line.rstrip('\r\n') for line in fh.readlines()]
    HASHLIST = [my_hash(word) for word in WORDLIST]
    plaintexts = [crack(password) for password in passwords_from_file]
    return plaintexts

def my_hash(message, rounds=None, salt=None):
    """SHA-512 hash with optional and defaulting rounds and salt parameters."""
    if rounds is None: rounds = 5000
    if salt is None: salt = ''
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
        policy = Policy.custom_rounds_with_salt
        (_, algid, rounds, salt, hash_data) = fields
        rounds = int(rounds.strip('rounds='))
    # Default rounds without salt
    elif '$$' in password_line:
        policy = Policy.default_rounds_no_salt
        (_, algid, _, hash_data) = fields
        rounds = 5000
        salt = ''
    # Default rounds with salt
    else:
        policy = Policy.default_rounds_with_salt
        (_, algid, salt, hash_data) = fields
        rounds = 5000
    return PasswordDetails(policy, algid, rounds, salt, hash_data)

def crack(password_line):
    details = parse(password_line)
    if details.policy == Policy.default_rounds_no_salt:
        print("Found = {}".format(WORDLIST[HASHLIST.index(details.hash_data)]))
        return WORDLIST[HASHLIST.index(details.hash_data)]
    else: # either policy that includes salt
        for word in WORDLIST:
            hash_attempt = my_hash(word, details.rounds, details.salt)
            if hash_attempt == details.hash_data:
                print("Found = {}".format(word))
                return word
    return "ERROR - No candidate found."

with open('passwords.txt', 'r') as fh:
    plaintexts = \
        crack_passwords([line.rstrip('\r\n') for line in fh.readlines()])
    print('\n'.join(plaintexts))
