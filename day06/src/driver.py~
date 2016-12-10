from RoomNum import RoomNum
import argparse
import sys


def main(filename, second):
    lst = []
    count = 0
    with open(filename) as f:
        firstCount = 0
        for l in f.readlines():
            r = RoomNum(l)

            if r.isValid():
                firstCount += r.section
                print r.decrypt() + " " + str(r.section)

    print "\nFirst Answer: %d" % firstCount

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('filename')
    parser.add_argument('--second', action='store_true')
    args = parser.parse_args()

    main(args.filename, args.second)












         
