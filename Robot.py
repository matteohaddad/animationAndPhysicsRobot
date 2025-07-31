from pxr import Usd, UsdGeom, UsdLux

file_path = "C:/Users/matte/OneDrive - Lebanese American University/Desktop/RobotArmUsd/Robot.usda"
stage = Usd.Stage.CreateNew(file_path)
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)

robot_prim = UsdGeom.Xform.Define(stage, "/Robot")
stage.SetDefaultPrim(robot_prim.GetPrim())

base = UsdGeom.Xform.Define(stage, "/Robot/Base")
base.GetPrim().GetReferences().AddReference("Base.usda")
UsdGeom.XformCommonAPI(base).SetTranslate((0, 0, 0))

lower = UsdGeom.Xform.Define(stage, "/Robot/LowerArm")
lower.GetPrim().GetReferences().AddReference("LowerArm.usda")
UsdGeom.XformCommonAPI(lower).SetTranslate((0, 2, 0))  

upper = UsdGeom.Xform.Define(stage, "/Robot/UpperArm")
upper.GetPrim().GetReferences().AddReference("UpperArm.usda")
UsdGeom.XformCommonAPI(upper).SetTranslate((0, 4, 0))  

gripper = UsdGeom.Xform.Define(stage, "/Robot/Gripper")
gripper.GetPrim().GetReferences().AddReference("Gripper.usda")
UsdGeom.XformCommonAPI(gripper).SetTranslate((0, 5.5, 0))

stage.GetRootLayer().Save()
print("Robot.usda created.")
