import bpy
import requests 
import sys

# https://blender.stackexchange.com/questions/6817/how-to-pass-command-line-arguments-to-a-blender-python-script

# Command from command line
# blender --background --python UVMapping.py -- blobUrl localPath outputPath

# argv = sys.argv
# argv = argv[argv.index("--") + 1:]  # get all args after "--"

# print(argv)  # --> ['blobUrl', 'localPath', 'outputPath']

# Blob URL from website where we read the glb from
# blobUrl = argv[0]

# LocalPath on server where we write the glb to
# localPath = argv[1] 

# Output path on server where we write the UV-Mapped glb to
# outputPath = argv[2]

# r = requests.get('blobUrl')
# if r.status_code == 200:
#     with open(path, 'wb') as f:
#         for chunk in r:
#             f.write(chunk)

# From the command line in the future
inputPath = "C:/Users/CXJKCS/Dev/Protiq/lschoenepxc.github.io/test.glb"
            
bpy.ops.import_scene.gltf(filepath=inputPath)

obj = bpy.context.object.children[0]

# Select each object
obj.select_set(True)
# Make it active
bpy.context.view_layer.objects.active = obj
# Toggle into Edit Mode
bpy.ops.object.mode_set(mode='EDIT')
# Select the geometry
bpy.ops.mesh.select_all(action='SELECT')
# Call the smart project operator
bpy.ops.uv.smart_project(island_margin=0.001)
# Toggle out of Edit Mode
bpy.ops.object.mode_set(mode='OBJECT')

# From command line in the future
outputPath = "C:/Users/CXJKCS/Dev/Protiq/lschoenepxc.github.io/modelUV.glb"

bpy.ops.export_scene.gltf(filepath=outputPath)

bpy.ops.object.delete(use_global=False)