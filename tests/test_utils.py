import pytest
import sys
sys.path.append("../src/")
import cryspy
from cryspy.fromstr import fromstr as fs
import numpy as np


def test_Karussell():
    metric = cryspy.geo.Cellparameters(1, 1, 1, 90, 90, 90).to_Metric()
    k = cryspy.utils.Karussell(metric, fs("d 1 0 0"), fs("d 0 1 0"))
    d1 = k.direction(0)
    assert float(metric.length(d1 - fs("d 1.0 0.0 0"))) < 1e-9
    d2 = k.direction(np.pi / 2)
    assert float(metric.length(d2 - fs("d 0 1 0"))) < 1e-9

    metric = cryspy.geo.Cellparameters(1, 1, 1, 90, 90, 45).to_Metric()
    k = cryspy.utils.Karussell(metric, fs("d 1 0 0"), fs("d 0 1 0"))
    d1 = k.direction(0)
    assert float(metric.length(d1 - fs("d 1.0 0.0 0"))) < 1e-9
    d2 = k.direction(np.pi / 4)
    assert float(metric.length(d2 - fs("d 0 1 0"))) < 1e-9

def test_fill():
    atomset = cryspy.crystal.Atomset({cryspy.crystal.Atom("Fe1", "Fe", fs("p 1/2 1/2 1/2"))})
    atomset = cryspy.utils.fill(atomset, [0.6, 0.6, 0.6])
    assert len(atomset.menge) == 27
    
    atomset = cryspy.crystal.Atomset({cryspy.crystal.Atom("Fe1", "Fe", fs("p 0 0 0"))})
    atomset = cryspy.utils.fill(atomset, [0.1, 0.1, 0.1])
    assert len(atomset.menge) == 8

def test_ldu_decomposition():
    A = fs("< 5 >")
    assert cryspy.utils.ldu_decomposition(A) == \
        [fs("<1>"), fs("<5>"), fs("<1>")]
    A = fs(" 2 1 1 0 \n 4 3 3 1 \n 8 7 9 5 \n 6 7 9 8")

    [L, D, U] = cryspy.utils.ldu_decomposition(A)
    print(L)
    print(D)
    print(U)
    assert L == fs("1 0 0 0 \n 2 1 0 0 \n 4 3 1 0 \n 3 4 1 1")
    assert D == fs("2 0 0 0 \n 0 1 0 0 \n 0 0 2 0 \n 0 0 0 2")
    assert U == fs("1 1/2 1/2 0 \n 0 1 1 1 \n 0 0 1 1 \n 0 0 0 1")
