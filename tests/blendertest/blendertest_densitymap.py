import numpy as np
import pylab as pl
import cryspy
from cryspy.fromstr import fromstr as fs

metric = cryspy.geo.Cellparameters(13.6, 4.2, 15.2, 90, 99.8, 90).to_Metric()

array = cryspy.utils.read_densitymap("densitymap.asc")
origin = fs("p 1/2 0 0")
xtip = fs("p 0 1 0")
ytip = fs("p 0 0 2")
resolution = 10
slice = cryspy.utils.slice(array, origin, xtip, ytip, resolution)

maxvalue = max([-np.min(slice), np.max(slice)])
minvalue = -maxvalue
bitmap = cryspy.utils.slice_to_bitmap(slice, "bwr", [minvalue, maxvalue], "RGBA")

bf = cryspy.crystal.Bitmapface(
    "slice",
    origin, xtip, ytip, xtip + (ytip - origin),
    bitmap, "RGBA"
)

atomset = cryspy.crystal.Atomset({bf})

cryspy.blender.make_blender_script(
    atomset,
    metric,
    "structure",
    "blenderscript.py"
)
