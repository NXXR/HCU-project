import bpy
from mathutils import Euler


# delete all objects in scene
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)

# place floor plane
bpy.ops.mesh.primitive_plane_add(location=(0, 0, -0.01), radius=10)

# place corridor wall (X+)
verts = [(2, -1, 0), (8, -1, 0), (8, -1, 2.5), (2, -1, 2.5),
         (2, 1, 0), (8, 1, 0), (8, 1, 2.5), (2, 1, 2.5)]
faces = [(0, 1, 2, 3), (4, 5, 6, 7), (2, 3, 7, 6), (0, 1, 5, 4)]

mesh = bpy.data.meshes.new("Xpos")
obj = bpy.data.objects.new("Xpos", mesh)

bpy.context.scene.objects.link(obj)

mesh.from_pydata(verts, [], faces)
mesh.update(calc_edges=True)

# place corridor wall (Y+)
bpy.ops.object.select_all(action="DESELECT")
bpy.data.objects["Xpos"].select = True
bpy.ops.object.duplicate()
bpy.data.objects["Xpos.001"].name = "Ypos"
bpy.data.objects["Ypos"].rotation_euler = Euler((0, 0, radians(90)))
