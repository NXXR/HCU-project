import bpy
import bmesh

# delete all objects in scene
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)

# place floor plane
bpy.ops.mesh.primitive_plane_add(location=(0, 0, -0.01), radius=10)

# place corridor wall
verts = [(   1,  10,   0), (   1,  10, 2.5),
         (   1, -10,   0), (   1, -10, 2.5)]
mesh = bpy.data.meshes.new("mesh")
obj = bpy.data.objects.new("XPWall", mesh)

scene = bpy.context.scene
scene.objects.link(obj)
scene.objects.active = obj
obj.select = True

mesh = bpy.context.object.data
bm = bmesh.new()

for v in verts:
    bm.verts.new(v)

# TODO: Add Faces
# mesh.from_pydata(verts,[],[(0, 1, 2, 3)])
# mesh.update(calc_edges=True)

bm.to_mesh(mesh)
bm.free()
