import cryspy
from cryspy.fromstr import fromstr as fs
import cryspy.numbers as nb
import cryspy.geo as geo
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


def fill(atomset, extraextensions):
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
    return fill_plusminus_clever(
               atomset,
               [extraextensions[0], extraextensions[0],
                extraextensions[1], extraextensions[1],
                extraextensions[2], extraextensions[2]],
           )

def fill_hexagon(atomset, extraextensions):
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
    atomset = fill_plusminus_clever(atomset, [0, extraextensions[0],
                                    0, extraextensions[0],
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

    face1 = cryspy.crystal.Face("Face1", [one, two, top])
    face2 = cryspy.crystal.Face("Face2", [two, three, top])
    face3 = cryspy.crystal.Face("Face3", [three, four, top])
    face4 = cryspy.crystal.Face("Face4", [four, one, top])
    face5 = cryspy.crystal.Face("Face5", [one, two, bottom])
    face6 = cryspy.crystal.Face("Face6", [two, three, bottom])
    face7 = cryspy.crystal.Face("Face7", [three, four, bottom])
    face8 = cryspy.crystal.Face("Face8", [four, one, bottom])

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
                    print(loop_header)
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
                        print(atom_name, atom_type, x, y, z)
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

