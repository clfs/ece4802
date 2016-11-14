#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util import Counter

names = ['ecb', 'cbc', 'ctr']
modes = [AES.MODE_ECB, AES.MODE_CBC, AES.MODE_CTR]

# problem specifies key and IV of zero
key = b'0' * AES.block_size
iv = key

with open('Gompei.bmp','rb') as in_file:

    # find size of header
    in_file.seek(10)
    offset = int.from_bytes(in_file.read(4),'little')

    # get image header
    in_file.seek(0)
    header = in_file.read(offset)

    # 3x: encrypt image content and write to new file
    for name, mode in zip(names, modes):
       
        # open new file for writing
        with open('Gompei_{}.bmp'.format(name),'wb') as out_file:

            # get image content, no header
            in_file.seek(offset)
            content = in_file.read()

            # encrypt content
            if mode == AES.MODE_CTR:
                aes = AES.new(key, mode, iv, counter=Counter.new(128))
            else:
                aes = AES.new(key, mode, iv)
            encrypted_content = aes.encrypt(content)
            
            # write out header and content
            out_file.write(header)
            out_file.write(encrypted_content)
