import traceback
import pdb
import sys

class RoomNum:

    def __init__(self, encName):

        self.countMap = {}
        self.totals = []
        self.sort = {}
        self.encName = encName.strip()
        sections = self.encName.split('-')

        self.encSecs = sections[:len(sections)-1]
        checkSec = sections[len(sections) - 1]
        self.section = int(checkSec.split('[')[0])
        self.checkSum = checkSec.split('[')[1][:len(checkSec.split('[')[1])-1]

        self._count()
        self._sort()

    def _count(self):
        for sec in self.encSecs:
            for let in sec:
                if not let in self.countMap:
                    self.countMap[let] = 0
                self.countMap[let] += 1
        for key in self.countMap:
            self.totals.append((key, self.countMap[key]))
            
    def _sort(self):
        return
        
        
    def isValid(self):

        try:
            mp = self.countMap
            first = self.checkSum[0]
            if first not in self.countMap:
                return False
            lrg = mp[first]
            for key in self.countMap:
                if key == first:
                    continue
                if mp[key] > lrg:
#                    print "(%s, %d) > (%s, %d)"% (key, mp[key], first, lrg)
                    return False
            for i in range(len(self.checkSum)-1):
                cur = self.checkSum[i]
                nxt = self.checkSum[i+1]
                if mp[cur] < mp[nxt]:
#                    print "(%s, %d) < (%s, %d)" % (cur, mp[cur], nxt, mp[nxt])
                    return False
                if mp[cur] ==  mp[nxt] and cur > nxt:
#                    print "(%s, %d) == (%s, %d)" % (cur, mp[cur], nxt, mp[nxt])
                    return False                    
            
        except Exception as e:
#            pdb.set_trace()
#            print "Errror:"
#            print e
#            traceback.print_exc(file=sys.stdout)
            return False
        return True

    def decrypt(self):
        r = ""
        for name in self.encSecs:
            for let in name:
                new = ord(let)
                for i in range(self.section):
                    new += 1
                    if new == ord('z') + 1:
                        new  = ord('a')
                r += chr(new)

            r += ' '
        
        return r.strip()
