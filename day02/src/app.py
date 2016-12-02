from Console import Console
import argparse
import sys


def main(filename, second):
    c = Console(turnz=second)
    lst = []
    with open(filename) as f:
        for l in f.readlines():
            c.turn(l)

    ans = ""
    for num in c.code:
        ans += str(num)
    print "\nFirst Answer: %s" % ans

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('filename')
    parser.add_argument('--second', action='store_true')
    args = parser.parse_args()

    main(args.filename, args.second)












         
