
from Bot import Bot


def test_01():
    b = Bot('2')

    b.addValue('1')
    assert not b.needsToAct(), "Thinks it needs to act with one"
    b.addValue('   33  ')
    assert b.needsToAct(), "Thinks it doesn't need to act"
    try:
        b.getValue('233')
        assert False, "Bot accepted 3 values."
    except:
        pass

    
def test_02():
    b1 = Bot('2', (2, 3))
    b2 = Bot('1', (2, 3))
    b3 = Bot('1', (2, 3))
    b4 = Bot('1', (2, 3))

    b1.addValue('3')
    b1.addValue('2')
    b2.addValue('3')
    b2.addValue('3')
    b4.addValue('3')

    assert b1.foundIt(), "Bot didn't find it."
    assert not b2.foundIt(), "Bot didn't find it"
    assert not b3.foundIt()

    
def test_04():
    b = Bot('output 2')

    b.addValue('1')
    b.addValue('2')
    b.setInstruction('output 4', '3')

    d1, d2 = b.instruct()

    assert d1[0] == 'output 4'
    assert d1[1] == 2
    assert d2[0] == '3'
    assert d2[1] == 1

    
def test_05():
    b = Bot('2')

    b.addValue('1')
    b.addValue('2')
    b.setInstruction('3', '4')

    d1, d2 = b.instruct()

    assert d1[0] == '3'
    assert d1[1] == 2
    assert d2[0] == '4'
    assert d2[1] == 1
    
"""
value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2
"""

