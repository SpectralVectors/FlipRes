bl_info = {
    "name": "Flip Resolution",
    "author": "Spectral Vectors",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "Properties > Output > Format",
    "description": "Switches your render X/Y resolution from Landscape to Portrait and back",
    "category": "Render"
}

import bpy

class FlipResolution(bpy.types.Operator):
    """Flips the X/Y render resolution: Landscape to Portrait"""
    bl_idname = "render.flip_resolution"
    bl_label = "Flip X/Y Resolution"

    def execute(self, context):
        res_x = context.scene.render.resolution_x
        res_y = context.scene.render.resolution_y
        new_y = res_x
        new_x = res_y
        context.scene.render.resolution_x = new_x
        context.scene.render.resolution_y = new_y        
        return {'FINISHED'}

def extra_button(self, context):
    layout = self.layout
    split = layout.split(factor=0.4)
    split.label(text='')
    split.operator('render.flip_resolution', icon='FILE_REFRESH')
        
def register():
    bpy.utils.register_class(FlipResolution)
    bpy.types.RENDER_PT_format.prepend(extra_button)

def unregister():
    bpy.utils.unregister_class(FlipResolution)
    bpy.types.RENDER_PT_format.remove(extra_button)
    

if __name__ == "__main__":
    register()
