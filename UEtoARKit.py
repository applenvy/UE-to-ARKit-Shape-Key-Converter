import bpy

bl_info = {
    "name": "UEtoARKit",
    "author": "applenvy",
    "description": "Translates shape keys from the Unified Expressions standard to the Apple ARKit standard",
    "location": "Object > Convert UE to ARKit",
    "blender": (3, 0, 0),
    "version": (1, 0),
    "wiki_url": "",
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
            shapekeys = obj.data.shape_keys.key_blocks
        except AttributeError:
            # no shape keys
            return {'ERROR'}
        
        for shapekey in shapekeys:
            if shapekey.name in shapekeyTranslator:
                shapekey.name = shapekeyTranslator[shapekey.name]
        
        print("Shape keys converted!")
        return {'FINISHED'}
    
def menu_func(self,context):
    self.layout.operator(ShapeKeyRenameUEtoARKit.bl_idname)
    
def register():
    bpy.utils.register_class(ShapeKeyRenameUEtoARKit)
    bpy.types.VIEW3D_MT_object.append(menu_func)
    
def unregister():
    bpy.utils.unregister_class(ShapeKeyRenameUEtoARKit)

if __name__ == "__main__":
    register()