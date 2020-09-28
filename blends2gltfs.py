#===================================#
#           BLENDS2GLTFS            #
#                                   #
#  a .blend to .gltf mass exporter  #
#                                   #
# Author: Belery Olivier            #
# Version: 1.0                      #
# License: MIT                      #
#===================================#
#
# Description:
# ------------
# Exports all blend files (even nested in subdirectories) to GLTF 2.
# Exported files are saved in a specified location.
# This py scipt uses Blender's embeded python interpreter. No other Python required.
# Use case: Export multiple blender files content to single Unity/Godot/A-frame assets folder.  
#
# USAGE:
#
#   WINDOWS: "C:/program files (x86)/blender foundation/blender/blender.exe" --background --python blends2gltfs.py -- PATH_WHERE TO EXPORT YOUR_GLTF
#   UNIX   : blender --background --python blends2gltfs.py -- PATH_WHERE TO EXPORT YOUR_GLTF

import os
import bpy
import sys
import time
import glob
from bpy.app.handlers import persistent


########## persistent operator ##########
@persistent
def load_handler(dummy):
    #getting output dir from system vars
    argv = sys.argv
    argv = argv[argv.index("--") + 1:]
    outputdir = argv[0]

    #Generate output filename and path bpy.data.filepath
    outputfile = bpy.path.display_name_from_filepath(files[0]) + ".glb"
    outputpath = outputdir + "\\" + outputfile

    print("EXPORTING " + outputfile + " ..... "),
    #exporting file

    bpy.ops.export_scene.gltf(
    export_format='GLB',
    export_yup=True,
    export_animations=False,
    export_image_format ='PNG',
    export_apply=True,
    export_normals=True,
    export_tangents=False,
    export_colors =True,
    export_materials=True,
    filepath=outputpath)
    print("done")

    processed.append(files.pop(0))
    if(len(files) > 0): 
        time.sleep(1)
        bpy.ops.wm.open_mainfile(filepath=files[0])
    else:
        print("OPERATION FINISHED - processed files:" + str(len(processed)))
        print("OPERATION OUTPUT PATH IS: " + outputdir)
        blockPrint()
        bpy.ops.wm.quit_blender()
########## persistent operator end ##########
    
#declaring persitent handler to use when opening file
bpy.app.handlers.load_post.append(load_handler)

# Disable printout
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore printout
def enablePrint():
    sys.stdout = sys.__stdout__

# Getting .blend files list of current folder and subfolder (1 level deep)
files = []
processed = []
for f in glob.iglob("./*/*.blend"):
    files.append(f)

# Opens up the first file on initial script execution.
# Folowing files loading will be handled by the persistent operator (load_handler)
bpy.ops.wm.open_mainfile(filepath=files[0])