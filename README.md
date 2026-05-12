# Advance-Manipulator-Model2

This repository documents Phase 2 of the 3-DOF robotic manipulator project

## Improvements over Model 1
- **Simulation Environment:** Moved from basic physical testing to native **MuJoCo** physics simulation.
- **Advanced Controls:** Transitioning from raw joint-space serial commands to an automated **Forward Kinematics (DH Parameter)** framework.
- **Structural Accuracy:** Developed 4 cleanly isolated rigid links to accurately model mass, inertia, and collision boundaries.

## Specifications & Physical Dimensions
- **Simulation Engine:** MuJoCo (Native XML Model)
- **Actuation:** 3x Controlled Revolute Joints (Base Yaw, Shoulder Pitch, Elbow Pitch)
- **Link 1 (Base Height):** 125 mm
- **Link 2 (Upper Arm):** 100 mm
- **Link 3 (Forearm):** 120 mm
- **Software:** FreeCAD, MuJuCo, Visual Studio

## Kinematic Framework/Code working

The Code is based on Denavit-Hartenberg parameters and is using Forward Kinematics to predict the co-ordinate for the End-Factor of the Manipulator.

The given table is the DH Parameters table for the Manipulator Default position.

| Link ($i$) | Joint Angle ($\theta_i$) | Link Twist ($\alpha_i$) | Link Length ($a_i$) | Link Offset ($d_i$) |
| :---: | :---: | :---: | :---: | :---: |
| **1 (Base)** | $\theta_1$ | $\pi/2$ | $0\text{ mm}$ | $125\text{ mm}$ |
| **2 (Shoulder)** | $\theta_2$ | $0$ | $100\text{ mm}$ | $0\text{ mm}$ |
| **3 (Elbow)** | $\theta_3$ | $0$ | $120\text{ mm}$ | $0\text{ mm}$ |

! [**Rest Position of Manipulator**](Pictures/Default.PNG)

## 📁 Repository Structure
- `CAD_file/` - Raw FreeCAD assembly models (`.FCStd`)
- `STL_files/` - Individual 3D link meshes exported for simulation
- `MuJoCo/` - Native physics engine XML files mapping joint limits and boundaries
- `Code/` - Python scripts handling the mathematical calculations (`FK.py`)
