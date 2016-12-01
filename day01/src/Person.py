turn = {'N': {'L': 'W',
              'R': 'E'},
        'E': {'L': 'N',
              'R': 'S'},
        'S': {'L': 'E',
              'R': 'W'},
        'W': {'L': 'S',
              'R': 'N'}}


class Person:

    def __init__(self):
        self.cardinal = 'N'
        self.x = 0
        self.y = 0

        self.mover = {'N': (self.getY, self.setY, 1),
                      'E': (self.getX, self.setX, 1),
                      'S': (self.getY, self.setY, -1),
                      'W': (self.getX, self.setX, -1)}

    def setX(self, value):
        self.x = value
            
    def setY(self, value):
        self.y = value

    def getX(self):
        return self.x
        
    def getY(self):
        return self.y
                       
    def turn(self, direction):
        cur = self.cardinal
        self.cardinal = turn[cur][direction]
        print "Started %s turned %s now %s" % (cur, direction, self.cardinal)
        
    def move(self, steps):
        gettr, settr, mult = self.mover[self.cardinal]

        settr(gettr() + (mult * steps))

        
if __name__ == '__main__':
    p = Person()
    p.move(4)
    print str(p.x) + " " + str(p.y)

    p = Person()
    p.turn('R')
    p.move(4)
    print str(p.x) + " " + str(p.y)

    p = Person()
    p.turn('R')
    p.turn('R')
    p.move(4)
    print str(p.x) + " " + str(p.y)

    p = Person()
    p.turn('R')
    p.turn('R')
    p.turn('R')
    p.move(4)
    print str(p.x) + " " + str(p.y)

    p = Person()
    p.turn('L')
    p.turn('L')
    p.turn('L')
    

