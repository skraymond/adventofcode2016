import argparse
import sys
from screen import Screen

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
    scrn = Screen(7,3)
    scrn = Screen(50,6)

    count = 0
    with open(filename) as f:
        for l in f.readlines():
            """
            rect 19x1
            rotate column x=44 by 2
            rotate row y=5 by 10
            """
            print "\n%%%%%%%%%%%%%%%%%%%%%%%%%\n"
            cmd = l.strip()
            if cmd.startswith('rect'):
                zz = cmd.split(' ')
                zzz = zz[1].split('x')
                x = int(zzz[0])
                y = int(zzz[1])
                print "\n\n%s: %d, %d" % (l.strip(), x, y)
                if count != scrn.count():
                    print "err"
                    sys.exit(-1)
                print "Old count %d\n" % scrn.count()
                scrn.rec(x, y)
                count = scrn.count()
                scrn.printt()
                print "new count: %d\n" % scrn.count()

            elif cmd.startswith("rotate column"):
                zz = cmd.split(' ')
                start = int(zz[2].split('=')[1])
                amnt = int(zz[4])
                cmd = zz[2].split('=')[0]

                s = "\n\n--%s: %d, %d" % (l.strip(), start, amnt)
                print s
                c1 = scrn.count()
                scrn.rotate_column(start, amnt)
                scrn.printt()
                c2 = scrn.count()

                if c1 != c2:
                    print "crap"
                    sys.exit(-2)

            elif cmd.startswith("rotate row"):
                zz = cmd.split(' ')
                start = int(zz[2].split('=')[1])
                amnt = int(zz[4])
                cmd = zz[2].split('=')[0]

                c1 = scrn.count()
                print "\n\n++%s: %d, %d" % (l.strip(), start, amnt)
                scrn.rotate_row(start, amnt)
                
                c2 = scrn.count()
                scrn.printt()

                if c1 != c2:
                    print "crap"
                    sys.exit(-2)
                
            else:
                print "da fuck?"
                sys.exit(-1)

    print "\n\n"
    scrn.printt()

    print "\n\n%d" % scrn.count()



if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('filename')
    parser.add_argument('--second', action='store_true')
    args = parser.parse_args()

    main(args.filename, args.second)


#    > 101
