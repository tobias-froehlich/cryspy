import pytest
import sys
sys.path.append("../src/")
from cryspy import numbers as nb
import quicktions as fr
import uncertainties as uc


def approx(a, b):
    allowed_error = 1e-9
    assert isinstance(a, float), \
        "Can only compare two floats for approx equality"
    assert isinstance(b, float), \
        "Can only compare two floats for approx aquality"
    return abs(a - b) < allowed_error


def test_Mixed():
    # Create a number of type Mixed with 4 different types.
    q = fr.Fraction(2, 3)
    e = uc.ufloat(1.2, 0.1)
    i = 4
    f = 3.5
    q1 = fr.Fraction(2, 1)
    e1 = uc.ufloat(3.7, 0)
    assert isinstance(nb.Mixed(q).value, fr.Fraction)
    assert nb.Mixed(q).value == q
    assert isinstance(nb.Mixed(e).value, uc.UFloat)
    assert (nb.Mixed(e).value).n == e.n
    assert (nb.Mixed(e).value).s == e.s
    assert isinstance(nb.Mixed(i).value, int)
    assert nb.Mixed(i).value == i
    assert isinstance(nb.Mixed(f).value, float)
    assert nb.Mixed(f).value == f
    assert isinstance(nb.Mixed(q1).value, int)
    assert nb.Mixed(q1).value == 2
    assert isinstance(nb.Mixed(e1).value, uc.UFloat)
    assert nb.Mixed(e1).value == uc.ufloat(3.7, 0.0)

    # Convert a number of type Mixed to float.
    assert isinstance(float(nb.Mixed(q)), float)
    assert float(nb.Mixed(q)) == float(2 / 3)
    assert isinstance(float(nb.Mixed(e)), float)
    assert float(nb.Mixed(e)) == 1.2
    assert isinstance(float(nb.Mixed(i)), float)
    assert float(nb.Mixed(i)) == 4.0
    assert isinstance(float(nb.Mixed(f)), float)
    assert float(nb.Mixed(f)) == 3.5

    # Print a number of type Mixed as str.
    assert isinstance(nb.Mixed(q).__str__(), str)
    assert nb.Mixed(q).__str__() == "2/3"
    assert isinstance(nb.Mixed(e).__str__(), str)
    assert nb.Mixed(e).__str__() == "1.20(10)"
    assert isinstance(nb.Mixed(i).__str__(), str)
    assert nb.Mixed(i).__str__() == "4"
    assert isinstance(nb.Mixed(f).__str__(), str)
    assert nb.Mixed(f).__str__() == "3.5"

    # Hash
    assert isinstance(hash(nb.Mixed(q)), int)
    assert isinstance(hash(nb.Mixed(e)), int)
    assert isinstance(hash(nb.Mixed(i)), int)
    assert isinstance(hash(nb.Mixed(f)), int)
    assert hash(nb.Mixed(1.99999999999)) == hash(nb.Mixed(2.00000000000))
    assert (hash(nb.Mixed(1.9)) == hash(nb.Mixed(2.0))) == False
    e1 = uc.ufloat(1.2, 0.1)
    e2 = e1
    e3 = uc.ufloat(1.2, 0.1)
    me1 = nb.Mixed(e1)
    me2 = nb.Mixed(e2)
    me3 = nb.Mixed(e3)
    assert hash(me1) == hash(me2)
    assert (hash(me1) == hash(me3)) == False

    # Equal
    assert nb.Mixed(q) == nb.Mixed(q)
    assert nb.Mixed(e) == nb.Mixed(e)
    assert nb.Mixed(i) == nb.Mixed(i)
    assert nb.Mixed(f) == nb.Mixed(f)
    assert nb.Mixed(fr.Fraction(2, 3)) == nb.Mixed(fr.Fraction(2, 3))
    assert (nb.Mixed(fr.Fraction(2, 3)) == nb.Mixed(fr.Fraction(1, 3))) == False
    assert (nb.Mixed(uc.ufloat(1.2, 0.1)) == nb.Mixed(uc.ufloat(1.2, 0.1))) == False
    assert (nb.Mixed(uc.ufloat(1.2, 0.1)) == nb.Mixed(uc.ufloat(1.2, 0.2))) \
        == False
    x1 = uc.ufloat(0.5, 0.3)
    x2 = uc.ufloat(0.5, 0.4)
    x = nb.Mixed(x1) + nb.Mixed(x2)
    y = nb.Mixed(x1 + x2)
    assert x == y
    assert nb.Mixed(fr.Fraction(2, 3)) == nb.Mixed(fr.Fraction(2, 3))
    assert (nb.Mixed(fr.Fraction(2, 3)) == nb.Mixed(uc.ufloat(1.2, 0.1))) \
        == False
    assert (nb.Mixed(fr.Fraction(2, 3)) == nb.Mixed(1)) == False
    assert (nb.Mixed(fr.Fraction(2, 3)) == nb.Mixed(0.66)) == False
    assert (nb.Mixed(uc.ufloat(1.2, 0.1)) == nb.Mixed(fr.Fraction(2, 3))) \
        == False
    assert (nb.Mixed(uc.ufloat(1.2, 0.1) == nb.Mixed(uc.ufloat(1.2, 0.1)))) == False
    assert (nb.Mixed(uc.ufloat(1.2, 0.1)) == nb.Mixed(1)) == False
    assert (nb.Mixed(uc.ufloat(1.2, 0.1)) == nb.Mixed(0.66)) == False
    assert (nb.Mixed(1) == nb.Mixed(fr.Fraction(2, 3))) == False
    assert (nb.Mixed(1) == nb.Mixed(uc.ufloat(1.2, 0.1))) == False
    assert nb.Mixed(1) == nb.Mixed(1)
    assert (nb.Mixed(1) == nb.Mixed(1.0)) == False
    assert (nb.Mixed(1.0) == nb.Mixed(fr.Fraction(1, 1))) == False
    assert (nb.Mixed(1.0) == nb.Mixed(uc.ufloat(1.0, 0.0))) == False
    assert (nb.Mixed(1.0) == nb.Mixed(1)) == False
    assert nb.Mixed(1.0) == nb.Mixed(1.0)
    assert nb.Mixed(0) == 0
    assert (nb.Mixed(0.1) == 0) == False
    assert nb.Mixed(fr.Fraction(2, 1)) == 2
    u1 = nb.Mixed(uc.ufloat(0.1, 0.0001))
    u2 = u1 + 1
    u3 = u2 - 1
    assert u1 == u3


    # Other relations

    # Addition

    mq = nb.Mixed(q)
    me = nb.Mixed(e)
    mi = nb.Mixed(i)
    mf = nb.Mixed(f)

    mi0 = nb.Mixed(0)
    
    assert isinstance(mq + mq, nb.Mixed)
    assert isinstance((mq + mq).value, fr.Fraction)
    assert mq + mq == nb.Mixed(fr.Fraction(4, 3))
    assert isinstance(mq + q, nb.Mixed)
    assert isinstance((mq + q).value, fr.Fraction)
    assert mq + q == nb.Mixed(fr.Fraction(4, 3))
    assert isinstance(q + mq, nb.Mixed)
    assert isinstance((q + mq).value, fr.Fraction)
    assert q + mq == nb.Mixed(fr.Fraction(4, 3))

    assert isinstance(mq + me, nb.Mixed)
    assert isinstance((mq + me).value, uc.UFloat)
    assert mq + me == nb.Mixed(e + 2 / 3)
    assert isinstance(mq + e, nb.Mixed)
    assert isinstance((mq + e).value, uc.UFloat)
    assert mq + e == nb.Mixed(e + 2 / 3)
    assert isinstance(q + me, nb.Mixed)
    assert isinstance((q + me).value, uc.UFloat)
    assert q + me == nb.Mixed(e + 2 / 3)

    assert isinstance(mq + mi, nb.Mixed)
    assert isinstance((mq + mi).value, fr.Fraction)
    assert mq + mi == nb.Mixed(fr.Fraction(14, 3))
    assert isinstance(mq + i, nb.Mixed)
    assert isinstance((mq + i).value, fr.Fraction)
    assert mq + i == nb.Mixed(fr.Fraction(14, 3))
    assert isinstance(q + mi, nb.Mixed)
    assert isinstance((q + mi).value, fr.Fraction)
    assert q + mi == nb.Mixed(fr.Fraction(14, 3))

    assert isinstance(mq + mf, nb.Mixed)
    assert isinstance((mq + mf).value, float)
    assert mq + mf == nb.Mixed(3.5 + 2 / 3)
    assert isinstance(mq + f, nb.Mixed)
    assert isinstance((mq + f).value, float)
    assert mq + f == nb.Mixed(3.5 + 2 / 3)
    assert isinstance(q + mf, nb.Mixed)
    assert isinstance((q + mf).value, float)
    assert q + mf == nb.Mixed(3.5 + 2 / 3)

    assert isinstance(me + mq, nb.Mixed)
    assert isinstance((me + mq).value, uc.UFloat)
    assert me + mq == nb.Mixed(e + 2 / 3)
    assert isinstance(me + q, nb.Mixed)
    assert isinstance((me + q).value, uc.UFloat)
    assert me + q == nb.Mixed(e + 2 / 3)
    assert isinstance(e + mq, nb.Mixed)
    assert isinstance((e + mq).value, uc.UFloat)
    assert e + mq == nb.Mixed(e + 2 / 3)

    assert isinstance(me + me, nb.Mixed)
    assert isinstance((me + me).value, uc.UFloat)
    assert me + me == nb.Mixed(e + e)
    assert isinstance(me + e, nb.Mixed)
    assert isinstance((me + e).value, uc.UFloat)
    assert me + e == nb.Mixed(e + e)
    assert isinstance(e + me, nb.Mixed)
    assert isinstance((e + me).value, uc.UFloat)
    assert e + me == nb.Mixed(e + e)

    assert isinstance(me + mi, nb.Mixed)
    assert isinstance((me + mi).value, uc.UFloat)
    assert me + mi == nb.Mixed(e + i)
    assert isinstance(me + i, nb.Mixed)
    assert isinstance((me + i).value, uc.UFloat)
    assert me + i == nb.Mixed(e + i)
    assert isinstance(e + mi, nb.Mixed)
    assert isinstance((e + mi).value, uc.UFloat)
    assert me + i == nb.Mixed(e + i)
    assert me + mi0 == nb.Mixed(e)


    assert isinstance(me + mf, nb.Mixed)
    assert isinstance((me + mf).value, uc.UFloat)
    assert me + mf == nb.Mixed(e + f)
    assert isinstance(me + f, nb.Mixed)
    assert isinstance((me + f).value, uc.UFloat)
    assert me + f == nb.Mixed(e + f)
    assert isinstance(e + mf, nb.Mixed)
    assert isinstance((e + mf).value, uc.UFloat)
    assert e + mf == nb.Mixed(e + f)

    assert isinstance(mi + mq, nb.Mixed)
    assert isinstance((mi + mq).value, fr.Fraction)
    assert mi + mq == nb.Mixed(fr.Fraction(14, 3))
    assert isinstance(mi + q, nb.Mixed)
    assert isinstance((mi + q).value, fr.Fraction)
    assert mi + q == nb.Mixed(fr.Fraction(14, 3))
    assert isinstance(i + mq, nb.Mixed)
    assert isinstance((i + mq).value, fr.Fraction)
    assert i + mq == nb.Mixed(fr.Fraction(14, 3))

    assert isinstance(mi + me, nb.Mixed)
    assert isinstance((mi + me).value, uc.UFloat)
    assert mi + me == nb.Mixed(i + e)
    assert isinstance(mi + e, nb.Mixed)
    assert isinstance((mi + e).value, uc.UFloat)
    assert mi + me == nb.Mixed(i + e)
    assert isinstance(i + me, nb.Mixed)
    assert isinstance((i + me).value, uc.UFloat)
    assert i + me == nb.Mixed(i + e)

    assert isinstance(mi + mi, nb.Mixed)
    assert isinstance((mi + mi).value, int)
    assert mi + mi == nb.Mixed(8)
    assert isinstance(mi + i, nb.Mixed)
    assert isinstance((mi + i).value, int)
    assert mi + i == nb.Mixed(8)
    assert isinstance(i + mi, nb.Mixed)
    assert isinstance((i + mi).value, int)
    assert i + mi == nb.Mixed(8)

    assert isinstance(mi + mf, nb.Mixed)
    assert isinstance((mi + mf).value, float)
    assert mi + mf == nb.Mixed(7.5)
    assert isinstance(mi + f, nb.Mixed)
    assert isinstance((mi + f).value, float)
    assert mi + f == nb.Mixed(7.5)
    assert isinstance(i + mf, nb.Mixed)
    assert isinstance((i + mf).value, float)
    assert i + mf == nb.Mixed(7.5)

    assert isinstance(mf + mq, nb.Mixed)
    assert isinstance((mf + mq).value, float)
    assert mf + mq == nb.Mixed(3.5 + 2 / 3)
    assert isinstance(mf + q, nb.Mixed)
    assert isinstance((mf + q).value, float)
    assert mf + q == nb.Mixed(3.5 + 2 / 3)
    assert isinstance(f + mq, nb.Mixed)
    assert isinstance((f + mq).value, float)
    assert f + mq == nb.Mixed(3.5 + 2 / 3)

    assert isinstance(mf + me, nb.Mixed)
    assert isinstance((mf + me).value, uc.UFloat)
    assert mf + me == nb.Mixed(f + e)
    assert isinstance(mf + e, nb.Mixed)
    assert isinstance((mf + e).value, uc.UFloat)
    assert mf + e == nb.Mixed(f + e)
    assert isinstance(f + me, nb.Mixed)
    assert isinstance((f + me).value, uc.UFloat)
    assert f + me == nb.Mixed(f + e)

    # Subtraction
    q1 = fr.Fraction(1, 2)
    q2 = fr.Fraction(1, 4)
    e1 = uc.ufloat(1.2, 0.3)
    e2 = uc.ufloat(0.2, 0.4)
    i1 = 4
    i2 = 3
    f1 = 3.5
    f2 = 3.4
    mq1 = nb.Mixed(q1)
    mq2 = nb.Mixed(q2)
    me1 = nb.Mixed(e1)
    me2 = nb.Mixed(e2)
    mi1 = nb.Mixed(i1)
    mi2 = nb.Mixed(i2)
    mf1 = nb.Mixed(f1)
    mf2 = nb.Mixed(f2)

    assert isinstance(mq1 - mq2, nb.Mixed)
    assert isinstance((mq1 - mq2).value, fr.Fraction)
    assert mq1 - mq2 == nb.Mixed(fr.Fraction(1, 4))
    assert isinstance(mq1 - q2, nb.Mixed)
    assert isinstance((mq1 - q2).value, fr.Fraction)
    assert mq1 - q2 == nb.Mixed(fr.Fraction(1, 4))
    assert isinstance(q1 - mq2, nb.Mixed)
    assert isinstance((q1 - mq2).value, fr.Fraction)
    assert q1 - mq2 == nb.Mixed(fr.Fraction(1, 4))

    assert isinstance(mq1 - me1, nb.Mixed)
    assert isinstance((mq1 - me1).value, uc.UFloat)
    assert mq1 - me1 == nb.Mixed(float(q1) - e1)
    assert isinstance(mq1 - e1, nb.Mixed)
    assert isinstance((mq1 - e1).value, uc.UFloat)
    assert mq1 - e1 == nb.Mixed(float(q1) - e1)
    assert isinstance(q1 - me1, nb.Mixed)
    assert isinstance((q1 - me1).value, uc.UFloat)
    assert q1 - me1 == nb.Mixed(float(q1) - e1)

    assert isinstance(mq1 - mi1, nb.Mixed)
    assert isinstance((mq1 - mi1).value, fr.Fraction)
    assert mq1 - mi1 == nb.Mixed(q1 - i1)
    assert isinstance(mq1 - i1, nb.Mixed)
    assert isinstance((mq1 - i1).value, fr.Fraction)
    assert mq1 - i1 == nb.Mixed(q1 - i1)
    assert isinstance(q1 - mi1, nb.Mixed)
    assert isinstance((q1 - mi1).value, fr.Fraction)
    assert q1 - mi1 == nb.Mixed(q1 - i1)

    assert isinstance(mq1 - mf1, nb.Mixed)
    assert isinstance((mq1 - mf1).value, float)
    assert mq1 - mf1 == nb.Mixed(-3.0)
    assert isinstance(mq1 - f1, nb.Mixed)
    assert isinstance((mq1 - f1).value, float)
    assert mq1 - f1 == nb.Mixed(-3.0)
    assert isinstance(q1 - mf1, nb.Mixed)
    assert isinstance((q1 - mf1).value, float)
    assert q1 - mf1 == nb.Mixed(-3.0)

    assert isinstance(me1 - mq1, nb.Mixed)
    assert isinstance((me1 - mq1).value, uc.UFloat)
    assert me1 - mq1 == nb.Mixed(e1 - float(q1))
    assert isinstance(me1 - q1, nb.Mixed)
    assert isinstance((me1 - q1).value, uc.UFloat)
    assert me1 - q1 == nb.Mixed(e1 - float(q1))
    assert isinstance(e1 - mq1, nb.Mixed)
    assert isinstance((e1 - mq1).value, uc.UFloat)
    assert e1 - mq1 == nb.Mixed(e1 - float(q1))

    assert isinstance(me1 - me2, nb.Mixed)
    assert isinstance((me1 - me2).value, uc.UFloat)
    assert me1 - me2 == nb.Mixed(e1 - e2)
    assert isinstance(me1 - e2, nb.Mixed)
    assert isinstance((me1 - e2).value, uc.UFloat)
    assert me1 - e2 == nb.Mixed(e1 - e2)
    assert isinstance(e1 - me2, nb.Mixed)
    assert isinstance((e1 - me2).value, uc.UFloat)
    assert e1 - me2 == nb.Mixed(e1 - e2)

    assert isinstance(me1 - mi1, nb.Mixed)
    assert isinstance((me1 - mi1).value, uc.UFloat)
    assert me1 - mi1 == nb.Mixed(e1 - i1)
    assert isinstance(me1 - i1, nb.Mixed)
    assert isinstance((me1 - i1).value, uc.UFloat)
    assert me1 - i1 == nb.Mixed(e1 - i1)
    assert isinstance(e1 - mi1, nb.Mixed)
    assert isinstance((e1 - mi1).value, uc.UFloat)
    assert e1 - mi1 == nb.Mixed(e1 - i1)

    assert isinstance(me1 - mf1, nb.Mixed)
    assert isinstance((me1 - mf1).value, uc.UFloat)
    assert me1 - mf1 == nb.Mixed(e1 - f1)
    assert isinstance(me1 - f1, nb.Mixed)
    assert isinstance((me1 - f1).value, uc.UFloat)
    assert me1 - f1 == nb.Mixed(e1 - f1)
    assert isinstance(e1 - mf1, nb.Mixed)
    assert isinstance((e1 - mf1).value, uc.UFloat)
    assert e1 - mf1 == nb.Mixed(e1 - f1)

    assert isinstance(mi1 - mq1, nb.Mixed)
    assert isinstance((mi1 - mq1).value, fr.Fraction)
    assert mi1 - mq1 == nb.Mixed(fr.Fraction(7, 2))
    assert isinstance(mi1 - q1, nb.Mixed)
    assert isinstance((mi1 - q1).value, fr.Fraction)
    assert mi1 - q1 == nb.Mixed(fr.Fraction(7, 2))
    assert isinstance(i1 - mq1, nb.Mixed)
    assert isinstance((i1 - mq1).value, fr.Fraction)
    assert i1 - mq1 == nb.Mixed(fr.Fraction(7, 2))

    assert isinstance(mi1 - me1, nb.Mixed)
    assert isinstance((mi1 - me1).value, uc.UFloat)
    assert mi1 - me1 == nb.Mixed(i1 - e1)
    assert isinstance(mi1 - e1, nb.Mixed)
    assert isinstance((mi1 - e1).value, uc.UFloat)
    assert mi1 - e1 == nb.Mixed(i1 - e1)
    assert isinstance(i1 - me1, nb.Mixed)
    assert isinstance((i1 - me1).value, uc.UFloat)
    assert i1 - me1 == nb.Mixed(i1 - e1)

    assert isinstance(mi1 - mi2, nb.Mixed)
    assert isinstance((mi1 - mi2).value, int)
    assert mi1 - mi2 == nb.Mixed(1)
    assert isinstance(mi1 - i2, nb.Mixed)
    assert isinstance((mi1 - i2).value, int)
    assert mi1 - i2 == nb.Mixed(1)
    assert isinstance(i1 - mi2, nb.Mixed)
    assert isinstance((i1 - mi2).value, int)
    assert i1 - mi2 == nb.Mixed(1)

    assert isinstance(mi1 - mf1, nb.Mixed)
    assert isinstance((mi1 - mf1).value, float)
    assert mi1 - mf1 == nb.Mixed(0.5)
    assert isinstance(mi1 - f1, nb.Mixed)
    assert isinstance((mi1 - f1).value, float)
    assert mi1 - f1 == nb.Mixed(0.5)
    assert isinstance(i1 - mf1, nb.Mixed)
    assert isinstance((i1 - mf1).value, float)
    assert i1 - mf1 == nb.Mixed(0.5)

    assert isinstance(mf1 - mq1, nb.Mixed)
    assert isinstance((mf1 - mq1).value, float)
    assert mf1 - mq1 == nb.Mixed(3.0)
    assert isinstance(mf1 - q1, nb.Mixed)
    assert isinstance((mf1 - q1).value, float)
    assert mf1 - q1 == nb.Mixed(3.0)
    assert isinstance(f1 - mq1, nb.Mixed)
    assert isinstance((f1 - mq1).value, float)
    assert f1 - mq1 == nb.Mixed(3.0)

    assert isinstance(mf1 - me1, nb.Mixed)
    assert isinstance((mf1 - me1).value, uc.UFloat)
    assert mf1 - me1 == nb.Mixed(f1 - e1)
    assert isinstance(mf1 - e1, nb.Mixed)
    assert isinstance((mf1 - e1).value, uc.UFloat)
    assert mf1 - e1 == nb.Mixed(f1 - e1)
    assert isinstance(f1 - me1, nb.Mixed)
    assert isinstance((f1 - me1).value, uc.UFloat)
    assert f1 - me1 == nb.Mixed(f1 - e1)

    assert isinstance(mf1 - mi1, nb.Mixed)
    assert isinstance((mf1 - mi1).value, float)
    assert mf1 - mi1 == nb.Mixed(-0.5)
    assert isinstance(mf1 - i1, nb.Mixed)
    assert isinstance((mf1 - i1).value, float)
    assert mf1 - i1 == nb.Mixed(-0.5)
    assert isinstance(f1 - mi1, nb.Mixed)
    assert isinstance((f1 - mi1).value, float)
    assert f1 - mi1 == nb.Mixed(-0.5)

    assert isinstance(mf1 - mf2, nb.Mixed)
    assert isinstance((mf1 - mf2).value, float)
    assert mf1 - mf2 == nb.Mixed(3.5 - 3.4)
    assert isinstance(mf1 - f2, nb.Mixed)
    assert isinstance((mf1 - f2).value, float)
    assert mf1 - f2 == nb.Mixed(3.5 - 3.4)
    assert isinstance(f1 - mf2, nb.Mixed)
    assert isinstance((f1 - mf2).value, float)
    assert f1 - mf2 == nb.Mixed(3.5 - 3.4)

    # Multiplication

    q1 = fr.Fraction(1, 2)
    q2 = fr.Fraction(1, 4)
    e1 = uc.ufloat(1.2, 0.3)
    e2 = uc.ufloat(0.2, 0.4)
    i1 = 4
    i2 = 3
    f1 = 3.5
    f2 = 3.4
    mq1 = nb.Mixed(q1)
    mq2 = nb.Mixed(q2)
    me1 = nb.Mixed(e1)
    me2 = nb.Mixed(e2)
    mi1 = nb.Mixed(i1)
    mi2 = nb.Mixed(i2)
    mf1 = nb.Mixed(f1)
    mf2 = nb.Mixed(f2)

    assert isinstance(mq1 * mq2, nb.Mixed)
    assert isinstance((mq1 * mq2).value, fr.Fraction)
    assert mq1 * mq2 == nb.Mixed(fr.Fraction(1, 8))
    assert isinstance(mq1 * q2, nb.Mixed)
    assert isinstance((mq1 * q2).value, fr.Fraction)
    assert mq1 * q2 == nb.Mixed(fr.Fraction(1, 8))
    assert isinstance(q1 * mq2, nb.Mixed)
    assert isinstance((q1 * mq2).value, fr.Fraction)
    assert q1 * mq2 == nb.Mixed(fr.Fraction(1, 8))

    assert isinstance(mq1 * me1, nb.Mixed)
    assert isinstance((mq1 * me1).value, uc.UFloat)
    assert mq1 * me1 == nb.Mixed(float(q1) * e1)
    assert isinstance(mq1 * e1, nb.Mixed)
    assert isinstance((mq1 * e1).value, uc.UFloat)
    assert mq1 * e1 == nb.Mixed(float(q1) * e1)
    assert isinstance(q1 * me1, nb.Mixed)
    assert isinstance((q1 * me1).value, uc.UFloat)
    assert q1 * me1 == nb.Mixed(float(q1) * e1)

    assert isinstance(mq1 * mi2, nb.Mixed)
    assert isinstance((mq1 * mi2).value, fr.Fraction)
    assert mq1 * mi2 == nb.Mixed(fr.Fraction(3, 2))
    assert isinstance(mq1 * i2, nb.Mixed)
    assert isinstance((mq1 * i2).value, fr.Fraction)
    assert mq1 * i2 == nb.Mixed(fr.Fraction(3, 2))
    assert isinstance(q1 * mi2, nb.Mixed)
    assert isinstance((q1 * mi2).value, fr.Fraction)
    assert q1 * mi2 == nb.Mixed(fr.Fraction(3, 2))

    assert isinstance(mq1 * mf1, nb.Mixed)
    assert isinstance((mq1 * mf1).value, float)
    assert mq1 * mf1 == nb.Mixed(1.75)
    assert isinstance(mq1 * f1, nb.Mixed)
    assert isinstance((mq1 * f1).value, float)
    assert mq1 * f1 == nb.Mixed(1.75)
    assert isinstance(q1 * mf1, nb.Mixed)
    assert isinstance((q1 * mf1).value, float)
    assert q1 * mf1 == nb.Mixed(1.75)

    assert isinstance(me1 * mq1, nb.Mixed)
    assert isinstance((me1 * mq1).value, uc.UFloat)
    assert me1 * mq1 == nb.Mixed(e1 * float(q1))
    assert isinstance(me1 * q1, nb.Mixed)
    assert isinstance((me1 * q1).value, uc.UFloat)
    assert me1 * q1 == nb.Mixed(e1 * float(q1))
    assert isinstance(e1 * mq1, nb.Mixed)
    assert isinstance((e1 * mq1).value, uc.UFloat)
    assert e1 * mq1 == nb.Mixed(e1 * float(q1))

    assert isinstance(me1 * me2, nb.Mixed)
    assert isinstance((me1 * me2).value, uc.UFloat)
    assert me1 * me2 == nb.Mixed(e1 * e2)
    assert isinstance(me1 * e2, nb.Mixed)
    assert isinstance((me1 * e2).value, uc.UFloat)
    assert me1 * e2 == nb.Mixed(e1 * e2)
    assert isinstance(e1 * me2, nb.Mixed)
    assert isinstance((e1 * me2).value, uc.UFloat)
    assert e1 * me2 == nb.Mixed(e1 * e2)

    assert isinstance(me1 * mi1, nb.Mixed)
    assert isinstance((me1 * mi1).value, uc.UFloat)
    assert me1 * mi1 == nb.Mixed(e1 * i1)
    assert isinstance(me1 * i1, nb.Mixed)
    assert isinstance((me1 * i1).value, uc.UFloat)
    assert me1 * i1 == nb.Mixed(e1 * i1)
    assert isinstance(e1 * mi1, nb.Mixed)
    assert isinstance((e1 * mi1).value, uc.UFloat)
    assert e1 * mi1 == nb.Mixed(e1 * i1)

    assert isinstance(me1 * mf1, nb.Mixed)
    assert isinstance((me1 * mf1).value, uc.UFloat)
    assert me1 * mf1 == nb.Mixed(e1 * f1)
    assert isinstance(me1 * f1, nb.Mixed)
    assert isinstance((me1 * f1).value, uc.UFloat)
    assert me1 * f1 == nb.Mixed(e1 * f1)
    assert isinstance(e1 * mf1, nb.Mixed)
    assert isinstance((e1 * mf1).value, uc.UFloat)
    assert e1 * mf1 == nb.Mixed(e1 * f1)

    assert isinstance(nb.Mixed(3) * mq1, nb.Mixed)
    assert isinstance((nb.Mixed(3) * mq1).value, fr.Fraction)
    assert nb.Mixed(3) * mq1 == nb.Mixed(fr.Fraction(3, 2))
    assert isinstance(nb.Mixed(3) * q1, nb.Mixed)
    assert isinstance((nb.Mixed(3) * q1).value, fr.Fraction)
    assert nb.Mixed(3) * q1 == nb.Mixed(fr.Fraction(3, 2))
    assert isinstance(3 * mq1, nb.Mixed)
    assert isinstance((3 * mq1).value, fr.Fraction)
    assert 3 * mq1 == nb.Mixed(fr.Fraction(3, 2))

    assert isinstance(mi1 * me1, nb.Mixed)
    assert isinstance((mi1 * me1).value, uc.UFloat)
    assert mi1 * me1 == nb.Mixed(i1 * e1)
    assert isinstance(mi1 * e1, nb.Mixed)
    assert isinstance((mi1 * e1).value, uc.UFloat)
    assert mi1 * e1 == nb.Mixed(i1 * e1)
    assert isinstance(i1 * me1, nb.Mixed)
    assert isinstance((i1 * me1).value, uc.UFloat)
    assert i1 * me1 == nb.Mixed(i1 * e1)

    assert isinstance(mi1 * mi2, nb.Mixed)
    assert isinstance((mi1 * mi2).value, int)
    assert mi1 * mi2 == nb.Mixed(12)
    assert isinstance(mi1 * i2, nb.Mixed)
    assert isinstance((mi1 * i2).value, int)
    assert mi1 * i2 == nb.Mixed(12)
    assert isinstance(i1 * mi2, nb.Mixed)
    assert isinstance((i1 * mi2).value, int)
    assert i1 * mi2 == nb.Mixed(12)

    assert isinstance(mi1 * mf1, nb.Mixed)
    assert isinstance((mi1 * mf1).value, float)
    assert mi1 * mf1 == nb.Mixed(14.0)
    assert isinstance(mi1 * f1, nb.Mixed)
    assert isinstance((mi1 * f1).value, float)
    assert mi1 * f1 == nb.Mixed(14.0)
    assert isinstance(i1 * mf1, nb.Mixed)
    assert isinstance((i1 * mf1).value, float)
    assert i1 * mf1 == nb.Mixed(14.0)

    assert isinstance(mf1 * mq1, nb.Mixed)
    assert isinstance((mf1 * mq1).value, float)
    assert mf1 * mq1 == nb.Mixed(1.75)
    assert isinstance(mf1 * q1, nb.Mixed)
    assert isinstance((mf1 * q1).value, float)
    assert mf1 * q1 == nb.Mixed(1.75)
    assert isinstance(f1 * mq1, nb.Mixed)
    assert isinstance((f1 * mq1).value, float)
    assert f1 * mq1 == nb.Mixed(1.75)

    assert isinstance(mf1 * me1, nb.Mixed)
    assert isinstance((mf1 * me1).value, uc.UFloat)
    assert mf1 * me1 == nb.Mixed(f1 * e1)
    assert isinstance(mf1 * e1, nb.Mixed)
    assert isinstance((mf1 * e1).value, uc.UFloat)
    assert mf1 * e1 == nb.Mixed(f1 * e1)
    assert isinstance(f1 * me1, nb.Mixed)
    assert isinstance((f1 * me1).value, uc.UFloat)
    assert f1 * me1 == nb.Mixed(f1 * e1)

    assert isinstance(mf1 * mi1, nb.Mixed)
    assert isinstance((mf1 * mi1).value, float)
    assert mf1 * mi1 == nb.Mixed(14.0)
    assert isinstance(mf1 * i1, nb.Mixed)
    assert isinstance((mf1 * i1).value, float)
    assert mf1 * i1 == nb.Mixed(14.0)
    assert isinstance(f1 * mi1, nb.Mixed)
    assert isinstance((f1 * mi1).value, float)
    assert f1 * mi1 == nb.Mixed(14.0)

    assert isinstance(mf1 * mf2, nb.Mixed)
    assert isinstance((mf1 * mf2).value, float)
    assert mf1 * mf2 == nb.Mixed(11.9)
    assert isinstance(mf1 * f2, nb.Mixed)
    assert isinstance((mf1 * f2).value, float)
    assert mf1 * f2 == nb.Mixed(11.9)
    assert isinstance(f1 * mf2, nb.Mixed)
    assert isinstance((f1 * mf2).value, float)
    assert f1 * mf2 == nb.Mixed(11.9)

    # Multiplication with integer 0

    q = fr.Fraction(2, 3)
    e = uc.ufloat(1.2, 0.1)
    i = 4
    f = 3.5
    mq = nb.Mixed(q)
    me = nb.Mixed(e)
    mi = nb.Mixed(i)
    mf = nb.Mixed(f)
    m0 = nb.Mixed(0)

    for m in [mq, me, mi, mf]:
        assert m * m0 == m0
        assert m * 0 == m0
        assert m0 * m == m0
        assert 0 * m == m0

    for z in [q, e, i, f]:
        assert z * m0 == m0
        assert m0 * z == m0

    # Division
    q1 = fr.Fraction(2, 3)
    q2 = fr.Fraction(3, 4)
    e1 = uc.ufloat(0.5, 0.3)
    e2 = uc.ufloat(0.75, 0.4)
    i1 = 4
    i2 = 3
    f1 = 1.5
    f2 = 1.6
    mq1 = nb.Mixed(q1)
    mq2 = nb.Mixed(q2)
    me1 = nb.Mixed(e1)
    me2 = nb.Mixed(e2)
    mi1 = nb.Mixed(i1)
    mi2 = nb.Mixed(i2)
    mf1 = nb.Mixed(f1)
    mf2 = nb.Mixed(f2)

    assert isinstance(mq1 / mq2, nb.Mixed)
    assert isinstance((mq1 / mq2).value, fr.Fraction)
    assert mq1 / mq2 == nb.Mixed(fr.Fraction(8, 9))
    assert isinstance(mq1 / q2, nb.Mixed)
    assert isinstance((mq1 / q2).value, fr.Fraction)
    assert mq1 / q2 == nb.Mixed(fr.Fraction(8, 9))
    assert isinstance(q1 / mq2, nb.Mixed)
    assert isinstance((q1 / mq2).value, fr.Fraction)
    assert q1 / mq2 == nb.Mixed(fr.Fraction(8, 9))

    assert isinstance(mq1 / me1, nb.Mixed)
    assert isinstance((mq1 / me1).value, uc.UFloat)
    assert mq1 / me1 == nb.Mixed(float(q1) / e1)
    assert isinstance(mq1 / e1, nb.Mixed)
    assert isinstance((mq1 / e1).value, uc.UFloat)
    assert mq1 / e1 == nb.Mixed(float(q1) / e1)
    assert isinstance(q1 / me1, nb.Mixed)
    assert isinstance((q1 / me1).value, uc.UFloat)
    assert q1 / me1 == nb.Mixed(float(q1) / e1)

    assert isinstance(mq1 / mi1, nb.Mixed)
    assert isinstance((mq1 / mi1).value, fr.Fraction)
    assert mq1 / mi1 == nb.Mixed(fr.Fraction(1, 6))
    assert isinstance(mq1 / i1, nb.Mixed)
    assert isinstance((mq1 / i1).value, fr.Fraction)
    assert mq1 / i1 == nb.Mixed(fr.Fraction(1, 6))
    assert isinstance(q1 / mi1, nb.Mixed)
    assert isinstance((q1 / mi1).value, fr.Fraction)
    assert q1 / mi1 == nb.Mixed(fr.Fraction(1, 6))

    assert isinstance(mq1 / mf1, nb.Mixed)
    assert isinstance((mq1 / mf1).value, float)
    assert mq1 / mf1 == nb.Mixed(4.0 / 9.0)
    assert isinstance(mq1 / f1, nb.Mixed)
    assert isinstance((mq1 / f1).value, float)
    assert mq1 / f1 == nb.Mixed(4.0 / 9.0)
    assert isinstance(q1 / mf1, nb.Mixed)
    assert isinstance((q1 / mf1).value, float)
    assert q1 / mf1 == nb.Mixed(4.0 / 9.0)

    assert isinstance(me1 / mq1, nb.Mixed)
    assert isinstance((me1 / mq1).value, uc.UFloat)
    assert me1 / mq1 == nb.Mixed(e1 / float(q1))
    assert isinstance(me1 / q1, nb.Mixed)
    assert isinstance((me1 / q1).value, uc.UFloat)
    assert me1 / q1 == nb.Mixed(e1 / float(q1))
    assert isinstance(e1 / mq1, nb.Mixed)
    assert isinstance((e1 / mq1).value, uc.UFloat)
    assert e1 / mq1 == nb.Mixed(e1 / float(q1))

    assert isinstance(me1 / me2, nb.Mixed)
    assert isinstance((me1 / me2).value, uc.UFloat)
    assert me1 / me2 == nb.Mixed(e1 / e2)
    assert isinstance(me1 / e2, nb.Mixed)
    assert isinstance((me1 / e2).value, uc.UFloat)
    assert me1 / e2 == nb.Mixed(e1 / e2)
    assert isinstance(e1 / me2, nb.Mixed)
    assert isinstance((e1 / me2).value, uc.UFloat)
    assert e1 / me2 == nb.Mixed(e1 / e2)

    assert isinstance(me1 / mi1, nb.Mixed)
    assert isinstance((me1 / mi1).value, uc.UFloat)
    assert me1 / mi1 == nb.Mixed(e1 / i1)
    assert isinstance(me1 / i1, nb.Mixed)
    assert isinstance((me1 / i1).value, uc.UFloat)
    assert me1 / i1 == nb.Mixed(e1 / i1)
    assert isinstance(e1 / mi1, nb.Mixed)
    assert isinstance((e1 / mi1).value, uc.UFloat)
    assert e1 / mi1 == nb.Mixed(e1 / i1)

    assert isinstance(me1 / mf1, nb.Mixed)
    assert isinstance((me1 / mf1).value, uc.UFloat)
    assert me1 / mf1 == nb.Mixed(e1 / f1)
    assert isinstance(me1 / f1, nb.Mixed)
    assert isinstance((me1 / f1).value, uc.UFloat)
    assert me1 / f1 == nb.Mixed(e1 / f1)
    assert isinstance(e1 / mf1, nb.Mixed)
    assert isinstance((e1 / mf1).value, uc.UFloat)
    assert e1 / mf1 == nb.Mixed(e1 / f1)

    assert isinstance(mi1 / mq2, nb.Mixed)
    assert isinstance((mi1 / mq2).value, fr.Fraction)
    assert mi1 / mq2 == nb.Mixed(fr.Fraction(16, 3))
    assert isinstance(mi1 / q2, nb.Mixed)
    assert isinstance((mi1 / q2).value, fr.Fraction)
    assert mi1 / q2 == nb.Mixed(fr.Fraction(16, 3))
    assert isinstance(i1 / mq2, nb.Mixed)
    assert isinstance((i1 / mq2).value, fr.Fraction)
    assert i1 / mq2 == nb.Mixed(fr.Fraction(16, 3))

    assert isinstance(mi1 / me1, nb.Mixed)
    assert isinstance((mi1 / me1).value, uc.UFloat)
    assert mi1 / me1 == nb.Mixed(i1 / e1)
    assert isinstance(mi1 / e1, nb.Mixed)
    assert isinstance((mi1 / e1).value, uc.UFloat)
    assert mi1 / e1 == nb.Mixed(i1 / e1)
    assert isinstance(i1 / me1, nb.Mixed)
    assert isinstance((i1 / me1).value, uc.UFloat)
    assert i1 / me1 == nb.Mixed(i1 / e1)

    assert isinstance(mi1 / mi2, nb.Mixed)
    assert isinstance((mi1 / mi2).value, fr.Fraction)
    assert mi1 / mi2 == nb.Mixed(fr.Fraction(4, 3))
    assert isinstance(mi1 / i2, nb.Mixed)
    assert isinstance((mi1 / i2).value, fr.Fraction)
    assert mi1 / i2 == nb.Mixed(fr.Fraction(4, 3))
    assert isinstance(i1 / mi2, nb.Mixed)
    assert isinstance((i1 / mi2).value, fr.Fraction)
    assert i1 / mi2 == nb.Mixed(fr.Fraction(4, 3))

    assert isinstance(mi1 / mf1, nb.Mixed)
    assert isinstance((mi1 / mf1).value, float)
    assert mi1 / mf1 == nb.Mixed(4.0 / 1.5)
    assert isinstance(mi1 / f1, nb.Mixed)
    assert isinstance((mi1 / f1).value, float)
    assert mi1 / f1 == nb.Mixed(4.0 / 1.5)
    assert isinstance(i1 / mf1, nb.Mixed)
    assert isinstance((i1 / mf1).value, float)
    assert i1 / mf1 == nb.Mixed(4.0 / 1.5)

    assert isinstance(mf1 / mq1, nb.Mixed)
    assert isinstance((mf1 / mq1).value, float)
    assert mf1 / mq1 == nb.Mixed(2.25)
    assert isinstance(mf1 / q1, nb.Mixed)
    assert isinstance((mf1 / q1).value, float)
    assert mf1 / q1 == nb.Mixed(2.25)
    assert isinstance(f1 / mq1, nb.Mixed)
    assert isinstance((f1 / mq1).value, float)
    assert f1 / mq1 == nb.Mixed(2.25)

    assert isinstance(mf1 / me1, nb.Mixed)
    assert isinstance((mf1 / me1).value, uc.UFloat)
    assert mf1 / me1 == nb.Mixed(f1 / e1)
    assert isinstance(mf1 / e1, nb.Mixed)
    assert isinstance((mf1 / e1).value, uc.UFloat)
    assert mf1 / e1 == nb.Mixed(f1 / e1)
    assert isinstance(f1 / me1, nb.Mixed)
    assert isinstance((f1 / me1).value, uc.UFloat)
    assert f1 / me1 == nb.Mixed(f1 / e1)

    assert isinstance(mf1 / mi1, nb.Mixed)
    assert isinstance((mf1 / mi1).value, float)
    assert mf1 / mi1 == nb.Mixed(0.375)
    assert isinstance(mf1 / i1, nb.Mixed)
    assert isinstance((mf1 / i1).value, float)
    assert mf1 / i1 == nb.Mixed(0.375)
    assert isinstance(f1 / mi1, nb.Mixed)
    assert isinstance((f1 / mi1).value, float)
    assert f1 / mi1 == nb.Mixed(0.375)

    assert isinstance(mf1 / mf2, nb.Mixed)
    assert isinstance((mf1 / mf2).value, float)
    assert mf1 / mf2 == nb.Mixed(0.9375)
    assert isinstance(mf1 / f2, nb.Mixed)
    assert isinstance((mf1 / f2).value, float)
    assert mf1 / f2 == nb.Mixed(0.9375)
    assert isinstance(f1 / mf2, nb.Mixed)
    assert isinstance((f1 / mf2).value, float)
    assert f1 / mf2 == nb.Mixed(0.9375)

    # Dividing integer 0

    q = fr.Fraction(2, 3)
    e = uc.ufloat(1.2, 0.1)
    i = 4
    f = 3.5
    mq = nb.Mixed(q)
    me = nb.Mixed(e)
    mi = nb.Mixed(i)
    mf = nb.Mixed(f)
    m0 = nb.Mixed(0)

    for m in [mq, me, mi, mf]:
        assert m0 / m == m0
        assert 0 / m == m0

    for z in [q, e, i, f]:
        assert m0 / z == m0

    # negative

    q = fr.Fraction(3, 2)
    e = uc.ufloat(1.2, 0.1)
    i = 4
    f = 3.5
    mq = nb.Mixed(q)
    me = nb.Mixed(e)
    mi = nb.Mixed(i)
    mf = nb.Mixed(f)

    assert isinstance(-mq, nb.Mixed)
    assert isinstance((-mq).value, fr.Fraction)
    assert -mq == nb.Mixed(fr.Fraction(-3, 2))

    assert isinstance(-me, nb.Mixed)
    assert isinstance((-me).value, uc.UFloat)
    assert -me == nb.Mixed(-e)

    assert isinstance(-mi, nb.Mixed)
    assert isinstance((-mi).value, int)
    assert -mi == nb.Mixed(-4)

    assert isinstance(-mf, nb.Mixed)
    assert isinstance((-mf).value, float)
    assert -mf == nb.Mixed(-3.5)

    # Modulo

    q = fr.Fraction(5, 2)
    e = uc.ufloat(3.2, 0.1)
    i = 3
    f = 3.5
    mq = nb.Mixed(q)
    me = nb.Mixed(e)
    mi = nb.Mixed(i)
    mf = nb.Mixed(f)

    assert isinstance(mq % 2, nb.Mixed)
    assert isinstance((mq % 2).value, fr.Fraction)
    assert mq % 2 == nb.Mixed(fr.Fraction(1, 2))

    assert isinstance(me % 2, nb.Mixed)
    assert isinstance((me % 2).value, uc.UFloat)
    assert approx((me % 2).value.n, 1.2)
    assert approx((me % 2).value.s, 0.1)

    assert isinstance(mi % 2, nb.Mixed)
    assert isinstance((mi % 2).value, int)
    assert mi % 2 == nb.Mixed(1)

    assert isinstance(mf % 2, nb.Mixed)
    assert isinstance((mf % 2).value, float)
    assert approx((mf % 2).value, 1.5)

    # Constants

    assert isinstance(nb.pi, nb.Mixed)
    assert isinstance((nb.pi).value, float)
    assert (nb.pi).value == 3.141592653589793

    # Square-Root

    a = nb.sqrt(nb.Mixed(fr.Fraction(2, 3)))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.816496580)
    a = nb.sqrt(fr.Fraction(2, 3))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.816496580)
    a = nb.sqrt(nb.Mixed(fr.Fraction(1, 2)))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.70710678118)
    a = nb.sqrt(fr.Fraction(1, 2))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.70710678118)
    a = nb.sqrt(nb.Mixed(fr.Fraction(2, 1)))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 1.41421356237)
    a = nb.sqrt(fr.Fraction(2, 1))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 1.41421356237)
    a = nb.sqrt(nb.Mixed(fr.Fraction(4, 9)))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, fr.Fraction)
    assert a == nb.Mixed(fr.Fraction(2, 3))
    a = nb.sqrt(fr.Fraction(4, 9))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, fr.Fraction)
    assert a == nb.Mixed(fr.Fraction(2, 3))

    a = nb.sqrt(nb.Mixed(uc.ufloat(0.3, 0.1)))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, uc.UFloat)
    assert approx(a.value.n, 0.54772255750)
    assert approx(a.value.s, 0.09128709291)
    a = nb.sqrt(uc.ufloat(0.3, 0.1))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, uc.UFloat)
    assert approx(a.value.n, 0.54772255750)
    assert approx(a.value.s, 0.09128709291)

    a = nb.sqrt(nb.Mixed(3))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 1.7320508075688)
    a = nb.sqrt(3)
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 1.7320508075688)
    a = nb.sqrt(nb.Mixed(4))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, int)
    assert a.value == 2
    a = nb.sqrt(4)
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, int)
    assert a.value == 2

    a = nb.sqrt(nb.Mixed(0.5))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.7071067811)
    a = nb.sqrt(0.5)
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.7071067811)

    # Trigonometric Functions:

    a = nb.deg2rad(nb.Mixed(fr.Fraction(180, 1)))
    assert approx(a.value, 3.1415926535)
    a = nb.deg2rad(fr.Fraction(180, 1))
    assert approx(a.value, 3.1415926535)
    a = nb.deg2rad(nb.Mixed(uc.ufloat(180.0, 10.0)))
    assert approx(a.value.n, 3.1415926535)
    assert approx(a.value.s, 0.174532925199)
    a = nb.deg2rad(uc.ufloat(180.0, 10.0))
    assert approx(a.value.n, 3.1415926535)
    assert approx(a.value.s, 0.174532925199)
    a = nb.deg2rad(nb.Mixed(180))
    assert approx(a.value, 3.1415926535)
    a = nb.deg2rad(180)
    assert approx(a.value, 3.1415926535)
    a = nb.deg2rad(nb.Mixed(180.0))
    assert approx(a.value, 3.1415926535)
    a = nb.deg2rad(180.0)
    assert approx(a.value, 3.1415926535)

    a = nb.rad2deg(nb.Mixed(fr.Fraction(1, 2)))
    assert approx(a.value, 28.647889756)
    a = nb.rad2deg(fr.Fraction(1, 2))
    assert approx(a.value, 28.647889756)
    a = nb.rad2deg(nb.Mixed(uc.ufloat(3.1415926535897931, 0.17453292519943295)))
    assert approx(a.value.n, 180.0)
    assert approx(a.value.s, 10.0)
    a = nb.rad2deg(uc.ufloat(3.1415926535897931, 0.17453292519943295))
    assert approx(a.value.n, 180.0)
    assert approx(a.value.s, 10.0)
    a = nb.rad2deg(nb.Mixed(1))
    assert approx(a.value, 57.295779513082323)
    a = nb.rad2deg(1)
    assert approx(a.value, 57.295779513082323)
    a = nb.rad2deg(nb.Mixed(3.1415926535897931))
    assert approx(a.value, 180.0)
    a = nb.rad2deg(3.1415926535897931)
    assert approx(a.value, 180.0)

    a = nb.sin(nb.Mixed(fr.Fraction(1, 2)))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.47942553860420301)
    a = nb.sin(fr.Fraction(1, 2))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.479425538604203)
    a = nb.sin(nb.Mixed(uc.ufloat(0.5, 0.1)))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, uc.UFloat)
    assert approx(a.value.n, 0.479425538604203)
    assert approx(a.value.s, 0.08775825618903728)
    a = nb.sin(uc.ufloat(0.5, 0.1))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, uc.UFloat)
    assert approx(a.value.n, 0.479425538604203)
    assert approx(a.value.s, 0.08775825618903728)
    a = nb.sin(nb.Mixed(1))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.8414709848078965)
    a = nb.sin(1)
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.8414709848078965)
    a = nb.sin(nb.Mixed(0.5))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.479425538604203)
    a = nb.sin(0.5)
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.479425538604203)

    a = nb.cos(nb.Mixed(fr.Fraction(1, 2)))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.8775825618903)
    a = nb.cos(fr.Fraction(1, 2))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.8775825618903)
    a = nb.cos(nb.Mixed(uc.ufloat(0.5, 0.1)))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, uc.UFloat)
    assert approx(a.value.n, 0.8775825619803)
    assert approx(a.value.s, 0.0479425538604)
    a = nb.cos(uc.ufloat(0.5, 0.1))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, uc.UFloat)
    assert approx(a.value.n, 0.8775825619803)
    assert approx(a.value.s, 0.0479425538604)
    a = nb.cos(nb.Mixed(1))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.54030230586)
    a = nb.cos(1)
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.54030230586)
    a = nb.cos(nb.Mixed(0.5))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.8775825618903)
    a = nb.cos(0.5)
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.8775825618903)

    a = nb.arcsin(nb.Mixed(fr.Fraction(1, 2)))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.52359877559829)
    a = nb.arcsin(fr.Fraction(1, 2))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.52359877559829)
    a = nb.arcsin(nb.Mixed(uc.ufloat(0.5, 0.1)))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, uc.UFloat)
    assert approx(a.value.n, 0.52359877559829)
    assert approx(a.value.s, 0.11547005383)
    a = nb.arcsin(uc.ufloat(0.5, 0.1))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, uc.UFloat)
    assert approx(a.value.n, 0.52359877559829)
    assert approx(a.value.s, 0.11547005383)
    a = nb.arcsin(nb.Mixed(1))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 1.57079632679)
    a = nb.arcsin(1)
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 1.57079632679)
    a = nb.arcsin(nb.Mixed(0.5))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.52359877559829)
    a = nb.arcsin(0.5)
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.52359877559829)

    a = nb.arccos(nb.Mixed(fr.Fraction(1, 2)))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 1.04719755119)
    a = nb.arccos(fr.Fraction(1, 2))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 1.04719755119)
    a = nb.arccos(nb.Mixed(uc.ufloat(0.5, 0.1)))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, uc.UFloat)
    assert approx(a.value.n, 1.04719755119)
    assert approx(a.value.s, 0.11547005383)
    a = nb.arccos(uc.ufloat(0.5, 0.1))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, uc.UFloat)
    assert approx(a.value.n, 1.04719755119)
    assert approx(a.value.s, 0.11547005383)
    a = nb.arccos(nb.Mixed(1))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.0)
    a = nb.arccos(1)
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.0)
    a = nb.arccos(nb.Mixed(0.5))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 1.04719755119)
    a = nb.arccos(0.5)
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 1.04719755119)

    a = nb.dsin(fr.Fraction(1, 2))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.00872653549)
    a = nb.dsin(fr.Fraction(1, 2))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.00872653549)
    a = nb.dsin(nb.Mixed(uc.ufloat(0.5, 0.1)))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, uc.UFloat)
    assert approx(a.value.n, 0.00872653549)
    assert approx(a.value.s, 0.00174526279)
    a = nb.dsin(uc.ufloat(0.5, 0.1))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, uc.UFloat)
    assert approx(a.value.n, 0.00872653549)
    assert approx(a.value.s, 0.00174526279)
    a = nb.dsin(nb.Mixed(1))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.017452406437)
    a = nb.dsin(1)
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.017452406437)
    a = nb.dsin(nb.Mixed(0.5))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.00872653549)
    a = nb.dsin(0.5)
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.00872653549)
    z = nb.Mixed(0)
    o = nb.Mixed(1)
    h = nb.Mixed(fr.Fraction(1,2))
    xs = [0, 30, 90, 150, 180, 210, 270, 330]
    ys = [z,  h,  o,   h,   z,  -h,  -o,  -h]
    for i in range(len(xs)):
        x = xs[i]
        y = ys[i]
        a = nb.dsin(x)
        assert a == y
        a = nb.dsin(fr.Fraction(x, 1))
        assert a == y
        a = nb.dsin(nb.Mixed(x))
        assert a == y
        a = nb.dsin(nb.Mixed(fr.Fraction(x, 1)))
        assert a == y

    a = nb.dcos(fr.Fraction(1, 2))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.999961923064)
    a = nb.dcos(fr.Fraction(1, 2))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.999961923064)
    a = nb.dcos(nb.Mixed(uc.ufloat(0.5, 0.1)))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, uc.UFloat)
    assert approx(a.value.n, 0.999961923064)
    assert approx(a.value.s, 1.5230677e-5)
    a = nb.dcos(uc.ufloat(0.5, 0.1))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, uc.UFloat)
    assert approx(a.value.n, 0.999961923064)
    assert approx(a.value.s, 1.5230677e-5)
    a = nb.dcos(nb.Mixed(1))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.9998476951)
    a = nb.dcos(1)
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.9998476951)
    a = nb.dcos(nb.Mixed(0.5))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.999961923064)
    a = nb.dcos(0.5)
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 0.999961923064)
    z = nb.Mixed(0)
    o = nb.Mixed(1)
    h = nb.Mixed(fr.Fraction(1,2))
    xs = [0, 60, 90, 120, 180, 240, 270, 300]
    ys = [o,  h,  z,  -h,  -o,  -h,  -z,   h]
    for i in range(len(xs)):
        x = xs[i]
        y = ys[i]
        a = nb.dcos(x)
        assert a == y
        a = nb.dcos(fr.Fraction(x, 1))
        assert a == y
        a = nb.dcos(nb.Mixed(x))
        assert a == y
        a = nb.dcos(nb.Mixed(fr.Fraction(x, 1)))
        assert a == y

    a = nb.darcsin(nb.Mixed(fr.Fraction(1, 3)))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 19.47122063449)
    a = nb.darcsin(fr.Fraction(1, 3))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 19.47122063449)
    a = nb.darcsin(nb.Mixed(uc.ufloat(0.5, 0.1)))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, uc.UFloat)
    assert approx(a.value.n, 30.0)
    assert approx(a.value.s, 6.615946745061)
    a = nb.darcsin(uc.ufloat(0.5, 0.1))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, uc.UFloat)
    assert approx(a.value.n, 30.0)
    assert approx(a.value.s, 6.615946745061)
    a = nb.darcsin(nb.Mixed(0.5))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 30.0)
    a = nb.darcsin(0.5)
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 30.0)
    xs = [-fr.Fraction(1, 1), -fr.Fraction(1, 2),
        fr.Fraction(0, 1), fr.Fraction(1, 2),
        fr.Fraction(1, 1)]
    ys = [-90, -30, 0, 30, 90]
    for i in range(len(xs)):
        x = xs[i]
        y = ys[i]
        assert isinstance(nb.darcsin(x), nb.Mixed)
        assert isinstance(nb.darcsin(x).value, int)
        assert nb.darcsin(x) == y
        assert isinstance(nb.darcsin(nb.Mixed(x)), nb.Mixed)
        assert isinstance(nb.darcsin(nb.Mixed(x)).value, int)
        assert nb.darcsin(nb.Mixed(x)) == y
    xs = [-1, 0, 1]
    ys = [-90, 0, 90]
    for i in range(len(xs)):
        x = xs[i]
        y = ys[i]
        assert isinstance(nb.darcsin(x), nb.Mixed)
        assert isinstance(nb.darcsin(x).value, int)
        assert nb.darcsin(x) == y
        assert isinstance(nb.darcsin(nb.Mixed(x)), nb.Mixed)
        assert isinstance(nb.darcsin(nb.Mixed(x)).value, int)
        assert nb.darcsin(nb.Mixed(x)) == y

    a = nb.darccos(nb.Mixed(fr.Fraction(1, 3)))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 70.5287793655)
    a = nb.darccos(fr.Fraction(1, 3))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 70.5287793655)
    a = nb.darccos(nb.Mixed(uc.ufloat(0.5, 0.1)))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, uc.UFloat)
    assert approx(a.value.n, 60.0)
    assert approx(a.value.s, 6.615946745061)
    a = nb.darccos(uc.ufloat(0.5, 0.1))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, uc.UFloat)
    assert approx(a.value.n, 60.0)
    assert approx(a.value.s, 6.615946745061)
    a = nb.darccos(nb.Mixed(0.5))
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 60.0)
    a = nb.darccos(0.5)
    assert isinstance(a, nb.Mixed)
    assert isinstance(a.value, float)
    assert approx(a.value, 60.0)
    xs = [-fr.Fraction(1, 1), -fr.Fraction(1, 2),
        fr.Fraction(0, 1), fr.Fraction(1, 2),
        fr.Fraction(1, 1)]
    ys = [180, 120, 90, 60, 0]
    for i in range(len(xs)):
        x = xs[i]
        y = ys[i]
        assert isinstance(nb.darccos(x), nb.Mixed)
        assert isinstance(nb.darccos(x).value, int)
        assert nb.darccos(x) == y
        assert isinstance(nb.darccos(nb.Mixed(x)), nb.Mixed)
        assert isinstance(nb.darccos(nb.Mixed(x)).value, int)
        assert nb.darccos(nb.Mixed(x)) == y
    xs = [-1, 0, 1]
    ys = [180, 90, 0]
    for i in range(len(xs)):
        x = xs[i]
        y = ys[i]
        assert isinstance(nb.darccos(x), nb.Mixed)
        assert isinstance(nb.darccos(x).value, int)
        assert nb.darccos(x) == y
        assert isinstance(nb.darccos(nb.Mixed(x)), nb.Mixed)
        assert isinstance(nb.darccos(nb.Mixed(x)).value, int)
        assert nb.darccos(nb.Mixed(x)) == y

