import sys

sys.path.append("../src")
from Person import Person


def test_turn():
    p = Person()
    card = p.cardinal
    assert card == 'N', "Person didn't start north"

    p.turn('L')
    assert p.cardinal == 'W', "Problem starting %s turning L" % card
    card = p.cardinal

    p.turn('L')
    assert p.cardinal == 'S', "Problem starting %s turning L" % card
    card = p.cardinal

    p.turn('L')
    assert p.cardinal == 'E', "Problem starting %s turning L" % card
    card = p.cardinal

    p.turn('L')
    assert p.cardinal == 'N', "Problem starting %s turning L" % card
    card = p.cardinal

    p.turn('R')
    assert p.cardinal == 'E', "Problem starting %s turning L" % card
    card = p.cardinal

    p.turn('R')
    assert p.cardinal == 'S', "Problem starting %s turning L" % card
    card = p.cardinal

    p.turn('R')
    assert p.cardinal == 'W', "Problem starting %s turning L" % card
    card = p.cardinal

    p.turn('R')
    assert p.cardinal == 'N', "Problem starting %s turning L" % card
    card = p.cardinal


def test_move_north():
    p = Person()

    err = "Incorrect %s when testing moving %s"
    p.move(2)
    assert p.x == 0, err % ('x', p.cardinal)
    assert p.y == 2, err % ('y', p.cardinal)


def test_move_east():
    p = Person()
    p.turn('R')
    err = "Incorrect %s when testing moving %s"
    p.move(2)
    assert p.x == 2, err % ('x', p.cardinal)
    assert p.y == 0, err % ('y', p.cardinal)

    
def test_move_south():
    p = Person()
    p.turn('R')
    p.turn('R')
    err = "Incorrect %s when testing moving %s"
    p.move(2)
    assert p.x == 0, err % ('x', p.cardinal)
    assert p.y == -2, err % ('y', p.cardinal)

    
def test_move_west():
    p = Person()
    p.turn('L')
    
    err = "Incorrect %s when testing moving %s"
    p.move(2)
    assert p.x == -2, err % ('x', p.cardinal)
    assert p.y == 0, err % ('y', p.cardinal)


