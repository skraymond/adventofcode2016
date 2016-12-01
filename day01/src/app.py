from Person import Person
import argparse
import sys


def main(filename, second):
    p = Person()
    lst = []
    with open(filename) as f:
        for l in f.readlines():
            for d in l.split(","):
                print "\n"
                dd = d.strip()
                turn = dd[0]
                moves = int(dd[1:])

                print "Turn %s while facing %s moving %d" % (turn, p.cardinal, moves)
                p.turn(turn)
                xyL = p.move(moves)

                print xyL
                if second:
                    for xy in xyL:
                        if xy in lst:
                            print lst
                            print "Second answer:"
                            print "%d, %d" % (xy[0], xy[1])
                            print "\nSecond Answer: %d" % (abs(xy[0]) + abs(xy[1]))
                            sys.exit(0)
                        lst.append(xy)
    if second:
        print "\nDidn't find an answer"
        sys.exit(-1)
    print "%d, %d" % (p.x, p.y)
    print lst
    print "\nAnswer: %d" % (abs(p.x) + abs(p.y))

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('filename')
    parser.add_argument('--second', action='store_true')
    args = parser.parse_args()

    main(args.filename, args.second)












         
