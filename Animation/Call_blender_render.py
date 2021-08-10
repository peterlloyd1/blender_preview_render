# Task:
# Somehow call all files in folder and save them as path
# then call them as blender for render, when one is rendered, render the next.


import os
import subprocess

# Grab all files from current directory
files = os.listdir(".")

blend_files = []

# filter trough current folder and check if the name ".blend " is in there.
for file in files:
    if ".blend" in file:
        if file[-1] == "1":
            print("deleted " + file)
        else:
            blend_files.append(file)

        # Need remove all files that end with .blend1 somehow

print("blender " + blend_files[0] + " --python Blender_Render.py")


# subprocess.call(
#    "blender " + blend_files[0] + " --python Blender_Render.py", shell=True)


print(blend_files)
