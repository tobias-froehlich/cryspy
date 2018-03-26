import cryspy
from cryspy.fromstr import fromstr as fs

metric = cryspy.geo.Cellparameters(
    1, 1, 1, 90, 90, 90
).to_Metric()

atomset = cryspy.crystal.Atomset({
    cryspy.crystal.Atom("Fe1", "Fe", fs("p 1/4 1/4 1/4"))
    cryspy.crystal.Momentum("M1", fs("p 1/4 1/4 1/4"), fs("A 0 0 1"))
})

cryspy.blender.make_blender_script(
    atomset,
    metric,
    "structure",
    "/tmp/blenderscript.py"
)
