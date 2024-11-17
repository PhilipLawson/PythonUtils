import bpy
import bmesh
from math import radians
from bpy.props import *

bl_info = {
    "name": "Blender Stage Tool",
    "author": "Philip Lawson",
    "version": (1, 0, 0),
    "blender": (4, 2, 1),
    "location": "bpy>types>operator",
    "description": "Creates a stage",
    "warning": "",
    "wcooliki_url": "",
    "tracker_url": "",
    "category": ""}

def add_stage(width, height, depth, edgebevel):
    """
    This function takes inputs and returns vertex and face arrays.
    no actual mesh data creation is done here.
    """
    if(edgebevel == False):
        verts = [
            (+1.0, +1.0, 0.0),  #0
            (+1.0, -1.0, 0.0),  #1
            (-1.0, -1.0, 0.0),  #2
            (-1.0, +1.0, 0.0),  #3
            (+1.0, +1.0, +2.0), #4
            (+1.0, -1.0, +2.0), #5
        ]
        
        faces = [
        (0, 1, 2, 3),
        (4, 5, 1, 0),
        ]
    else:
        verts = [
            (+0.9, +1.0, 0.0),  #0
            (+0.9, -1.0, 0.0),  #1
            (-0.9, -1.0, 0.0),  #2
            (-0.9, +1.0, 0.0),  #3
            (-1.0, -1.0, 0.0),  #4
            (-1.0, +1.0, 0.0),  #5
            (+1.0, +1.0, +0.1), #6
            (+1.0, -1.0, +0.1), #7
            (+1.0, +1.0, +1.9), #8
            (+1.0, -1.0, +1.9), #9
            (+1.0, +1.0, +2.0), #10
            (+1.0, -1.0, +2.0), #11
        ]
        faces = [
            (4, 5, 3, 2),
            (2, 3, 0, 1),
            (1, 0, 6, 7),
            (7, 6, 8, 9),
            (9, 8, 10, 11),
            ] 

    # apply size
    for i, v in enumerate(verts):
        verts[i] = v[0] * width, v[1] * depth, v[2] * height

    return verts, faces


class stage_tool(bpy.types.Operator):
    bl_idname = "object.stage_tool"
    bl_label = "Stage Tool"
    bl_options = {'REGISTER', 'UNDO'}
    
    #create properties
    width: FloatProperty(
        name="Width",
        description="Stage Width",
        min=0.01, max=100.0,
        default=1.0,
    )
    height: FloatProperty(
        name="Height",
        description="Stage Height",
        min=1.0, max=100.0,
        default=1.0,
    )
    depth: FloatProperty(
        name="Depth",
        description="Stage Depth",
        min=0.01, max=100.0,
        default=1.0,
    )
    edgebevel: BoolProperty(
        name="Edge Bevel",
        default=False,
    )
    subdivide: BoolProperty(
        name="Subdivide",
        default=False,
    )
    layers: BoolVectorProperty(
        name="Layers",
        description="Object Layers",
        size=20,
        options={'HIDDEN', 'SKIP_SAVE'},
    )
    # generic transform props
    align_items = (
        ('WORLD', "World", "Align the new object to the world"),
        ('VIEW', "View", "Align the new object to the view"),
        ('CURSOR', "3D Cursor", "Use the 3D cursor orientation for the new object")
    )
    align: EnumProperty(
        name="Align",
        items=align_items,
        default='WORLD',
    )
    location: FloatVectorProperty(
        name="Location",
        subtype='TRANSLATION',
    )
    rotation: FloatVectorProperty(
        name="Rotation",
        subtype='EULER',
    )

    def execute(self, context):


        verts_loc, faces = add_stage(
            self.depth,
            self.height,
            self.width,
            self.edgebevel,
        )

        mesh = bpy.data.meshes.new("Stage")

        bm = bmesh.new()

        for v_co in verts_loc:
            bm.verts.new(v_co)

        bm.verts.ensure_lookup_table()
        bm.faces.ensure_lookup_table()
        for f_idx in faces:
            bm.faces.new([bm.verts[i] for i in f_idx]) 
       
        bm.to_mesh(mesh)    
        mesh.update()

        # add the mesh as an object into the scene with this utility module
        from bpy_extras import object_utils
        object_utils.object_data_add(context, mesh, operator=self)
        
        bpy.ops.object.shade_smooth()
        
        if self.subdivide == True:
            bpy.ops.object.modifier_add(type='SUBSURF')
            bpy.context.object.modifiers["Subdivision"].levels = 3
            
        bm.free()
        return {'FINISHED'}
    

    def bevelEdge():
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.bevel(offset=0.3, offset_pct=0, affect='EDGES')


def menu_func(self, context):
    self.layout.operator(stage_tool.bl_idname, text=stage_tool.bl_label)


# Register and add to the "object" menu (required to also use F3 search "Simple Object Operator" for quick access).
def register():
    bpy.utils.register_class(stage_tool)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(stage_tool)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.object.stage_tool()
