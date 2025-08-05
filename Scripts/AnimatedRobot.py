from pxr import Usd, UsdGeom, Gf, Sdf
import os
import sys

# Fix import path for Script Editor (adjust if needed)
sys.path.append("C:/Users/matte/OneDrive - Lebanese American University/Desktop/RobotArmUsd")

# --- Local versions of utils.py functions ---

def MakeInitialStage(path):
    stage = Usd.Stage.CreateNew(path)
    UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)
    stage.SetStartTimeCode(1)
    stage.SetEndTimeCode(192)
    return stage

def AddReferenceToGeometry(stage, prim_path, reference_file):
    geom = UsdGeom.Xform.Define(stage, prim_path)
    geom.GetPrim().GetReferences().AddReference(reference_file)
    return geom

# --- Animation logic ---

def AddBaseAnimation(base):
    spin = base.AddRotateYOp(opSuffix="spin")
    spin.Set(time=1, value=0)
    spin.Set(time=192, value=360)

def AddUpperArmAnimation(upper):
    twist = upper.AddRotateZOp(opSuffix="twist")
    twist.Set(time=1, value=0)
    twist.Set(time=96, value=30)

def AddGripperAnimation(gripper):
    scale = gripper.AddScaleOp(opSuffix="openClose")
    scale.Set(time=1, value=Gf.Vec3f(1, 1, 1))
    scale.Set(time=96, value=Gf.Vec3f(2, 2, 2))
    scale.Set(time=192, value=Gf.Vec3f(1, 1, 1))

# --- Main animation function ---

def AnimateRobot():
    stage = MakeInitialStage("C:/Users/matte/OneDrive - Lebanese American University/Desktop/RobotArmUsd/animated_robot.usda")


    # Reference robot base
    robot = AddReferenceToGeometry(stage, "/Robot", "Robot.usda")

    # Override children to add animation
    base = stage.OverridePrim("/Robot/Base")
    upper = stage.OverridePrim("/Robot/UpperArm")
    gripper = stage.OverridePrim("/Robot/Gripper")

    AddBaseAnimation(base)
    AddUpperArmAnimation(upper)
    AddGripperAnimation(gripper)

    stage.SetMetadata("comment", "Time-sampled animated robot")
    stage.GetRootLayer().Save()
    print("✅ animated_robot.usda created.")

# --- Run ---
AnimateRobot()
