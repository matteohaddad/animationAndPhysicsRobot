from pxr import Usd, UsdGeom

stage = Usd.Stage.CreateNew("Gripper.usda")
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)

sphere = UsdGeom.Sphere.Define(stage, '/Gripper')
sphere.CreateRadiusAttr(0.5)

stage.GetRootLayer().Save()
print("✅ Gripper.usda created.")
