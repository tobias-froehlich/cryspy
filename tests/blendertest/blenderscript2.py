import bpy
import bmesh

for ob in bpy.data.objects:
    if ob.name.startswith('structure'):
        ob.select = True
bpy.ops.object.delete()
for me in bpy.data.meshes:
    if me.name.startswith('structure'):
        bpy.data.meshes.remove(me)
for mat in bpy.data.materials:
    if mat.name.startswith('structure'):
        bpy.data.materials.remove(mat)
for tex in bpy.data.textures:
    if tex.name.startswith('structure'):
        bpy.data.textures.remove(tex)
bpy.ops.object.select_all(action='DESELECT')
for object in bpy.data.objects:
    if object.type == 'LAMP':
        object.select = True
bpy.ops.object.delete()
bpy.data.worlds['World'].horizon_color = (1, 1, 1)
bpy.ops.object.lamp_add(type='POINT')
l = bpy.context.object
l.name = 'structure.Lamp1'
l.location = (5, -5, 10)
bpy.ops.object.lamp_add(type='HEMI')
l = bpy.context.object
l.name = 'structure.LampHemi'
l.location = (-10, -10, 10)
l.data.energy =     0.5000
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 6, diameter1 =     0.0500, diameter2 =     0.0500, depth =     4.7931)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     2.3966))
mesh = bpy.data.meshes.new('structure.meshXAxis_cylinder')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.XAxis_cylinder', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    1.0000,     0.0000,     0.0000,     0.0000], \
 [   -0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    0.0000,     0.0000,     0.0000)
bpy.context.scene.objects.link(ob1)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 24, diameter1 =     0.2000, diameter2 =     0.0100, depth =     0.5000)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     5.0431))
mesh = bpy.data.meshes.new('structure.meshXAxis_cone')
bm.to_mesh(mesh)
ob2 = bpy.data.objects.new('structure.XAxis_cone', mesh)
ob2.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob2.data.transform([[    1.0000,     0.0000,     0.0000,     0.0000], \
 [   -0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob2.location = (    0.0000,     0.0000,     0.0000)
bpy.context.scene.objects.link(ob2)
bpy.ops.object.select_all(action='DESELECT')
ob1.select = True
ob2.select = True
bpy.context.scene.objects.active = ob1
bpy.ops.object.join()
mat = bpy.data.materials.new('structure.material.XAxis')
mat.diffuse_color = (0, 0, 0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 6, diameter1 =     0.0500, diameter2 =     0.0500, depth =     5.3384)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     2.6692))
mesh = bpy.data.meshes.new('structure.meshYAxis_cylinder')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.YAxis_cylinder', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.0000,     1.0000,     0.0000,     0.0000], \
 [   -1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    0.0000,     0.0000,     0.0000)
bpy.context.scene.objects.link(ob1)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 24, diameter1 =     0.2000, diameter2 =     0.0100, depth =     0.5000)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     5.5884))
mesh = bpy.data.meshes.new('structure.meshYAxis_cone')
bm.to_mesh(mesh)
ob2 = bpy.data.objects.new('structure.YAxis_cone', mesh)
ob2.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob2.data.transform([[    0.0000,     1.0000,     0.0000,     0.0000], \
 [   -1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob2.location = (    0.0000,     0.0000,     0.0000)
bpy.context.scene.objects.link(ob2)
bpy.ops.object.select_all(action='DESELECT')
ob1.select = True
ob2.select = True
bpy.context.scene.objects.active = ob1
bpy.ops.object.join()
mat = bpy.data.materials.new('structure.material.YAxis')
mat.diffuse_color = (0, 0, 0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 6, diameter1 =     0.0500, diameter2 =     0.0500, depth =     6.9025)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     3.4512))
mesh = bpy.data.meshes.new('structure.meshZAxis_cylinder')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.ZAxis_cylinder', mesh)
ob1.data.transform([[    1.0000,     0.0000,    -0.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    1.0000,     0.0000,     0.0000,     0.0000], \
 [   -0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    0.0000,     0.0000,     0.0000)
bpy.context.scene.objects.link(ob1)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 24, diameter1 =     0.2000, diameter2 =     0.0100, depth =     0.5000)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     7.1525))
mesh = bpy.data.meshes.new('structure.meshZAxis_cone')
bm.to_mesh(mesh)
ob2 = bpy.data.objects.new('structure.ZAxis_cone', mesh)
ob2.data.transform([[    1.0000,     0.0000,    -0.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob2.data.transform([[    1.0000,     0.0000,     0.0000,     0.0000], \
 [   -0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob2.location = (    0.0000,     0.0000,     0.0000)
bpy.context.scene.objects.link(ob2)
bpy.ops.object.select_all(action='DESELECT')
ob1.select = True
ob2.select = True
bpy.context.scene.objects.active = ob1
bpy.ops.object.join()
mat = bpy.data.materials.new('structure.material.ZAxis')
mat.diffuse_color = (0, 0, 0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bpy.ops.mesh.primitive_cube_add(location=(0,0,0))
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.delete(type='VERT')
bpy.ops.object.mode_set(mode='OBJECT')
posobject = bpy.context.object
posobject.name = 'structure.Positions'
bpy.ops.mesh.primitive_ico_sphere_add(location=(0,0,0), size=0.292400, subdivisions=3)
ob = bpy.context.object
me = ob.data
me.name = 'structure.mesh.Mn'
bpy.ops.object.delete()
mat = bpy.data.materials.new('structure.material.Mn')
mat.diffuse_color = (0.6118, 0.4784, 0.7804)
me.materials.append(mat)
bpy.ops.mesh.primitive_ico_sphere_add(location=(0,0,0), size=0.200000, subdivisions=3)
ob = bpy.context.object
me = ob.data
me.name = 'structure.mesh.O'
bpy.ops.object.delete()
mat = bpy.data.materials.new('structure.material.O')
mat.diffuse_color = (1.0, 0.051, 0.051)
me.materials.append(mat)
bpy.ops.mesh.primitive_ico_sphere_add(location=(0,0,0), size=0.402100, subdivisions=3)
ob = bpy.context.object
me = ob.data
me.name = 'structure.mesh.Tb'
bpy.ops.object.delete()
mat = bpy.data.materials.new('structure.material.Tb')
mat.diffuse_color = (0.1882, 1.0, 0.7804)
me.materials.append(mat)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (0.000000, 2.919200, 7.402500)
ob = bpy.data.objects.new(             'structure.Atom001(Mn1_3r_2u)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (0.000000, 2.919200, 7.402500)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (6.860439, 3.933914, 4.078778)
ob = bpy.data.objects.new(             'structure.Atom002(O2_2rr)', bpy.data.meshes['structure.mesh.O'])
ob.location = (6.860439, 3.933914, 4.078778)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (5.842568, 2.724781, 1.850625)
ob = bpy.data.objects.new(             'structure.Atom003(O1_3r_3r)', bpy.data.meshes['structure.mesh.O'])
ob.location = (5.842568, 2.724781, 1.850625)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (7.390282, 5.643981, 1.850625)
ob = bpy.data.objects.new(             'structure.Atom004(O1_3rr)', bpy.data.meshes['structure.mesh.O'])
ob.location = (7.390282, 5.643981, 1.850625)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.097142, 5.643981, 1.850625)
ob = bpy.data.objects.new(             'structure.Atom005(O1_3r)', bpy.data.meshes['structure.mesh.O'])
ob.location = (2.097142, 5.643981, 1.850625)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-2.646570, 5.838400, 3.701250)
ob = bpy.data.objects.new(             'structure.Atom006(Mn1_3r_1lf)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (-2.646570, 5.838400, 3.701250)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-1.567299, 1.904486, 3.323722)
ob = bpy.data.objects.new(             'structure.Atom007(O2_2r_4l)', bpy.data.meshes['structure.mesh.O'])
ob.location = (-1.567299, 1.904486, 3.323722)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (0.549428, 2.724781, 1.850625)
ob = bpy.data.objects.new(             'structure.Atom008(O1_3r_3)', bpy.data.meshes['structure.mesh.O'])
ob.location = (0.549428, 2.724781, 1.850625)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-2.646570, 0.000000, 0.000000)
ob = bpy.data.objects.new(             'structure.Atom009(Mn1_3r_3l)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (-2.646570, 0.000000, 0.000000)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-2.097142, 0.194419, 5.551875)
ob = bpy.data.objects.new(             'structure.Atom010(O1_3r_2l)', bpy.data.meshes['structure.mesh.O'])
ob.location = (-2.097142, 0.194419, 5.551875)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.736024, 3.400284, 1.850625)
ob = bpy.data.objects.new(             'structure.Atom011(Tb1_3)', bpy.data.meshes['structure.mesh.Tb'])
ob.location = (2.736024, 3.400284, 1.850625)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (0.089454, 5.357316, 5.551875)
ob = bpy.data.objects.new(             'structure.Atom012(Tb1_2)', bpy.data.meshes['structure.mesh.Tb'])
ob.location = (0.089454, 5.357316, 5.551875)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (5.293140, 2.919200, 7.402500)
ob = bpy.data.objects.new(             'structure.Atom013(Mn1_3r_2ru)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (5.293140, 2.919200, 7.402500)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.646570, 5.838400, 3.701250)
ob = bpy.data.objects.new(             'structure.Atom014(Mn1_3r_1f)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (2.646570, 5.838400, 3.701250)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-2.646570, 5.838400, 0.000000)
ob = bpy.data.objects.new(             'structure.Atom015(Mn1_3r_3lf)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (-2.646570, 5.838400, 0.000000)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.646570, 5.838400, 7.402500)
ob = bpy.data.objects.new(             'structure.Atom016(Mn1_3r_3fu)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (2.646570, 5.838400, 7.402500)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (7.939710, 5.838400, 7.402500)
ob = bpy.data.objects.new(             'structure.Atom017(Mn1_3r_3rfu)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (7.939710, 5.838400, 7.402500)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (0.000000, 2.919200, 0.000000)
ob = bpy.data.objects.new(             'structure.Atom018(Mn1_3r_2)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (0.000000, 2.919200, 0.000000)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (0.000000, 2.919200, 3.701250)
ob = bpy.data.objects.new(             'structure.Atom019(Mn1_3r)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (0.000000, 2.919200, 3.701250)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (3.195998, 6.032819, 5.551875)
ob = bpy.data.objects.new(             'structure.Atom020(O1_3r_2f)', bpy.data.meshes['structure.mesh.O'])
ob.location = (3.195998, 6.032819, 5.551875)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (5.382594, 5.357316, 5.551875)
ob = bpy.data.objects.new(             'structure.Atom021(Tb1_2r)', bpy.data.meshes['structure.mesh.Tb'])
ob.location = (5.382594, 5.357316, 5.551875)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-2.557116, 3.400284, 1.850625)
ob = bpy.data.objects.new(             'structure.Atom022(Tb1_3l)', bpy.data.meshes['structure.mesh.Tb'])
ob.location = (-2.557116, 3.400284, 1.850625)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-2.646570, 5.838400, 7.402500)
ob = bpy.data.objects.new(             'structure.Atom023(Mn1_3r_3lfu)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (-2.646570, 5.838400, 7.402500)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (3.195998, 0.194419, 5.551875)
ob = bpy.data.objects.new(             'structure.Atom024(O1_3r_2)', bpy.data.meshes['structure.mesh.O'])
ob.location = (3.195998, 0.194419, 5.551875)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (7.939710, 5.838400, 0.000000)
ob = bpy.data.objects.new(             'structure.Atom025(Mn1_3r_3rf)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (7.939710, 5.838400, 0.000000)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (1.567299, 3.933914, 4.078778)
ob = bpy.data.objects.new(             'structure.Atom026(O2_2r)', bpy.data.meshes['structure.mesh.O'])
ob.location = (1.567299, 3.933914, 4.078778)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (7.939710, 0.000000, 3.701250)
ob = bpy.data.objects.new(             'structure.Atom027(Mn1_3r_1r)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (7.939710, 0.000000, 3.701250)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (6.860439, 3.933914, 7.024972)
ob = bpy.data.objects.new(             'structure.Atom028(O2_2r_6r)', bpy.data.meshes['structure.mesh.O'])
ob.location = (6.860439, 3.933914, 7.024972)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (5.203686, 0.481084, 1.850625)
ob = bpy.data.objects.new(             'structure.Atom029(Tb1_4)', bpy.data.meshes['structure.mesh.Tb'])
ob.location = (5.203686, 0.481084, 1.850625)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (5.293140, 2.919200, 3.701250)
ob = bpy.data.objects.new(             'structure.Atom030(Mn1_3rr)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (5.293140, 2.919200, 3.701250)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-1.079271, 4.823686, 3.323722)
ob = bpy.data.objects.new(             'structure.Atom031(O2_2r_1l)', bpy.data.meshes['structure.mesh.O'])
ob.location = (-1.079271, 4.823686, 3.323722)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (6.372411, 1.014714, 4.078778)
ob = bpy.data.objects.new(             'structure.Atom032(O2_2r_5r)', bpy.data.meshes['structure.mesh.O'])
ob.location = (6.372411, 1.014714, 4.078778)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (7.850256, 2.438116, 5.551875)
ob = bpy.data.objects.new(             'structure.Atom033(Tb1_5r)', bpy.data.meshes['structure.mesh.Tb'])
ob.location = (7.850256, 2.438116, 5.551875)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-0.549428, 3.113619, 5.551875)
ob = bpy.data.objects.new(             'structure.Atom034(O1_3r_1l)', bpy.data.meshes['structure.mesh.O'])
ob.location = (-0.549428, 3.113619, 5.551875)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (3.725841, 1.904486, 3.323722)
ob = bpy.data.objects.new(             'structure.Atom035(O2_2r_4)', bpy.data.meshes['structure.mesh.O'])
ob.location = (3.725841, 1.904486, 3.323722)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-1.567299, 1.904486, 0.377528)
ob = bpy.data.objects.new(             'structure.Atom036(O2_2r_2l)', bpy.data.meshes['structure.mesh.O'])
ob.location = (-1.567299, 1.904486, 0.377528)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.557116, 2.438116, 5.551875)
ob = bpy.data.objects.new(             'structure.Atom037(Tb1_5)', bpy.data.meshes['structure.mesh.Tb'])
ob.location = (2.557116, 2.438116, 5.551875)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-0.089454, 0.481084, 1.850625)
ob = bpy.data.objects.new(             'structure.Atom038(Tb1_4l)', bpy.data.meshes['structure.mesh.Tb'])
ob.location = (-0.089454, 0.481084, 1.850625)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (5.293140, 2.919200, 0.000000)
ob = bpy.data.objects.new(             'structure.Atom039(Mn1_3r_2r)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (5.293140, 2.919200, 0.000000)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (1.567299, 3.933914, 7.024972)
ob = bpy.data.objects.new(             'structure.Atom040(O2_2r_6)', bpy.data.meshes['structure.mesh.O'])
ob.location = (1.567299, 3.933914, 7.024972)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (7.939710, 0.000000, 0.000000)
ob = bpy.data.objects.new(             'structure.Atom041(Mn1_3r_3r)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (7.939710, 0.000000, 0.000000)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (3.725841, 1.904486, 0.377528)
ob = bpy.data.objects.new(             'structure.Atom042(O2_2r_2)', bpy.data.meshes['structure.mesh.O'])
ob.location = (3.725841, 1.904486, 0.377528)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (7.939710, 5.838400, 3.701250)
ob = bpy.data.objects.new(             'structure.Atom043(Mn1_3r_1rf)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (7.939710, 5.838400, 3.701250)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (1.079271, 1.014714, 4.078778)
ob = bpy.data.objects.new(             'structure.Atom044(O2_2r_5)', bpy.data.meshes['structure.mesh.O'])
ob.location = (1.079271, 1.014714, 4.078778)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-2.097142, 6.032819, 5.551875)
ob = bpy.data.objects.new(             'structure.Atom045(O1_3r_2lf)', bpy.data.meshes['structure.mesh.O'])
ob.location = (-2.097142, 6.032819, 5.551875)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.646570, 5.838400, 0.000000)
ob = bpy.data.objects.new(             'structure.Atom046(Mn1_3r_3f)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (2.646570, 5.838400, 0.000000)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (7.390282, -0.194419, 1.850625)
ob = bpy.data.objects.new(             'structure.Atom047(O1_3rrb)', bpy.data.meshes['structure.mesh.O'])
ob.location = (7.390282, -0.194419, 1.850625)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-2.646570, 0.000000, 7.402500)
ob = bpy.data.objects.new(             'structure.Atom048(Mn1_3r_3lu)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (-2.646570, 0.000000, 7.402500)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (4.213869, 4.823686, 3.323722)
ob = bpy.data.objects.new(             'structure.Atom049(O2_2r_1)', bpy.data.meshes['structure.mesh.O'])
ob.location = (4.213869, 4.823686, 3.323722)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (6.372411, 1.014714, 7.024972)
ob = bpy.data.objects.new(             'structure.Atom050(O2_2r_3r)', bpy.data.meshes['structure.mesh.O'])
ob.location = (6.372411, 1.014714, 7.024972)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (7.939710, 0.000000, 7.402500)
ob = bpy.data.objects.new(             'structure.Atom051(Mn1_3r_3ru)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (7.939710, 0.000000, 7.402500)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (4.743712, 3.113619, 5.551875)
ob = bpy.data.objects.new(             'structure.Atom052(O1_3r_1)', bpy.data.meshes['structure.mesh.O'])
ob.location = (4.743712, 3.113619, 5.551875)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (1.079271, 1.014714, 7.024972)
ob = bpy.data.objects.new(             'structure.Atom053(O2_2r_3)', bpy.data.meshes['structure.mesh.O'])
ob.location = (1.079271, 1.014714, 7.024972)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-2.646570, 0.000000, 3.701250)
ob = bpy.data.objects.new(             'structure.Atom054(Mn1_3r_1l)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (-2.646570, 0.000000, 3.701250)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.646570, 0.000000, 7.402500)
ob = bpy.data.objects.new(             'structure.Atom055(Mn1_3r_3u)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (2.646570, 0.000000, 7.402500)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.646570, 0.000000, 0.000000)
ob = bpy.data.objects.new(             'structure.Atom056(Mn1_3r_3)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (2.646570, 0.000000, 0.000000)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (4.213869, 4.823686, 0.377528)
ob = bpy.data.objects.new(             'structure.Atom057(O2_2r_7)', bpy.data.meshes['structure.mesh.O'])
ob.location = (4.213869, 4.823686, 0.377528)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-1.079271, 4.823686, 0.377528)
ob = bpy.data.objects.new(             'structure.Atom058(O2_2r_7l)', bpy.data.meshes['structure.mesh.O'])
ob.location = (-1.079271, 4.823686, 0.377528)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.646570, 0.000000, 3.701250)
ob = bpy.data.objects.new(             'structure.Atom059(Mn1_3r_1)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (2.646570, 0.000000, 3.701250)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.097142, -0.194419, 1.850625)
ob = bpy.data.objects.new(             'structure.Atom060(O1_3rb)', bpy.data.meshes['structure.mesh.O'])
ob.location = (2.097142, -0.194419, 1.850625)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
for ob in bpy.data.objects:
    if ob.name.startswith('structure.Atom'):
        ob.select = True
    else:
        ob.select = False
bpy.ops.object.shade_smooth()
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_3lu.meshBond001')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3lu.Bond001', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -2.0971,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3lu.material.Bond001')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_3lu.meshBond002')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3lu.Bond002', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -2.0971,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3lu.material.Bond002')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_3lu.meshBond003')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3lu.Bond003', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -2.0971,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3lu.material.Bond003')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_3lu.meshBond004')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3lu.Bond004', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     7.7429,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3lu.material.Bond004')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_3lu.meshBond005')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3lu.Bond005', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     6.8531,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3lu.material.Bond005')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_3lu.meshBond006')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3lu.Bond006', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -2.0971,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3lu.material.Bond006')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_3lu.meshBond007')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3lu.Bond007', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     6.8531,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3lu.material.Bond007')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_3lu.meshBond008')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3lu.Bond008', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,     3.9339,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3lu.material.Bond008')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_3lu.meshBond009')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3lu.Bond009', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3lu.material.Bond009')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_3lu.meshBond010')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3lu.Bond010', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,     3.9339,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3lu.material.Bond010')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_3lu.meshBond011')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3lu.Bond011', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3lu.material.Bond011')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_3lu.meshBond012')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3lu.Bond012', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     7.7429,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3lu.material.Bond012')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3lu.meshFace001')
mesh_data.from_pydata([(   -3.1960,     5.6440,     9.2531), (   -1.5673,     7.7429,     7.7800), (   -1.0793,     4.8237,     7.7800)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3lu.Face001', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3lu.material.Face001')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3lu.meshFace002')
mesh_data.from_pydata([(   -2.0971,     6.0328,     5.5519), (   -1.5673,     7.7429,     7.7800), (   -4.2139,     6.8531,     7.0250)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3lu.Face002', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3lu.material.Face002')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3lu.meshFace003')
mesh_data.from_pydata([(   -3.1960,     5.6440,     9.2531), (   -1.0793,     4.8237,     7.7800), (   -3.7258,     3.9339,     7.0250)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3lu.Face003', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3lu.material.Face003')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3lu.meshFace004')
mesh_data.from_pydata([(   -2.0971,     6.0328,     5.5519), (   -4.2139,     6.8531,     7.0250), (   -3.7258,     3.9339,     7.0250)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3lu.Face004', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3lu.material.Face004')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3lu.meshFace005')
mesh_data.from_pydata([(   -3.1960,     5.6440,     9.2531), (   -3.7258,     3.9339,     7.0250), (   -4.2139,     6.8531,     7.0250)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3lu.Face005', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3lu.material.Face005')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3lu.meshFace006')
mesh_data.from_pydata([(   -3.1960,     5.6440,     9.2531), (   -4.2139,     6.8531,     7.0250), (   -1.5673,     7.7429,     7.7800)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3lu.Face006', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3lu.material.Face006')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3lu.meshFace007')
mesh_data.from_pydata([(   -2.0971,     6.0328,     5.5519), (   -1.0793,     4.8237,     7.7800), (   -1.5673,     7.7429,     7.7800)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3lu.Face007', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3lu.material.Face007')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3lu.meshFace008')
mesh_data.from_pydata([(   -2.0971,     6.0328,     5.5519), (   -3.7258,     3.9339,     7.0250), (   -1.0793,     4.8237,     7.7800)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3lu.Face008', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3lu.material.Face008')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
for ob in bpy.data.objects:
    if ob.name.startswith('structure.Octahedron_3lu.Atom'):
        ob.select = True
    else:
        ob.select = False
bpy.ops.object.shade_smooth()
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_1r.meshBond001')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_1r.Bond001', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    7.3903,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1r.material.Bond001')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_1r.meshBond002')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_1r.Bond002', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    7.3903,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1r.material.Bond002')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_1r.meshBond003')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_1r.Bond003', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     1.9045,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1r.material.Bond003')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_1r.meshBond004')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_1r.Bond004', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,    -1.9045,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1r.material.Bond004')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_1r.meshBond005')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_1r.Bond005', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,    -1.9045,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1r.material.Bond005')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_1r.meshBond006')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_1r.Bond006', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    7.3903,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1r.material.Bond006')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_1r.meshBond007')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_1r.Bond007', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    7.3903,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1r.material.Bond007')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_1r.meshBond008')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_1r.Bond008', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1r.material.Bond008')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_1r.meshBond009')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_1r.Bond009', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1r.material.Bond009')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_1r.meshBond010')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_1r.Bond010', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,    -1.0147,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1r.material.Bond010')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_1r.meshBond011')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_1r.Bond011', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     1.9045,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1r.material.Bond011')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_1r.meshBond012')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_1r.Bond012', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,    -1.0147,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1r.material.Bond012')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_1r.meshFace001')
mesh_data.from_pydata([(    8.4891,     0.1944,     5.5519), (    9.5070,    -1.0147,     3.3237), (    6.8604,    -1.9045,     4.0788)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_1r.Face001', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1r.material.Face001')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_1r.meshFace002')
mesh_data.from_pydata([(    7.3903,    -0.1944,     1.8506), (    9.5070,    -1.0147,     3.3237), (    9.0190,     1.9045,     3.3237)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_1r.Face002', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1r.material.Face002')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_1r.meshFace003')
mesh_data.from_pydata([(    7.3903,    -0.1944,     1.8506), (    6.3724,     1.0147,     4.0788), (    6.8604,    -1.9045,     4.0788)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_1r.Face003', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1r.material.Face003')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_1r.meshFace004')
mesh_data.from_pydata([(    7.3903,    -0.1944,     1.8506), (    9.0190,     1.9045,     3.3237), (    6.3724,     1.0147,     4.0788)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_1r.Face004', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1r.material.Face004')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_1r.meshFace005')
mesh_data.from_pydata([(    8.4891,     0.1944,     5.5519), (    9.0190,     1.9045,     3.3237), (    9.5070,    -1.0147,     3.3237)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_1r.Face005', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1r.material.Face005')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_1r.meshFace006')
mesh_data.from_pydata([(    7.3903,    -0.1944,     1.8506), (    6.8604,    -1.9045,     4.0788), (    9.5070,    -1.0147,     3.3237)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_1r.Face006', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1r.material.Face006')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_1r.meshFace007')
mesh_data.from_pydata([(    8.4891,     0.1944,     5.5519), (    6.3724,     1.0147,     4.0788), (    9.0190,     1.9045,     3.3237)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_1r.Face007', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1r.material.Face007')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_1r.meshFace008')
mesh_data.from_pydata([(    8.4891,     0.1944,     5.5519), (    6.8604,    -1.9045,     4.0788), (    6.3724,     1.0147,     4.0788)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_1r.Face008', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1r.material.Face008')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
for ob in bpy.data.objects:
    if ob.name.startswith('structure.Octahedron_1r.Atom'):
        ob.select = True
    else:
        ob.select = False
bpy.ops.object.shade_smooth()
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_3r.meshBond001')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3r.Bond001', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     6.0328,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3r.material.Bond001')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_3r.meshBond002')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3r.Bond002', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     7.7429,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3r.material.Bond002')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_3r.meshBond003')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3r.Bond003', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     6.0328,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3r.material.Bond003')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_3r.meshBond004')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3r.Bond004', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     6.0328,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3r.material.Bond004')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_3r.meshBond005')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3r.Bond005', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     7.7429,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3r.material.Bond005')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_3r.meshBond006')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3r.Bond006', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     6.8531,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3r.material.Bond006')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_3r.meshBond007')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3r.Bond007', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     6.0328,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3r.material.Bond007')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_3r.meshBond008')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3r.Bond008', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     6.8531,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3r.material.Bond008')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_3r.meshBond009')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3r.Bond009', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,     4.8237,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3r.material.Bond009')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_3r.meshBond010')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3r.Bond010', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,     4.8237,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3r.material.Bond010')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_3r.meshBond011')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3r.Bond011', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3r.material.Bond011')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_3r.meshBond012')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3r.Bond012', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3r.material.Bond012')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3r.meshFace001')
mesh_data.from_pydata([(    7.3903,     5.6440,     1.8506), (    6.8604,     3.9339,    -0.3775), (    6.3724,     6.8531,    -0.3775)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3r.Face001', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3r.material.Face001')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3r.meshFace002')
mesh_data.from_pydata([(    8.4891,     6.0328,    -1.8506), (    6.8604,     3.9339,    -0.3775), (    9.5070,     4.8237,     0.3775)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3r.Face002', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3r.material.Face002')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3r.meshFace003')
mesh_data.from_pydata([(    8.4891,     6.0328,    -1.8506), (    9.5070,     4.8237,     0.3775), (    9.0190,     7.7429,     0.3775)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3r.Face003', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3r.material.Face003')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3r.meshFace004')
mesh_data.from_pydata([(    7.3903,     5.6440,     1.8506), (    6.3724,     6.8531,    -0.3775), (    9.0190,     7.7429,     0.3775)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3r.Face004', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3r.material.Face004')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3r.meshFace005')
mesh_data.from_pydata([(    8.4891,     6.0328,    -1.8506), (    6.3724,     6.8531,    -0.3775), (    6.8604,     3.9339,    -0.3775)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3r.Face005', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3r.material.Face005')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3r.meshFace006')
mesh_data.from_pydata([(    7.3903,     5.6440,     1.8506), (    9.5070,     4.8237,     0.3775), (    6.8604,     3.9339,    -0.3775)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3r.Face006', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3r.material.Face006')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3r.meshFace007')
mesh_data.from_pydata([(    7.3903,     5.6440,     1.8506), (    9.0190,     7.7429,     0.3775), (    9.5070,     4.8237,     0.3775)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3r.Face007', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3r.material.Face007')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3r.meshFace008')
mesh_data.from_pydata([(    8.4891,     6.0328,    -1.8506), (    9.0190,     7.7429,     0.3775), (    6.3724,     6.8531,    -0.3775)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3r.Face008', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3r.material.Face008')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
for ob in bpy.data.objects:
    if ob.name.startswith('structure.Octahedron_3r.Atom'):
        ob.select = True
    else:
        ob.select = False
bpy.ops.object.shade_smooth()
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_2r.meshBond001')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_2r.Bond001', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2r.material.Bond001')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_2r.meshBond002')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_2r.Bond002', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2r.material.Bond002')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_2r.meshBond003')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_2r.Bond003', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2r.material.Bond003')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_2r.meshBond004')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_2r.Bond004', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2r.material.Bond004')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_2r.meshBond005')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_2r.Bond005', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2r.material.Bond005')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_2r.meshBond006')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_2r.Bond006', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    5.8426,     2.7248,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2r.material.Bond006')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_2r.meshBond007')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_2r.Bond007', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    5.8426,     2.7248,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2r.material.Bond007')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_2r.meshBond008')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_2r.Bond008', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    5.8426,     2.7248,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2r.material.Bond008')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_2r.meshBond009')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_2r.Bond009', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2r.material.Bond009')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_2r.meshBond010')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_2r.Bond010', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2r.material.Bond010')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_2r.meshBond011')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_2r.Bond011', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2r.material.Bond011')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_2r.meshBond012')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_2r.Bond012', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    5.8426,     2.7248,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2r.material.Bond012')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_2r.meshFace001')
mesh_data.from_pydata([(    5.8426,     2.7248,     1.8506), (    3.7258,     1.9045,     0.3775), (    4.2139,     4.8237,     0.3775)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_2r.Face001', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2r.material.Face001')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_2r.meshFace002')
mesh_data.from_pydata([(    4.7437,     3.1136,    -1.8506), (    3.7258,     1.9045,     0.3775), (    6.3724,     1.0147,    -0.3775)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_2r.Face002', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2r.material.Face002')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_2r.meshFace003')
mesh_data.from_pydata([(    4.7437,     3.1136,    -1.8506), (    6.3724,     1.0147,    -0.3775), (    6.8604,     3.9339,    -0.3775)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_2r.Face003', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2r.material.Face003')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_2r.meshFace004')
mesh_data.from_pydata([(    5.8426,     2.7248,     1.8506), (    6.8604,     3.9339,    -0.3775), (    6.3724,     1.0147,    -0.3775)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_2r.Face004', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2r.material.Face004')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_2r.meshFace005')
mesh_data.from_pydata([(    4.7437,     3.1136,    -1.8506), (    4.2139,     4.8237,     0.3775), (    3.7258,     1.9045,     0.3775)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_2r.Face005', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2r.material.Face005')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_2r.meshFace006')
mesh_data.from_pydata([(    5.8426,     2.7248,     1.8506), (    4.2139,     4.8237,     0.3775), (    6.8604,     3.9339,    -0.3775)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_2r.Face006', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2r.material.Face006')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_2r.meshFace007')
mesh_data.from_pydata([(    5.8426,     2.7248,     1.8506), (    6.3724,     1.0147,    -0.3775), (    3.7258,     1.9045,     0.3775)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_2r.Face007', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2r.material.Face007')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_2r.meshFace008')
mesh_data.from_pydata([(    4.7437,     3.1136,    -1.8506), (    6.8604,     3.9339,    -0.3775), (    4.2139,     4.8237,     0.3775)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_2r.Face008', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2r.material.Face008')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
for ob in bpy.data.objects:
    if ob.name.startswith('structure.Octahedron_2r.Atom'):
        ob.select = True
    else:
        ob.select = False
bpy.ops.object.shade_smooth()
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_3rbu.meshBond001')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3rbu.Bond001', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rbu.material.Bond001')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_3rbu.meshBond002')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3rbu.Bond002', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,    -1.9045,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rbu.material.Bond002')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_3rbu.meshBond003')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3rbu.Bond003', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,    -1.0147,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rbu.material.Bond003')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_3rbu.meshBond004')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3rbu.Bond004', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,    -1.9045,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rbu.material.Bond004')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_3rbu.meshBond005')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3rbu.Bond005', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rbu.material.Bond005')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_3rbu.meshBond006')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3rbu.Bond006', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rbu.material.Bond006')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_3rbu.meshBond007')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3rbu.Bond007', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     1.9045,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rbu.material.Bond007')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_3rbu.meshBond008')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3rbu.Bond008', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rbu.material.Bond008')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_3rbu.meshBond009')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3rbu.Bond009', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rbu.material.Bond009')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_3rbu.meshBond010')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3rbu.Bond010', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rbu.material.Bond010')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_3rbu.meshBond011')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3rbu.Bond011', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,    -1.0147,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rbu.material.Bond011')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_3rbu.meshBond012')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3rbu.Bond012', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     1.9045,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rbu.material.Bond012')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3rbu.meshFace001')
mesh_data.from_pydata([(    7.3903,    -0.1944,     9.2531), (    6.8604,    -1.9045,     7.0250), (    6.3724,     1.0147,     7.0250)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3rbu.Face001', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rbu.material.Face001')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3rbu.meshFace002')
mesh_data.from_pydata([(    7.3903,    -0.1944,     9.2531), (    6.3724,     1.0147,     7.0250), (    9.0190,     1.9045,     7.7800)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3rbu.Face002', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rbu.material.Face002')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3rbu.meshFace003')
mesh_data.from_pydata([(    8.4891,     0.1944,     5.5519), (    9.0190,     1.9045,     7.7800), (    6.3724,     1.0147,     7.0250)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3rbu.Face003', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rbu.material.Face003')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3rbu.meshFace004')
mesh_data.from_pydata([(    7.3903,    -0.1944,     9.2531), (    9.5070,    -1.0147,     7.7800), (    6.8604,    -1.9045,     7.0250)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3rbu.Face004', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rbu.material.Face004')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3rbu.meshFace005')
mesh_data.from_pydata([(    7.3903,    -0.1944,     9.2531), (    9.0190,     1.9045,     7.7800), (    9.5070,    -1.0147,     7.7800)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3rbu.Face005', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rbu.material.Face005')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3rbu.meshFace006')
mesh_data.from_pydata([(    8.4891,     0.1944,     5.5519), (    6.8604,    -1.9045,     7.0250), (    9.5070,    -1.0147,     7.7800)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3rbu.Face006', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rbu.material.Face006')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3rbu.meshFace007')
mesh_data.from_pydata([(    8.4891,     0.1944,     5.5519), (    9.5070,    -1.0147,     7.7800), (    9.0190,     1.9045,     7.7800)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3rbu.Face007', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rbu.material.Face007')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3rbu.meshFace008')
mesh_data.from_pydata([(    8.4891,     0.1944,     5.5519), (    6.3724,     1.0147,     7.0250), (    6.8604,    -1.9045,     7.0250)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3rbu.Face008', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rbu.material.Face008')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
for ob in bpy.data.objects:
    if ob.name.startswith('structure.Octahedron_3rbu.Atom'):
        ob.select = True
    else:
        ob.select = False
bpy.ops.object.shade_smooth()
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_3ru.meshBond001')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3ru.Bond001', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     6.8531,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3ru.material.Bond001')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_3ru.meshBond002')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3ru.Bond002', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3ru.material.Bond002')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_3ru.meshBond003')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3ru.Bond003', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     7.7429,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3ru.material.Bond003')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_3ru.meshBond004')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3ru.Bond004', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3ru.material.Bond004')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_3ru.meshBond005')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3ru.Bond005', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3ru.material.Bond005')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_3ru.meshBond006')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3ru.Bond006', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,     4.8237,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3ru.material.Bond006')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_3ru.meshBond007')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3ru.Bond007', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3ru.material.Bond007')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_3ru.meshBond008')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3ru.Bond008', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,     4.8237,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3ru.material.Bond008')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_3ru.meshBond009')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3ru.Bond009', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     7.7429,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3ru.material.Bond009')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_3ru.meshBond010')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3ru.Bond010', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3ru.material.Bond010')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_3ru.meshBond011')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3ru.Bond011', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3ru.material.Bond011')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_3ru.meshBond012')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3ru.Bond012', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     6.8531,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3ru.material.Bond012')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3ru.meshFace001')
mesh_data.from_pydata([(    8.4891,     6.0328,     5.5519), (    6.8604,     3.9339,     7.0250), (    9.5070,     4.8237,     7.7800)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3ru.Face001', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3ru.material.Face001')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3ru.meshFace002')
mesh_data.from_pydata([(    7.3903,     5.6440,     9.2531), (    9.0190,     7.7429,     7.7800), (    9.5070,     4.8237,     7.7800)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3ru.Face002', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3ru.material.Face002')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3ru.meshFace003')
mesh_data.from_pydata([(    7.3903,     5.6440,     9.2531), (    6.3724,     6.8531,     7.0250), (    9.0190,     7.7429,     7.7800)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3ru.Face003', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3ru.material.Face003')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3ru.meshFace004')
mesh_data.from_pydata([(    8.4891,     6.0328,     5.5519), (    9.0190,     7.7429,     7.7800), (    6.3724,     6.8531,     7.0250)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3ru.Face004', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3ru.material.Face004')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3ru.meshFace005')
mesh_data.from_pydata([(    8.4891,     6.0328,     5.5519), (    6.3724,     6.8531,     7.0250), (    6.8604,     3.9339,     7.0250)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3ru.Face005', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3ru.material.Face005')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3ru.meshFace006')
mesh_data.from_pydata([(    8.4891,     6.0328,     5.5519), (    9.5070,     4.8237,     7.7800), (    9.0190,     7.7429,     7.7800)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3ru.Face006', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3ru.material.Face006')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3ru.meshFace007')
mesh_data.from_pydata([(    7.3903,     5.6440,     9.2531), (    9.5070,     4.8237,     7.7800), (    6.8604,     3.9339,     7.0250)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3ru.Face007', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3ru.material.Face007')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3ru.meshFace008')
mesh_data.from_pydata([(    7.3903,     5.6440,     9.2531), (    6.8604,     3.9339,     7.0250), (    6.3724,     6.8531,     7.0250)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3ru.Face008', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3ru.material.Face008')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
for ob in bpy.data.objects:
    if ob.name.startswith('structure.Octahedron_3ru.Atom'):
        ob.select = True
    else:
        ob.select = False
bpy.ops.object.shade_smooth()
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_6.meshBond001')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_6.Bond001', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6.material.Bond001')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_6.meshBond002')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_6.Bond002', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -0.5494,     3.1136,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6.material.Bond002')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_6.meshBond003')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_6.Bond003', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6.material.Bond003')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_6.meshBond004')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_6.Bond004', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -0.5494,     3.1136,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6.material.Bond004')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_6.meshBond005')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_6.Bond005', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6.material.Bond005')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_6.meshBond006')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_6.Bond006', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -0.5494,     3.1136,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6.material.Bond006')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_6.meshBond007')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_6.Bond007', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6.material.Bond007')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_6.meshBond008')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_6.Bond008', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6.material.Bond008')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_6.meshBond009')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_6.Bond009', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6.material.Bond009')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_6.meshBond010')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_6.Bond010', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6.material.Bond010')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_6.meshBond011')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_6.Bond011', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6.material.Bond011')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_6.meshBond012')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_6.Bond012', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -0.5494,     3.1136,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6.material.Bond012')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_6.meshFace001')
mesh_data.from_pydata([(   -1.0793,     4.8237,     0.3775), (    1.5673,     3.9339,    -0.3775), (    0.5494,     2.7248,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_6.Face001', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6.material.Face001')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_6.meshFace002')
mesh_data.from_pydata([(    1.5673,     3.9339,    -0.3775), (    1.0793,     1.0147,    -0.3775), (    0.5494,     2.7248,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_6.Face002', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6.material.Face002')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_6.meshFace003')
mesh_data.from_pydata([(    1.0793,     1.0147,    -0.3775), (    1.5673,     3.9339,    -0.3775), (   -0.5494,     3.1136,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_6.Face003', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6.material.Face003')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_6.meshFace004')
mesh_data.from_pydata([(   -1.0793,     4.8237,     0.3775), (   -1.5673,     1.9045,     0.3775), (   -0.5494,     3.1136,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_6.Face004', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6.material.Face004')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_6.meshFace005')
mesh_data.from_pydata([(   -1.5673,     1.9045,     0.3775), (   -1.0793,     4.8237,     0.3775), (    0.5494,     2.7248,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_6.Face005', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6.material.Face005')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_6.meshFace006')
mesh_data.from_pydata([(    1.0793,     1.0147,    -0.3775), (   -1.5673,     1.9045,     0.3775), (    0.5494,     2.7248,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_6.Face006', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6.material.Face006')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_6.meshFace007')
mesh_data.from_pydata([(   -1.5673,     1.9045,     0.3775), (    1.0793,     1.0147,    -0.3775), (   -0.5494,     3.1136,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_6.Face007', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6.material.Face007')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_6.meshFace008')
mesh_data.from_pydata([(    1.5673,     3.9339,    -0.3775), (   -1.0793,     4.8237,     0.3775), (   -0.5494,     3.1136,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_6.Face008', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6.material.Face008')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
for ob in bpy.data.objects:
    if ob.name.startswith('structure.Octahedron_6.Atom'):
        ob.select = True
    else:
        ob.select = False
bpy.ops.object.shade_smooth()
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_5.meshBond001')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5.Bond001', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     7.7429,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5.material.Bond001')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_5.meshBond002')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5.Bond002', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5.material.Bond002')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_5.meshBond003')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5.Bond003', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     6.8531,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5.material.Bond003')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_5.meshBond004')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5.Bond004', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5.material.Bond004')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_5.meshBond005')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5.Bond005', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     6.8531,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5.material.Bond005')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_5.meshBond006')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5.Bond006', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5.material.Bond006')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_5.meshBond007')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5.Bond007', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     7.7429,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5.material.Bond007')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_5.meshBond008')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5.Bond008', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5.material.Bond008')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_5.meshBond009')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5.Bond009', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5.material.Bond009')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_5.meshBond010')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5.Bond010', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5.material.Bond010')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_5.meshBond011')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5.Bond011', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5.material.Bond011')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_5.meshBond012')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5.Bond012', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5.material.Bond012')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_5.meshFace001')
mesh_data.from_pydata([(    1.5673,     3.9339,     4.0788), (    4.2139,     4.8237,     3.3237), (    2.0971,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_5.Face001', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5.material.Face001')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_5.meshFace002')
mesh_data.from_pydata([(    4.2139,     4.8237,     3.3237), (    1.5673,     3.9339,     4.0788), (    3.1960,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_5.Face002', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5.material.Face002')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_5.meshFace003')
mesh_data.from_pydata([(    1.5673,     3.9339,     4.0788), (    1.0793,     6.8531,     4.0788), (    3.1960,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_5.Face003', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5.material.Face003')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_5.meshFace004')
mesh_data.from_pydata([(    1.0793,     6.8531,     4.0788), (    1.5673,     3.9339,     4.0788), (    2.0971,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_5.Face004', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5.material.Face004')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_5.meshFace005')
mesh_data.from_pydata([(    3.7258,     7.7429,     3.3237), (    4.2139,     4.8237,     3.3237), (    3.1960,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_5.Face005', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5.material.Face005')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_5.meshFace006')
mesh_data.from_pydata([(    1.0793,     6.8531,     4.0788), (    3.7258,     7.7429,     3.3237), (    3.1960,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_5.Face006', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5.material.Face006')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_5.meshFace007')
mesh_data.from_pydata([(    3.7258,     7.7429,     3.3237), (    1.0793,     6.8531,     4.0788), (    2.0971,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_5.Face007', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5.material.Face007')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_5.meshFace008')
mesh_data.from_pydata([(    4.2139,     4.8237,     3.3237), (    3.7258,     7.7429,     3.3237), (    2.0971,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_5.Face008', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5.material.Face008')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
for ob in bpy.data.objects:
    if ob.name.startswith('structure.Octahedron_5.Atom'):
        ob.select = True
    else:
        ob.select = False
bpy.ops.object.shade_smooth()
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_7lu.meshBond001')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7lu.Bond001', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     1.0147,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lu.material.Bond001')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_7lu.meshBond002')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7lu.Bond002', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     1.0147,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lu.material.Bond002')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_7lu.meshBond003')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7lu.Bond003', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,    -0.1944,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lu.material.Bond003')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_7lu.meshBond004')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7lu.Bond004', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lu.material.Bond004')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_7lu.meshBond005')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7lu.Bond005', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,    -0.1944,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lu.material.Bond005')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_7lu.meshBond006')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7lu.Bond006', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,    -0.1944,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lu.material.Bond006')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_7lu.meshBond007')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7lu.Bond007', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,    -1.0147,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lu.material.Bond007')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_7lu.meshBond008')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7lu.Bond008', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,    -1.0147,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lu.material.Bond008')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_7lu.meshBond009')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7lu.Bond009', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,    -1.9045,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lu.material.Bond009')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_7lu.meshBond010')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7lu.Bond010', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lu.material.Bond010')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_7lu.meshBond011')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7lu.Bond011', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,    -1.9045,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lu.material.Bond011')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_7lu.meshBond012')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7lu.Bond012', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,    -0.1944,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lu.material.Bond012')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_7lu.meshFace001')
mesh_data.from_pydata([(   -3.7258,    -1.9045,     7.0250), (   -4.2139,     1.0147,     7.0250), (   -3.1960,    -0.1944,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_7lu.Face001', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lu.material.Face001')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_7lu.meshFace002')
mesh_data.from_pydata([(   -1.5673,     1.9045,     7.7800), (   -1.0793,    -1.0147,     7.7800), (   -3.1960,    -0.1944,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_7lu.Face002', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lu.material.Face002')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_7lu.meshFace003')
mesh_data.from_pydata([(   -1.0793,    -1.0147,     7.7800), (   -3.7258,    -1.9045,     7.0250), (   -3.1960,    -0.1944,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_7lu.Face003', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lu.material.Face003')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_7lu.meshFace004')
mesh_data.from_pydata([(   -1.5673,     1.9045,     7.7800), (   -4.2139,     1.0147,     7.0250), (   -2.0971,     0.1944,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_7lu.Face004', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lu.material.Face004')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_7lu.meshFace005')
mesh_data.from_pydata([(   -1.0793,    -1.0147,     7.7800), (   -1.5673,     1.9045,     7.7800), (   -2.0971,     0.1944,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_7lu.Face005', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lu.material.Face005')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_7lu.meshFace006')
mesh_data.from_pydata([(   -4.2139,     1.0147,     7.0250), (   -3.7258,    -1.9045,     7.0250), (   -2.0971,     0.1944,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_7lu.Face006', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lu.material.Face006')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_7lu.meshFace007')
mesh_data.from_pydata([(   -3.7258,    -1.9045,     7.0250), (   -1.0793,    -1.0147,     7.7800), (   -2.0971,     0.1944,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_7lu.Face007', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lu.material.Face007')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_7lu.meshFace008')
mesh_data.from_pydata([(   -4.2139,     1.0147,     7.0250), (   -1.5673,     1.9045,     7.7800), (   -3.1960,    -0.1944,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_7lu.Face008', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lu.material.Face008')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
for ob in bpy.data.objects:
    if ob.name.startswith('structure.Octahedron_7lu.Atom'):
        ob.select = True
    else:
        ob.select = False
bpy.ops.object.shade_smooth()
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_5b.meshBond001')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5b.Bond001', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5b.material.Bond001')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_5b.meshBond002')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5b.Bond002', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5b.material.Bond002')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_5b.meshBond003')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5b.Bond003', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5b.material.Bond003')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_5b.meshBond004')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5b.Bond004', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,    -1.9045,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5b.material.Bond004')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_5b.meshBond005')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5b.Bond005', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5b.material.Bond005')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_5b.meshBond006')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5b.Bond006', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5b.material.Bond006')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_5b.meshBond007')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5b.Bond007', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5b.material.Bond007')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_5b.meshBond008')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5b.Bond008', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5b.material.Bond008')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_5b.meshBond009')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5b.Bond009', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5b.material.Bond009')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_5b.meshBond010')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5b.Bond010', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,    -1.0147,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5b.material.Bond010')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_5b.meshBond011')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5b.Bond011', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,    -1.9045,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5b.material.Bond011')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_5b.meshBond012')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5b.Bond012', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,    -1.0147,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5b.material.Bond012')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_5b.meshFace001')
mesh_data.from_pydata([(    3.7258,     1.9045,     3.3237), (    1.0793,     1.0147,     4.0788), (    2.0971,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_5b.Face001', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5b.material.Face001')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_5b.meshFace002')
mesh_data.from_pydata([(    1.0793,     1.0147,     4.0788), (    1.5673,    -1.9045,     4.0788), (    2.0971,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_5b.Face002', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5b.material.Face002')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_5b.meshFace003')
mesh_data.from_pydata([(    3.7258,     1.9045,     3.3237), (    4.2139,    -1.0147,     3.3237), (    3.1960,     0.1944,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_5b.Face003', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5b.material.Face003')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_5b.meshFace004')
mesh_data.from_pydata([(    1.5673,    -1.9045,     4.0788), (    4.2139,    -1.0147,     3.3237), (    2.0971,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_5b.Face004', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5b.material.Face004')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_5b.meshFace005')
mesh_data.from_pydata([(    1.0793,     1.0147,     4.0788), (    3.7258,     1.9045,     3.3237), (    3.1960,     0.1944,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_5b.Face005', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5b.material.Face005')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_5b.meshFace006')
mesh_data.from_pydata([(    1.5673,    -1.9045,     4.0788), (    1.0793,     1.0147,     4.0788), (    3.1960,     0.1944,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_5b.Face006', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5b.material.Face006')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_5b.meshFace007')
mesh_data.from_pydata([(    4.2139,    -1.0147,     3.3237), (    3.7258,     1.9045,     3.3237), (    2.0971,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_5b.Face007', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5b.material.Face007')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_5b.meshFace008')
mesh_data.from_pydata([(    4.2139,    -1.0147,     3.3237), (    1.5673,    -1.9045,     4.0788), (    3.1960,     0.1944,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_5b.Face008', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5b.material.Face008')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
for ob in bpy.data.objects:
    if ob.name.startswith('structure.Octahedron_5b.Atom'):
        ob.select = True
    else:
        ob.select = False
bpy.ops.object.shade_smooth()
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_1l.meshBond001')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_1l.Bond001', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1l.material.Bond001')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_1l.meshBond002')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_1l.Bond002', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,    -1.0147,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1l.material.Bond002')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_1l.meshBond003')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_1l.Bond003', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1l.material.Bond003')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_1l.meshBond004')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_1l.Bond004', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,    -1.9045,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1l.material.Bond004')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_1l.meshBond005')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_1l.Bond005', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,    -1.9045,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1l.material.Bond005')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_1l.meshBond006')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_1l.Bond006', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     1.0147,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1l.material.Bond006')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_1l.meshBond007')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_1l.Bond007', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     1.0147,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1l.material.Bond007')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_1l.meshBond008')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_1l.Bond008', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1l.material.Bond008')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_1l.meshBond009')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_1l.Bond009', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1l.material.Bond009')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_1l.meshBond010')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_1l.Bond010', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1l.material.Bond010')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_1l.meshBond011')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_1l.Bond011', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1l.material.Bond011')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_1l.meshBond012')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_1l.Bond012', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,    -1.0147,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1l.material.Bond012')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_1l.meshFace001')
mesh_data.from_pydata([(   -2.0971,     0.1944,     5.5519), (   -3.7258,    -1.9045,     4.0788), (   -4.2139,     1.0147,     4.0788)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_1l.Face001', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1l.material.Face001')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_1l.meshFace002')
mesh_data.from_pydata([(   -3.1960,    -0.1944,     1.8506), (   -3.7258,    -1.9045,     4.0788), (   -1.0793,    -1.0147,     3.3237)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_1l.Face002', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1l.material.Face002')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_1l.meshFace003')
mesh_data.from_pydata([(   -2.0971,     0.1944,     5.5519), (   -4.2139,     1.0147,     4.0788), (   -1.5673,     1.9045,     3.3237)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_1l.Face003', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1l.material.Face003')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_1l.meshFace004')
mesh_data.from_pydata([(   -3.1960,    -0.1944,     1.8506), (   -4.2139,     1.0147,     4.0788), (   -3.7258,    -1.9045,     4.0788)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_1l.Face004', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1l.material.Face004')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_1l.meshFace005')
mesh_data.from_pydata([(   -2.0971,     0.1944,     5.5519), (   -1.5673,     1.9045,     3.3237), (   -1.0793,    -1.0147,     3.3237)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_1l.Face005', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1l.material.Face005')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_1l.meshFace006')
mesh_data.from_pydata([(   -2.0971,     0.1944,     5.5519), (   -1.0793,    -1.0147,     3.3237), (   -3.7258,    -1.9045,     4.0788)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_1l.Face006', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1l.material.Face006')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_1l.meshFace007')
mesh_data.from_pydata([(   -3.1960,    -0.1944,     1.8506), (   -1.0793,    -1.0147,     3.3237), (   -1.5673,     1.9045,     3.3237)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_1l.Face007', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1l.material.Face007')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_1l.meshFace008')
mesh_data.from_pydata([(   -3.1960,    -0.1944,     1.8506), (   -1.5673,     1.9045,     3.3237), (   -4.2139,     1.0147,     4.0788)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_1l.Face008', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_1l.material.Face008')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
for ob in bpy.data.objects:
    if ob.name.startswith('structure.Octahedron_1l.Atom'):
        ob.select = True
    else:
        ob.select = False
bpy.ops.object.shade_smooth()
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_5r.meshBond001')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5r.Bond001', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,     4.8237,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5r.material.Bond001')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_5r.meshBond002')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5r.Bond002', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5r.material.Bond002')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_5r.meshBond003')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5r.Bond003', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     6.8531,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5r.material.Bond003')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_5r.meshBond004')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5r.Bond004', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5r.material.Bond004')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_5r.meshBond005')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5r.Bond005', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,     4.8237,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5r.material.Bond005')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_5r.meshBond006')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5r.Bond006', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5r.material.Bond006')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_5r.meshBond007')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5r.Bond007', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5r.material.Bond007')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_5r.meshBond008')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5r.Bond008', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     6.8531,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5r.material.Bond008')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_5r.meshBond009')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5r.Bond009', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     7.7429,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5r.material.Bond009')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_5r.meshBond010')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5r.Bond010', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5r.material.Bond010')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_5r.meshBond011')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5r.Bond011', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5r.material.Bond011')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_5r.meshBond012')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5r.Bond012', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     7.7429,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5r.material.Bond012')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_5r.meshFace001')
mesh_data.from_pydata([(    6.3724,     6.8531,     4.0788), (    9.0190,     7.7429,     3.3237), (    8.4891,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_5r.Face001', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5r.material.Face001')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_5r.meshFace002')
mesh_data.from_pydata([(    6.8604,     3.9339,     4.0788), (    6.3724,     6.8531,     4.0788), (    8.4891,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_5r.Face002', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5r.material.Face002')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_5r.meshFace003')
mesh_data.from_pydata([(    9.0190,     7.7429,     3.3237), (    9.5070,     4.8237,     3.3237), (    8.4891,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_5r.Face003', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5r.material.Face003')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_5r.meshFace004')
mesh_data.from_pydata([(    6.8604,     3.9339,     4.0788), (    9.5070,     4.8237,     3.3237), (    7.3903,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_5r.Face004', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5r.material.Face004')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_5r.meshFace005')
mesh_data.from_pydata([(    6.3724,     6.8531,     4.0788), (    6.8604,     3.9339,     4.0788), (    7.3903,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_5r.Face005', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5r.material.Face005')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_5r.meshFace006')
mesh_data.from_pydata([(    9.5070,     4.8237,     3.3237), (    6.8604,     3.9339,     4.0788), (    8.4891,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_5r.Face006', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5r.material.Face006')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_5r.meshFace007')
mesh_data.from_pydata([(    9.5070,     4.8237,     3.3237), (    9.0190,     7.7429,     3.3237), (    7.3903,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_5r.Face007', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5r.material.Face007')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_5r.meshFace008')
mesh_data.from_pydata([(    9.0190,     7.7429,     3.3237), (    6.3724,     6.8531,     4.0788), (    7.3903,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_5r.Face008', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5r.material.Face008')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
for ob in bpy.data.objects:
    if ob.name.startswith('structure.Octahedron_5r.Atom'):
        ob.select = True
    else:
        ob.select = False
bpy.ops.object.shade_smooth()
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_3.meshBond001')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3.Bond001', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3.material.Bond001')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_3.meshBond002')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3.Bond002', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     6.0328,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3.material.Bond002')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_3.meshBond003')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3.Bond003', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3.material.Bond003')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_3.meshBond004')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3.Bond004', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     6.0328,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3.material.Bond004')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_3.meshBond005')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3.Bond005', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3.material.Bond005')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_3.meshBond006')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3.Bond006', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     6.0328,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3.material.Bond006')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_3.meshBond007')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3.Bond007', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     6.8531,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3.material.Bond007')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_3.meshBond008')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3.Bond008', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3.material.Bond008')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_3.meshBond009')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3.Bond009', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     6.8531,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3.material.Bond009')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_3.meshBond010')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3.Bond010', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     7.7429,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3.material.Bond010')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_3.meshBond011')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3.Bond011', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     6.0328,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3.material.Bond011')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_3.meshBond012')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3.Bond012', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     7.7429,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3.material.Bond012')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3.meshFace001')
mesh_data.from_pydata([(    2.0971,     5.6440,     1.8506), (    1.0793,     6.8531,    -0.3775), (    3.7258,     7.7429,     0.3775)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3.Face001', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3.material.Face001')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3.meshFace002')
mesh_data.from_pydata([(    3.1960,     6.0328,    -1.8506), (    4.2139,     4.8237,     0.3775), (    3.7258,     7.7429,     0.3775)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3.Face002', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3.material.Face002')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3.meshFace003')
mesh_data.from_pydata([(    2.0971,     5.6440,     1.8506), (    4.2139,     4.8237,     0.3775), (    1.5673,     3.9339,    -0.3775)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3.Face003', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3.material.Face003')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3.meshFace004')
mesh_data.from_pydata([(    2.0971,     5.6440,     1.8506), (    3.7258,     7.7429,     0.3775), (    4.2139,     4.8237,     0.3775)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3.Face004', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3.material.Face004')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3.meshFace005')
mesh_data.from_pydata([(    3.1960,     6.0328,    -1.8506), (    1.5673,     3.9339,    -0.3775), (    4.2139,     4.8237,     0.3775)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3.Face005', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3.material.Face005')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3.meshFace006')
mesh_data.from_pydata([(    3.1960,     6.0328,    -1.8506), (    3.7258,     7.7429,     0.3775), (    1.0793,     6.8531,    -0.3775)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3.Face006', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3.material.Face006')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3.meshFace007')
mesh_data.from_pydata([(    3.1960,     6.0328,    -1.8506), (    1.0793,     6.8531,    -0.3775), (    1.5673,     3.9339,    -0.3775)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3.Face007', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3.material.Face007')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3.meshFace008')
mesh_data.from_pydata([(    2.0971,     5.6440,     1.8506), (    1.5673,     3.9339,    -0.3775), (    1.0793,     6.8531,    -0.3775)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3.Face008', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3.material.Face008')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
for ob in bpy.data.objects:
    if ob.name.startswith('structure.Octahedron_3.Atom'):
        ob.select = True
    else:
        ob.select = False
bpy.ops.object.shade_smooth()
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_7l.meshBond001')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7l.Bond001', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7l.material.Bond001')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_7l.meshBond002')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7l.Bond002', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     1.0147,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7l.material.Bond002')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_7l.meshBond003')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7l.Bond003', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7l.material.Bond003')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_7l.meshBond004')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7l.Bond004', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,    -1.9045,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7l.material.Bond004')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_7l.meshBond005')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7l.Bond005', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7l.material.Bond005')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_7l.meshBond006')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7l.Bond006', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7l.material.Bond006')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_7l.meshBond007')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7l.Bond007', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,    -1.9045,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7l.material.Bond007')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_7l.meshBond008')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7l.Bond008', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,    -1.0147,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7l.material.Bond008')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_7l.meshBond009')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7l.Bond009', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,    -1.0147,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7l.material.Bond009')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_7l.meshBond010')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7l.Bond010', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7l.material.Bond010')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_7l.meshBond011')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7l.Bond011', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     1.0147,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7l.material.Bond011')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_7l.meshBond012')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7l.Bond012', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7l.material.Bond012')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_7l.meshFace001')
mesh_data.from_pydata([(   -3.7258,    -1.9045,    -0.3775), (   -4.2139,     1.0147,    -0.3775), (   -3.1960,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_7l.Face001', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7l.material.Face001')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_7l.meshFace002')
mesh_data.from_pydata([(   -4.2139,     1.0147,    -0.3775), (   -1.5673,     1.9045,     0.3775), (   -3.1960,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_7l.Face002', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7l.material.Face002')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_7l.meshFace003')
mesh_data.from_pydata([(   -1.5673,     1.9045,     0.3775), (   -4.2139,     1.0147,    -0.3775), (   -2.0971,     0.1944,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_7l.Face003', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7l.material.Face003')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_7l.meshFace004')
mesh_data.from_pydata([(   -1.0793,    -1.0147,     0.3775), (   -3.7258,    -1.9045,    -0.3775), (   -3.1960,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_7l.Face004', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7l.material.Face004')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_7l.meshFace005')
mesh_data.from_pydata([(   -1.5673,     1.9045,     0.3775), (   -1.0793,    -1.0147,     0.3775), (   -3.1960,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_7l.Face005', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7l.material.Face005')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_7l.meshFace006')
mesh_data.from_pydata([(   -3.7258,    -1.9045,    -0.3775), (   -1.0793,    -1.0147,     0.3775), (   -2.0971,     0.1944,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_7l.Face006', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7l.material.Face006')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_7l.meshFace007')
mesh_data.from_pydata([(   -1.0793,    -1.0147,     0.3775), (   -1.5673,     1.9045,     0.3775), (   -2.0971,     0.1944,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_7l.Face007', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7l.material.Face007')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_7l.meshFace008')
mesh_data.from_pydata([(   -4.2139,     1.0147,    -0.3775), (   -3.7258,    -1.9045,    -0.3775), (   -2.0971,     0.1944,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_7l.Face008', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7l.material.Face008')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
for ob in bpy.data.objects:
    if ob.name.startswith('structure.Octahedron_7l.Atom'):
        ob.select = True
    else:
        ob.select = False
bpy.ops.object.shade_smooth()
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_7.meshBond001')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7.Bond001', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    2.0971,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7.material.Bond001')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_7.meshBond002')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7.Bond002', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7.material.Bond002')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_7.meshBond003')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7.Bond003', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    2.0971,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7.material.Bond003')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_7.meshBond004')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7.Bond004', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    2.0971,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7.material.Bond004')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_7.meshBond005')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7.Bond005', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,    -1.0147,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7.material.Bond005')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_7.meshBond006')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7.Bond006', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,    -1.0147,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7.material.Bond006')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_7.meshBond007')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7.Bond007', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    2.0971,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7.material.Bond007')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_7.meshBond008')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7.Bond008', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7.material.Bond008')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_7.meshBond009')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7.Bond009', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,    -1.9045,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7.material.Bond009')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_7.meshBond010')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7.Bond010', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,    -1.9045,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7.material.Bond010')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_7.meshBond011')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7.Bond011', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7.material.Bond011')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_7.meshBond012')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7.Bond012', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7.material.Bond012')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_7.meshFace001')
mesh_data.from_pydata([(    3.7258,     1.9045,     0.3775), (    1.0793,     1.0147,    -0.3775), (    3.1960,     0.1944,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_7.Face001', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7.material.Face001')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_7.meshFace002')
mesh_data.from_pydata([(    3.7258,     1.9045,     0.3775), (    4.2139,    -1.0147,     0.3775), (    2.0971,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_7.Face002', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7.material.Face002')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_7.meshFace003')
mesh_data.from_pydata([(    1.0793,     1.0147,    -0.3775), (    3.7258,     1.9045,     0.3775), (    2.0971,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_7.Face003', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7.material.Face003')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_7.meshFace004')
mesh_data.from_pydata([(    4.2139,    -1.0147,     0.3775), (    1.5673,    -1.9045,    -0.3775), (    2.0971,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_7.Face004', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7.material.Face004')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_7.meshFace005')
mesh_data.from_pydata([(    1.5673,    -1.9045,    -0.3775), (    4.2139,    -1.0147,     0.3775), (    3.1960,     0.1944,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_7.Face005', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7.material.Face005')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_7.meshFace006')
mesh_data.from_pydata([(    4.2139,    -1.0147,     0.3775), (    3.7258,     1.9045,     0.3775), (    3.1960,     0.1944,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_7.Face006', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7.material.Face006')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_7.meshFace007')
mesh_data.from_pydata([(    1.5673,    -1.9045,    -0.3775), (    1.0793,     1.0147,    -0.3775), (    2.0971,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_7.Face007', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7.material.Face007')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_7.meshFace008')
mesh_data.from_pydata([(    1.0793,     1.0147,    -0.3775), (    1.5673,    -1.9045,    -0.3775), (    3.1960,     0.1944,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_7.Face008', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7.material.Face008')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
for ob in bpy.data.objects:
    if ob.name.startswith('structure.Octahedron_7.Atom'):
        ob.select = True
    else:
        ob.select = False
bpy.ops.object.shade_smooth()
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_5l.meshBond001')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5l.Bond001', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     6.8531,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5l.material.Bond001')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_5l.meshBond002')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5l.Bond002', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     7.7429,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5l.material.Bond002')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_5l.meshBond003')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5l.Bond003', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -2.0971,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5l.material.Bond003')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_5l.meshBond004')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5l.Bond004', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -2.0971,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5l.material.Bond004')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_5l.meshBond005')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5l.Bond005', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     7.7429,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5l.material.Bond005')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_5l.meshBond006')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5l.Bond006', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5l.material.Bond006')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_5l.meshBond007')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5l.Bond007', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -2.0971,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5l.material.Bond007')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_5l.meshBond008')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5l.Bond008', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5l.material.Bond008')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_5l.meshBond009')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5l.Bond009', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,     3.9339,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5l.material.Bond009')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_5l.meshBond010')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5l.Bond010', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     6.8531,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5l.material.Bond010')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_5l.meshBond011')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5l.Bond011', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,     3.9339,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5l.material.Bond011')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_5l.meshBond012')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_5l.Bond012', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -2.0971,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5l.material.Bond012')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_5l.meshFace001')
mesh_data.from_pydata([(   -1.5673,     7.7429,     3.3237), (   -4.2139,     6.8531,     4.0788), (   -3.1960,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_5l.Face001', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5l.material.Face001')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_5l.meshFace002')
mesh_data.from_pydata([(   -3.7258,     3.9339,     4.0788), (   -4.2139,     6.8531,     4.0788), (   -2.0971,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_5l.Face002', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5l.material.Face002')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_5l.meshFace003')
mesh_data.from_pydata([(   -1.0793,     4.8237,     3.3237), (   -1.5673,     7.7429,     3.3237), (   -3.1960,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_5l.Face003', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5l.material.Face003')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_5l.meshFace004')
mesh_data.from_pydata([(   -1.5673,     7.7429,     3.3237), (   -1.0793,     4.8237,     3.3237), (   -2.0971,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_5l.Face004', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5l.material.Face004')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_5l.meshFace005')
mesh_data.from_pydata([(   -3.7258,     3.9339,     4.0788), (   -1.0793,     4.8237,     3.3237), (   -3.1960,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_5l.Face005', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5l.material.Face005')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_5l.meshFace006')
mesh_data.from_pydata([(   -4.2139,     6.8531,     4.0788), (   -1.5673,     7.7429,     3.3237), (   -2.0971,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_5l.Face006', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5l.material.Face006')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_5l.meshFace007')
mesh_data.from_pydata([(   -1.0793,     4.8237,     3.3237), (   -3.7258,     3.9339,     4.0788), (   -2.0971,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_5l.Face007', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5l.material.Face007')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_5l.meshFace008')
mesh_data.from_pydata([(   -4.2139,     6.8531,     4.0788), (   -3.7258,     3.9339,     4.0788), (   -3.1960,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_5l.Face008', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_5l.material.Face008')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
for ob in bpy.data.objects:
    if ob.name.startswith('structure.Octahedron_5l.Atom'):
        ob.select = True
    else:
        ob.select = False
bpy.ops.object.shade_smooth()
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron.meshBond001')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron.Bond001', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron.material.Bond001')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron.meshBond002')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron.Bond002', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron.material.Bond002')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron.meshBond003')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron.Bond003', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron.material.Bond003')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron.meshBond004')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron.Bond004', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron.material.Bond004')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron.meshBond005')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron.Bond005', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron.material.Bond005')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron.meshBond006')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron.Bond006', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron.material.Bond006')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron.meshBond007')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron.Bond007', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -0.5494,     3.1136,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron.material.Bond007')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron.meshBond008')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron.Bond008', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron.material.Bond008')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron.meshBond009')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron.Bond009', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron.material.Bond009')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron.meshBond010')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron.Bond010', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -0.5494,     3.1136,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron.material.Bond010')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron.meshBond011')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron.Bond011', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -0.5494,     3.1136,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron.material.Bond011')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron.meshBond012')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron.Bond012', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -0.5494,     3.1136,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron.material.Bond012')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron.meshFace001')
mesh_data.from_pydata([(    0.5494,     2.7248,     1.8506), (   -1.5673,     1.9045,     3.3237), (    1.0793,     1.0147,     4.0788)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron.Face001', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron.material.Face001')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron.meshFace002')
mesh_data.from_pydata([(    0.5494,     2.7248,     1.8506), (   -1.0793,     4.8237,     3.3237), (   -1.5673,     1.9045,     3.3237)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron.Face002', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron.material.Face002')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron.meshFace003')
mesh_data.from_pydata([(   -0.5494,     3.1136,     5.5519), (   -1.5673,     1.9045,     3.3237), (   -1.0793,     4.8237,     3.3237)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron.Face003', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron.material.Face003')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron.meshFace004')
mesh_data.from_pydata([(   -0.5494,     3.1136,     5.5519), (    1.0793,     1.0147,     4.0788), (   -1.5673,     1.9045,     3.3237)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron.Face004', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron.material.Face004')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron.meshFace005')
mesh_data.from_pydata([(    0.5494,     2.7248,     1.8506), (    1.5673,     3.9339,     4.0788), (   -1.0793,     4.8237,     3.3237)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron.Face005', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron.material.Face005')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron.meshFace006')
mesh_data.from_pydata([(   -0.5494,     3.1136,     5.5519), (    1.5673,     3.9339,     4.0788), (    1.0793,     1.0147,     4.0788)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron.Face006', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron.material.Face006')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron.meshFace007')
mesh_data.from_pydata([(    0.5494,     2.7248,     1.8506), (    1.0793,     1.0147,     4.0788), (    1.5673,     3.9339,     4.0788)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron.Face007', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron.material.Face007')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron.meshFace008')
mesh_data.from_pydata([(   -0.5494,     3.1136,     5.5519), (   -1.0793,     4.8237,     3.3237), (    1.5673,     3.9339,     4.0788)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron.Face008', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron.material.Face008')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
for ob in bpy.data.objects:
    if ob.name.startswith('structure.Octahedron.Atom'):
        ob.select = True
    else:
        ob.select = False
bpy.ops.object.shade_smooth()
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_6u.meshBond001')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_6u.Bond001', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6u.material.Bond001')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_6u.meshBond002')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_6u.Bond002', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6u.material.Bond002')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_6u.meshBond003')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_6u.Bond003', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -0.5494,     3.1136,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6u.material.Bond003')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_6u.meshBond004')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_6u.Bond004', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6u.material.Bond004')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_6u.meshBond005')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_6u.Bond005', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6u.material.Bond005')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_6u.meshBond006')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_6u.Bond006', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6u.material.Bond006')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_6u.meshBond007')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_6u.Bond007', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -0.5494,     3.1136,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6u.material.Bond007')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_6u.meshBond008')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_6u.Bond008', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6u.material.Bond008')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_6u.meshBond009')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_6u.Bond009', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6u.material.Bond009')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_6u.meshBond010')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_6u.Bond010', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6u.material.Bond010')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_6u.meshBond011')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_6u.Bond011', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -0.5494,     3.1136,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6u.material.Bond011')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_6u.meshBond012')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_6u.Bond012', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -0.5494,     3.1136,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6u.material.Bond012')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_6u.meshFace001')
mesh_data.from_pydata([(   -1.0793,     4.8237,     7.7800), (    1.5673,     3.9339,     7.0250), (    0.5494,     2.7248,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_6u.Face001', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6u.material.Face001')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_6u.meshFace002')
mesh_data.from_pydata([(    1.5673,     3.9339,     7.0250), (   -1.0793,     4.8237,     7.7800), (   -0.5494,     3.1136,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_6u.Face002', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6u.material.Face002')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_6u.meshFace003')
mesh_data.from_pydata([(   -1.0793,     4.8237,     7.7800), (   -1.5673,     1.9045,     7.7800), (   -0.5494,     3.1136,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_6u.Face003', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6u.material.Face003')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_6u.meshFace004')
mesh_data.from_pydata([(    1.0793,     1.0147,     7.0250), (   -1.5673,     1.9045,     7.7800), (    0.5494,     2.7248,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_6u.Face004', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6u.material.Face004')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_6u.meshFace005')
mesh_data.from_pydata([(    1.5673,     3.9339,     7.0250), (    1.0793,     1.0147,     7.0250), (    0.5494,     2.7248,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_6u.Face005', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6u.material.Face005')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_6u.meshFace006')
mesh_data.from_pydata([(    1.0793,     1.0147,     7.0250), (    1.5673,     3.9339,     7.0250), (   -0.5494,     3.1136,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_6u.Face006', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6u.material.Face006')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_6u.meshFace007')
mesh_data.from_pydata([(   -1.5673,     1.9045,     7.7800), (    1.0793,     1.0147,     7.0250), (   -0.5494,     3.1136,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_6u.Face007', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6u.material.Face007')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_6u.meshFace008')
mesh_data.from_pydata([(   -1.5673,     1.9045,     7.7800), (   -1.0793,     4.8237,     7.7800), (    0.5494,     2.7248,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_6u.Face008', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_6u.material.Face008')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
for ob in bpy.data.objects:
    if ob.name.startswith('structure.Octahedron_6u.Atom'):
        ob.select = True
    else:
        ob.select = False
bpy.ops.object.shade_smooth()
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_3bu.meshBond001')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3bu.Bond001', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,    -1.9045,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3bu.material.Bond001')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_3bu.meshBond002')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3bu.Bond002', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,    -1.9045,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3bu.material.Bond002')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_3bu.meshBond003')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3bu.Bond003', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3bu.material.Bond003')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_3bu.meshBond004')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3bu.Bond004', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3bu.material.Bond004')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_3bu.meshBond005')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3bu.Bond005', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3bu.material.Bond005')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_3bu.meshBond006')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3bu.Bond006', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3bu.material.Bond006')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_3bu.meshBond007')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3bu.Bond007', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3bu.material.Bond007')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_3bu.meshBond008')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3bu.Bond008', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3bu.material.Bond008')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_3bu.meshBond009')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3bu.Bond009', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3bu.material.Bond009')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_3bu.meshBond010')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3bu.Bond010', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,    -1.0147,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3bu.material.Bond010')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_3bu.meshBond011')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3bu.Bond011', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,    -1.0147,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3bu.material.Bond011')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_3bu.meshBond012')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3bu.Bond012', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3bu.material.Bond012')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3bu.meshFace001')
mesh_data.from_pydata([(    3.1960,     0.1944,     5.5519), (    1.0793,     1.0147,     7.0250), (    1.5673,    -1.9045,     7.0250)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3bu.Face001', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3bu.material.Face001')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3bu.meshFace002')
mesh_data.from_pydata([(    2.0971,    -0.1944,     9.2531), (    3.7258,     1.9045,     7.7800), (    4.2139,    -1.0147,     7.7800)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3bu.Face002', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3bu.material.Face002')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3bu.meshFace003')
mesh_data.from_pydata([(    2.0971,    -0.1944,     9.2531), (    1.5673,    -1.9045,     7.0250), (    1.0793,     1.0147,     7.0250)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3bu.Face003', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3bu.material.Face003')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3bu.meshFace004')
mesh_data.from_pydata([(    3.1960,     0.1944,     5.5519), (    3.7258,     1.9045,     7.7800), (    1.0793,     1.0147,     7.0250)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3bu.Face004', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3bu.material.Face004')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3bu.meshFace005')
mesh_data.from_pydata([(    3.1960,     0.1944,     5.5519), (    4.2139,    -1.0147,     7.7800), (    3.7258,     1.9045,     7.7800)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3bu.Face005', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3bu.material.Face005')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3bu.meshFace006')
mesh_data.from_pydata([(    2.0971,    -0.1944,     9.2531), (    1.0793,     1.0147,     7.0250), (    3.7258,     1.9045,     7.7800)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3bu.Face006', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3bu.material.Face006')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3bu.meshFace007')
mesh_data.from_pydata([(    3.1960,     0.1944,     5.5519), (    1.5673,    -1.9045,     7.0250), (    4.2139,    -1.0147,     7.7800)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3bu.Face007', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3bu.material.Face007')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3bu.meshFace008')
mesh_data.from_pydata([(    2.0971,    -0.1944,     9.2531), (    4.2139,    -1.0147,     7.7800), (    1.5673,    -1.9045,     7.0250)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3bu.Face008', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3bu.material.Face008')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
for ob in bpy.data.objects:
    if ob.name.startswith('structure.Octahedron_3bu.Atom'):
        ob.select = True
    else:
        ob.select = False
bpy.ops.object.shade_smooth()
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedronr.meshBond001')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedronr.Bond001', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedronr.material.Bond001')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedronr.meshBond002')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedronr.Bond002', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedronr.material.Bond002')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedronr.meshBond003')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedronr.Bond003', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedronr.material.Bond003')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedronr.meshBond004')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedronr.Bond004', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedronr.material.Bond004')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedronr.meshBond005')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedronr.Bond005', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.7437,     3.1136,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedronr.material.Bond005')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedronr.meshBond006')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedronr.Bond006', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedronr.material.Bond006')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedronr.meshBond007')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedronr.Bond007', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.7437,     3.1136,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedronr.material.Bond007')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedronr.meshBond008')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedronr.Bond008', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.7437,     3.1136,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedronr.material.Bond008')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedronr.meshBond009')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedronr.Bond009', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedronr.material.Bond009')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedronr.meshBond010')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedronr.Bond010', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.7437,     3.1136,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedronr.material.Bond010')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedronr.meshBond011')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedronr.Bond011', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedronr.material.Bond011')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedronr.meshBond012')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedronr.Bond012', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedronr.material.Bond012')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedronr.meshFace001')
mesh_data.from_pydata([(    5.8426,     2.7248,     1.8506), (    4.2139,     4.8237,     3.3237), (    3.7258,     1.9045,     3.3237)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedronr.Face001', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedronr.material.Face001')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedronr.meshFace002')
mesh_data.from_pydata([(    4.7437,     3.1136,     5.5519), (    3.7258,     1.9045,     3.3237), (    4.2139,     4.8237,     3.3237)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedronr.Face002', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedronr.material.Face002')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedronr.meshFace003')
mesh_data.from_pydata([(    4.7437,     3.1136,     5.5519), (    4.2139,     4.8237,     3.3237), (    6.8604,     3.9339,     4.0788)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedronr.Face003', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedronr.material.Face003')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedronr.meshFace004')
mesh_data.from_pydata([(    5.8426,     2.7248,     1.8506), (    6.3724,     1.0147,     4.0788), (    6.8604,     3.9339,     4.0788)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedronr.Face004', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedronr.material.Face004')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedronr.meshFace005')
mesh_data.from_pydata([(    5.8426,     2.7248,     1.8506), (    3.7258,     1.9045,     3.3237), (    6.3724,     1.0147,     4.0788)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedronr.Face005', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedronr.material.Face005')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedronr.meshFace006')
mesh_data.from_pydata([(    4.7437,     3.1136,     5.5519), (    6.8604,     3.9339,     4.0788), (    6.3724,     1.0147,     4.0788)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedronr.Face006', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedronr.material.Face006')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedronr.meshFace007')
mesh_data.from_pydata([(    5.8426,     2.7248,     1.8506), (    6.8604,     3.9339,     4.0788), (    4.2139,     4.8237,     3.3237)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedronr.Face007', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedronr.material.Face007')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedronr.meshFace008')
mesh_data.from_pydata([(    4.7437,     3.1136,     5.5519), (    6.3724,     1.0147,     4.0788), (    3.7258,     1.9045,     3.3237)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedronr.Face008', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedronr.material.Face008')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
for ob in bpy.data.objects:
    if ob.name.startswith('structure.Octahedronr.Atom'):
        ob.select = True
    else:
        ob.select = False
bpy.ops.object.shade_smooth()
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_2ru.meshBond001')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_2ru.Bond001', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    5.8426,     2.7248,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2ru.material.Bond001')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_2ru.meshBond002')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_2ru.Bond002', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2ru.material.Bond002')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_2ru.meshBond003')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_2ru.Bond003', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2ru.material.Bond003')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_2ru.meshBond004')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_2ru.Bond004', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    5.8426,     2.7248,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2ru.material.Bond004')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_2ru.meshBond005')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_2ru.Bond005', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    5.8426,     2.7248,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2ru.material.Bond005')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_2ru.meshBond006')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_2ru.Bond006', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2ru.material.Bond006')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_2ru.meshBond007')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_2ru.Bond007', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    5.8426,     2.7248,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2ru.material.Bond007')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_2ru.meshBond008')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_2ru.Bond008', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2ru.material.Bond008')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_2ru.meshBond009')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_2ru.Bond009', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2ru.material.Bond009')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_2ru.meshBond010')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_2ru.Bond010', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2ru.material.Bond010')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_2ru.meshBond011')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_2ru.Bond011', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2ru.material.Bond011')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_2ru.meshBond012')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_2ru.Bond012', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2ru.material.Bond012')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_2ru.meshFace001')
mesh_data.from_pydata([(    5.8426,     2.7248,     9.2531), (    4.2139,     4.8237,     7.7800), (    6.8604,     3.9339,     7.0250)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_2ru.Face001', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2ru.material.Face001')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_2ru.meshFace002')
mesh_data.from_pydata([(    5.8426,     2.7248,     9.2531), (    6.8604,     3.9339,     7.0250), (    6.3724,     1.0147,     7.0250)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_2ru.Face002', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2ru.material.Face002')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_2ru.meshFace003')
mesh_data.from_pydata([(    5.8426,     2.7248,     9.2531), (    6.3724,     1.0147,     7.0250), (    3.7258,     1.9045,     7.7800)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_2ru.Face003', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2ru.material.Face003')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_2ru.meshFace004')
mesh_data.from_pydata([(    5.8426,     2.7248,     9.2531), (    3.7258,     1.9045,     7.7800), (    4.2139,     4.8237,     7.7800)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_2ru.Face004', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2ru.material.Face004')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_2ru.meshFace005')
mesh_data.from_pydata([(    4.7437,     3.1136,     5.5519), (    6.3724,     1.0147,     7.0250), (    6.8604,     3.9339,     7.0250)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_2ru.Face005', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2ru.material.Face005')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_2ru.meshFace006')
mesh_data.from_pydata([(    4.7437,     3.1136,     5.5519), (    4.2139,     4.8237,     7.7800), (    3.7258,     1.9045,     7.7800)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_2ru.Face006', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2ru.material.Face006')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_2ru.meshFace007')
mesh_data.from_pydata([(    4.7437,     3.1136,     5.5519), (    6.8604,     3.9339,     7.0250), (    4.2139,     4.8237,     7.7800)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_2ru.Face007', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2ru.material.Face007')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_2ru.meshFace008')
mesh_data.from_pydata([(    4.7437,     3.1136,     5.5519), (    3.7258,     1.9045,     7.7800), (    6.3724,     1.0147,     7.0250)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_2ru.Face008', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_2ru.material.Face008')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
for ob in bpy.data.objects:
    if ob.name.startswith('structure.Octahedron_2ru.Atom'):
        ob.select = True
    else:
        ob.select = False
bpy.ops.object.shade_smooth()
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_3rb.meshBond001')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3rb.Bond001', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rb.material.Bond001')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_3rb.meshBond002')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3rb.Bond002', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     1.9045,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rb.material.Bond002')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_3rb.meshBond003')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3rb.Bond003', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     1.9045,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rb.material.Bond003')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_3rb.meshBond004')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3rb.Bond004', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     0.1944,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rb.material.Bond004')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_3rb.meshBond005')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3rb.Bond005', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,    -1.0147,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rb.material.Bond005')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_3rb.meshBond006')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3rb.Bond006', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     0.1944,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rb.material.Bond006')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_3rb.meshBond007')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3rb.Bond007', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,    -1.0147,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rb.material.Bond007')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_3rb.meshBond008')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3rb.Bond008', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     0.1944,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rb.material.Bond008')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_3rb.meshBond009')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3rb.Bond009', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     0.1944,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rb.material.Bond009')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_3rb.meshBond010')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3rb.Bond010', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,    -1.9045,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rb.material.Bond010')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_3rb.meshBond011')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3rb.Bond011', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,    -1.9045,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rb.material.Bond011')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_3rb.meshBond012')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3rb.Bond012', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rb.material.Bond012')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3rb.meshFace001')
mesh_data.from_pydata([(    8.4891,     0.1944,    -1.8506), (    6.8604,    -1.9045,    -0.3775), (    9.5070,    -1.0147,     0.3775)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3rb.Face001', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rb.material.Face001')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3rb.meshFace002')
mesh_data.from_pydata([(    8.4891,     0.1944,    -1.8506), (    6.3724,     1.0147,    -0.3775), (    6.8604,    -1.9045,    -0.3775)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3rb.Face002', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rb.material.Face002')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3rb.meshFace003')
mesh_data.from_pydata([(    7.3903,    -0.1944,     1.8506), (    9.5070,    -1.0147,     0.3775), (    6.8604,    -1.9045,    -0.3775)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3rb.Face003', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rb.material.Face003')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3rb.meshFace004')
mesh_data.from_pydata([(    7.3903,    -0.1944,     1.8506), (    6.3724,     1.0147,    -0.3775), (    9.0190,     1.9045,     0.3775)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3rb.Face004', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rb.material.Face004')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3rb.meshFace005')
mesh_data.from_pydata([(    7.3903,    -0.1944,     1.8506), (    9.0190,     1.9045,     0.3775), (    9.5070,    -1.0147,     0.3775)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3rb.Face005', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rb.material.Face005')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3rb.meshFace006')
mesh_data.from_pydata([(    8.4891,     0.1944,    -1.8506), (    9.5070,    -1.0147,     0.3775), (    9.0190,     1.9045,     0.3775)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3rb.Face006', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rb.material.Face006')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3rb.meshFace007')
mesh_data.from_pydata([(    8.4891,     0.1944,    -1.8506), (    9.0190,     1.9045,     0.3775), (    6.3724,     1.0147,    -0.3775)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3rb.Face007', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rb.material.Face007')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3rb.meshFace008')
mesh_data.from_pydata([(    7.3903,    -0.1944,     1.8506), (    6.8604,    -1.9045,    -0.3775), (    6.3724,     1.0147,    -0.3775)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3rb.Face008', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3rb.material.Face008')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
for ob in bpy.data.objects:
    if ob.name.startswith('structure.Octahedron_3rb.Atom'):
        ob.select = True
    else:
        ob.select = False
bpy.ops.object.shade_smooth()
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_3u.meshBond001')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3u.Bond001', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3u.material.Bond001')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_3u.meshBond002')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3u.Bond002', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3u.material.Bond002')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_3u.meshBond003')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3u.Bond003', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3u.material.Bond003')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_3u.meshBond004')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3u.Bond004', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3u.material.Bond004')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_3u.meshBond005')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3u.Bond005', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3u.material.Bond005')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_3u.meshBond006')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3u.Bond006', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     6.8531,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3u.material.Bond006')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_3u.meshBond007')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3u.Bond007', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     7.7429,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3u.material.Bond007')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_3u.meshBond008')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3u.Bond008', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     7.7429,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3u.material.Bond008')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_3u.meshBond009')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3u.Bond009', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3u.material.Bond009')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_3u.meshBond010')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3u.Bond010', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3u.material.Bond010')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_3u.meshBond011')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3u.Bond011', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     6.8531,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3u.material.Bond011')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_3u.meshBond012')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_3u.Bond012', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3u.material.Bond012')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3u.meshFace001')
mesh_data.from_pydata([(    2.0971,     5.6440,     9.2531), (    1.0793,     6.8531,     7.0250), (    3.7258,     7.7429,     7.7800)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3u.Face001', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3u.material.Face001')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3u.meshFace002')
mesh_data.from_pydata([(    3.1960,     6.0328,     5.5519), (    3.7258,     7.7429,     7.7800), (    1.0793,     6.8531,     7.0250)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3u.Face002', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3u.material.Face002')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3u.meshFace003')
mesh_data.from_pydata([(    2.0971,     5.6440,     9.2531), (    4.2139,     4.8237,     7.7800), (    1.5673,     3.9339,     7.0250)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3u.Face003', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3u.material.Face003')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3u.meshFace004')
mesh_data.from_pydata([(    2.0971,     5.6440,     9.2531), (    1.5673,     3.9339,     7.0250), (    1.0793,     6.8531,     7.0250)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3u.Face004', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3u.material.Face004')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3u.meshFace005')
mesh_data.from_pydata([(    3.1960,     6.0328,     5.5519), (    1.0793,     6.8531,     7.0250), (    1.5673,     3.9339,     7.0250)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3u.Face005', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3u.material.Face005')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3u.meshFace006')
mesh_data.from_pydata([(    3.1960,     6.0328,     5.5519), (    1.5673,     3.9339,     7.0250), (    4.2139,     4.8237,     7.7800)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3u.Face006', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3u.material.Face006')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3u.meshFace007')
mesh_data.from_pydata([(    2.0971,     5.6440,     9.2531), (    3.7258,     7.7429,     7.7800), (    4.2139,     4.8237,     7.7800)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3u.Face007', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3u.material.Face007')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_3u.meshFace008')
mesh_data.from_pydata([(    3.1960,     6.0328,     5.5519), (    4.2139,     4.8237,     7.7800), (    3.7258,     7.7429,     7.7800)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_3u.Face008', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_3u.material.Face008')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
for ob in bpy.data.objects:
    if ob.name.startswith('structure.Octahedron_3u.Atom'):
        ob.select = True
    else:
        ob.select = False
bpy.ops.object.shade_smooth()
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_7lf.meshBond001')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7lf.Bond001', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,     5.6440,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lf.material.Bond001')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_7lf.meshBond002')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7lf.Bond002', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,     5.6440,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lf.material.Bond002')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_7lf.meshBond003')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7lf.Bond003', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,     5.6440,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lf.material.Bond003')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.Octahedron_7lf.meshBond004')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7lf.Bond004', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     6.8531,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lf.material.Bond004')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_7lf.meshBond005')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7lf.Bond005', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     6.8531,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lf.material.Bond005')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_7lf.meshBond006')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7lf.Bond006', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,     3.9339,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lf.material.Bond006')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.Octahedron_7lf.meshBond007')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7lf.Bond007', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     7.7429,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lf.material.Bond007')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_7lf.meshBond008')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7lf.Bond008', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,     3.9339,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lf.material.Bond008')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.Octahedron_7lf.meshBond009')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7lf.Bond009', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     7.7429,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lf.material.Bond009')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.Octahedron_7lf.meshBond010')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7lf.Bond010', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lf.material.Bond010')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.Octahedron_7lf.meshBond011')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7lf.Bond011', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,     5.6440,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lf.material.Bond011')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.1000, diameter2 =     0.1000, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.Octahedron_7lf.meshBond012')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Octahedron_7lf.Bond012', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lf.material.Bond012')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_7lf.meshFace001')
mesh_data.from_pydata([(   -4.2139,     6.8531,    -0.3775), (   -1.5673,     7.7429,     0.3775), (   -3.1960,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_7lf.Face001', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lf.material.Face001')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_7lf.meshFace002')
mesh_data.from_pydata([(   -1.0793,     4.8237,     0.3775), (   -1.5673,     7.7429,     0.3775), (   -2.0971,     6.0328,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_7lf.Face002', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lf.material.Face002')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_7lf.meshFace003')
mesh_data.from_pydata([(   -4.2139,     6.8531,    -0.3775), (   -3.7258,     3.9339,    -0.3775), (   -2.0971,     6.0328,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_7lf.Face003', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lf.material.Face003')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_7lf.meshFace004')
mesh_data.from_pydata([(   -1.5673,     7.7429,     0.3775), (   -4.2139,     6.8531,    -0.3775), (   -2.0971,     6.0328,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_7lf.Face004', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lf.material.Face004')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_7lf.meshFace005')
mesh_data.from_pydata([(   -1.5673,     7.7429,     0.3775), (   -1.0793,     4.8237,     0.3775), (   -3.1960,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_7lf.Face005', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lf.material.Face005')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_7lf.meshFace006')
mesh_data.from_pydata([(   -3.7258,     3.9339,    -0.3775), (   -1.0793,     4.8237,     0.3775), (   -2.0971,     6.0328,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_7lf.Face006', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lf.material.Face006')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_7lf.meshFace007')
mesh_data.from_pydata([(   -3.7258,     3.9339,    -0.3775), (   -4.2139,     6.8531,    -0.3775), (   -3.1960,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_7lf.Face007', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lf.material.Face007')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.Octahedron_7lf.meshFace008')
mesh_data.from_pydata([(   -1.0793,     4.8237,     0.3775), (   -3.7258,     3.9339,    -0.3775), (   -3.1960,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Octahedron_7lf.Face008', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.Octahedron_7lf.material.Face008')
mat.use_transparency = True
mat.alpha =     0.5000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
for ob in bpy.data.objects:
    if ob.name.startswith('structure.Octahedron_7lf.Atom'):
        ob.select = True
    else:
        ob.select = False
bpy.ops.object.shade_smooth()
