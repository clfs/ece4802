#!/usr/bin/env python3

import time
from enum import Enum
from hashlib import sha512

class Policy(Enum):
    """Password policies used in `passwords.txt`."""
    default_rounds_with_salt = 1
    default_rounds_no_salt = 2
    custom_rounds_with_salt = 3

def crack_passwords(passwords_from_file):
    """Return plaintext passwords recovered from `passwords.txt`."""
    with open('dictionary.txt', 'r') as fh:
        wordlist = [line.rstrip('\r\n') for line in fh.readlines()]
    hashlist = [my_hash(word) for word in wordlist]
    plaintexts = [crack(password) for password in passwords_from_file]
    return plaintexts

def my_hash(message, rounds=None, salt=None)
    """SHA-512 hash with optional and defaulting rounds and salt parameters."""
    if rounds is None:
        rounds = 5000
    if salt is None:
        salt = ''
    # first round
    digest = sha512((salt + message).encode('utf-8')).hexdigest()
    rounds -= 1
    # remaining rounds
    for range(rounds):
        digest = sha512(digest.encode('utf-8')).hexdigest()
    return digest

def categorize(password_line):
    return policy

def crack(password_line):
    return plaintext








with open('passwords.txt', 'r') as fh:
    plaintexts = \
        crack_passwords([line.rstrip('\r\n') for line in fh.readlines()])
    print(plaintexts)
