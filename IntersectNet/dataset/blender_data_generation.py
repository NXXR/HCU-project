import bpy
import math
from mathutils import Euler
from random import randint

center_options = {
    3:  {  # 3 connections centerpieces
        1:  {
            "verts": [
                     (2,-1,0),  (2,1,0),  (1,1,0),  (1,2,0),  (-1,2,0),  (-1,1,0),  (-2,1,0),  (-2,-1,0),
                     (2,-1,2.5),(2,1,2.5),(1,1,2.5),(1,2,2.5),(-1,2,2.5),(-1,1,2.5),(-2,1,2.5),(-2,-1,2.5)
                     ],
            "faces": [
                     ( 0, 1, 2, 3, 4, 5, 6, 7),  # Floor face
                     ( 8, 9,10,11,12,13,14,15),  # Ceiling face
                     (1,2,10,9),(2,3,11,10),(4,5,13,12),(5,6,14,13),(7,0,8,15)  # Wall faces
                     ]
        },
        2:  {
            "verts": [
                     (2,-1,0),   (2,1,0),   (1,2,0),   (-1,2,0),   (-2,1,0),   (-2,-1,0),   # Bottom verts
                     (2,-1,2.5), (2,1,2.5), (1,2,2.5), (-1,2,2.5), (-2,1,2.5), (-2,-1,2.5)  # Top verts
                     ],
            "faces": [
                     ( 0, 1, 2, 3, 4, 5),  # Floor faces
                     ( 6, 7, 8, 9,10,11),  # Ceiling faces
                     (1,2,8,7),(3,4,10,9),(5,0,6,11)  # Wall faces
                     ]
        }
    },
    4:  {  # 4 connections centerpieces
        1:  {
            "verts": [
                     (2,-1,0),  (2,1,0),  (1,1,0),  (1,2,0),  (-1,2,0),  (-1,1,0),  (-2,1,0),  (-2,-1,0),  (-1,-1,0),  (-1,-2,0),  (1,-2,0),  (1,-1,0),
                     (2,-1,2.5),(2,1,2.5),(1,1,2.5),(1,2,2.5),(-1,2,2.5),(-1,1,2.5),(-2,1,2.5),(-2,-1,2.5),(-1,-1,2.5),(-1,-2,2.5),(1,-2,2.5),(1,-1,2.5)
                     ],
            "faces": [
                     ( 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11),  # Floor face
                     (12,13,14,15,16,17,18,19,20,21,22,23),  # Ceiling face
                     (1,2,14,13),(2,3,15,14),(4,5,17,16),(5,6,18,17),(7,8,20,19),(8,9,21,20),(10,11,23,22),(11,0,12,23)  # Wall faces
                     ]
        },
        2:  {
            "verts": [
                     (2,-1,0),   (2,1,0),   (1,2,0),   (-1,2,0),   (-2,1,0),   (-2,-1,0),   (-1,-1,0),   (-1,-2,0),   (1,-2,0),   (1,-1,0),   # Bottom verts
                     (2,-1,2.5), (2,1,2.5), (1,2,2.5), (-1,2,2.5), (-2,1,2.5), (-2,-1,2.5), (-1,-1,2.5), (-1,-2,2.5), (1,-2,2.5), (1,-1,2.5)  # Top verts
                     ],
            "faces": [
                     ( 0, 1, 2, 3, 4, 5, 6, 7, 8, 9),  # Floor faces
                     (10,11,12,13,14,15,16,17,18,19),  # Ceiling faces
                     (1,2,12,11), (3,4,14,13), (5,6,16,15), (6,7,17,16), (8,9,19,18), (9,0,10,19)  # Wall faces
                     ]
        }
    }
}

def create_random_centerpiece(connections: int):
    try:
        bpy.ops.object.select_all(action="DESELECT")
        bpy.data.objects["Centerpiece"].select = True
    except KeyError:
        print("Centerpiece doesn't exist, creating...")
    finally:
        mesh = bpy.data.meshes.new("Centerpiece")
        obj = bpy.data.objects.new("Centerpiece", mesh)

        bpy.context.scene.objects.link(obj)

        option = randint(1,2)
        mesh.from_pydata(center_options[connections][option]["verts"], [], center_options[connections][option]["faces"])
        mesh.update(calc_edges=True)
        bpy.data.objects["Centerpiece"].rotation_euler = Euler((0, 0, randint(0,3) * math.radians(90)))


# delete all objects in scene
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)

# place floor plane
bpy.ops.mesh.primitive_plane_add(location=(0, 0, -0.01), radius=10)

# place corridor X+
verts = [(2, -1, 0), (8, -1, 0), (8, -1, 2.5), (2, -1, 2.5),
         (2, 1, 0), (8, 1, 0), (8, 1, 2.5), (2, 1, 2.5)]
faces = [(0, 1, 2, 3), (4, 5, 6, 7), (2, 3, 7, 6), (0, 1, 5, 4)]

mesh = bpy.data.meshes.new("Xpos")
obj = bpy.data.objects.new("Xpos", mesh)

bpy.context.scene.objects.link(obj)

mesh.from_pydata(verts, [], faces)
mesh.update(calc_edges=True)

# place corridor Y+
bpy.ops.object.select_all(action="DESELECT")
bpy.data.objects["Xpos"].select = True
bpy.ops.object.duplicate()
bpy.data.objects["Xpos.001"].name = "Ypos"
bpy.data.objects["Ypos"].rotation_euler = Euler((0, 0, math.radians(90)))

# place corridor X-
bpy.ops.object.select_all(action="DESELECT")
bpy.data.objects["Xpos"].select = True
bpy.ops.object.duplicate()
bpy.data.objects["Xpos.001"].name = "Xneg"
bpy.data.objects["Xneg"].rotation_euler = Euler((0, 0, math.radians(180)))

# place corridor Y-
bpy.ops.object.select_all(action="DESELECT")
bpy.data.objects["Xpos"].select = True
bpy.ops.object.duplicate()
bpy.data.objects["Xpos.001"].name = "Yneg"
bpy.data.objects["Yneg"].rotation_euler = Euler((0, 0, math.radians(-90)))

# place random centerpiece
create_random_centerpiece(4)
