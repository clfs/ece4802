#!/usr/bin/env ruby

$alphabet = *('A'..'Z')

def break_caesar(pt)
    for k in 0..25
        puts k, pt.tr($alphabet.join, $alphabet.rotate(k).join)
    end
end

break_caesar('AOLLULTFRUVDZAOLZFZALT')
