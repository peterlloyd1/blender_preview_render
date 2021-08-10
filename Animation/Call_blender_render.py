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
            continue
        else:
            blend_files.append(file)

# Printing all blend files in current blend_file list of render
print(blend_files)

# Calling consol on each blend file to call Blender_render.py
for file in blend_files:
    subprocess.call("blender " + file +
                    " --python Blender_Render.py", shell=True)
