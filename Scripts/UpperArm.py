from pxr import Usd, UsdGeom

file_path = "C:/Users/matte/OneDrive - Lebanese American University/Desktop/RobotArmUsd/UpperArm.usda"
stage = Usd.Stage.CreateNew(file_path)

UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)
xform = UsdGeom.Xform.Define(stage, "/UpperArm")
cube = UsdGeom.Cube.Define(stage, "/UpperArm/Geom")
cube.CreateSizeAttr(1.2)  # Same size as LowerArm

stage.SetDefaultPrim(xform.GetPrim())
stage.GetRootLayer().Save()
print("✅ UpperArm.usda created.")
