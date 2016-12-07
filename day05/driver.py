import md5

num = 'abc'
num = 'wtnhxymk'

print format(0xfff, '02x')
r = ""
for i in range(10000000):
    dg = md5.new(num + str(i)).hexdigest()
    if dg.startswith('00000'):
        r += dg[5]
        print dg[5]
print r



