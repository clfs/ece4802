#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util import Counter

names = ['ecb', 'cbc', 'ctr']
modes = [AES.MODE_ECB, AES.MODE_CBC, AES.MODE_CTR]

with open('Gompei.bmp','rb') as in_file:

    # find size of header
    in_file.seek(10)
    offset = int.from_bytes(in_file.read(4),'little')

    # 3x: read data in chunks, encrypt and write to new file
    for name, mode in zip(names, modes):
       
        # open new file for writing
        with open('Gompei_{}.bmp'.format(name),'wb') as out_file:

            # separate header and content
            in_file.seek(0)
            header = in_file.read(offset)
            in_file.seek(offset)
            content = in_file.read()
            # out_file.write(header)

            key = b'0' * AES.block_size
            iv = key

            if mode == AES.MODE_CTR:
                aes = AES.new(key, mode, iv, counter=Counter.new(128))
            else:
                aes = AES.new(key, mode, iv)
            
            encrypted_content = aes.encrypt(content)
            
            out_file.write(header)
            out_file.write(encrypted_content)

        # read/write data in chunks of 64 bit
	# funky b/c python has no do-while
        #buf = in_file.read(16)
        #while len(buf)==16:
        #    out_file.write(buf)
        #    buf = in_file.read(16)

        #** Insert your code to encrypt the data ********
        #** using the appropriate mode of encryption ****
        #** above this point
        
        # write final chunk of data (not necessary since size is multiple of 16)
        #out_file.write(buf)

    # files are automatically closed after leaving the "with"
