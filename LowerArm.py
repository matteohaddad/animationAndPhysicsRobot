from pxr import Usd, UsdGeom

file_path = "C:/Users/matte/OneDrive - Lebanese American University/Desktop/RobotArmUsd/LowerArm.usda"
stage = Usd.Stage.CreateNew(file_path)

UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)
xform = UsdGeom.Xform.Define(stage, "/LowerArm")
cube = UsdGeom.Cube.Define(stage, "/LowerArm/Geom")
cube.CreateSizeAttr(1.2)  # Tall rectangular prism

stage.SetDefaultPrim(xform.GetPrim())
stage.GetRootLayer().Save()
print("✅ LowerArm.usda created.")
