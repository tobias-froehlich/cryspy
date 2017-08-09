import cryspy
from cryspy.fromstr import fromstr as fs


def test_floathash_1():
    cryspy.hash.floatlist = []
    cryspy.hash.hashlist = []

    h = cryspy.hash.floathash(5.0)
    h1 = hash(5.0)
    assert h == h1
    assert cryspy.hash.floatlist == [5.0]
    assert cryspy.hash.hashlist  == [h1]

    h = cryspy.hash.floathash(6.0)
    h2 = hash(6.0)
    assert h == h2
    assert cryspy.hash.floatlist == [5.0, 6.0]
    assert cryspy.hash.hashlist == [h1, h2]

    h = cryspy.hash.floathash(7.0)
    h3 = hash(7.0)
    assert h == h3
    assert cryspy.hash.floatlist == [5.0, 6.0, 7.0]
    assert cryspy.hash.hashlist == [h1, h2, h3]

def test_floathash_2():
    cryspy.hash.floatlist = []
    cryspy.hash.hashlist = []

    h = cryspy.hash.floathash(5.0)
    h1 = hash(5.0)
    assert h == h1
    assert cryspy.hash.floatlist == [5.0]
    assert cryspy.hash.hashlist  == [h1]

    h = cryspy.hash.floathash(6.0)
    h2 = hash(6.0)
    assert h == h2
    assert cryspy.hash.floatlist == [5.0, 6.0]
    assert cryspy.hash.hashlist == [h1, h2]

    h = cryspy.hash.floathash(4.0)
    h3 = hash(4.0)
    assert h == h3
    assert cryspy.hash.floatlist == [4.0, 5.0, 6.0]
    assert cryspy.hash.hashlist == [h3, h1, h2]

def test_floathash_3():
    cryspy.hash.floatlist = []
    cryspy.hash.hashlist = []

    h = cryspy.hash.floathash(6.0)
    h1 = hash(6.0)
    assert h == h1
    assert cryspy.hash.floatlist == [6.0]
    assert cryspy.hash.hashlist  == [h1]

    h = cryspy.hash.floathash(5.0)
    h2 = hash(5.0)
    assert h == h2
    assert cryspy.hash.floatlist == [5.0, 6.0]
    assert cryspy.hash.hashlist == [h2, h1]

def test_floathash_4():
    cryspy.hash.floatlist = []
    cryspy.hash.hashlist = []

    h = cryspy.hash.floathash(5.0)
    h1 = hash(5.0)
    assert h == h1
    assert cryspy.hash.floatlist == [5.0]
    assert cryspy.hash.hashlist  == [h1]

    h = cryspy.hash.floathash(6.0)
    h2 = hash(6.0)
    assert h == h2
    assert cryspy.hash.floatlist == [5.0, 6.0]
    assert cryspy.hash.hashlist == [h1, h2]

    h = cryspy.hash.floathash(7.0)
    h3 = hash(7.0)
    assert h == h3
    assert cryspy.hash.floatlist == [5.0, 6.0, 7.0]
    assert cryspy.hash.hashlist == [h1, h2, h3]

    h = cryspy.hash.floathash(5.5)
    h4 = hash(5.5)
    assert h == h4
    assert cryspy.hash.floatlist == [5.0, 5.5, 6.0, 7.0]
    assert cryspy.hash.hashlist == [h1, h4, h2, h3]

    h = cryspy.hash.floathash(6.0 + cryspy.numbers.delta/2)
    h5 = hash(6.0)
    assert h == h5
    assert cryspy.hash.floatlist == [5.0, 5.5, 6.0, 7.0]
    assert cryspy.hash.hashlist == [h1, h4, h2, h3]


   

