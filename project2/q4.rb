#!/usr/bin/env ruby

require 'openssl'

pt = 0x48656c6c6f212121
ct = 0xd52bd481f21e25a1

des = OpenSSL::Cipher::Cipher.new 'des-ede3'
des.decrypt

for k in (0...9223372036854775807)
    des.key = k.to_s
    break if des.update(ct) + des.final == pt
end
        
puts k
