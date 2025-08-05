from pxr import Usd, UsdGeom, Sdf

# --- Create the USD stage with time codes and up axis ---
def CreateStage(path):
    stage = Usd.Stage.CreateNew(path)
    UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)
    stage.SetStartTimeCode(1)
    stage.SetEndTimeCode(192)
    return stage

# --- Add an instance of the robot with optional time offset and scale ---
def AddRobotInstance(stage, name, x_offset, offset=0, scale=1.0):
    robot_prim = UsdGeom.Xform.Define(stage, f"/{name}")
    UsdGeom.XformCommonAPI(robot_prim).SetTranslate((x_offset, 0, 0))

    layer_offset = Sdf.LayerOffset(offset=offset, scale=scale)
    robot_prim.GetPrim().GetReferences().AddReference(
        "C:/Users/matte/OneDrive - Lebanese American University/Desktop/RobotArmUsd/animated_robot.usda",
        layerOffset=layer_offset
    )

# --- Main function to create multiple animated robot instances ---
def CreateMultipleRobots():
    stage = CreateStage("C:/Users/matte/OneDrive - Lebanese American University/Desktop/RobotArmUsd/multiple_animated_robots.usda")

    # Add robots:
    AddRobotInstance(stage, "RobotA", 0, 0)           # Original
    AddRobotInstance(stage, "RobotB", 10, 48)         # Delayed start
    AddRobotInstance(stage, "RobotC", 20, 0, 0.5)     # Slower animation

    stage.GetRootLayer().Save()
    print("✅ multiple_animated_robots.usda created successfully.")

# --- Run the script ---
CreateMultipleRobots()
