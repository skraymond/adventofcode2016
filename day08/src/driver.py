import argparse
import sys


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    
def printColor(str1ng, firstC, secondC):
    cl = str1ng.replace(firstC,
                        "%s%s[%s" % (bcolors.BOLD, bcolors.FAIL, bcolors.ENDC))
    cl = cl.replace(secondC, "%s%s]%s" % (bcolors.BOLD,
                                          bcolors.FAIL, bcolors.ENDC))
    print cl


def main(filename, second):
    lst = []
    count = 0
    for i in range(9):
        lst.append({})
        
    with open(filename) as f:
        firstCount = 0
        for l in f.readlines():
            i = 0
            for char in l:
                print i
                d = lst[i]
                if char not in d:
                    d[char] = 0
                d[char] = d[char]+1

                i += 1

    r = ""

    for l in lst:
        c = None
        i = 99        
        for key in l:
            print "%d, %d %s" % (i, l[key], key)
            if i > l[key]:                
                c = key
                i = l[key]
        r += str(c)

    print r

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('filename')
    parser.add_argument('--second', action='store_true')
    args = parser.parse_args()

    main(args.filename, args.second)












         
