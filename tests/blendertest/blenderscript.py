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
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 6, diameter1 =     0.0500, diameter2 =     0.0500, depth =     0.5000)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     0.2500))
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
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     0.7500))
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
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 6, diameter1 =     0.0500, diameter2 =     0.0500, depth =     1.5000)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     0.7500))
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
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.7500))
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
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 6, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.5000)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.2500))
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
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     2.7500))
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
mesh_data = bpy.data.meshes.new('structure.meshBitmapface001')
mesh_data.from_pydata([(    0.0000,     2.0000,     0.0000), (    1.0000,     0.0000,     0.0000), (    1.0000,     0.0000,     3.0000), (    0.0000,     2.0000,     3.0000)], [], [(0, 1, 2, 3)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Bitmapface001', mesh_data)
bpy.context.scene.objects.link(ob1)
img = bpy.data.images.new('structure.matBitmapface001', 10, 10)
img.pixels = [1.000,1.000,0.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,0.000,1.000,1.000,1.000,
1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,
1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,
1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,
1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,
1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,
1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,
1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,
1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,
1.000,0.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,
]
tex = bpy.data.textures.new('structure.texBitmapface001', 'IMAGE')
tex.image = img
bpy.context.scene.objects.active = ob1
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.uv.unwrap(method='ANGLE_BASED')
bpy.ops.object.mode_set(mode='OBJECT')
ob1.data.uv_layers[0].data[0].uv = (0.0, 0.0)
ob1.data.uv_layers[0].data[1].uv = (1.0, 0.0)
ob1.data.uv_layers[0].data[2].uv = (1.0, 1.0)
ob1.data.uv_layers[0].data[3].uv = (0.0, 1.0)
mat.texture_slots.add()
mat.texture_slots[0].texture = tex
ob1.data.materials.append(mat)
for ob in bpy.data.objects:
    if ob.name.startswith('structure.Atom'):
        ob.select = True
    else:
        ob.select = False
bpy.ops.object.shade_smooth()
