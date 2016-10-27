m = 'AOLLULTFRUVDZAOLZFZALT'
a = *('A'..'Z')
for k in 0..25
    puts a[k], m.tr(a.join, a.rotate(k).join)
end
