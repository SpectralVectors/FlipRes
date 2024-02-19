import bpy
from bl_ui import properties_output
from .properties_output_flipres import classes

bl_info = {
    "name": "Flip Resolution",
    "author": "Spectral Vectors",
    "version": (1, 2),
    "blender": (2, 80, 0),
    "location": "Properties > Output > Format",
    "description": "Switches your render from Landscape to Portrait and back",
    "category": "Render"
}


output_props = [cls for cls in properties_output.classes]


def register():
    for cls in output_props:
        if cls.is_registered:
            bpy.utils.unregister_class(cls)

    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    for cls in output_props:
        if not cls.is_registered:
            bpy.utils.register_class(cls)


if __name__ == "__main__":
    register()
