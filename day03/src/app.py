from Triangle import Triangle
import argparse
import sys


def main(filename, second):
    lst = []
    count = 0
    with open(filename) as f:
        num = 1
        ll = [ [], [], [] ]
        for l in f.readlines():
            print "-----%s----" % l.strip()
            if not second:                        
                print l
                t = Triangle(l.strip())
                
                if t.isValid():
                    count+= 1
            else:
                splitz = l.strip().split()
                for i in range(3):
                    ll[i].append(splitz[i])
                if num != 0 and num % 3 == 0:
                    print ll
                    for i in range(3):
                        t = Triangle(" ".join(ll[i]))
                        if t.isValid():
                            count+= 1
                    ll = [ [], [], [] ]
            num += 1
                                    
    print "\nFirst Answer: %d" % count

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('filename')
    parser.add_argument('--second', action='store_true')
    args = parser.parse_args()

    main(args.filename, args.second)












         
