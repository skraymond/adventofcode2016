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

    def setX(self, value, diff):
        gettr, settr, mult = self.mover[self.cardinal]
        movedThrough = []

        print "x : cur: %d, value: %d, mult: %d" % (self.y, diff, mult)
        for i in range(1, diff+1):
            movedThrough.append((self.x + (i * mult), self.y))
            
        self.x = value
        return movedThrough
            
    def setY(self, value, diff):
        gettr, settr, mult = self.mover[self.cardinal]
        movedThrough = []

        print "y : cur: %d, value: %d, mult: %d" % (self.y, diff, mult)
        for i in range(1, diff+1):
            movedThrough.append((self.x, self.y + (i * mult)))
        
        gettr, settr, mult = self.mover[self.cardinal]
        self.y = value
        return movedThrough

    def getX(self):
        return self.x
        
    def getY(self):
        return self.y
                       
    def turn(self, direction):
        cur = self.cardinal
        self.cardinal = turn[cur][direction]
#        print "Started %s turned %s now %s" % (cur, direction, self.cardinal)
        
    def move(self, steps):
        gettr, settr, mult = self.mover[self.cardinal]

        return settr(gettr() + (mult * steps), steps)
        
