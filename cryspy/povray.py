import cryspy
from cryspy.fromstr import fromstr as fs
import cryspy.const as const

def make_povray_script(atomset, metric, outfilename):
    outstr = ""
    outstr += "camera {\n"
    outstr += "    location <1, 1, -20>\n"
    outstr += "    look_at <0, 0, 0>\n"
    outstr += "}\n"
    outstr += "\n"
    outstr += "background {color rgb <1, 1, 1>}\n"
    outstr += draw_axis(metric, "x")
    outstr += draw_axis(metric, "y")
    outstr += draw_axis(metric, "z")

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
