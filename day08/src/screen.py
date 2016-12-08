import copy

class Screen:

    def __init__(self, x, y):
        self.xmax = x
        self.ymax = y
        self.grid = {}
        for i in range(x):
            for z in range(y):
                self.grid[(i, -z)] = '.'
                # print "%d,%d", (i, -z)

    def rec(self, x, y):
        for i in range(x):
            for z in range(y):
                self.grid[(i, -z)] = '#'

    def upX(self, num):
        num += 1
        if num == self.xmax:
            num = 0
        return num

    def downX(self, num):
        num -= 1
        if num == -1:
            num = self.xmax - 1

        return num

    def upY(self, num):
        num += 1
        if num > 0:
            num = -1 * (self.ymax - 1)
        return num

    def downY(self, num):
        num -= 1
        if num == -1 * (self.ymax):
            num = 0

        return num

    def rotate_column(self, start, amount):
        original = copy.deepcopy(self.grid)

        print "start = %d", start
        for i in range(amount):
            for keyx, keyy in self.grid:
                if keyx == start:
                    s = "%d,%d" % (keyx, keyy)
                    print s
                    val = original[(keyx, self.upY(keyy))]
                    s = "org: %d, %d, %s" % (keyx, self.upY(keyy), val)
                    print s
                    self.grid[(keyx, keyy)] = val
            original = copy.deepcopy(self.grid)

    def rotate_row(self, start, amount):
        original = copy.deepcopy(self.grid)
        print "start = %d", start
        for i in range(amount):
            for keyx, keyy in self.grid:
                if keyy == start:
                    s = "%d,%d" % (keyx, keyy)
                    # print s
                    val = original[(self.downX(keyx), keyy)]
                    s = "org: %d, %d, %s" % (self.downX(keyx), keyy, val)
                    # print s
                    self.grid[(keyx, keyy)] = val
            original = copy.deepcopy(self.grid)

    def printt(self):
        for y in range(self.ymax):
            for x in range(self.xmax):
                #print "%s%s" % (self.grid[(x, -y)], "%s,%s"%(x,y)),
                print "%s" % (self.grid[(x, -y)]),
            print ""


maxX=7
maxY=3
s = Screen(maxX, maxY)

assert s.downX(0) == maxX-1, "%d"%s.downX(0)
assert s.upX(maxX-1) == 0, "%d"%s.upX(maxX-1)
assert s.upY(0) == -1 * (maxY-1), "%s" % s.upY(0)
assert s.downY(-1 * (maxY-1)) == 0, "%d" % (s.downY(-1 * (maxY-1)))

# s.printt()

s.rec(3, 2)
s.printt()

s.rotate_column(1, 1)
print "\n\nRotate:\n"
s.printt()

s.rotate_row(0, 4)
print "\n\nRotate:\n"
s.printt()

s.rotate_column(1, 1)
print "\n\nRotate:\n"
s.printt()
