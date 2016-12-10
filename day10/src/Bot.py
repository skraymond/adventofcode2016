class Bot:

    def __init__(self, num, searchingFor=None):
        self.botnum = num
        self.vals = []
        self.instructions = {'hi': '', 'lw': ''}
        self.searchFor = searchingFor
        
    def __str__(self):
        n1 = -1
        n2 = -1
        if len(self.vals) == 2:
            n1, n2 = self._maxmin(self.vals[0], self.vals[1])
        if len(self.vals) == 1:
            n1 = self.vals[0]
        s = "%s with (%d %d) with %d instructions"
        return s % (self.botnum, n1, n2, len(self.instructions))
        
    def addValue(self, value):
        self.vals.append(int(value.strip()))
        if len(self.vals) > 2:
            err = "bot %s had two value: %s"
            err = err % (self.botnum, ', '.join(str(x) for x in self.vals))
            raise Exception(err)

    def _maxmin(self, num1, num2):
        m1 = max(num1, num2)
        m2 = min(num1, num2)
        return m1, m2
        
    def foundIt(self):
        if self.searchFor is None:
            return False
        if len(self.vals) != 2:
            return False

        i1, i2 = self._maxmin(self.searchFor[0], self.searchFor[1])
        n1, n2 = self._maxmin(self.vals[0], self.vals[1])

        return i1 == n1 and i2 == n2
                
    def needsToAct(self):
        return len(self.vals) == 2

    def instruct(self):
        if not self.needsToAct():
            raise Exception("Trying to act when not needed: %s", str(self))
        n1, n2 = self._maxmin(self.vals[0], self.vals[1])
        self.vals = []
        instructions = self.instructions
        self.instructions = {'hi': '', 'lw': ''}
        return (instructions['hi'], n1), (instructions['lw'], n2)
    
        
    def setInstruction(self, hi, lw):
        self.instructions['hi'] = hi
        self.instructions['lw'] = lw
