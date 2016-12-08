import argparse
import sys
import re




    
def supports(string):
    m = re.split('.*\[.*\].*', string)
    print string
    print m

    r = " ".join(m)
    print "r:%s" % r
    charsWeCharAbout = r

    bad = ""
    for i in range(len(charsWeCharAbout)-3):
        try:
            c1 = r[i]
            c2 = r[i+1]
            c3 = r[i+2]
            c4 = r[i+3]

            if c1 == c4 and c2 == c3 and c1 != c2:
                tt = "%s%s%s%s" % (c1, c2, c3, c4)
#                print cl
#                print string.replace(tt, "___%s___"%tt)
#                print "True: %s%s == %s%s\n\n" % (c1, c2, c3, c4)
                return 1
            else:
                bad += "%s\n" % string
            
        except Exception as e:
            print e
            continue
    cl = string.replace("[", "%s%s[%s" % (bcolors.BOLD, bcolors.FAIL, bcolors.ENDC))
    cl = cl.replace("]", "%s%s]%s" % (bcolors.BOLD, bcolors.FAIL, bcolors.ENDC))
    print cl

        
 #   print "\n\n"
    return 0
    
# 86-123
def main(filename, second):
#    inputs = [ "abba[mnop]qrst",
#               'abcd[bddb]xyyx',
#               'aaaa[qwer]tyui',
#               'ioxxoj[asdfgh]zxcvbn',
#               'wysextplwqpvipxdv[srzvtwbfzqtspxnethm]syqbzgtboxxzpwr[kljvjjkjyojzrstfgrw]obdhcczonzvbfby[svotajtpttohxsh]cooktbyumlpxostt',
#               'emzopymywhhxulxuctj[dwwvkzhoigmbmnf]nxgbgfwqvrypqxppyq[qozsihnhpztcrpbdc]rnhnakmrdcowatw[rhvchmzmyfxlolwe]uysecbspabtauvmixa',
#               'qujnmepaefnkxgrrg[yxdnlyihixwasibuy]qtmnryswxwzkuqw[ozuwcixlzlbiacytv]oylpudpmjaqgwfqvsb[wljtqzfawkmrnkgkvla]kgdvfppcbpyazklfdk']
#    supports('qujnmepaefnkxgrrg[yxdnlyihixwasibuy]qtmnryswxwzkuqw[ozuwcixlzlbiacytv]oylpudpmjaqgwfqvsb[wljtqzfawkmrnkgkvla]kgdvfppcbpyazklfdk')
#
#
    supports('gmmabzkwsehkwjnevvd[uuzdntitdazeykwek]aebpajrwpyknqgx[kczhcuveeawmdiwljzl]ugwigmilwkczrcqnfo[piezzmfwnfdhnlbranp]qhremthdwdegacvptfe')
    return
    count = 0    
    with open(filename) as f:

        for l in f.readlines():
            i = supports(l.strip())            
            count += i
            if i == 0:
                with open('/tmp/ddd', 'a') as f:
                    f.writelines(l)
            

    print "Answer: %d" % count

     
if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('filename')
    parser.add_argument('--second', action='store_true')
    args = parser.parse_args()

    main(args.filename, args.second)












         
