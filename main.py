import bpy
import os
import math
import mathutils

# Setup paths relative to script
script_dir = os.path.dirname(os.path.abspath(__file__))
stl_folder = os.path.join(script_dir, "STLFiles")
output_folder = os.path.join(stl_folder, "screenshots")

def clean_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

def import_stl(filepath):
    bpy.ops.import_mesh.stl(filepath=filepath)
    return bpy.context.selected_objects[0]

def direction_to_euler(direction):
    vec = mathutils.Vector(direction)
    rot_quat = vec.to_track_quat('-Z', 'Y')
    return rot_quat.to_euler()

def setup_camera_and_lighting(target_obj):
    cam_data = bpy.data.cameras.new(name="Camera")
    cam_obj = bpy.data.objects.new("Camera", cam_data)
    bpy.context.collection.objects.link(cam_obj)
    bpy.context.scene.camera = cam_obj

    light_data = bpy.data.lights.new(name="Light", type='SUN')
    light_obj = bpy.data.objects.new(name="Light", object_data=light_data)
    light_obj.location = (5, -5, 5)
    bpy.context.collection.objects.link(light_obj)

    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = target_obj
    target_obj.select_set(True)
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
    target_obj.location = (0, 0, 0)

    radius = target_obj.dimensions.length * 2
    angle_horizontal = math.radians(45)
    angle_vertical = math.radians(60)
    x = radius * math.sin(angle_horizontal)
    y = -radius * math.cos(angle_horizontal)
    z = radius * math.sin(angle_vertical)
    cam_obj.location = (x, y, z)

    direction = (-x, -y, -z)
    cam_obj.rotation_euler = direction_to_euler(direction)

def render_image(output_path):
    bpy.context.scene.render.filepath = output_path
    bpy.context.scene.render.image_settings.file_format = 'PNG'
    bpy.context.scene.render.resolution_x = 800
    bpy.context.scene.render.resolution_y = 800
    bpy.ops.render.render(write_still=True)

# Walk through all folders and subfolders
for root, dirs, files in os.walk(stl_folder):
    for filename in files:
        if filename.lower().endswith(".stl"):
            stl_path = os.path.join(root, filename)
            print(f"Processing file: {stl_path}")

            # Get relative path from STLFiles folder to the file's folder
            relative_dir = os.path.relpath(root, stl_folder)

            # Prepare output directory keeping folder structure
            output_dir = os.path.join(output_folder, relative_dir)
            os.makedirs(output_dir, exist_ok=True)

            # Output file path for screenshot
            output_file = os.path.join(output_dir, os.path.splitext(filename)[0] + ".png")

            clean_scene()
            obj = import_stl(stl_path)
            setup_camera_and_lighting(obj)
            render_image(output_file)

            print(f"Saved screenshot: {output_file}")

print("✅ All STL files rendered with folder structure preserved.")
