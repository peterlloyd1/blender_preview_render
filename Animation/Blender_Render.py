# Task:
# Somehow call all files in folder and save them as path
# then call them as blender for render, when one is rendered, render the next.
#

import bpy

# Turning off Overlays
for area in bpy.context.screen.areas:
    if area.type == 'VIEW_3D':
        for space in area.spaces:
            if space.type == 'VIEW_3D':
                space.overlay.show_overlays = False
                break
# Could have also done this if only 1 window open
# area.spaces[0].overlay.show_overlays = False

# Changing output to mp4
bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
bpy.context.scene.render.ffmpeg.format = 'MPEG4'


# getting the blender file number
file_number = bpy.path.basename(bpy.context.blend_data.filepath)[-8:-6]

# Creating folder and file output based on Blockout number
bpy.data.scenes[0].render.filepath = "//Preview/" + \
    "/" + str(file_number) + "_"


# Calling blender to preview render the file
bpy.ops.render.opengl(write_still=True, animation=True)

# When finished, exit.
exit()
