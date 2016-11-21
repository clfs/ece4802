#!/usr/bin/python3

from Crypto.Cipher import AES

def pad(message):
    """Append padding to message for AES input."""
    m_len = len(message)
    s1_pad = b'\x80' + bytes(15 - (m_len % 8)) # single-1 padding
    ls_pad = (m_len*8).to_bytes(8, byteorder='big') # length strengthening
    return message + s1_pad + ls_pad

def CBCMAC_AES(message, key):
    """Compute the CBC-MAC of the message under AES."""
    enc_message = AES.new(key, AES.MODE_CBC, bytes(16)).encrypt(pad(message))
    return enc_message[-16:]

def main():
    tests = [
        {'key': b'Sixteen byte key',
         'msg': b'The quick brown fox jumps over the lazy dog',
         'mac': b'\x94maSb\x14\x08\x15\xef<\x8c:\xbe\xb9LF'},
        {'key': b'Sixteen byte key',
         'msg': b'The quick brown fox jumps over the lazy doh',
         'mac': b'|K\x8b\x06\x96K#\x1d\x87\xdd\x1e\xca\xa9o\xad\x83'}
    ]
    for t in tests:
        assert(CBCMAC_AES(t['msg'],t['key']) == t['mac'])
    print("Success!")
    return

if __name__ == '__main__':
    main()
