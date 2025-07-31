from pxr import Usd, UsdGeom

stage = Usd.Stage.CreateNew("Base.usda")
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)

cylinder = UsdGeom.Cylinder.Define(stage, '/Base')
cylinder.CreateHeightAttr(2.0)     # Short
cylinder.CreateRadiusAttr(3.0)     # Wide

stage.GetRootLayer().Save()
print("✅ Base.usda created.")
