import cryspy
from cryspy.fromstr import fromstr as fs


def test_elementary_Goniometer():
    G = cryspy.lab.Goniometer("translation", "x", "positive", "wrumm")
    assert str(G) == \
        " /    translate by   \\ \n" \
        "|            wrumm    |\n" \
        "|        along        |\n" \
        "|        x-axis       |\n" \
        " \\     positive      / "
   
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


    G = cryspy.lab.Goniometer("rotation", "x", "clockwise", "phi")
    assert G.operator({"phi": 90}) == \
        cryspy.geo.Operator(fs("1 0 0 0 \n 0 0 1 0 \n 0 -1 0 0 \n 0 0 0 1"))
    assert str(G) == \
        " /     rotate by    \\ \n" \
        "|              phi   |\n" \
        "|        around      |\n" \
        "|        x-axis      |\n" \
        " \\        clockwise / "
    G = cryspy.lab.Goniometer("rotation", "x", "counterclockwise", "phi")
    assert G.operator({"phi": 90}) == \
        cryspy.geo.Operator(fs("1 0 0 0 \n 0 0 -1 0 \n 0 1 0 0 \n 0 0 0 1"))
    assert G.operator({"phi": 90}) ** fs("p 0 1 0") == fs("p 0 0 1")
    G = cryspy.lab.Goniometer("rotation", "y", "counterclockwise", "phi")
    assert G.operator({"phi": 90}) == \
        cryspy.geo.Operator(fs("0 0 1 0 \n 0 1 0 0 \n -1 0 0 0 \n 0 0 0 1"))
    assert G.operator({"phi": 90}) ** fs("p 0 0 1") == fs("p 1 0 0")
    G = cryspy.lab.Goniometer("rotation", "z", "counterclockwise", "phi")
    assert G.operator({"phi": 90}) == \
        cryspy.geo.Operator(fs("0 -1 0 0 \n 1 0 0 0 \n 0 0 1 0 \n 0 0 0 1"))
    assert G.operator({"phi": 90, "does_not_exist": 0}) ** fs("p 1 0 0") == fs("p 0 1 0")
    assert str(G) == \
        " /     rotate by    \\ \n" \
        "|              phi   |\n" \
        "|        around      |\n" \
        "|        z-axis      |\n" \
        " \\ counterclockwise / "


    G1 = cryspy.lab.Goniometer("rotation", "z", "counterclockwise", "phi")
    G2 = cryspy.lab.Goniometer("rotation", "y", "counterclockwise", "theta")
    G3 = cryspy.lab.Goniometer("translation", "x", "positive", "s")
    G = G1 * G2
    assert G.operator({"phi": 90, "theta": 90}) == \
        cryspy.geo.Operator(
            cryspy.numbers.Matrix(
                [[ 0, -1,  0, 0],
                 [ 0,  0,  1, 0],
                 [-1,  0,  0, 0],
                 [ 0, 0,  0, 1]]
            )
        )
    assert str(G1*G2*G3) == \
        " /     rotate by    \\   /     rotate by    \\   /    translate by   \\ \n" \
        "|              phi   | |            theta   | |                s    |\n" \
        "|        around      |*|        around      |*|        along        |\n" \
        "|        z-axis      | |        y-axis      | |        x-axis       |\n" \
        " \\ counterclockwise /   \\ counterclockwise /   \\     positive      / "

