class Triangle:

    def __init__(self, sides):
        self.sd1 = int(sides.split()[0].strip())
        self.sd2 = int(sides.split()[1].strip())
        self.sd3 = int(sides.split()[2].strip())

    def isValid(self):
        valid = True
        if not self.sd1 + self.sd2 > self.sd3:
            print "%d + %d < %d" %(self.sd1, self.sd2, self.sd3)
            return False
        if not self.sd1 + self.sd3 > self.sd2:
            print "%d + %d < %d" %(self.sd1, self.sd3, self.sd2)
            return False
        if not self.sd2 + self.sd3 > self.sd1:
            print "%d + %d < %d" %(self.sd2, self.sd3, self.sd1)
            return False
        if not self.sd2 + self.sd1 > self.sd3:
            print "%d + %d < %d" %(self.sd2, self.sd1, self.sd3)
            return False
        if not self.sd3 + self.sd2 > self.sd1:
            print "%d + %d < %d" %(self.sd3, self.sd2, self.sd1)
            return False
        if not self.sd3 + self.sd1 > self.sd2:
            print "%d + %d < %d" %(self.sd3, self.sd1, self.sd2)
            return False

            
        return valid
