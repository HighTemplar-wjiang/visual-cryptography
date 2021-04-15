# Generate cloud of cubes from pre-generated visual cryptography images.
bl_info = {
    "name": "MyAddon",
    "author": "GnomeX",
    "version": (1, 0),
    "blender": (2, 91, 0),
    "location": "View3d > Tool",
    "warning": "",
    "wiki_url": "weiweijiang.xyz",
    "category": "Add Mesh",
}

import bpy

# Redirect output to the Blender console.
# Credits: https://blender.stackexchange.com/a/142317
def print(data):
    for window in bpy.context.window_manager.windows:
        screen = window.screen
        for area in screen.areas:
            if area.type == 'CONSOLE':
                override = {'window': window, 'screen': screen, 'area': area}
                bpy.ops.console.scrollback_append(override, text=str(data), type="OUTPUT")


class TestPanel(bpy.types.Panel):
    bl_label = "Test Panel"
    bl_idname = "PT_TestPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MyAddon"
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text="Add an object", icon="BONE_DATA")
        
        row = layout.row()
        row.operator("mesh.primitive_cube_add")
        
        row = layout.row()
        row.operator("mesh.primitive_uv_sphere_add")
        

class PanelA(bpy.types.Panel):
    bl_label = "Panel A"
    bl_idname = "PT_Panel_A"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MyAddonA"
    bl_parent_id = "PT_TestPanel"
    bl_options = {"DEFAULT_CLOSED"}
    
    
    def draw(self, context):
        layout = self.layout
        object = context.object
        
        row = layout.row()
        row.label(text="Panel A", icon="OUTLINER_OB_LIGHT")
        
        row = layout.row()
        row.operator("transform.resize")
        row.scale_y = 2
        
#        row = layout.row()
#        layout.scale_y = 1.4
        
        col = layout.column()
        col.prop(object, "scale")
        
        
        
class PanelB(bpy.types.Panel):
    bl_label = "Panel B"
    bl_idname = "PT_Panel_B"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MyAddonB"
    bl_parent_id = "PT_TestPanel"
    bl_options = {"DEFAULT_CLOSED"}
    
    def draw(self, context):
        layout = self.layout
        object = context.object
        
        row = layout.row()
        row.label(text="Panel B", icon="EXPERIMENTAL")
        
        row = layout.row()
        row.operator("object.shade_smooth", text="Set Shade Smooth", icon="RENDER_ANIMATION")
        row.operator("object.subdivision_set", text="Set Subdivision", icon="EMPTY_DATA")
        
        row = layout.row()
        row.operator("object.modifier_add")
        
        
        
        
def register():
    bpy.utils.register_class(TestPanel)
    bpy.utils.register_class(PanelA)
    bpy.utils.register_class(PanelB)
    
    
def unregister():
    bpy.utils.unregister_class(TestPanel)
    bpy.utils.unregister_class(PanelA)
    bpy.utils.unregister_class(PanelB)
    

if __name__ == "__main__":
    register()
    
    


