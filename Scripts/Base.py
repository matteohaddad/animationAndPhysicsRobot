from pxr import Usd, UsdGeom

file_path = "C:/Users/matte/OneDrive - Lebanese American University/Desktop/RobotArmUsd/Base.usda"


stage = Usd.Stage.CreateNew(file_path)
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)

cylinder = UsdGeom.Cylinder.Define(stage, '/Base')
cylinder.CreateHeightAttr(2.0)
cylinder.CreateRadiusAttr(3.0)

stage.SetDefaultPrim(cylinder.GetPrim())
stage.GetRootLayer().Save()
print("✅ Base.usda created.")
