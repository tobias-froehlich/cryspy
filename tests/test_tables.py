import pytest
import sys
sys.path.append("../src/")
from cryspy import geo as geo
from cryspy.fromstr import fromstr as fs
from cryspy import tables as tb


def test_cryspy_tables():
    sg = tb.spacegroup(1)
    assert sg.is_really_a_spacegroup() == True
#    sg = tb.spacegroup(2)
#    assert sg.is_really_a_spacegroup() == True
#    sg = tb.spacegroup(4)
#    assert sg.is_really_a_spacegroup() == True
#    sg = tb.spacegroup(7)
#    assert sg.is_really_a_spacegroup() == True
#    sg = tb.spacegroup(9)
#    assert sg.is_really_a_spacegroup() == True
#    sg = tb.spacegroup(10)
#    assert sg.is_really_a_spacegroup() == True
#    sg = tb.spacegroup(11)
#    assert sg.is_really_a_spacegroup() == True 
#    sg = tb.spacegroup(12)
#    assert sg.is_really_a_spacegroup() == True
#    sg = tb.spacegroup(13)
#    assert sg.is_really_a_spacegroup() == True
#    sg = tb.spacegroup(14)
#    assert sg.is_really_a_spacegroup() == True
#    sg = tb.spacegroup(15)
#    assert sg.is_really_a_spacegroup() == True
#    sg = tb.spacegroup(19)
#    assert sg.is_really_a_spacegroup() == True
#    sg = tb.spacegroup(26)
#    assert sg.is_really_a_spacegroup() == True
#    sg = tb.spacegroup(31)
#    assert sg.is_really_a_spacegroup() == True
#    sg = tb.spacegroup(33)
#    assert sg.is_really_a_spacegroup() == True
#    sg = tb.spacegroup(46)
#    assert sg.is_really_a_spacegroup() == True
#    sg = tb.spacegroup(59)
#    assert sg.is_really_a_spacegroup() == True
#    sg = tb.spacegroup(62)
#    assert sg.is_really_a_spacegroup() == True
#    sg = tb.spacegroup(63)
#    assert sg.is_really_a_spacegroup() == True
#    sg = tb.spacegroup(73)
#    assert sg.is_really_a_spacegroup() == True
#    sg = tb.spacegroup(142)
#    assert sg.is_really_a_spacegroup() == True
#    sg = tb.spacegroup(148)
#    assert sg.is_really_a_spacegroup() == True
#    sg = tb.spacegroup(166)
#    assert sg.is_really_a_spacegroup() == True
#    sg = tb.spacegroup(198)
#    assert sg.is_really_a_spacegroup() == True
#    sg = tb.spacegroup(186)
#    assert sg.is_really_a_spacegroup() == True
#    sg = tb.spacegroup(194)
#    assert sg.is_really_a_spacegroup() == True
#    sg = tb.spacegroup(212)
#    assert sg.is_really_a_spacegroup() == True
#    sg = tb.spacegroup(225)
#    assert sg.is_really_a_spacegroup() == True
#    sg = tb.spacegroup(227)
#    assert sg.is_really_a_spacegroup() == True


def test_colorscheme():
    assert tb.colorscheme("Mt") == (0.4777, (0.9216, 0.0000, 0.1490))
    tb.add_atom_to_colorscheme("My_atom", 0.5, (0.1, 0.2, 0.8))
    tb.colorscheme("My_atom")

def test_formfactor():
    assert 72.633286681565636 == tb.formfactor('Au', fs('0.13445'))
