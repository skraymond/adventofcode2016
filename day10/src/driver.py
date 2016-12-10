import argparse
import sys
from Bot import Bot

lookingfor = (61, 17)
#lookingfor = (5, 2)

    
def getBot(bots, botnum):
    if botnum not in bots:
        bots[botnum] = Bot(botnum, lookingfor)
    return bots[botnum]


def foundIt(bot):
    if bot.foundIt():
        print "Found it: %s" % str(bot)
        # sys.exit(1)

        
def act(bots, b1, b2=None):

    # print "\n\n%s\n%s" % (str(b1), str(b2))
    for bot in b1, b2:
        if bot is None:
            continue
        if bot.needsToAct():
            hwIns, lwIns = bot.instruct()
            hBot = getBot(bots, hwIns[0])
            hBot.addValue(str(hwIns[1]))
            foundIt(hBot)

            lBot = getBot(bots, lwIns[0])
            lBot.addValue(str(lwIns[1]))
            foundIt(lBot)
            act(bots, hBot, lBot)

            
def main(filename, second):
    
    bots = {}

    with open(filename) as f:
        for l in f.readlines():
            l = l.strip()
            if l.startswith('value '):
                val = l.split(' ')[1]
                botnum = " ".join((l.split(' ')[4], l.split(' ')[5]))

                if botnum not in bots:
                    bots[botnum] = Bot(botnum, lookingfor)
                bots[botnum].addValue(val)
      
                # print l
                # print bots[botnum]
            elif l.startswith('bot '):
                
                botnum = 'bot ' + l.split(' ')[1]
                low = " ".join((l.split(' ')[5], l.split(' ')[6]))
                high = " ".join((l.split(' ')[6+4], l.split(' ')[7+4]))

                # print l
                # print "'%s'\t'%s'\t'%s'" % (botnum, low, high)
                if botnum not in bots:
                    bots[botnum] = Bot(botnum, lookingfor)
                
                bots[botnum].setInstruction(high, low)
                
            else:
                raise Exception("Bad instruction: %s" % l)

        b = None
        for botnum in bots:
            if bots[botnum].needsToAct():
                b = bots[botnum]

        act(bots, b)

        for botnum in bots:
            # rint botnum
            output = ['output 0','output 1','output 2']
            if botnum in output:
                print str(bots[botnum])
        
        # print bots[key]

    print "\n\n%d" % 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('filename')
    parser.add_argument('--second', action='store_true')
    args = parser.parse_args()

    main(args.filename, args.second)


#    > 101
