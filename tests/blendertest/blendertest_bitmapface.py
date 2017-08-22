import numpy as np
import cryspy
from cryspy.fromstr import fromstr as fs

metric = cryspy.geo.Cellparameters(1, 2, 3, 90, 90, 90).to_Metric()
bitmap = np.zeros([10, 10, 4])
bitmap += 1
bitmap[0, 0, 2] = 0
bitmap[9, 0, 1] = 0
bitmap[0, 9, 0] = 0
bitmap[9, 9, 0] = 0
bitmap[9, 9, 1] = 0
bitmap[9, 9, 2] = 0

bitmapface = cryspy.crystal.Bitmapface(
    "BF1",
    fs("p 0 1 0"), fs("p 1 0 0"), fs("p 0 1 1"), fs("p 1 0 1"),
    bitmap, "RGBA"
)

atomset = cryspy.crystal.Atomset({bitmapface})
cryspy.blender.make_blender_script(atomset, metric, "structure", "blenderscript.py")

