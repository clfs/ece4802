### This is a template file for a simple CBCMAC for Python 3
##
##  Please implement the provided functions and assure that your code
##  works correctly for the example given below
##
##  Name: <your name>
##

from Crypto.Cipher import AES

key = b'Sixteen byte key'
iv  = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
out = b''   
m   = b'The quick brown fox jumps over the lazy doh'

""" You can use this instruction to
    encrypt using AES.
    cipher = AES.new(key)
    msg = cipher.encrypt(message)
    """



def padding(message):
    """Append padding to message in order to
       become multiple of 16 in order to fit in
       AES input"""

    # put your code here
    
    return pad

def CBCMACbasedOnAES(message, key):
    """This function computes the MAC of message using key.
       The MAC function is CBC-MAC with AES and both single-1
       padding and length strengthening provided by the
       padding function.
       key must be convertible to bytes of length 16
       message must be convertible to bytes type"""
    

    # put your code here
    
    return out

def main():
    CBCMACbasedOnAES(m, key)

    """ Two testvectors are given below:
    m1 =          b'The quick brown fox jumps over the lazy dog'
    CBC-MAC1 =    b'\x94maSb\x14\x08\x15\xef<\x8c:\xbe\xb9LF'

    m2 =          b'The quick brown fox jumps over the lazy doh'
    CBC-MAC2 =    b'|K\x8b\x06\x96K#\x1d\x87\xdd\x1e\xca\xa9o\xad\x83'
    """

if __name__ == '__main__':
    main()
