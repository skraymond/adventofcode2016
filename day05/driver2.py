import md5

num = 'abc'
num = 'wtnhxymk'

print format(0xfff, '02x')
r = { 0:' ', 1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' '}
count = 0
i = 0
while count != 8:
    dg = md5.new(num + str(i)).hexdigest()
    i+=1
    if dg.startswith('00000'):
        pos = 0
        try:
            pos = int(dg[5])
        except:
            continue
        c = dg[6]
        if pos not in r:
            continue
        if r[pos] == ' ':
            r[pos] = c
            print r
            count +=1 

print "done: " +str(r)
rt = ""
for i in range(8):
    rt += r[i]

print rt



