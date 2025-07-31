from pxr import Usd, UsdGeom, Sdf

# Create the main stage file
stage = Usd.Stage.CreateNew("C:\Users\matte\OneDrive - Lebanese American University\Desktop\RobotArmUsd\Robot.usda")

UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)

# Robot root XForm
robot = UsdGeom.Xform.Define(stage, "/Robot")

# Base
base = UsdGeom.Xform.Define(stage, "/Robot/Base")
base.GetPrim().GetReferences().AddReference("Base.usda")

# Lower Arm
lower = UsdGeom.Xform.Define(stage, "/Robot/LowerArm")
lower.GetPrim().GetReferences().AddReference("LowerArm.usda")
UsdGeom.XformCommonAPI(lower).SetTranslate((0, 2, 0))  # adjust position if needed

# Upper Arm
upper = UsdGeom.Xform.Define(stage, "/Robot/UpperArm")
upper.GetPrim().GetReferences().AddReference("UpperArm.usda")
UsdGeom.XformCommonAPI(upper).SetTranslate((0, 4, 0))  # adjust position if needed

# Gripper
gripper = UsdGeom.Xform.Define(stage, "/Robot/Gripper")
gripper.GetPrim().GetReferences().AddReference("Gripper.usda")
UsdGeom.XformCommonAPI(gripper).SetTranslate((0, 6, 0))  # adjust position if needed

# Save the stage
stage.GetRootLayer().Save()
print("✅ Robot.usda created successfully!")
