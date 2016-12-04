from RoomNum import RoomNum

def test_one():
    r = RoomNum('  aaaaa-bbb-z-y-x-123[abxyz]  ')

    assert r.section == 123, "Section number was wrong."
    assert r.checkSum == 'abxyz', 'Checksum was %s, suppose to be %s' % (r.checkSum, 'abxyz')
    assert len(r.encSecs) == 5, "Encrypted sections length wrong."

def test_nine():
    r = RoomNum('  aaaaa-bbb-z-y-x-123[abxyz]  ')
    assert r.countMap['a'] == 5
    assert r.countMap['b'] == 3
    assert r.countMap['x'] == 1
    assert r.countMap['y'] == 1
    assert r.countMap['z'] == 1
    assert len(r.countMap) == 5

def test_ten():
    r = RoomNum('  aaaaa-bbb-z-y-x-123[abxyz]  ')
    assert ('a', 5) in r.totals
    assert ('b', 3) in r.totals
    assert ('x', 1) in r.totals
    assert ('y', 1) in r.totals
    assert ('z', 1) in r.totals
    assert len(r.totals) == 5

    
def test_two():
    r = RoomNum('  aaaaa-bbb-z-y-x-123[abxyz]  ')
    assert r.isValid(), "Wrong: %s, %s, %s" % (r.isValid(), str(r.countMap), str(r.sort))


def test_three():
    r = RoomNum('a-b-c-d-e-f-g-h-987[abcde] ')
    assert r.isValid(), "Wrong: %s, %s, %s" % (r.isValid(), str(r.countMap), str(r.sort))

def test_four():
    r = RoomNum('not-a-real-room-404[oarel] ')
    assert not r.isValid(), "Wrong: %s, %s, %s" % (r.isValid(), str(r.countMap), str(r.checkSum))

def test_five():
    r = RoomNum('totally-real-room-200[decoy] ')
    assert not r.isValid(), "Wrong: %s, %s, %s" % (r.isValid(), str(r.countMap), str(r.sort))
    
    
