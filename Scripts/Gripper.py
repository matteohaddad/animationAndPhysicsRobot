from pxr import Usd, UsdGeom

file_path = "C:/Users/matte/OneDrive - Lebanese American University/Desktop/RobotArmUsd/Gripper.usda"
stage = Usd.Stage.CreateNew(file_path)

UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)
xform = UsdGeom.Xform.Define(stage, "/Gripper")
sphere = UsdGeom.Sphere.Define(stage, "/Gripper/Geom")
sphere.CreateRadiusAttr(0.5)  # Small and centered

stage.SetDefaultPrim(xform.GetPrim())
stage.GetRootLayer().Save()
print("✅ Gripper.usda created.")
