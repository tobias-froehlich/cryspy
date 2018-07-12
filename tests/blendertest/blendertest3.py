import cryspy
from cryspy.fromstr import fromstr as fs

metric = cryspy.geo.Cellparameters(
    2, 1, 1, 90, 90, 90
).to_Metric()

atomset = cryspy.crystal.Atomset({
    cryspy.crystal.Atom("Fe1", "Fe", fs("p 1/4 1/4 1/4")),
    cryspy.crystal.Momentum("M1", fs("p 1/4 1/4 1/4"), fs("A 1 0 0"))
})

cryspy.blender.make_blender_script(
    atomset,
    metric,
    "structure",
    "/tmp/blenderscript.py"
)

cryspy.povray.make_povray_script(
    atomset,
    metric,
    "/tmp/structure.pov"
)

cryspy.povray.setup_rendering(
    "/tmp/structure.pov",
    camera_pos=(0.5, -5, 0.5),
    camera_lookat=(0.5, 0.5, 0.5),
    camera_angle=60
)
