with open('input/offficl.input') as f:
    for l in f.readlines():

        c1 = 0
        c2 = 0
        for let in l:            
            if let == ']':
                c1 += 1
            if let == ']':
                c2 += 1
        if c1 != c2:            
            print "%d/%d. %s" % (c1, c2, l)
#        else:
#            print "%d %d" % (c1, c2)
