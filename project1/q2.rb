#!/usr/bin/env ruby

ct = %{NVIFABE NVIFABE BINNBE MNWL
PGV I VGFCEL VPWN YGQ WLE
QH WOGUE NPE VGLBC MG PITP
BIAE W CIWDGFC IF NPE MAY

VPEF NPE OBWZIFT MQF IM TGFE
VPEF PE FGNPIFT MPIFEM QHGF
NPEF YGQ MPGV YGQL BINNBE BITPN
NVIFABE NVIFABE WBB NPE FITPN

NPEF NPE NLWUEBEL IF NPE CWLA 
NPWFAM YGQ SGL YGQL NIFY MHWLA
PE RGQBC FGN MEE VPIRP VWY NG TG
IS YGQ CIC FGN NVIFABE MG}

# Part 3a

h = Hash.new(0)                         # create hash
ct.scan(/\w/).each{|c| h[c] += 1}       # fill hash; letters only
puts h.sort_by{|k,v| v}.reverse.to_h    # sort, print hash

print '... Enter to continue'; gets

# Part 3b

# First attempt, using letter frequency attack
ct_freq = 'ENFPGIBVWMLQAYCTHRSUOZDJKX'
en_freq = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
puts ct.tr(ct_freq, en_freq)

print '... Enter to continue'; gets

# Second attempt, using known plaintext attack
ct_alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
pt_alph = 'KLDMENOPI**RSTBHUCFGVWA*YZ'
puts ct.tr(ct_alph, pt_alph)
