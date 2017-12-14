import cryspy
from cryspy.fromstr import fromstr as fs
import cryspy.const as const

# After building a cryspy.crystal.Atomset with a cryspy.geo.Metric,
# call make_povray_ascript(atomset, metric, "imagename.pov") and then
# call setup_rendering("imagename.pov"). Then call imagename_render.sh
# which uses povray to render the image whith the settings you set before.
#
# make_povray_script() creates a pov-file, but without camera.
# setup_rendering() reopens this script and sets a camera.
# You can call it several times without calling make_povray_script() again,
# in order to adjust the camera.
# The sh-script contains a command line with a povray-call that has
# the correct parameters.

def setup_rendering(povfilename, camera_pos=(1, -20, 10), camera_lookat=(0, 0, 0),
    camera_sky=(0, 0, 1), camera_angle=30, width=600, height=400, imagefilename=None,
    legendlist=[]):
    camerasystem = Camerasystem(
        camera_pos, camera_lookat, camera_sky, camera_angle, width, height
    )

    if imagefilename == None:
        imagefilename = povfilename[:-4] + ".png"
    camstr = ""
    (pos_x, pos_y, pos_z) = camera_pos
    (la_x, la_y, la_z) = camera_lookat
    (sky_x, sky_y, sky_z) = camera_sky
    camstr += "camera {\n"
    camstr += "    location <%f, %f, %f>\n"%(pos_x, pos_z, pos_y)
    camstr += "    angle %f\n"%(camera_angle)
    camstr += "    sky <%f, %f, %f>\n"%(sky_x, sky_z, sky_y)
    camstr += "    look_at <%f, %f, %f>\n"%(la_x, la_z, la_y)
    camstr += "    right <%i, 0, 0>\n"%(width)
    camstr += "    up <0, %i, 0>\n"%(height)
    camstr += "}\n"
    camstr += ""
    camstr += "background {color rgb <1, 1, 1>}\n"
    camstr += "\n"
    camstr += "light_source {\n"
    camstr += "    <0, 10, 3>\n"
    camstr += "    color rgb <1, 1, 1>\n"
    camstr += "}\n"
    camstr += "global_settings { ambient_light rgb <4, 4, 4> }\n"
    infile = open(povfilename, "r")
    instr = infile.read()
    infile.close()
    inlines = instr.split("\n")
    during_cam = False
    cam_finished = False
    during_legend = False
    legend_finished = False
    outstr = ""
    for inline in inlines:
        if inline == "//END_CAM":
            during_cam = False
        if inline == "//START_CAM":
            during_cam = True
            outstr += inline + "\n"
        if inline == "//END_LEGEND":
            during_legend = False
        if inline == "//START_LEGEND":
            during_legend = True
            outstr += inline + "\n"
        if during_cam:
            if not cam_finished:
                outstr += camstr
                cam_finished = True
        elif during_legend:
            if not legend_finished:
                for t in range(len(legendlist)):
                    typ = legendlist[len(legendlist) - t - 1]
                    (x, y, z) = camerasystem.xyz(
                        -1 + cryspy.const.povray__legend_horizontal_margin,
                        -0.9 + cryspy.const.povray__legend_vertical_margin
                            + t*cryspy.const.povray__legend_spacing
                    )
                    outstr += "object {\n"
                    outstr += "    Atom_%s\n"%(typ)
                    outstr += "    translate <%f, %f, %f>\n"%(x, z, y)
                    outstr += "}\n"
                legend_finished = True
        else:
            outstr += inline + "\n"
            
    outfile = open(povfilename, "w")
    outfile.write(outstr)
    outfile.close()
    renderfilename = povfilename[:-4] + "_render.sh"
    renderfile = open(renderfilename, "w")
    renderfile.write("povray Width=%i Height=%i +V +I%s +O%s +P +A0.2"%(width, height, povfilename, imagefilename))
    renderfile.close()
    
    
class Camerasystem:
    def __init__(self, camera_pos, camera_lookat,
        camera_sky, camera_angle, width, height):
        def tuple_to_pos(tup):
            return fs("p %f %f %f"%(tup[0], tup[1], tup[2]))
        def tuple_to_dif(tup):
            return fs("d %f %f %f"%(tup[0], tup[1], tup[2]))
        camera_pos = tuple_to_pos(camera_pos)
        camera_lookat = tuple_to_pos(camera_lookat)
        camera_sky = tuple_to_dif(camera_sky)
        cart = cryspy.geo.Cellparameters(1, 1, 1, 90, 90, 90).to_Metric()
        direction = (camera_lookat - camera_pos) * (1 / cart.length(camera_lookat - camera_pos))
        up = camera_sky - direction * cart.dot(camera_sky, direction)
        up = up * (1 / cart.length(up))
        (x1, y1, z1) = (direction.x(), direction.y(), direction.z())
        (x2, y2, z2) = (up.x(), up.y(), up.z())
        right = fs("d %f %f %f"%(y1*z2 - y2*z1, z1*x2 - z2*x1, x1*y2 - x2*y1))
        tan = cryspy.numbers.dsin(camera_angle * 0.5) / cryspy.numbers.dcos(camera_angle * 0.5)
        up = up * cart.length(camera_lookat - camera_pos) * (tan * height / width)
        right = right * cart.length(camera_lookat - camera_pos) * tan
        self.right = right
        self.up = up
        self.lookat = camera_lookat

    def xyz(self, u, v):
        # u, v: camera-coordinates
        # returns (x, y, z): cartesian coordinates
        pos = self.lookat \
            + self.right * cryspy.numbers.Mixed(u) \
            + self.up * cryspy.numbers.Mixed(v)
        (x, y, z) = (pos.x(), pos.y(), pos.z())
        return (x, y, z)


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
    momentums = []
    for item in atomset.menge:
        if isinstance(item, cryspy.crystal.Atom):
            atoms.append(item)
        elif isinstance(item, cryspy.crystal.Bond):
            bonds.append(item)
        elif isinstance(item, cryspy.crystal.Face):
            faces.append(item)
        elif isinstance(item, cryspy.crystal.Momentum):
            momentums.append(item)

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

    outstr += "//START_LEGEND\n"
    outstr += "//END_LEGEND\n"

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

    for momentum in momentums:
        if momentum.has_plotlength:
            plotlength = momentum.plotlength
        else:
            plotlength = const.povray__std_momentum_plotlength
        if momentum.has_color:
            color = momentum.color
        else:
            color = const.povray__std_momentum_color
        x0 = float((schmidt ** momentum.pos).x())
        y0 = float((schmidt ** momentum.pos).y())
        z0 = float((schmidt ** momentum.pos).z())
        dx = float((schmidt ** momentum.direction).x())
        dy = float((schmidt ** momentum.direction).y())
        dz = float((schmidt ** momentum.direction).z())


        """
        length = np.sqrt(dx*dx + dy*dy + dz*dz)
        x1 = x0 - dx * plotlength / length
        y1 = y0 - dy * plotlength / length
        z1 = z0 - dz * plotlength / length
        x2 = x0 + dx * plotlength / length
        y2 = y0 + dy * plotlength / length
        z2 = z0 + dz * plotlength / length
        """

        length = metric.length(momentum.direction)
        start = momentum.pos - momentum.direction * cryspy.numbers.Mixed(plotlength / length)
        end = momentum.pos + momentum.direction * cryspy.numbers.Mixed(plotlength / length)
        outstr += draw_momentum(metric, start, end, color)


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

def draw_momentum(metric, start, end, color):
    outstr = ""
    length = metric.length(end - start)
    cone_start = end - (end - start)*cryspy.numbers.Mixed(const.povray__height_of_momentum_tip/length)
    thickness = const.povray__thickness_of_momentum_shaft
    outstr += draw_cylinder(metric, start, cone_start, thickness, color)
    thickness = const.povray__thickness_of_momentum_tip
    outstr += draw_cone(metric, cone_start, end, thickness, color)
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
