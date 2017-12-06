import cryspy
from cryspy.fromstr import fromstr as fs
import cryspy.const as const

def setup_rendering(povfilename, camera_pos=(1, -20, 10), camera_lookat=(0, 0, 0),
    camera_sky=(0, 0, 1), camera_angle=30, width=600, height=400, imagefilename=None):
    if imagefilename == None:
        imagefilename = povfilename[:-4] + ".png"
    outstr = ""
    outstr += "//START_CAM\n"
    outstr = ""
    (pos_x, pos_y, pos_z) = camera_pos
    (la_x, la_y, la_z) = camera_lookat
    (sky_x, sky_y, sky_z) = camera_sky
    outstr += "camera {\n"
    outstr += "    location <%f, %f, %f>\n"%(pos_x, pos_z, pos_y)
    outstr += "    angle %f\n"%(camera_angle)
    outstr += "    sky <%f, %f, %f>\n"%(sky_x, sky_z, sky_y)
    outstr += "    look_at <%f, %f, %f>\n"%(la_x, la_z, la_y)
    outstr += "    right <%i, 0, 0>\n"%(width)
    outstr += "    up <0, %i, 0>\n"%(height)
    outstr += "}\n"
    outstr += ""
    outstr += "background {color rgb <1, 1, 1>}\n"
    outstr += "\n"
    outstr += "light_source {\n"
    outstr += "    <0, 10, 3>\n"
    outstr += "    color rgb <1, 1, 1>\n"
    outstr += "}\n"
    outstr += "global_settings { ambient_light rgb <4, 4, 4> }\n"
    outstr += "//END_CAM\n"
    outstr += "\n"
    infile = open(povfilename, "r")
    instr = infile.read()
    infile.close()
    inlines = instr.split("\n")
    before_camera = True
    after_camera = False
    for inline in inlines:
        if after_camera:
            outstr += inline + "\n"
        if inline == "//START_CAM":
            before_camera = False
        if inline == "//END_CAM":
            after_camera = True
            
    outfile = open(povfilename, "w")
    outfile.write(outstr)
    outfile.close()
    renderfilename = povfilename[:-4] + "_render.sh"
    renderfile = open(renderfilename, "w")
    renderfile.write("povray Width=%i Height=%i +V +I%s +O%s +P +A0.2"%(width, height, povfilename, imagefilename))
    renderfile.close()
    

def make_povray_script(atomset, metric, outfilename):
    atomset = atomset.unpack_subsets()
    schmidt = metric.schmidttransformation
    outstr = ""
    outstr += "//START_CAM\n"
    outstr += "//END_CAM\n"
    outstr += draw_axis(metric, "x")
    outstr += draw_axis(metric, "y")
    outstr += draw_axis(metric, "z")
    outstr += "\n"

    atoms = []
    bonds = []
    faces = []
    for item in atomset.menge:
        if isinstance(item, cryspy.crystal.Atom):
            atoms.append(item)
        elif isinstance(item, cryspy.crystal.Bond):
            bonds.append(item)
        elif isinstance(item, cryspy.crystal.Face):
            faces.append(item)

    atomtypes = []
    for atom in atoms:
        typ = atom.typ
        if typ not in atomtypes:
            atomtypes.append(typ)

    for typ in atomtypes:
        (spheresize, color) = cryspy.tables.colorscheme(typ)
        (r, g, b) = color
        outstr += "#declare Atom_%s = sphere {\n"%(typ)
        outstr += "    <0, 0, 0>, %f\n"%(spheresize)
        outstr += "    pigment {\n"
        outstr += "        color rgb <%f, %f, %f>\n"%(r, g, b)
        outstr += "    }\n"
        outstr += "}\n"

    for atom in atoms:
        pos_c = schmidt ** atom.pos
        x = float(pos_c.x())
        y = float(pos_c.y())
        z = float(pos_c.z())
        outstr += "object {\n"
        outstr += "    Atom_%s\n"%(atom.typ)
        outstr += "    translate <%f, %f, %f>\n"%(x, z, y)
        outstr += "}\n"

    for bond in bonds:
        if bond.has_thickness:
            thickness = bond.thickness
        else:
            thickness = const.povray__std_bond_thickness
        if bond.has_color:
            color = bond.color
        else:
            color = const.povray__std_bond_color
        outstr += draw_cylinder(metric, bond.start, bond.target, thickness, color)
 
    for face in faces:
        outstr += draw_face(metric, face)

    outfile = open(outfilename, "w")
    outfile.write(outstr)
    outfile.close()


def draw_axis(metric, xyorz):
    assert isinstance(xyorz, str), \
        "xyorz must be of type str. It might be 'x', 'y' or 'z'."
    assert xyorz in ['x', 'y', 'z'], \
        "xyorz must be of type str. It might be 'x', 'y' or 'z'."

    outstr = ""
    start = fs("p 0 0 0")
    if xyorz == "x":
        end = fs("p 1 0 0")
    elif xyorz == "y":
        end = fs("p 0 1 0")
    elif xyorz == "z":
        end = fs("p 0 0 1")
    length = metric.length(end - cryspy.geo.origin)
    tip_start = cryspy.geo.origin + \
        (end - cryspy.geo.origin)* (1 - const.povray__height_of_axis_tip / length)
    outstr += draw_cylinder(
        metric, start, tip_start,
        const.povray__thickness_of_axis_shaft,
        const.povray__axes_color
    )
    outstr += draw_cone(
        metric, tip_start, end,
        const.povray__thickness_of_axis_tip,
        const.povray__axes_color
    )
    return outstr

def draw_cylinder(metric, start, end, thickness, color):
    assert isinstance(metric, cryspy.geo.Metric), \
        "metric must be of type cryspy.geo.Metric."
    assert isinstance(start, cryspy.geo.Pos) \
        and isinstance(end, cryspy.geo.Pos), \
        "start and end must be of type cryspy.geo.Pos."
    assert isinstance(color, list) or isinstance(color, tuple), \
        "color must be of type list or tuple."
    assert len(color) == 3, \
        "color must be a list of length 3."
    for item in range(len(color)):
        assert isinstance(item, float) or isinstance(item, int), \
            "color must be a list of int or float."

    outstr = ""
    schmidt = metric.schmidttransformation
    start_c = schmidt ** start
    end_c = schmidt ** end
    start_x = float(start_c.x())
    start_y = float(start_c.y())
    start_z = float(start_c.z())
    end_x = float(end_c.x())
    end_y = float(end_c.y())
    end_z = float(end_c.z())

    outstr += "cylinder {\n"
    outstr += "    <%f, %f, %f>,\n"%(start_x, start_z, start_y)
    outstr += "    <%f, %f, %f>,\n"%(end_x, end_z, end_y)
    outstr += "    %f\n"%(thickness)
    outstr += "    pigment {\n"
    r = color[0]
    g = color[1]
    b = color[2]
    outstr += "        color rgb <%f, %f, %f>\n"%(r, g, b)
    outstr += "    }\n"
    outstr += "}\n"
    return outstr

def draw_cone(metric, start, end, thickness, color):
    assert isinstance(metric, cryspy.geo.Metric), \
        "metric must be of type cryspy.geo.Metric."
    assert isinstance(start, cryspy.geo.Pos) \
        and isinstance(end, cryspy.geo.Pos), \
        "start and end must be of type cryspy.geo.Pos."
    assert isinstance(color, list) or isinstance(color, tuple), \
        "color must be of type list or tuple."
    assert len(color) == 3, \
        "color must be a list of length 3."
    for item in range(len(color)):
        assert isinstance(item, float) or isinstance(item, int), \
            "color must be a list of int or float."


    outstr = ""
    schmidt = metric.schmidttransformation
    start_c = schmidt ** start
    end_c = schmidt ** end
    start_x = float(start_c.x())
    start_y = float(start_c.y())
    start_z = float(start_c.z())
    end_x = float(end_c.x())
    end_y = float(end_c.y())
    end_z = float(end_c.z())

    outstr += "cone {\n"
    outstr += "    <%f, %f, %f>,\n"%(start_x, start_z, start_y)
    outstr += "    %f\n"%(thickness)
    outstr += "    <%f, %f, %f>,\n"%(end_x, end_z, end_y)
    outstr += "    0\n"
    outstr += "    pigment {\n"
    r = color[0]
    g = color[1]
    b = color[2]
    outstr += "        color rgb <%f, %f, %f>\n"%(r, g, b)
    outstr += "    }\n"
    outstr += "}\n"
    return outstr

def draw_face(metric, face):
    if face.has_color:
        color = face.color
    else:
        color = const.povray__std_face_color
    (r, g, b) = color
    if face.has_opacity:
        opacity = face.opacity
    else:
        opacity = const.povray__std_face_opacity
    schmidt = metric.schmidttransformation
    outstr = ""
    number_of_corners = len(face.corners)
    outstr += "mesh2 {\n"
    outstr += "    vertex_vectors {"
    outstr += "%i, "%(number_of_corners)
    for corner in face.corners:
        pos_c = schmidt ** corner
        x = float(pos_c.x())
        y = float(pos_c.y())
        z = float(pos_c.z())
        outstr += "<%f, %f, %f>, "%(x, z, y)
    outstr = outstr[:-2]
    outstr += "}\n"
    outstr += "    face_indices {"
    outstr += "%i, "%(number_of_corners - 2)
    for i in range(1, number_of_corners - 1):
        outstr += "<%i, %i, %i>, "%(0, i, i+1)
    outstr = outstr[:-2]
    outstr += "}\n"
    outstr += "    pigment {\n"
    outstr += "        color rgbt <%f, %f, %f, %f>\n"%(r, g, b, 1 - opacity)
    outstr += "    }\n"
    outstr += "}\n"
    return outstr
