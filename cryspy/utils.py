import cryspy
from cryspy.fromstr import fromstr as fs
import cryspy.numbers as nb
import cryspy.geo as geo
import cryspy.crystal as crystal
import cryspy.const as const
import numpy as np

def calculate_twotheta(metric, wavelength, q):
    assert isinstance(metric, cryspy.geo.Metric), \
         "First argument of calculate_twotheta(...) must be of type cryspy.geo.Metric!"
    assert isinstance(wavelength, cryspy.numbers.Mixed) \
        or isinstance(wavelength, int) \
        or isinstance(wavelength, float), \
        "Second argument of calculate_twotheta(...) must be of type " \
        "cryspy.numbers.Mixed or int or float."
    assert isinstance(q, cryspy.geo.Rec), \
        "Third argument of calculate_twotheta(...) must be of type cryspy.geo.Rec!"
    # Lattice plane distance  =  1/(length of reciprocal vector)
    # can be found here:
    # Carmelo Giacovazzo et al.: Fundamentals of Crystallography
    # Oxford University Press (1992)
    d = float(1 / metric.length(q))
    theta = np.arcsin(float(wavelength)/2/d)
    twotheta = 2 * theta
    return twotheta

def calculate_dtwotheta(metric, wavelength, q):
    return cryspy.numbers.rad2deg(calculate_twotheta(metric, wavelength, q))

class Karussell:
    def __init__(self, metric, zerodirection, positivedirection):
        self.zerodir = zerodirection * (1 / metric.length(zerodirection))
        self.positivedir = positivedirection - self.zerodir * metric.dot(positivedirection, self.zerodir)
        self.positivedir *= 1 / metric.length(self.positivedir)
        self.metric = metric

    def direction(self, angle):
        x = nb.cos(angle)
        y = nb.sin(angle)
        return self.zerodir * x + self.positivedir * y

def plate(name, metric, zerodirection, positivedirection, radius, num_of_corners):
    assert isinstance(name, str), \
        "First parameter of cryspy.utils.plate() must be of type str."
    assert isinstance(metric, cryspy.geo.Metric), \
        "Second parameter of cryspy.utils.plate() must be of type cryspy.geo.Metric."
    assert isinstance(zerodirection, cryspy.geo.Dif) \
        and isinstance(positivedirection, cryspy.geo.Dif), \
        "Third and fourth parameter of cryspy.utils.plate() must be of typ cryspy.geo.Dif."
    assert isinstance(radius, int) \
        or isinstance(radius, float) \
        or isinstance(radius, cryspy.numbers.Mixed), \
        "Fifth parameter of cryspy.utils.plate must be of type int, float or cryspy.numbers.Mixed."
    assert isinstance(num_of_corners, int), \
        "Sixth parameter of cryspy.utils.plate must be of type int."
    karussell = Karussell(metric, zerodirection, positivedirection)
    twopi = 2 * np.pi
    corners = []
    for i in range(num_of_corners):
        d = karussell.direction(i * twopi / num_of_corners)
        corners.append(geo.origin + cryspy.geo.Dif(radius*d.value))
    return cryspy.crystal.Face(name, corners)


def fill_plusminus(atomset, extraextensions):
    assert isinstance(atomset, cryspy.crystal.Atomset), \
        "First argument of cryspy.utils.fill(...) must be of " \
        "type cryspy.crystal.Atomset."
    assert isinstance(extraextensions, list), \
        "Second argument of cryspy.utils.fill(...) must be of " \
        "type list."
    assert len(extraextensions) == 6, \
        "Second argument of cryspy.utils.fill(...) must be a " \
        "list of three numbers."
    for item in extraextensions:
        assert isinstance(item, cryspy.numbers.Mixed) \
            or isinstance(item, float) or isinstance(item, int), \
            "Scond argument of cryspy.utils.fill(...) must be a " \
            "list of three numbers."

    atomset_new =  \
                 ((atomset + "lbd") + fs("d -1 -1 -1")) \
               + ((atomset + "lb") + fs("d -1 -1  0")) \
               + ((atomset + "lbu") + fs("d -1 -1 +1")) \
               + ((atomset + "ld") + fs("d -1  0 -1")) \
               + ((atomset + "l") + fs("d -1  0  0")) \
               + ((atomset + "lu") + fs("d -1  0 +1")) \
               + ((atomset + "lfd") + fs("d -1 +1 -1")) \
               + ((atomset + "lf") + fs("d -1 +1  0")) \
               + ((atomset + "lfu") + fs("d -1 +1 +1")) \
               + ((atomset + "bd") + fs("d  0 -1 -1")) \
               + ((atomset + "b") + fs("d  0 -1  0")) \
               + ((atomset + "bu") + fs("d  0 -1 +1")) \
               + ((atomset + "d") + fs("d  0  0 -1")) \
               + ((atomset + "") + fs("d  0  0  0")) \
               + ((atomset + "u") + fs("d  0  0 +1")) \
               + ((atomset + "fd") + fs("d  0 +1 -1")) \
               + ((atomset + "f") + fs("d  0 +1  0")) \
               + ((atomset + "fu") + fs("d  0 +1 +1")) \
               + ((atomset + "rbd") + fs("d +1 -1 -1")) \
               + ((atomset + "rb") + fs("d +1 -1  0")) \
               + ((atomset + "rbu") + fs("d +1 -1 +1")) \
               + ((atomset + "rd") + fs("d +1  0 -1")) \
               + ((atomset + "r") + fs("d +1  0  0")) \
               + ((atomset + "ru") + fs("d +1  0 +1")) \
               + ((atomset + "rfd") + fs("d +1 +1 -1")) \
               + ((atomset + "rf") + fs("d +1 +1  0")) \
               + ((atomset + "rfu") + fs("d +1 +1 +1")) \

    menge = atomset_new.menge
    menge_new = set([])
    extra_xm = extraextensions[0]
    extra_xp = extraextensions[1]
    extra_ym = extraextensions[2]
    extra_yp = extraextensions[3]
    extra_zm = extraextensions[4]
    extra_zp = extraextensions[5]
    for atom in menge:
        if (0 - extra_xm <= float(atom.pos.x()) <= 1 + extra_xp) \
            and (0 - extra_ym <= float(atom.pos.y()) <= 1 + extra_yp) \
            and (0 - extra_zm <= float(atom.pos.z()) <= 1 + extra_zp):
            menge_new.add(atom)
    return cryspy.crystal.Atomset(menge_new)


def fill_plusminus_clever(atomset, extraextensions):
    assert isinstance(atomset, cryspy.crystal.Atomset), \
        "First argument of cryspy.utils.fill(...) must be of " \
        "type cryspy.crystal.Atomset."
    assert isinstance(extraextensions, list), \
        "Second argument of cryspy.utils.fill(...) must be of " \
        "type list."
    assert len(extraextensions) == 6, \
        "Second argument of cryspy.utils.fill(...) must be a " \
        "list of three numbers."
    for item in extraextensions:
        assert isinstance(item, cryspy.numbers.Mixed) \
            or isinstance(item, float) or isinstance(item, int), \
            "Scond argument of cryspy.utils.fill(...) must be a " \
            "list of three numbers."

    extra_xm = extraextensions[0]
    extra_xp = extraextensions[1]
    extra_ym = extraextensions[2]
    extra_yp = extraextensions[3]
    extra_zm = extraextensions[4]
    extra_zp = extraextensions[5]

    def pos_is_within_the_box(pos):
        x = float(pos.x())
        y = float(pos.y())
        z = float(pos.z())
        if (-extra_xm <= x <= 1 + extra_xp) \
            and (-extra_ym <= y <= 1 + extra_yp) \
            and (-extra_zm <= z <= 1 + extra_zp):
            return True
        else:
            return False

    newset = set([])
    difxs = [fs("d -1 0 0"), fs("d 0 0 0"), fs("d 1 0 0")]
    difys = [fs("d 0 -1 0"), fs("d 0 0 0"), fs("d 0 1 0")]
    difzs = [fs("d 0 0 -1"), fs("d 0 0 0"), fs("d 0 0 1")]
    for item in atomset.menge:
        for xi in [0, 1, 2]:
            for yi in [0, 1, 2]:
                for zi in [0, 1, 2]:
                    dif = difxs[xi] + difys[yi] + difzs[zi]
                    if pos_is_within_the_box(item.pos + dif):
                        ending = ""
                        if xi == 0:
                            ending += "l"
                        if xi == 2:
                            ending += "r"
                        if yi == 0:
                            ending += "b"
                        if yi == 2:
                            ending += "f"
                        if zi == 0:
                            ending += "d"
                        if zi == 2:
                            ending += "u"
                        newitem = (item + ending) + dif
                        newset.add(newitem)
    return cryspy.crystal.Atomset(newset)


def fill(atomset, extraextensions, typesonly=None):
    assert isinstance(atomset, cryspy.crystal.Atomset), \
        "First argument of cryspy.utils.fill(...) must be of " \
        "type cryspy.crystal.Atomset."
    assert isinstance(extraextensions, list), \
        "Second argument of cryspy.utils.fill(...) must be of " \
        "type list."
    assert len(extraextensions) == 3, \
        "Second argument of cryspy.utils.fill(...) must be a " \
        "list of three numbers."
    for item in extraextensions:
        assert isinstance(item, cryspy.numbers.Mixed) \
            or isinstance(item, float) or isinstance(item, int), \
            "Scond argument of cryspy.utils.fill(...) must be a " \
            "list of three numbers."
    if typesonly == None:
        return fill_plusminus_clever(
                   atomset,
                   [extraextensions[0], extraextensions[0],
                    extraextensions[1], extraextensions[1],
                    extraextensions[2], extraextensions[2]],
               )
    else:
        assert isinstance(typesonly, list), \
            "Argument typesonly of cryspy.utils.fill(...) must " \
            "be of type list."
        for typ in typesonly:
            assert isinstance(typ, str), \
                "Argument typesonly of cryspy.utils.fill(...) " \
                "must be a list of str."
        atomset1 = cryspy.crystal.Atomset(set([]))
        for atom in atomset.menge:
            if isinstance(atom, cryspy.crystal.Atom):
                if atom.typ in typesonly:
                    atomset1.add(atom)
        atomset1 = fill_plusminus_clever(
            atomset1,
            [extraextensions[0], extraextensions[0],
             extraextensions[1], extraextensions[1],
             extraextensions[2], extraextensions[2]
            ]
        )
        return atomset + atomset1
        
def fill_hexagon(atomset, extraextensions, typesonly=None):
    # extraextensions: [radially, down, up]
    #     for example: [0.05, 0.1, 0.5]
    #                  goes 0.05 unit cells larger than the Hexagon,
    #                  0.1 down in z-direction and 0.5 up.
    assert isinstance(atomset, cryspy.crystal.Atomset), \
        "First argument of cryspy.utils.fill_hexagon(...) must be of " \
        "type cryspy.crystal.Atomset"
    assert isinstance(extraextensions, list), \
        "Second argument of cryspy.utils.fill_hexagon(...) must be of " \
        "type list."
    assert len(extraextensions) == 3, \
        "Second argument of cryspy.utils.fill(...) must be a " \
        "list of three numbers."
    for item in extraextensions:
        assert isinstance(item, cryspy.numbers.Mixed) \
            or isinstance(item, float) or isinstance(item, int), \
            "Scond argument of cryspy.utils.fill(...) must be a " \
            "list of three numbers."
    if typesonly == None:
        atomset = fill_plusminus_clever(atomset, [extraextensions[0], extraextensions[0],
                                        extraextensions[0], extraextensions[0],
                                        extraextensions[1], extraextensions[2]]
        )
        atomset =  atomset \
                + ((atomset + fs("d -1  0 0")) + "_hex1") \
                + ((atomset + fs("d -1 -1 0")) + "_hex2") \
                + ((atomset + fs("d  0 -1 0")) + "_hex3")
        newatomset = cryspy.crystal.Atomset(set([]))
        for item in atomset.menge:
            aux = float(item.pos.x() - item.pos.y())
            if -1 - extraextensions[0] < aux < 1 + extraextensions[0]:
                newatomset.add(item)
    
        return newatomset
    else:
        assert isinstance(typesonly, list), \
            "Argument typesonly of cryspy.utils.fill_hexagon(...) must " \
            "be of type list."
        for typ in typesonly:
            assert isinstance(typ, str), \
                "Argument typesonly of cryspy.utils.fill_hexagon(...) " \
                "must be a list of str."
        atomset1 = cryspy.crystal.Atomset(set([]))
        for atom in atomset.menge:
            if isinstance(atom, cryspy.crystal.Atom):
                if atom.typ in typesonly:
                    atomset1.add(atom)
        atomset1 = cryspy.utils.fill_hexagon(atomset1, extraextensions)
        return atomset + atomset1
       
    
def octahedron(name, top, one, two, three, four, bottom, 
               facecolor, faceopacity, plotedges, edgecolor, edgewidth):
    # name: any string for a name, e.g. "MyFancyOctahedron"
    # top, one, two, three, four, bottom: The six corners of octahedron.
    #     top and bottom are the poles, one ... four are the
    #     equatorial corners. The corners must be objects of type
    #     cryspy.geo.Pos .
    # facecolor: e.g. (1, 0, 0) for red
    # faceopacity: 0 = invisible -> 1 = fully opaque
    # plot edge: True = with edges, False = without edges
    # edgecolor: e.g. (0, 0, 0) for black
    # edgewidth: width of edge in Angstroem, e.g. 0.1

    assert isinstance(name, str), \
        "The name of the octahedron must be of type str."
    for corner in [top, one, two, three, four, bottom]:
        assert isinstance(corner, cryspy.geo.Pos), \
            "The corners of the octahedron must be of type " \
            "cryspy.geo.Pos ."
    for color in [facecolor, edgecolor]:
        assert isinstance(color, list) or isinstance(color, tuple), \
            "The face- and edgecolor of the octahedron must be " \
            "lists or tuples."
        for item in color:
            assert isinstance(item, float) \
                or isinstance(item, int) \
                or isinstance(item, cryspy.numbers.Mixed), \
                "The face- and edgecolor of the octahedron must be " \
                "lists or tuples of type float, int or " \
                "cryspy.numbers.Mixed ."
    assert isinstance(faceopacity, float) \
        or isinstance(faceopacity, int), \
        "The faceopacity of the octahedron must be of type " \
        "float or int."
    assert isinstance(plotedges, bool), \
        "The parameter plotedges of the octahedron (says whether " \
        "to plot the edges as cylinders or not) must be of " \
        "of type bool (True or False). "
    assert isinstance(edgewidth, float) \
        or isinstance(edgewidth, int), \
        "The edgewidth of the octahedron must be of type " \
        "float or int."

    face1 = cryspy.crystal.Face("Face1", [top, one, two])
    face2 = cryspy.crystal.Face("Face2", [top, two, three])
    face3 = cryspy.crystal.Face("Face3", [top, three, four])
    face4 = cryspy.crystal.Face("Face4", [top, four, one])
    face5 = cryspy.crystal.Face("Face5", [bottom, two, one])
    face6 = cryspy.crystal.Face("Face6", [bottom, three, two])
    face7 = cryspy.crystal.Face("Face7", [bottom, four, three])
    face8 = cryspy.crystal.Face("Face8", [bottom, one, four])

    faces = {face1, face2, face3, face4, face5, face6, face7, face8}
    for face in faces:
        face.set_color(facecolor)
        face.set_opacity(faceopacity)

    if plotedges:
        edge1 = cryspy.crystal.Bond("Edge1", top, one)
        edge2 = cryspy.crystal.Bond("Edge2", top, two)
        edge3 = cryspy.crystal.Bond("Edge3", top, three)
        edge4 = cryspy.crystal.Bond("Edge4", top, four)
        edge5 = cryspy.crystal.Bond("Edge5", one, two)
        edge6 = cryspy.crystal.Bond("Edge6", two, three)
        edge7 = cryspy.crystal.Bond("Edge7", three, four)
        edge8 = cryspy.crystal.Bond("Edge8", four, one)
        edge9 = cryspy.crystal.Bond("Edge9", one, bottom)
        edge10 = cryspy.crystal.Bond("Edge10", two, bottom)
        edge11 = cryspy.crystal.Bond("Edge11", three, bottom)
        edge12 = cryspy.crystal.Bond("Edge12", four, bottom)
        edges = {edge1, edge2, edge3, edge4,
                 edge5, edge6, edge7, edge8,
                 edge9, edge10, edge11, edge12}
        for edge in edges:
            edge.set_color(edgecolor)
            edge.set_thickness(edgewidth)
    else:
        edges = set([])


    edges_and_faces = edges | faces

    centre_of_gravity = cryspy.geo.centre_of_gravity(
        [top, one, two, three, four, bottom]
    )
    subset = cryspy.crystal.Subset(
        name,
        centre_of_gravity,
        edges_and_faces
    )
    return subset

def get_nearest_neighbours(atomset, metric, centre, typelist, number):
    atomlist = []
    for atom in atomset.menge:
        if isinstance(atom, crystal.Atom):
            if atom.typ in typelist:
                atomlist.append(atom)

    distancelist = []
    for atom in atomlist:
        distancelist.append(float(metric.length(centre - atom.pos)))

    atomlist = [i for (j, i) in sorted(zip(distancelist, atomlist), key=lambda pair: pair[0])]
    atomlist = atomlist[0:number]
    return atomlist

def find_atom(atomset, metric, pos, typ=None):
    atomlist = []
    for atom in atomset.menge:
        if isinstance(atom, crystal.Atom):
            if typ == None:
                atomlist.append(atom)
            elif atom.typ == typ:
                atomlist.append(atom)

    distancelist = []
    for atom in atomlist:
        distancelist.append(float(metric.length(pos - atom.pos)))

    atomlist = [i for (j, i) in sorted(zip(distancelist, atomlist), key=lambda pair: pair[0])]
    found_atom = atomlist[0]
    assert float(metric.length(found_atom.pos - pos)) <= const.utils__delta_for_finding, \
        "Error: There is no atom near the position \n %s.\n" \
        "Maybe it is useful to increase the number " \
        "const.utils__delta_for_finding which gives the " \
        "tolerance."%(str(pos))
    return found_atom
   

def auto_octahedron(name, atomset, metric, centre, typelist, 
               facecolor, faceopacity, plotedges, edgecolor, edgewidth):
    assert isinstance(name, str), \
        "The name of the octahedron must be of type str."
    assert isinstance(atomset, cryspy.crystal.Atomset), \
        "The second entry of cryspy.utils.auto_octahedron() must be " \
        "of type cryspy.crystal.Atomset."
    assert isinstance(metric, cryspy.geo.Metric), \
        "The third entry of cryspy.utils.auto_octahedron() must be " \
        "of type cryspy.geo.Metric"
    assert isinstance(centre, cryspy.geo.Pos), \
        "The centre of the auto_octahedron must be of type " \
        "cryspy.geo.Pos ."
    for typ in typelist:
        assert isinstance(typ, str), \
            "The corners of the octahedron must be of type str."
    for color in [facecolor, edgecolor]:
        assert isinstance(color, list) or isinstance(color, tuple), \
            "The face- and edgecolor of the octahedron must be " \
            "lists or tuples."
        for item in color:
            assert isinstance(item, float) \
                or isinstance(item, int) \
                or isinstance(item, cryspy.numbers.Mixed), \
                "The face- and edgecolor of the octahedron must be " \
                "lists or tuples of type float, int or " \
                "cryspy.numbers.Mixed ."
    assert isinstance(faceopacity, float) \
        or isinstance(faceopacity, int), \
        "The faceopacity of the octahedron must be of type " \
        "float or int."
    assert isinstance(plotedges, bool), \
        "The parameter plotedges of the octahedron (says whether " \
        "to plot the edges as cylinders or not) must be of " \
        "of type bool (True or False). "
    assert isinstance(edgewidth, float) \
        or isinstance(edgewidth, int), \
        "The edgewidth of the octahedron must be of type " \
        "float or int."

    atomlist = get_nearest_neighbours(atomset, metric, centre, typelist, 6)
    topatom = atomlist[0]
    atomlist = atomlist[1:6]
    distancelist = []
    for atom in atomlist:
        distancelist.append(float(metric.length(topatom.pos - atom.pos)))
    atomlist = [i for (j, i) in sorted(zip(distancelist, atomlist), key=lambda pair: pair[0])]

    atomlist2 = atomlist[0:3]
    distancelist2 = []
    for i in [0, 1, 2]:
        distancelist2.append(
            float(metric.length(atomlist2[i].pos - atomlist2[(i+1) % 3].pos))
          + float(metric.length(atomlist2[i].pos - atomlist2[(i+2) % 3].pos))
        )
    print(atomlist2)
    atomlist2 = [i for (j, i) in sorted(zip(distancelist2, atomlist2), key=lambda pair: pair[0])]
    print(atomlist2)
    A = atomlist2[1]
    B = atomlist2[0]
    C = atomlist2[2]

    edge0 = A.pos - topatom.pos
    edge1 = B.pos - topatom.pos
    edge2 = C.pos - topatom.pos
    det = edge0.value.hglue(edge1.value).hglue(edge2.value).hglue(
        cryspy.numbers.Matrix([[0], [0], [0], [1]])
    ).det()

    if float(det) < 0:
        oneatom = A
        twoatom = B
        threeatom = C
        fouratom = atomlist[3]
        bottomatom = atomlist[4]
    else:
        oneatom = atomlist[3]
        twoatom = C
        threeatom = B
        fouratom = A
        bottomatom = atomlist[4]
    
    return octahedron(
        name,
        topatom.pos, oneatom.pos,
        twoatom.pos, threeatom.pos,
        fouratom.pos, bottomatom.pos,
        facecolor, faceopacity,
        plotedges, edgecolor, edgewidth
    )


def tetrahedron(name, one, two, three, four, 
               facecolor, faceopacity, plotedges, edgecolor, edgewidth):
    # name: any string for a name, e.g. "MyFancyTetrahedron"
    # one, two, three, four: The four corners of octahedron.
    #     The corners must be objects of type
    #     cryspy.geo.Pos .
    # facecolor: e.g. (1, 0, 0) for red
    # faceopacity: 0 = invisible -> 1 = fully opaque
    # plot edge: True = with edges, False = without edges
    # edgecolor: e.g. (0, 0, 0) for black
    # edgewidth: width of edge in Angstroem, e.g. 0.1

    assert isinstance(name, str), \
        "The name of the tetrahedron must be of type str."
    for corner in [one, two, three, four]:
        assert isinstance(corner, cryspy.geo.Pos), \
            "The corners of the tetrahedron must be of type " \
            "cryspy.geo.Pos ."
    for color in [facecolor, edgecolor]:
        assert isinstance(color, list) or isinstance(color, tuple), \
            "The face- and edgecolor of the tetrahedron must be " \
            "lists or tuples."
        for item in color:
            assert isinstance(item, float) \
                or isinstance(item, int) \
                or isinstance(item, cryspy.numbers.Mixed), \
                "The face- and edgecolor of the tetrahedron must be " \
                "lists or tuples of type float, int or " \
                "cryspy.numbers.Mixed ."
    assert isinstance(faceopacity, float) \
        or isinstance(faceopacity, int), \
        "The faceopacity of the tetrahedron must be of type " \
        "float or int."
    assert isinstance(plotedges, bool), \
        "The parameter plotedges of the tetrahedron (says whether " \
        "to plot the edges as cylinders or not) must be of " \
        "of type bool (True or False). "
    assert isinstance(edgewidth, float) \
        or isinstance(edgewidth, int), \
        "The edgewidth of the tetrahedron must be of type " \
        "float or int."

    face1 = cryspy.crystal.Face("Face1", [one, two, three])
    face2 = cryspy.crystal.Face("Face2", [one, three, four])
    face3 = cryspy.crystal.Face("Face3", [one, four, two])
    face4 = cryspy.crystal.Face("Face4", [four, three, two])

    faces = {face1, face2, face3, face4}
    for face in faces:
        face.set_color(facecolor)
        face.set_opacity(faceopacity)

    if plotedges:
        edge1 = cryspy.crystal.Bond("Edge1", one, two)
        edge2 = cryspy.crystal.Bond("Edge2", one, three)
        edge3 = cryspy.crystal.Bond("Edge3", one, four)
        edge4 = cryspy.crystal.Bond("Edge4", two, three)
        edge5 = cryspy.crystal.Bond("Edge5", three, four)
        edge6 = cryspy.crystal.Bond("Edge6", four, two)
        edges = {edge1, edge2, edge3, edge4,
                 edge5, edge6}
        for edge in edges:
            edge.set_color(edgecolor)
            edge.set_thickness(edgewidth)
    else:
        edges = set([])


    edges_and_faces = edges | faces

    centre_of_gravity = cryspy.geo.centre_of_gravity(
        [one, two, three, four]
    )
    subset = cryspy.crystal.Subset(
        name,
        centre_of_gravity,
        edges_and_faces
    )
    return subset

def auto_tetrahedron(name, atomset, metric, centre, typelist, 
               facecolor, faceopacity, plotedges, edgecolor, edgewidth):
    assert isinstance(name, str), \
        "The name of the tetrahedron must be of type str."
    assert isinstance(atomset, cryspy.crystal.Atomset), \
        "The second entry of cryspy.utils.auto_tetrahedron() must be " \
        "of type cryspy.crystal.Atomset."
    assert isinstance(metric, cryspy.geo.Metric), \
        "The third entry of cryspy.utils.auto_tetrahedron() must be " \
        "of type cryspy.geo.Metric"
    assert isinstance(centre, cryspy.geo.Pos), \
        "The centre of the auto_tetrahedron must be of type " \
        "cryspy.geo.Pos ."
    for typ in typelist:
        assert isinstance(typ, str), \
            "The corners of the tetrahedron must be of type str."
    for color in [facecolor, edgecolor]:
        assert isinstance(color, list) or isinstance(color, tuple), \
            "The face- and edgecolor of the tetrahedron must be " \
            "lists or tuples."
        for item in color:
            assert isinstance(item, float) \
                or isinstance(item, int) \
                or isinstance(item, cryspy.numbers.Mixed), \
                "The face- and edgecolor of the tetrahedron must be " \
                "lists or tuples of type float, int or " \
                "cryspy.numbers.Mixed ."
    assert isinstance(faceopacity, float) \
        or isinstance(faceopacity, int), \
        "The faceopacity of the tetrahedron must be of type " \
        "float or int."
    assert isinstance(plotedges, bool), \
        "The parameter plotedges of the tetrahedron (says whether " \
        "to plot the edges as cylinders or not) must be of " \
        "of type bool (True or False). "
    assert isinstance(edgewidth, float) \
        or isinstance(edgewidth, int), \
        "The edgewidth of the tetrahedron must be of type " \
        "float or int."

    atomlist = []
    for atom in atomset.menge:
        if isinstance(atom, cryspy.crystal.Atom):
            if atom.typ in typelist:
                atomlist.append(atom)

    distancelist = []
    for atom in atomlist:
        distancelist.append(float(metric.length(centre - atom.pos)))

    print(distancelist)
    atomlist = [i for (j, i) in sorted(zip(distancelist, atomlist), key=lambda pair: pair[0])]
    edge01 = atomlist[1].pos - atomlist[0].pos
    edge02 = atomlist[2].pos - atomlist[0].pos
    edge03 = atomlist[3].pos - atomlist[0].pos
    det = edge01.value.hglue(edge02.value).hglue(edge03.value).hglue(
        cryspy.numbers.Matrix([[0], [0], [0], [1]])
    ).det()
    if float(det) < 0:
        return tetrahedron(
            name,
            atomlist[0].pos, atomlist[1].pos,
            atomlist[2].pos, atomlist[3].pos,
            facecolor, faceopacity,
            plotedges, edgecolor, edgewidth
        )
    else:
         return tetrahedron(
            name,
            atomlist[0].pos, atomlist[3].pos,
            atomlist[2].pos, atomlist[1].pos,
            facecolor, faceopacity,
            plotedges, edgecolor, edgewidth
        )


def read_metric_from_cif(infilepathname):
    # So far only for cif-files generated by JANA2006, and even this
    # without any warranty, and maybe not all parameters.

    infile = open(infilepathname, "r")
    for line in infile:
        words = line.split()
        if len(words) >= 2:
            if words[0] == "_cell_length_a":
                a = fs(words[1])
            if words[0] == "_cell_length_b":
                b = fs(words[1])
            if words[0] == "_cell_length_c":
                c = fs(words[1])
            if words[0] == "_cell_angle_alpha":
                alpha = fs(words[1])
            if words[0] == "_cell_angle_beta" :
                beta  = fs(words[1])
            if words[0] == "_cell_angle_gamma":
                gamma = fs(words[1])
    infile.close()
    return cryspy.geo.Cellparameters(
        a, b, c, alpha, beta, gamma
    ).to_Metric()

def read_atomset_from_cif(infilepathname):
    # So far only for cif-files generated by JANA2006, and even this
    # without any warranty, and maybe not all parameters.
    infile = open(infilepathname, "r")
    status = "waiting_for_loop"
    loop_header = []
    menge = set([])
    for line in infile:
        words = line.split()
        if len(words) >= 1:
            if status == "reading_loop_header":
                if words[0][0] == "_":
                    loop_header += [words[0]]
                else:
                    status = "reading_loop_data"
            if status == "reading_loop_data":
                if len(words) == len(loop_header):
                    atom_name = None
                    atom_type = None
                    x = None
                    y = None
                    z = None
                    for i in range(len(loop_header)):
                        if loop_header[i] == "_atom_site_label":
                            atom_name = words[i]
                        if loop_header[i] == "_atom_site_type_symbol":
                            atom_type = words[i]
                        if loop_header[i] == "_atom_site_fract_x":
                            x = fs(words[i])
                        if loop_header[i] == "_atom_site_fract_y":
                            y = fs(words[i])
                        if loop_header[i] == "_atom_site_fract_z":
                            z = fs(words[i])
                    if      isinstance(atom_name, str) \
                        and isinstance(atom_type, str) \
                        and isinstance(x, cryspy.numbers.Mixed) \
                        and isinstance(y, cryspy.numbers.Mixed) \
                        and isinstance(z, cryspy.numbers.Mixed):
                        menge.add(
                            cryspy.crystal.Atom(
                                atom_name, atom_type,
                                cryspy.geo.Pos(
                                    cryspy.numbers.Matrix([[x], [y], [z], [1]])
                                )
                            )
                        )

            if words[0] == "loop_":
                loop_header = []
                status = "reading_loop_header"
        if len(words) == 0:
            if status == "reading_loop_data":
                status = "waiting_for_loop"
    infile.close()
    return cryspy.crystal.Atomset(menge)


def ldu_decomposition(A):
    # LDU-Decomposition:
    # A square Matrix A is (if possible) decomposed into
    # a product L*D*U, wherein
    # L is a unipotent lower triangle matrix
    # D is a diagonal matrix
    # U is a unipotent upper triangle matrix
    shape = A.shape()
    assert shape[0] == shape[1], \
        "Error: I can only do a LDU-decomposition " \
        "of a square matrix."
    n = shape[0]
    if n == 1:
        return [
            cryspy.numbers.Matrix([[1]]),
            A,
            cryspy.numbers.Matrix([[1]])
        ]
    else:
        a11 = A.liste[0].liste[0]
        v = A.block(1, n, 0, 1)
        w = A.block(0, 1, 1, n)
        B = A.block(1, n, 1, n)
        
        A_sub = B - (1/a11) * (v*w)
        [L_sub, D_sub, U_sub] = ldu_decomposition(A_sub)
        L = cryspy.numbers.Matrix.vglue(
            cryspy.numbers.Matrix.hglue(cryspy.numbers.Matrix([[1]]), cryspy.numbers.Matrix([[0]*(n-1)])),
            cryspy.numbers.Matrix.hglue((1/a11)*v, L_sub)
        )
        D = cryspy.numbers.Matrix.vglue(
            cryspy.numbers.Matrix.hglue(cryspy.numbers.Matrix([[a11]]), cryspy.numbers.Matrix([[0]*(n-1)])),
            cryspy.numbers.Matrix.hglue(cryspy.numbers.Matrix([[0]]*(n-1)), D_sub)
        )
        U = cryspy.numbers.Matrix.vglue(
            cryspy.numbers.Matrix.hglue(cryspy.numbers.Matrix([[1]]), (1/a11) * w),
            cryspy.numbers.Matrix.hglue(cryspy.numbers.Matrix([[0]]*(n-1)), U_sub)
        )
        return [L, D, U]
        
    

def calculate_transformation_for_normalized_axes(metric):
    # Returns the basis transformation matrix that is needed
    # to get from metric to a new metric with the following
    # properties:
    # * Directions of basis vectors: The same as metric
    # * Lengths of basis vectors: 1
    #
    # metric: type cryspy.geo.Metric
    
    l1 = metric.length(fs("d 1 0 0"))
    l2 = metric.length(fs("d 0 1 0"))
    l3 = metric.length(fs("d 0 0 1"))

    return cryspy.geo.Transformation(
               cryspy.numbers.Matrix([
                   [l1, 0, 0, 0],
                   [0, l2, 0, 0],
                   [0, 0, l3, 0],
                   [0, 0,  0, 1]
               ])
           )


def read_densitymap(infilename):
    # In JANA2006 choose the following directions for the
    # contour plot:
    # Other choices are not possibile for this!
    #    
    #      1st 2nd 3rd
    #  x   (*)
    #  y   ( ) (*)
    #  z   ( ) ( ) (*)
    
    
    infile = open(infilename, "r")
    iline = 0
    ix = 0
    iy = 0
    iz = 0
    for line in infile:
        iline += 1
        if iline == 1:
            words = line.split()
            assert len(words) == 3, \
                "Error: *asc-file must have three integers in the first line!"
            nx = int(words[0])
            ny = int(words[1])
            nz = int(words[2])
            array = np.zeros([nx, ny, nz])
        else:
            words = line.split()
            for word in words:
                array[ix, iy, iz] = float(word) 
                ix += 1
                if ix >= nx:
                    ix = 0
                    iy += 1
                if iy >= ny:
                    iy = 0
                    iz += 1
    infile.close()
    return array

def get_value(array, ix, iy, iz):
    (nx, ny, nz) = array.shape
    return array[ix % nx, iy % ny, iz % nz]

def interpolate(array, pos):
    assert isinstance(pos, cryspy.geo.Pos), \
        "Error: first argument of interpolate() must be of type " \
        "cryspy.Pos"

    def floor(f): # argument: float
        return int(np.floor(f))

    def ceil(f): # argument: float
        c = int(np.ceil(f))
        if f == c:
            return c + 1
        else:
            return c

    x = float(pos.x())
    y = float(pos.y())
    z = float(pos.z())
    
    (nx, ny, nz) = array.shape

    ix = x * nx
    iy = y * ny
    iz = z * nz

    fix = floor(ix)
    fiy = floor(iy)
    fiz = floor(iz)
    cix = ceil(ix)
    ciy = ceil(iy)
    ciz = ceil(iz)

    return get_value(array, fix, fiy, fiz) * (cix - ix) * (ciy - iy) * (ciz - iz)\
         + get_value(array, fix, fiy, ciz) * (cix - ix) * (ciy - iy) * (iz - fiz)\
         + get_value(array, fix, ciy, fiz) * (cix - ix) * (iy - fiy) * (ciz - iz)\
         + get_value(array, fix, ciy, ciz) * (cix - ix) * (iy - fiy) * (iz - fiz)\
         + get_value(array, cix, fiy, fiz) * (ix - fix) * (ciy - iy) * (ciz - iz)\
         + get_value(array, cix, fiy, ciz) * (ix - fix) * (ciy - iy) * (iz - fiz)\
         + get_value(array, cix, ciy, fiz) * (ix - fix) * (iy - fiy) * (ciz - iz)\
         + get_value(array, cix, ciy, ciz) * (ix - fix) * (iy - fiy) * (iz - fiz)






class Transformer():
    # Coordinate systems:
    # * alice:   3D-System of the crystal unit cell
    # * bob:     2D-Subspace of 3D, spanned by the vectors xtip, ytip
    # * charlie: Like bob, but with cartesian basis.

    def __init__(self, origin, xtip, ytip, resolution):
        # origin: Origin of system bob written in system alice
        # xtip, ytip: tips of the axes of system bob written in alice
        # resolution: number of pixels per column/row in the drawing.
        self.resolution = resolution
        assert  isinstance(origin, cryspy.geo.Pos) \
            and isinstance(xtip, cryspy.geo.Pos) \
            and isinstance(ytip, cryspy.geo.Pos), \
            "The second, third and fourth parameters for creating an " \
            "object of type Transformer must be of type cryspy.geo.Pos ."
        if isinstance(resolution, cryspy.numbers.Mixed):
            resolution = resolution.value
        assert isinstance(resolution, int), \
            "The last parameter for creating an object of type " \
            "Transformer must be an integer number."       
        self.metric = None
        self.has_metric = False
        self.origin = origin
        self.xtip = xtip
        self.ytip = ytip
        self.resolution = resolution


    def set_metric(self, metric): 
        # metric: Metric of the crystal structure (alice)
        assert isinstance(metric, cryspy.geo.Metric), \
            "The first parameter for setting a metric for object of type " \
            "Transformer must be of type cryspy.geo.Metric ."
        self.metric = metric
        self.has_metric = True
        # Tips of the axes of system charlie written in system alice,
        # calculated by Schmidt:
        utip = origin + (xtip - origin) * (1 / metric.length(xtip - origin))
        vtip = origin \
             + (ytip - origin) \
             - (utip - origin) * metric.dot(ytip - origin, utip - origin)
        vtip = origin + (vtip - origin) * (1 / metric.length(vtip - origin))
        self.utip = utip
        self.vtip = vtip
        # Write the bob-axes xtip and ytip in sytem charlie:
        # (This is easy, because charlie is cartesian)
        u_xtip = metric.dot(xtip - origin, utip - origin)
        v_xtip = metric.dot(xtip - origin, vtip - origin)
        u_ytip = metric.dot(ytip - origin, utip - origin)
        v_ytip = metric.dot(ytip - origin, vtip - origin)
        self.matrix_bob_to_charlie = cryspy.numbers.Matrix(
            [[u_xtip, u_ytip],
             [v_xtip, v_ytip]]
        )
        self.matrix_charlie_to_bob = self.matrix_bob_to_charlie.inv()

    def bob_to_alice(self, x, y):
        x = cryspy.numbers.Mixed(x)
        y = cryspy.numbers.Mixed(y)
        assert  isinstance(x, cryspy.numbers.Mixed) \
            and isinstance(y, cryspy.numbers.Mixed), \
            "The two parameters of bob_to_alice must be numbers."
        return self.origin \
            + (self.xtip - self.origin) * x \
            + (self.ytip - self.origin) * y

    def charlie_to_alice(self, u, v):
        assert self.has_metric, \
            "Error: For using the method " \
            "cryspy.utils.Transformer.charlie_to_alice() , you must " \
            "set a metric for the object of type Transformer ."
        u = cryspy.numbers.Mixed(u)
        v = cryspy.numbers.Mixed(v)
        assert  isinstance(u, cryspy.numbers.Mixed) \
            and isinstance(v, cryspy.numbers.Mixed), \
            "The two last parameters of charlie_to_alice must be numbers."
        return self.origin \
            + (self.utip - self.origin) * u \
            + (self.vtip - self.origin) * v

    def bob_to_charlie(self, x, y):
        assert self.has_metric, \
            "Error: For using the method " \
            "cryspy.utils.Transformer.bob_to_charlie() , you must " \
            "set a metric for the object of type Transformer ."
        vector = cryspy.numbers.Matrix([[x], [y]])
        vector_new = self.matrix_bob_to_charlie * vector
        return (vector_new.liste[0].liste[0], vector_new.liste[1].liste[0])

    def charlie_to_bob(self, u, v):
        assert self.has_metric, \
        "Error: For using the method " \
        "cryspy.utils.Transformer.charlie_to_bob() , you must " \
        "set a metric for the object of type Transformer ."
        vector = cryspy.numbers.Matrix([[u], [v]])
        vector_new = self.matrix_charlie_to_bob * vector
        return (vector_new.liste[0].liste[0], vector_new.liste[1].liste[0])

    def calculate_boundingbox(self):
        assert self.has_metric, \
        "Error: For using the method " \
        "cryspy.utils.Transformer.calculate_boundingbox() , you must " \
        "set a metric for the object of type Transformer ."
        southwest = self.bob_to_charlie(0, 0)
        southeast = self.bob_to_charlie(1, 0)
        northwest = self.bob_to_charlie(0, 1)
        northeast = self.bob_to_charlie(1, 1)
        corners = [southwest, southeast, northwest, northeast]
        us = [float(corner[0]) for corner in corners]
        vs = [float(corner[1]) for corner in corners]
        return [min(us), max(us), min(vs), max(vs)]

def slice(array, origin, xtip, ytip, resolution):
    # array: density-map array as returned by 
    #        cryspy.utils.read_densitymap()
    # origin, xtip, ytip: Three corners of the slice (type cryspy.geo.Pos):
    #         
    #             ytip
    #              *------------------
    #              |                  |
    #              |                  |
    #              |                  |
    #              |                  |
    #              *------------------* xtip
    #       origin
    #
    # resolution: integer (number of pixels in the slice in each direction)
    transformer = Transformer(origin, xtip, ytip, resolution)
    result = np.zeros([resolution, resolution])
    for u in range(resolution):
        for v in range(resolution):
            pos = transformer.bob_to_alice(u/resolution, v/resolution)
            result[u, v] = interpolate(array, pos)
    return result


def slice_to_bitmap(slice, type, colorrange, format):
    # slice: numpy.array like returned by cryspy.utils.slice() .
    # type: "bwr": blue-white-red map for negative and positive values
    # type: "btr": blue-transparent-red map
    # colorrange: [lowest value for mapping, highest value for mapping]
    # format: "RGBA": compare to cryspy.crystal.Bitmapface 
    
    (width, height) = slice.shape
    middle = (colorrange[1] + colorrange[0])/2
    halfrange = colorrange[1] - middle
    if (type == "bwr") and (format == "RGBA"):
        bitmap = np.zeros([width, height, 4])
        for j in range(height):
            for i in range(width):
                value = slice[i, j]
                white = 1 - np.abs(value - middle)/halfrange
                if value >= 0:
                    bitmap[i, j, :] = [1, white, white, 1]
                else:
                    bitmap[i, j, :] = [white, white, 1, 1]
    elif (type == "btr") and (format == "RGBA"):
        bitmap = np.zeros([width, height, 4])
        for j in range(height):
            for i in range(width):
                value = slice[i, j]
                opacity = np.abs(value - middle)/halfrange
                if value >= 0:
                    bitmap[i, j, :] = [1, 0, 0, opacity]
                else:
                    bitmap[i, j, :] = [0, 0, 1, opacity]

    return bitmap

def axes_box(thickness, color):
    bonds = [
        cryspy.crystal.Bond("a1", fs("p 0 0 0"), fs("p 1 0 0")),
        cryspy.crystal.Bond("a2", fs("p 0 0 1"), fs("p 1 0 1")),
        cryspy.crystal.Bond("a3", fs("p 0 1 1"), fs("p 1 1 1")),
        cryspy.crystal.Bond("a4", fs("p 0 1 0"), fs("p 1 1 0")),
        cryspy.crystal.Bond("b1", fs("p 0 0 0"), fs("p 0 1 0")),
        cryspy.crystal.Bond("b2", fs("p 1 0 0"), fs("p 1 1 0")),
        cryspy.crystal.Bond("b3", fs("p 1 0 1"), fs("p 1 1 1")),
        cryspy.crystal.Bond("b4", fs("p 0 0 1"), fs("p 0 1 1")),
        cryspy.crystal.Bond("c1", fs("p 0 0 0"), fs("p 0 0 1")),
        cryspy.crystal.Bond("c2", fs("p 0 1 0"), fs("p 0 1 1")),
        cryspy.crystal.Bond("c3", fs("p 1 1 0"), fs("p 1 1 1")),
        cryspy.crystal.Bond("c4", fs("p 1 0 0"), fs("p 1 0 1")),
    ]
    for bond in bonds:
        bond.set_color(color)
        bond.set_thickness(thickness)
    
    return cryspy.crystal.Subset(
        "Axes_Box",
        fs("p 0 0 0"), 
        {bond for bond in bonds}
    )

def axes_box_hexagon(thickness, color):
    bonds = [
        cryspy.crystal.Bond("a01", fs("p 0 0 0"), fs("p 1 0 0")),
        cryspy.crystal.Bond("a02", fs("p 0 0 0"), fs("p 0 1 0")),
        cryspy.crystal.Bond("a03", fs("p 0 0 0"), fs("p -1 -1 0")),
        cryspy.crystal.Bond("a04", fs("p 0 0 1"), fs("p 1 0 1")),
        cryspy.crystal.Bond("a05", fs("p 0 0 1"), fs("p 0 1 1")),
        cryspy.crystal.Bond("a06", fs("p 0 0 1"), fs("p -1 -1 1")),
        cryspy.crystal.Bond("a07", fs("p 1 0 0"), fs("p 1 1 0")),
        cryspy.crystal.Bond("a08", fs("p 1 1 0"), fs("p 0 1 0")),
        cryspy.crystal.Bond("a09", fs("p 0 1 0"), fs("p -1 0 0")),
        cryspy.crystal.Bond("a10", fs("p -1 0 0"), fs("p -1 -1 0")),
        cryspy.crystal.Bond("a11", fs("p -1 -1 0"), fs("p 0 -1 0")),
        cryspy.crystal.Bond("a12", fs("p 0 -1 0"), fs("p 1 0 0")),
        cryspy.crystal.Bond("a13", fs("p 1 0 1"), fs("p 1 1 1")),
        cryspy.crystal.Bond("a14", fs("p 1 1 1"), fs("p 0 1 1")),
        cryspy.crystal.Bond("a15", fs("p 0 1 1"), fs("p -1 0 1")),
        cryspy.crystal.Bond("a16", fs("p -1 0 1"), fs("p -1 -1 1")),
        cryspy.crystal.Bond("a17", fs("p -1 -1 1"), fs("p 0 -1 1")),
        cryspy.crystal.Bond("a18", fs("p 0 -1 1"), fs("p 1 0 1")),
        cryspy.crystal.Bond("a19", fs("p 1 0 0"), fs("p 1 0 1")),
        cryspy.crystal.Bond("a20", fs("p 1 1 0"), fs("p 1 1 1")),
        cryspy.crystal.Bond("a21", fs("p 0 1 0"), fs("p 0 1 1")),
        cryspy.crystal.Bond("a22", fs("p -1 0 0"), fs("p -1 0 1")),
        cryspy.crystal.Bond("a23", fs("p -1 -1 0"), fs("p -1 -1 1")),
        cryspy.crystal.Bond("a24", fs("p 0 -1 0"), fs("p 0 -1 1")),
        cryspy.crystal.Bond("a25", fs("p 0 0 0"), fs("p 0 0 1")),
    ]
    for bond in bonds:
        bond.set_color(color)
        bond.set_thickness(thickness)
    
    return cryspy.crystal.Subset(
        "Axes_Box",
        fs("p 0 0 0"), 
        {bond for bond in bonds}
    )

def make_structures_similar(atomset1, atomset2, metric):
    # Two crystal structures might be very similar, but
    # small deviations can lead to the effect that
    # an atom is outside the unit cell. If the structures
    # are generating by applying a Spacegroup to an Atomset,
    # all atoms lie inside the unit cell. Thus, the positions
    # in the Atomset can be totally different even though the
    # differences are only very small. This function compares
    # the positions and corrects atomset2 in order to fit
    # to atomset1.
    """
    relevance_delta = 0.05 # Only atoms that are <= 0.05 relative units
                           # away from the unit cell border are taken
                           # into account.

    def seperate_to_relevant_and_notrelevant(atomset):
        relevant = cryspy.crystal.Atomset(set([]))
        notrelevant = cryspy.crystal.Atomset(set([]))
        for atom in atomset.menge:
            x = float(atom.pos.x())
            y = float(atom.pos.y())
            z = float(atom.pos.z())
            if      (relevance_delta < x < 1 - relevance_delta) \
                and (relevance_delta < y < 1 - relevance_delta) \
                and (relevance_delta < z < 1 - relevance_delta):
                    notrelevant.add(atom)
            else:
                    relevant.add(atom)
        return (relevant, notrelevant)

    (relevant1, notrelevant1) = seperate_to_relevant_and_notrelevant(atomset1)
    (relevant2, notrelevant2) = seperate_to_relevant_and_notrelevant(atomset2)

    relevant2_neu = cryspy.crystal.Atomset(set([]))
    for atom2 in relevant2.menge:
        atoms2 = []
        for zshift in [fs("d 0 0 -1"), fs("d 0 0 0"), fs("d 0 0 +1")]:
            for yshift in [fs("d 0 -1 0"), fs("d 0 0 0"), fs("d 0 +1 0")]:
                for xshift in [fs("d -1 0 0"), fs("d 0 0 0"), fs("d +1 0 0")]:
                    atoms2.append(atom2 + xshift + yshift + zshift)
        distances = []
        for atom1 in relevant1.menge:
            if atom1.typ == atom2.typ:
                distances_ = []
                for atom2_ in atoms2:
                    distances_.append(float(metric.length(atom2_.pos - atom1.pos)))
                index = distances_.index(min(distances))
                
                assert distances[index] <= 0.5, \
                    "Error: The atom distance is greater than 0.5 Angstroem!"
    """
    atomset2_all = cryspy.crystal.Atomset(set([]))
    for zshift in [fs("d 0 0 -1"), fs("d 0 0 0"), fs("d 0 0 +1")]:
        for yshift in [fs("d 0 -1 0"), fs("d 0 0 0"), fs("d 0 +1 0")]:
            for xshift in [fs("d -1 0 0"), fs("d 0 0 0"), fs("d +1 0 0")]:
                atomset2_all += (atomset2 + (xshift + yshift + zshift))

    atomset2_neu = cryspy.crystal.Atomset(set([]))
    for atom2 in atomset2_all.menge:
        for atom1 in atomset1.menge:
            if atom1.typ == atom2.typ:
                if float(metric.length(atom1.pos - atom2.pos)) <= 0.5:
                    atomset2_neu.add(atom2)

    return atomset2_neu
