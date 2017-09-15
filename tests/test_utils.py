import pytest
import sys
sys.path.append("../src/")
import cryspy
from cryspy.fromstr import fromstr as fs
import numpy as np

approxdelta = 0.00000001

def approx(x1, x2):
    x1 = cryspy.numbers.Mixed(x1)
    x2 = cryspy.numbers.Mixed(x2)
    if isinstance(x1.value, float) or isinstance(x2.value, float):
        return abs(x1.value - x2.value) < approxdelta
    else:
        return x1 == x2

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


def test_calculate_transformation_for_normalized_axes():
    

    metrics = [cryspy.geo.Cellparameters(1, 1, 1, 90, 90, 90).to_Metric(),
               cryspy.geo.Cellparameters(2, 1, 3, 90, 90, 40).to_Metric(),
               cryspy.geo.Cellparameters(3.0, 2.7, 3, 60.8, 67.9, 60).to_Metric(),
               cryspy.geo.Cellparameters(1.23, 3.8, 8.4, 60, 70, 80).to_Metric()
    ]
    for metric1 in metrics:
        T = cryspy.utils.calculate_transformation_for_normalized_axes(metric1)
        metric2 = T ** metric1
        print(fs("d 1 0 0"))
        print(T ** fs("d 1 0 0"))
        assert approx(metric2.dangle(fs("d 1 0 0"), T ** fs("d 1 0 0")), 0)
        assert approx(metric2.dangle(fs("d 0 1 0"), T ** fs("d 0 1 0")), 0)
        assert approx(metric2.dangle(fs("d 0 0 1"), T ** fs("d 0 0 1")), 0)
        assert approx(metric2.dangle(fs("d 0 1 0"), fs("d 0 0 1")),
               metric1.dangle(fs("d 0 1 0"), fs("d 0 0 1")))
        assert approx(metric2.dangle(fs("d 0 0 1"), fs("d 1 0 0")),
               metric1.dangle(fs("d 0 0 1"), fs("d 1 0 0")))
        assert approx(metric2.dangle(fs("d 1 0 0"), fs("d 0 1 0")),
               metric1.dangle(fs("d 1 0 0"), fs("d 0 1 0")))
        assert approx(metric1.length(T.inv() ** fs("d 1 0 0")), 1)
        assert approx(metric1.length(T.inv() ** fs("d 0 1 0")), 1)
        assert approx(metric1.length(T.inv() ** fs("d 0 0 1")), 1)
    
def test_autotetraeder():
    metric = cryspy.geo.Cellparameters(1, 1, 1, 90, 90, 90).to_Metric()
    Atom = cryspy.crystal.Atom
    facecolor = (1, 1, 1)
    faceopacity = 0.5
    plotedges = True
    edgecolor = (0, 0, 0)
    edgewidth = 0.02
    atomset = cryspy.crystal.Atomset({
        Atom("Fe1", "Fe", fs("p 1/2 1/2 1/2")),
        Atom("H1", "H", fs("p 0 0 0")),
        Atom("H2", "H", fs("p 1 1 0")),
        Atom("H3", "H", fs("p 0 1 1")),
        Atom("H4", "H", fs("p 1 0 1"))
    })
    tetra1 = cryspy.utils.auto_tetrahedron(
        "Tetra",
        atomset,
        metric,
        atomset.get_atom("Fe1").pos,
        ["H"],
        facecolor, faceopacity, plotedges, edgecolor, edgewidth
    )
    tetra2 = cryspy.utils.tetrahedron(
        "Tetra",
        atomset.get_atom("H1").pos,
        atomset.get_atom("H2").pos,
        atomset.get_atom("H4").pos,
        atomset.get_atom("H3").pos,
        facecolor, faceopacity, plotedges, edgecolor, edgewidth
    )
    assert tetra1 == tetra2

def test_auto_octahedron():
    metric = cryspy.geo.Cellparameters(1, 1, 1, 90, 90, 90).to_Metric()
    Atom = cryspy.crystal.Atom
    facecolor = (1, 1, 1)
    faceopacity = 0.5
    plotedges = True
    edgecolor = (0, 0, 0)
    edgewidth = 0.02
    atomset = cryspy.crystal.Atomset({
        Atom("Fe1", "Fe", fs("p 1/2 1/2 1/2")),
        Atom("H1", "H", fs("p 1/2 1/2 0")),
        Atom("H2", "H", fs("p 1/2 1/2 1")),
        Atom("H3", "H", fs("p 1/2 0 1/2")),
        Atom("H4", "H", fs("p 1/2 1 1/2")),
        Atom("H5", "H", fs("p 0 1/2 1/2")),
        Atom("H6", "H", fs("p 1 1/2 1/2"))
    })
    octa1 = cryspy.utils.auto_octahedron(
        "Octa",
        atomset,
        metric,
        atomset.get_atom("Fe1").pos,
        ["H"],
        facecolor, faceopacity, plotedges, edgecolor, edgewidth
    )
    octa2 = cryspy.utils.octahedron(
        "Octa",
        atomset.get_atom("H1").pos,
        atomset.get_atom("H3").pos,
        atomset.get_atom("H5").pos,
        atomset.get_atom("H4").pos,
        atomset.get_atom("H6").pos,
        atomset.get_atom("H2").pos,
        facecolor, faceopacity, plotedges, edgecolor, edgewidth
    )
    assert octa1 == octa2

