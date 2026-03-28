import bpy

bl_info = {
    "name": "UEtoARKit",
    "author": "applenvy",
    "description": "Translates shape keys from the Unified Expressions standard to the Apple ARKit standard",
    "location": "Object > Convert UE to ARKit",
    "blender": (3, 0, 0),
    "version": (1, 0, 1),
    "doc_url": "https://github.com/applenvy/UE-to-ARKit-Shape-Key-Converter",
    "category": "Object",
}

shapekeyTranslator = {
    "BrowInnerUp": "browInnerUp",
    "BrowOuterUpLeft": "browOuterUpLeft",
    "BrowOuterUpRight": "browOuterUpRight",
    "BrowDownLeft": "browDownLeft",
    "BrowDownRight": "browDownRight",
    "EyeClosedLeft": "eyeBlinkLeft",
    "EyeClosedRight": "eyeBlinkRight",
    "EyeLookUpLeft": "eyeLookUpLeft",
    "EyeLookUpRight": "eyeLookUpRight",
    "EyeLookDownLeft": "eyeLookDownLeft",
    "EyeLookDownRight": "eyeLookDownRight",
    "EyeLookOutLeft": "eyeLookOutLeft",
    "EyeLookOutRight": "eyeLookOutRight",
    "EyeLookInLeft": "eyeLookInLeft",
    "EyeLookInRight": "eyeLookInRight",
    "EyeSquintLeft": "eyeSquintLeft",
    "EyeSquintRight": "eyeSquintRight",
    "EyeWideLeft": "eyeWideLeft",
    "EyeWideRight": "eyeWideRight",
    "CheekPuff": "cheekPuff",
    "CheekSquintLeft": "cheekSquintLeft",
    "CheekSquintRight": "cheekSquintRight",
    "NoseSneerLeft": "noseSneerLeft",
    "NoseSneerRight": "noseSneerRight",
    "JawOpen": "jawOpen",
    "JawForward": "jawForward",
    "JawLeft": "jawLeft",
    "JawRight": "jawRight",
    "MouthClosed": "mouthClose",
    "MouthLeft": "mouthLeft",
    "MouthRight": "mouthRight",
    "MouthSmileLeft": "mouthSmileLeft",
    "MouthSmileRight": "mouthSmileRight",
    "MouthFrownLeft": "mouthFrownLeft",
    "MouthFrownRight": "mouthFrownRight",
    "MouthDimpleLeft": "mouthDimpleLeft",
    "MouthDimpleRight": "mouthDimpleRight",
    "MouthUpperUpLeft": "mouthUpperUpLeft",
    "MouthUpperUpRight": "mouthUpperUpRight",
    "MouthLowerDownLeft": "mouthLowerDownLeft",
    "MouthLowerDownRight": "mouthLowerDownRight",
    "MouthPressLeft": "mouthPressLeft",
    "MouthPressRight": "mouthPressRight",
    "MouthStretchLeft": "mouthStretchLeft",
    "MouthStretchRight": "mouthStretchRight",
    "MouthRaiserUpper": "mouthShrugUpper",
    "MouthRaiserLower": "mouthShrugLower",
    "LipFunnel": "mouthFunnel",
    "LipPucker": "mouthPucker",
    "LipSuckUpper": "mouthRollUpper",
    "LipSuckLower": "mouthRollLower",
    "TongueOut": "tongueOut"
}

class ShapeKeyRenameUEtoARKit(bpy.types.Operator):
    """Rename UE shape keys to ARKit standards"""
    bl_idname = "object.ue_to_arkit"
    bl_label = "Convert UE to ARKit"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        obj = context.active_object
        
        try:
            shape_keys = obj.data.shape_keys.key_blocks
        except AttributeError:
            self.report({'ERROR'}, "No shape keys found on mesh!")
            return {'CANCELLED'}
        
        converted_keys = []
        for shape_key in shape_keys:
            if shape_key.name in shapekeyTranslator:
                converted_keys.append(shape_key.name)
                shape_key.name = shapekeyTranslator[shape_key.name]
        
        # check if all shape keys were found
        # maybe consider referring to shape keys as something other than just "keys"
        # to avoid confusion with dictionary keys
        if len(converted_keys) == 0:
            self.report({'ERROR'}, "No UE-compatible shape keys were found!")
            
        elif len(converted_keys) == 52:
            self.report({'INFO'}, "Converted all 52 shape keys!")     
            
        else:
            missing_keys = [key for key in shapekeyTranslator.keys() if key not in converted_keys]
            self.report({'WARNING'}, f"Only {len(converted_keys)} out of 52 ARKit-compatible shape keys were found!\nMissing UE shape keys: {', '.join(missing_keys)}")

        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(ShapeKeyRenameUEtoARKit.bl_idname)
    
def register():
    bpy.utils.register_class(ShapeKeyRenameUEtoARKit)
    bpy.types.VIEW3D_MT_object.append(menu_func)
    
def unregister():
    bpy.utils.unregister_class(ShapeKeyRenameUEtoARKit)

if __name__ == "__main__":
    register()
