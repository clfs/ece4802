#!/usr/bin/env ruby

pt = 'AOLLULTFRUVDZAOLZFZALT'
alphabet = *('A'..'Z')
for key in 0..25
    puts key, pt.tr(alphabet.join, alphabet.rotate(key).join)
end
