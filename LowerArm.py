from pxr import Usd, UsdGeom, Gf

stage = Usd.Stage.CreateNew("LowerArm.usda")
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)

cube = UsdGeom.Cube.Define(stage, '/LowerArm')
cube.AddTransformOp().Set(Gf.Matrix4d().SetScale(Gf.Vec3d(1, 4, 1)))  # Tall

stage.GetRootLayer().Save()
print("✅ lower_arm.usda created.")
