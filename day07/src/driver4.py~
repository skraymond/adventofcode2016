import argparse
import sys
import re


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def supports(string):

    r = ""
    doRec = True
    for let in string:
        if let == ']' and not doRec:
            doRec = True

            r += "]"
            continue
        if let == '[' and doRec:
            doRec = False
            r += "["
            continue
        if doRec:
            r += let

    if doesit(r):
        return 1
    else:
        return 0

    
def rSupport(string):

    r = ""
    doRec = False
    for let in string:
        if let == '[' and not doRec:
            doRec = True
            r += "["
            continue
        if let == ']' and  doRec:
            doRec = False

            r += "]"
            continue
        if doRec:
            r += let

    print string
    print r
    print "\n\n"
    
    if doesit(r):
        return 0
    else:
        return 1
    

def doesit(r):
    for i in range(len(r)-3):
        try:
            c1 = r[i]
            c2 = r[i+1]
            c3 = r[i+2]
            c4 = r[i+3]

            if c1 == c4 and c2 == c3 and c1 != c2:
                tt = "%s%s%s%s" % (c1, c2, c3, c4)
#                cl = string.replace("[", "%s%s[" % (bcolors.BOLD, bcolors.FAIL))
#                cl = cl.replace("]", "%s%s]%s" % (bcolors.BOLD, bcolors.FAIL, bcolors.ENDC))
                # print cl
#                cl = string.replace(tt, "___%s___" % tt)
#                cl = cl.replace("[", "%s%s[" % (bcolors.BOLD, bcolors.FAIL))
#                cl = cl.replace("]", "%s%s]%s" % (bcolors.BOLD, bcolors.FAIL, bcolors.ENDC))

#                print cl
                return True
#                print "True: %s%s == %s%s\n\n" % (c1, c2, c3, c4)



        except Exception as e:
            print e
            continue
#    cl = string.replace("[", "%s%s[" % (bcolors.BOLD, bcolors.FAIL))
#    cl = cl.replace("]", "%s%s]%s" % (bcolors.BOLD, bcolors.FAIL, bcolors.ENDC))
#    print cl


 #   print "\n\n"
    return False

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
#    supports('gmmabzkwsehkwjnevvd[uuzdntitdazeykwek]aebpajrwpyknqgx[kczhcuveeawmdiwljzl]ugwigmilwkczrcqnfo[piezzmfwnfdhnlbranp]qhremthdwdegacvptfe')

    count = 0

    ll = []
    with open(filename) as f:
        for l in f.readlines():
            i = supports(l.strip())
            if i == 1:
                ll.append(l)

    count = 0
    print "ll: %d" % len(ll)
    for l in ll:
        count += rSupport(l)


                
    print "Answer: %d" % count


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('filename')
    parser.add_argument('--second', action='store_true')
    args = parser.parse_args()

    main(args.filename, args.second)
