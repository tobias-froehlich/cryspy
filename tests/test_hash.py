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

def test_ufloathash_1():
    cryspy.hash.ufloatlist = []
    cryspy.hash.ufloathashlist = []
    cryspy.hash.maxufloathash = -1

    a = fs("1.2(1)")

    h = cryspy.hash.ufloathash(a)
    assert h == 1
    assert cryspy.hash.ufloatlist == [a]
    assert cryspy.hash.ufloathashlist == [1]

    b = fs("1.4(1)")
    h = cryspy.hash.ufloathash(b)
    assert h == 2
    assert cryspy.hash.ufloatlist == [a, b]
    assert cryspy.hash.ufloathashlist == [1, 2]
   
def test_ufloathash_2():
    cryspy.hash.ufloatlist = []
    cryspy.hash.ufloathashlist = []
    cryspy.hash.maxufloathash = -1

    a = fs("1.2(1)")

    h = cryspy.hash.ufloathash(a)
    assert h == 1
    assert cryspy.hash.ufloatlist == [a]
    assert cryspy.hash.ufloathashlist == [1]

    b = fs("1.1(1)")
    h = cryspy.hash.ufloathash(b)
    assert h == 2
    assert cryspy.hash.ufloatlist == [b, a]
    assert cryspy.hash.ufloathashlist == [2, 1]

def test_ufloathash_3():
    cryspy.hash.ufloatlist = []
    cryspy.hash.ufloathashlist = []
    cryspy.hash.maxufloathash = -1

    a = fs("1.2(1)")

    h = cryspy.hash.ufloathash(a)
    assert h == 1
    assert cryspy.hash.ufloatlist == [a]
    assert cryspy.hash.ufloathashlist == [1]

    b = fs("1.4(1)")
    h = cryspy.hash.ufloathash(b)
    assert h == 2
    assert cryspy.hash.ufloatlist == [a, b]
    assert cryspy.hash.ufloathashlist == [1, 2]

    c = fs("1.3(1)")
    h = cryspy.hash.ufloathash(c)
    assert h == 3
    assert cryspy.hash.ufloatlist == [a, c, b]
    assert cryspy.hash.ufloathashlist == [1, 3, 2]

def test_ufloathash_4():
    cryspy.hash.ufloatlist = []
    cryspy.hash.ufloathashlist = []
    cryspy.hash.maxufloathash = -1

    a = fs("1.2(1)")

    h = cryspy.hash.ufloathash(a)
    assert h == 1
    assert cryspy.hash.ufloatlist == [a]
    assert cryspy.hash.ufloathashlist == [1]

    b = fs("1.4(1)")
    h = cryspy.hash.ufloathash(b)
    assert h == 2
    assert cryspy.hash.ufloatlist == [a, b]
    assert cryspy.hash.ufloathashlist == [1, 2]

    c = fs("1.0(1)")
    h = cryspy.hash.ufloathash(c)
    assert h == 3
    assert cryspy.hash.ufloatlist == [c, a, b]
    assert cryspy.hash.ufloathashlist == [3, 1, 2]

def test_ufloathash_5():
    cryspy.hash.ufloatlist = []
    cryspy.hash.ufloathashlist = []
    cryspy.hash.maxufloathash = -1

    a = fs("1.2(1)")

    h = cryspy.hash.ufloathash(a)
    assert h == 1
    assert cryspy.hash.ufloatlist == [a]
    assert cryspy.hash.ufloathashlist == [1]

    b = fs("1.4(1)")
    h = cryspy.hash.ufloathash(b)
    assert h == 2
    assert cryspy.hash.ufloatlist == [a, b]
    assert cryspy.hash.ufloathashlist == [1, 2]

    c = fs("1.5(1)")
    h = cryspy.hash.ufloathash(c)
    assert h == 3
    assert cryspy.hash.ufloatlist == [a, b, c]
    assert cryspy.hash.ufloathashlist == [1, 2, 3]

def test_ufloathash_6():
    cryspy.hash.ufloatlist = []
    cryspy.hash.ufloathashlist = []
    cryspy.hash.maxufloathash = -1

    a = fs("1.2(1)")

    h = cryspy.hash.ufloathash(a)
    assert h == 1
    assert cryspy.hash.ufloatlist == [a]
    assert cryspy.hash.ufloathashlist == [1]

    b = fs("1.4(1)")
    h = cryspy.hash.ufloathash(b)
    assert h == 2
    assert cryspy.hash.ufloatlist == [a, b]
    assert cryspy.hash.ufloathashlist == [1, 2]

    c = a
    h = cryspy.hash.ufloathash(c)
    assert h == 1
    assert cryspy.hash.ufloatlist == [a, b]
    assert cryspy.hash.ufloathashlist == [1, 2]

    d = b
    h = cryspy.hash.ufloathash(d)
    assert h == 2
    assert cryspy.hash.ufloatlist == [a, b]
    assert cryspy.hash.ufloathashlist == [1, 2]

    e = fs("1.4(1)")
    h = cryspy.hash.ufloathash(e)
    assert h == 3
    assert cryspy.hash.ufloatlist == [a, b, e]
    assert cryspy.hash.ufloathashlist == [1, 2, 3]



