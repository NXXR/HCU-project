import bpy
import math
import os
from mathutils import Euler
from random import randint

# setup textures
tex_path = os.path.join("C:/", "Users", "M.Zeumer", "Workspace", "HCU-project", "IntersectNet", "dataset", "textures")
tex_path = os.path.normpath(tex_path)
tex_names = os.listdir(tex_path)
material_options = {
    "floor": [],
    "wall": []
}

for filename in tex_names:
    img = bpy.data.images.load(os.path.join(tex_path, filename))
    fileinfo = filename.split("_")
    # Create image texture
    cTex = bpy.data.textures.new(fileinfo[1], type="IMAGE")
    cTex.image = img
    cTex.extension = "REPEAT"
    # Create material
    mat = bpy.data.materials.new("{}_mat".format(fileinfo[1]))
    # Add texture slot
    mtex = mat.texture_slots.add()
    mtex.texture = cTex
    mtex.texture_coords = "ORCO"
    mtex.use_map_color_diffuse = True
    mtex.use_map_color_emission = True
    mtex.emission_color_factor = 0.5
    mtex.use_map_density = True
    mtex.mapping = "FLAT"
    # scale texture
    mat.texture_slots[0].scale[0] = 20
    mat.texture_slots[0].scale[1] = 20
    # sort into dictionary
    if fileinfo[0] == "floor":
        material_options["floor"].append(mat)
    elif fileinfo[0] == "wall":
        mat.texture_slots[0].scale[0] = 1
        mat.texture_slots[0].scale[1] = 1
        material_options["wall"].append(mat)
    elif fileinfo[0] == "floorwall":
        material_options["floor"].append(mat)
        mat.texture_slots[0].scale[0] = 1
        mat.texture_slots[0].scale[1] = 1
        material_options["wall"].append(mat)


center_options = {
    2: {  # 2 connections centerpieces
        1: {
            "verts": [
                (2, -1, 0), (2, 1, 0), (-2, 1, 0), (-2, -1, 0),
                (2, -1, 2.5), (2, 1, 2.5), (-2, 1, 2.5), (-2, -1, 2.5)
            ],
            "faces": [
                (1, 2, 6, 5), (3, 0, 4, 7)  # Wall faces
            ]
        },
        2: {
            "verts": [
                (2, -1, 0), (2, 1, 0), (-2, 1, 0), (-2, -1, 0),
                (2, -1, 2.5), (2, 1, 2.5), (-2, 1, 2.5), (-2, -1, 2.5)
            ],
            "faces": [
                (1, 2, 6, 5), (3, 0, 4, 7)  # Wall faces
            ]
        }
    },
    3: {  # 3 connections centerpieces
        1: {
            "verts": [
                (2, -1, 0), (2, 1, 0), (1, 1, 0), (1, 2, 0), (-1, 2, 0), (-1, 1, 0), (-2, 1, 0), (-2, -1, 0),
                (2, -1, 2.5), (2, 1, 2.5), (1, 1, 2.5), (1, 2, 2.5), (-1, 2, 2.5), (-1, 1, 2.5), (-2, 1, 2.5),
                (-2, -1, 2.5)
            ],
            "faces": [
                (1, 2, 10, 9), (2, 3, 11, 10), (4, 5, 13, 12), (5, 6, 14, 13), (7, 0, 8, 15)  # Wall faces
            ]
        },
        2: {
            "verts": [
                (2, -1, 0), (2, 1, 0), (1, 2, 0), (-1, 2, 0), (-2, 1, 0), (-2, -1, 0),  # Bottom verts
                (2, -1, 2.5), (2, 1, 2.5), (1, 2, 2.5), (-1, 2, 2.5), (-2, 1, 2.5), (-2, -1, 2.5)  # Top verts
            ],
            "faces": [
                (1, 2, 8, 7), (3, 4, 10, 9), (5, 0, 6, 11)  # Wall faces
            ]
        }
    },
    4: {  # 4 connections centerpieces
        1: {
            "verts": [
                (2, -1, 0), (2, 1, 0), (1, 1, 0), (1, 2, 0), (-1, 2, 0), (-1, 1, 0), (-2, 1, 0), (-2, -1, 0),
                (-1, -1, 0), (-1, -2, 0), (1, -2, 0), (1, -1, 0),
                (2, -1, 2.5), (2, 1, 2.5), (1, 1, 2.5), (1, 2, 2.5), (-1, 2, 2.5), (-1, 1, 2.5), (-2, 1, 2.5),
                (-2, -1, 2.5), (-1, -1, 2.5), (-1, -2, 2.5), (1, -2, 2.5), (1, -1, 2.5)
            ],
            "faces": [
                (1, 2, 14, 13), (2, 3, 15, 14), (4, 5, 17, 16), (5, 6, 18, 17), (7, 8, 20, 19), (8, 9, 21, 20),
                (10, 11, 23, 22), (11, 0, 12, 23)  # Wall faces
            ]
        },
        2: {
            "verts": [
                (2, -1, 0), (2, 1, 0), (1, 2, 0), (-1, 2, 0), (-2, 1, 0), (-2, -1, 0), (-1, -1, 0), (-1, -2, 0),
                (1, -2, 0), (1, -1, 0),  # Bottom verts
                (2, -1, 2.5), (2, 1, 2.5), (1, 2, 2.5), (-1, 2, 2.5), (-2, 1, 2.5), (-2, -1, 2.5), (-1, -1, 2.5),
                (-1, -2, 2.5), (1, -2, 2.5), (1, -1, 2.5)  # Top verts
            ],
            "faces": [
                (1, 2, 12, 11), (3, 4, 14, 13), (5, 6, 16, 15), (6, 7, 17, 16), (8, 9, 19, 18), (9, 0, 10, 19)
                # Wall faces
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

        option = randint(1, 2)
        mesh.from_pydata(center_options[connections][option]["verts"], [], center_options[connections][option]["faces"])
        mesh.update(calc_edges=True)
        bpy.data.objects["Centerpiece"].rotation_euler = Euler((0, 0, randint(0, 3) * math.radians(90)))


# delete all objects in scene
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)

# place floor plane
bpy.ops.mesh.primitive_plane_add(location=(0, 0, 0), radius=10)
bpy.data.objects["Plane"].name = "Floor"
## add random floor texture to floor
bpy.data.objects["Floor"].data.materials.append(material_options["floor"][randint(0, len(material_options["floor"])-1)])

# place ceiling plane
bpy.ops.mesh.primitive_plane_add(location=(0, 0, 2.5), radius=10)
bpy.data.objects["Plane"].name = "Ceiling"
## add random floor (TODO: ceiling) texture to ceiling
bpy.data.objects["Ceiling"].data.materials.append(material_options["floor"][randint(0, len(material_options["floor"])-1)])

# place corridor X+
verts = [(2, -1, 0), (8, -1, 0), (8, -1, 2.5), (2, -1, 2.5),
         (2, 1, 0), (8, 1, 0), (8, 1, 2.5), (2, 1, 2.5)]
faces = [(0, 1, 2, 3), (4, 5, 6, 7)]

mesh = bpy.data.meshes.new("Xpos")
obj = bpy.data.objects.new("Xpos", mesh)

bpy.context.scene.objects.link(obj)

mesh.from_pydata(verts, [], faces)
mesh.update(calc_edges=True)

bpy.data.objects["Xpos"].data.materials.append(material_options["wall"][randint(0, len(material_options["wall"])-1)])

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
num_connections = randint(2, 4)
create_random_centerpiece(num_connections)

# place light source (wip:sun)
bpy.ops.object.lamp_add(type="POINT", location=(0, 0, 2))

#bpy.data.objects["<OBJECTNAME>"].data.materials.append(mat)
#bpy.data.objects["<OBJECTNAME>"].data.materials[0] = mat

# place camera
inside_intersection = True
## randomize position
if inside_intersection:
    cam_x = (randint(-10, 10) / 10) - 0.1
    cam_y = (randint(-10, 10) / 10) - 0.1
else:
    cam_x = (randint( 30, 70) / 10) - 0.1
    cam_y = (randint(-10, 10) / 10) - 0.1
## use randomized position and randomize rotation around z-axis
bpy.ops.object.camera_add(location=(cam_x, cam_y, 0.611), rotation=(math.radians(90), 0, math.radians(randint(0, 359))))
bpy.data.objects["Camera"].data.type = "PANO"
bpy.data.objects["Camera"].data.lens = 5

if num_connections > 2 and inside_intersection:
    print("Intersection")
else:
    print("Corridor")
