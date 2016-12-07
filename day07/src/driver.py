import argparse
import sys
import re

def supports(string):


    print string
    m = re.split('\[.*\]', string)
    print m
    return
    
    split = string.split('[')

    r = ""
    for s in split:
        print "s: %s" % s
        i = s.rfind(']')
        print "i:%d" % i
        
        if i == -1:
            r += s
            continue
        r += s[i:]
    print "%s\n\n%s" % (string, r)

    charsWeCharAbout = r

    for i in range(len(charsWeCharAbout)):
        try:
            c1 = r[i]
            c2 = r[i+1]
            c3 = r[i+2]
            c4 = r[i+3]

            if c1 == c4 and c2 == c3 and c1 != c2:
                tt = "%s%s%s%s" % (c1, c2, c3, c4)
                print string
                print string.replace(tt, "___%s___"%tt)
                print "True: %s%s == %s%s\n\n" % (c1, c2, c3, c4)
                return 1
        except:
            continue
 #   print "\n\n"
    return 0
    

def main(filename, second):
    inputs = [ "abba[mnop]qrst",
               'abcd[bddb]xyyx',
               'aaaa[qwer]tyui',
               'ioxxoj[asdfgh]zxcvbn',
               'wysextplwqpvipxdv[srzvtwbfzqtspxnethm]syqbzgtboxxzpwr[kljvjjkjyojzrstfgrw]obdhcczonzvbfby[svotajtpttohxsh]cooktbyumlpxostt',
               'emzopymywhhxulxuctj[dwwvkzhoigmbmnf]nxgbgfwqvrypqxppyq[qozsihnhpztcrpbdc]rnhnakmrdcowatw[rhvchmzmyfxlolwe]uysecbspabtauvmixa',
               'qujnmepaefnkxgrrg[yxdnlyihixwasibuy]qtmnryswxwzkuqw[ozuwcixlzlbiacytv]oylpudpmjaqgwfqvsb[wljtqzfawkmrnkgkvla]kgdvfppcbpyazklfdk']
    supports('qujnmepaefnkxgrrg[yxdnlyihixwasibuy]qtmnryswxwzkuqw[ozuwcixlzlbiacytv]oylpudpmjaqgwfqvsb[wljtqzfawkmrnkgkvla]kgdvfppcbpyazklfdk')


    return
    with open(filename) as f:
        firstCount = 0
        for l in f.readlines():
            count += supports(l.strip())

    print "Answer: %d" % count

     
if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('filename')
    parser.add_argument('--second', action='store_true')
    args = parser.parse_args()

    main(args.filename, args.second)












         
