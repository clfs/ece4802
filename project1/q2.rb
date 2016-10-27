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

# create hash
h = Hash[('A'..'Z').to_a.product([0])]
# fill hash
ct.scan(/\w/).join.each_char{|c| h[c] += 1}
# print the sorted hash
puts h.sort_by{|k,v| v}.reverse.to_h

=begin

ct_f = 'ENFPIGBVWMLQAYCTHUSROZDXKJ' # code above
en_f = 'ETAOINSHRDLCUMWFGYPBVKJXQZ' # wikipedia

# this doesn't work, so we need some fixes
puts ct.tr(ct_f, en_f)

# RITTRE is probably LITTLE, and the word length tips us off:

# NVIFABE NVIFABE BINNBE MNWL
# TWINKLE TWINKLE LITTLE STAR

# PGV I VGFCEL VPWN YGQ WLE
# HOW I WONDER WHAT YOU ARE

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key      = 'KLD*ENO*I**RST*HU****WA*Y*'

# Still missing some, but we can fill in:
puts ct.tr(alphabet, key)

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key      = 'KLDMENOPI**RSTBHUCFGVWA*YZ'

puts ct.tr(alphabet, key)

=end
