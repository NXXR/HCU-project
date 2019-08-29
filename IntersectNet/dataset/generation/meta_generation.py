import subprocess
import os

blender_path = os.path.join("C:/", "Program Files", "Blender Foundation", "Blender")
script_path = os.path.join("C:/", "Users", "M.Zeumer", "Workspace", "HCU-project", "IntersectNet", "dataset", "generation")
# list with script names and number of images to be generated
dataset = [
            ("pano/blenderscript_train_corridor.py",            2500),
            ("pano/blenderscript_train_intersection.py",        2500),
            ("pano/blenderscript_validation_corridor.py",       1000),
            ("pano/blenderscript_validation_intersection.py",   1000),
            ("normal/blenderscript_train_corridor.py",          2500),
            ("normal/blenderscript_train_intersection.py",      2500),
            ("normal/blenderscript_validation_corridor.py",     1000),
            ("normal/blenderscript_validation_intersection.py", 1000),
            ("blenderscript_test_corridor.py",                  1000),
            ("blenderscript_test_intersection.py",              1000),
          ]

# generate images for each script
for filename, amount in dataset:
    command = "cd "+blender_path+" && blender --background --python "+os.path.join(script_path, filename)+""
    print("--- Generating from {} ({} images)".format(filename, amount))
    for i in range(0, amount):
        process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        print("".join(output.decode("utf-8").split("\r\n")[-6:-4]))
        if error: print(error)
print("--- Generation Finished ---")
