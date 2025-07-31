from pxr import Usd, UsdGeom, Gf

stage = Usd.Stage.CreateNew("UpperArm.usda")
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)

cube = UsdGeom.Cube.Define(stage, '/UpperArm')
cube.AddTransformOp().Set(Gf.Matrix4d().SetScale(Gf.Vec3d(1, 4, 1)))  # Same height

stage.GetRootLayer().Save()
print("✅ upper_arm.usda created.")
