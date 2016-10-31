#!/usr/bin/env ruby

def break_caesar(pt)
    alphabet = *('A'..'Z')
    for k in 0..25
        puts k, pt.tr(alphabet.join, alphabet.rotate(k).join)
    end
end

break_caesar('AOLLULTFRUVDZAOLZFZALT')
