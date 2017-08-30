import cryspy
from cryspy.fromstr import fromstr as fs


def test_elementary_Goniometer():
    G = cryspy.lab.Goniometer("translation", "x", "positive", "wrumm")
    assert G.operator({"wrumm": fs("1/3")}) == \
        cryspy.geo.Operator(fs("1 0 0 1/3 \n 0 1 0 0 \n 0 0 1 0 \n 0 0 0 1"))
    assert G.operator({"wrumm": fs("1/3")}) ** fs("p 0 0 0") == fs("p 1/3 0 0")
    G = cryspy.lab.Goniometer("translation", "y", "positive", "wrumm")
    assert G.operator({"wrumm": fs("1/3")}) == \
        cryspy.geo.Operator(fs("1 0 0 0 \n 0 1 0 1/3 \n 0 0 1 0 \n 0 0 0 1"))
    G = cryspy.lab.Goniometer("translation", "z", "positive", "wrumm")
    assert G.operator({"wrumm": fs("1/3")}) == \
        cryspy.geo.Operator(fs("1 0 0 0 \n 0 1 0 0 \n 0 0 1 1/3 \n 0 0 0 1"))
    G = cryspy.lab.Goniometer("translation", "x", "negative", "wrumm")
    assert G.operator({"wrumm": fs("1/3")}) == \
        cryspy.geo.Operator(fs("1 0 0 -1/3 \n 0 1 0 0 \n 0 0 1 0 \n 0 0 0 1"))
    G = cryspy.lab.Goniometer("translation", "y", "negative", "wrumm")
    assert G.operator({"wrumm": fs("1/3")}) == \
        cryspy.geo.Operator(fs("1 0 0 0 \n 0 1 0 -1/3 \n 0 0 1 0 \n 0 0 0 1"))
    G = cryspy.lab.Goniometer("translation", "z", "negative", "wrumm")
    assert G.operator({"wrumm": fs("1/3")}) == \
        cryspy.geo.Operator(fs("1 0 0 0 \n 0 1 0 0 \n 0 0 1 -1/3 \n 0 0 0 1"))



