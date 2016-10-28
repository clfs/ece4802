ct = %{
NVIFABE NVIFABE BINNBE MNWL
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
IS YGQ CIC FGN NVIFABE MG
}

# Part A

h = Hash.new(0)                         # create hash
ct.scan(/\w/).each{|c| h[c] += 1}       # fill hash; letters only
puts h.sort_by{|k,v| v}.reverse.to_h    # sort, print hash

# Part B

ct_freq = 'ENFPGIBVWMLQAYCTHRSUOZDJKX'
en_freq = 'ETAOINSHRDLCUMWFGYPBVKJXQZ' # via wikipedia
puts ct.tr(ct_freq, en_freq)

# NVIFABE NVIFABE BINNBE MNWL
# TWINKLE TWINKLE LITTLE STAR

# PGV I VGFCEL VPWN YGQ WLE
# HOW I WONDER WHAT YOU ARE

ct_alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
pt_alph = 'KLDMENOPI**RSTBHUCFGVWA*YZ'
puts ct.tr(ct_alph, pt_alph)
