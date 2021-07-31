# Task:
# Somehow call all files in folder and save them as path
# then call them as blender for render, when one is rendered, render the next.
#

import os

# Grab all files from current directory
files = os.listdir('.')
blend_files = []

# filter trough current folder and check if the name ".blend " is in there. ASD
for file in files:
    if ".blend" in file:
        blend_files.append(file)

print(blend_files)
