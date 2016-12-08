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
    print "hello"
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


    r, v = doesit(r)
    if r:
        return 1, v
    else:
        return 0, None

    
def rSupport(string, vvv):

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

    for v in vvv:
        if v in r:
            return 1
    return 0

# > 140


def doesit(r):
    print "do it"
    gd = []
    for i in range(len(r)):        
        try:
            c1 = r[i]
            c2 = r[i+1]
            c3 = r[i+2]

            if c1 == c3 and c1 != c2:
                print "True: %s%s%s\n\n" % (c1, c2, c3)
                gd.append("%s%s%s" % (c2, c1, c2))

        except Exception as e:
            print e
            continue
    if len(gd) > 0:
        return True, gd
    return False, None

# 86-123


def main(filename, second):
    count = 0

    ll = []
    with open(filename) as f:
        for l in f.readlines():
            i, v = supports(l.strip())
            if i == 1:
                ll.append((l.strip(), v))

    count = 0

    for l, v in ll:
        count += rSupport(l, v)

 
    print "ll: %d" % len(ll)               
    print "Answer: %d" % count


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('filename')
    parser.add_argument('--second', action='store_true')
    args = parser.parse_args()

    main(args.filename, args.second)
