# Assignment 2 – Animation and Physics Integration

This project implements:
- Time-sampled animation on a robot arm
- Multiple robot instances with animation offsets
- Physics simulation using USD Composer and Python scripting

## 📁 Folder Structure

- `Scripts/`: Python files for animation and physics generation
- `usda/`: All generated USD stages

## 📂 Key Files

### Animation
- `animated_robot.usda`: Robot animated from frame 1 to 192
- `multiple_animated_robots.usda`: 3 versions:
  - Original
  - Offset (layerOffset: offset=48)
  - Slowed (layerOffset: scale=0.5)

### Physics
- `physicsTest`: Physics-enabled robot with ground plane and material

