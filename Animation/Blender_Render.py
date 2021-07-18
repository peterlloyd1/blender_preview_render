# Task:
# Somehow call all files in folder and save them as path
# then call them as blender for render, when one is rendered, render the next.
#


import bpy

# getting the blender file number
file_number = bpy.path.basename(bpy.context.blend_data.filepath)[-8:-6]

# This is how it was:
#bpy.data.scenes[0].render.filepath = "//Render/"+ str(file_number) + "/" + str(file_number) + "_"
bpy.data.scenes[0].render.filepath = "//Render/" + \
    str(file_number) + "/" + str(file_number) + "_"

bpy.ops.render.render(animation=False, use_viewport=False, write_still=True)

# filename = "test.py"
# exec(compile(open(filename).read(), filename, 'exec'))
# bpy.path.basename(bpy.context.blend_data.filepath)[:2]
