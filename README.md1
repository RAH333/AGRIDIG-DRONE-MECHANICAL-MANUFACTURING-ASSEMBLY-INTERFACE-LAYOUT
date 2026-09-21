# AGRIDIG-DRONE-MECHANICAL-MANUFACTURING-ASSEMBLY-INTERFACE-LAYOUT

# Agricultural AgriDig-Drone Project Repository

This repository contains the complete design, analysis framework, and firmware integration files for a small-scale, multi-functional agricultural drone capable of soil digging and sample picking.

## Repository Structure

```text
├── README.md                      # Project Overview and Quickstart
├── docs/
│   ├── design_specifications.md   # Detailed Mechanical & System Architecture
│   └── structural_analysis.md    # FEA, Motor Thrust, & Analytical Calculations
├── hardware/
│   ├── geometry_cad_bom.csv       # Component Dimensions, Weights, Materials, & BOM
│   └── drone_assembly_drawing.txt # ASCII Technical Manufacturing Layout
└── src/
    ├── main_controller.ino        # Flight Control & Mission Sequence State Machine
    └── actuator_sensor_driver.py  # Transducer, Sensor, & Actuator Interface Driver
```

## Quick Start
1. **Mechanical Design:** Review `hardware/drone_assembly_drawing.txt` and `hardware/geometry_cad_bom.csv` for structural metrics.
2. **Analysis:** Refer to `docs/structural_analysis.md` for aerodynamic thrust requirements and stress limits.
3. **Firmware:** Deploy `src/main_controller.ino` to your primary microcontroller board and run `src/actuator_sensor_driver.py` to handle peripheral loops.

## Quick Start
1. **Mechanical Design:** Review `hardware/drone_assembly_drawing.txt` and `hardware/geometry_cad_bom.csv` for structural metrics.
2. **Analysis:** Refer to `docs/structural_analysis.md` for aerodynamic thrust requirements and stress limits.
3. **Firmware:** Deploy `src/main_controller.ino` to your primary microcontroller board and run `src/actuator_sensor_driver.py` to handle peripheral loops.
```
================================================================================
AGRIDIG-DRONE MECHANICAL MANUFACTURING ASSEMBLY INTERFACE LAYOUT
================================================================================

            [Propeller Top]                  [Propeller Top]
                 \    /                           \    /
              =======O=======               =======O=======

              | Motor Top 1 |               | Motor Top 2 |
              ---------------               ---------------

                     |                             |
       ==============#=============================#==============
      / [Arm 1]                                           [Arm 2] \
     /                                                             \
    +---------------------------------------------------------------+

    |                  MAIN CARBON FIBER TOP PLATE                  |
    |                                                               |
    |      +-------------------------------------------------+      |
    |      |         src/main_controller.ino (MCU)          |      |
    |      +-------------------------------------------------+      |
    |                                                               |
    |      +-------------------------------------------------+      |
    |      |            LiPo Power Delivery Unit             |      |
    |      +-------------------------------------------------+      |
    |                                                               |
    |                  MAIN CARBON FIBER BOTTOM PLATE               |
    +---------------------------------------------------------------+
     \                                                             /
      \ [Arm 3]                                           [Arm 4] /
       ==============#=============================#==============

                     |                             |
              ---------------               ---------------

              | Motor Bott 3|               | Motor Bott 4|
              =======O=======               =======O=======
                 /    \                           /    \
            [Propeller Bott]                 [Propeller Bott]

                     ||                             ||
                     ||  [DIGGING PLUNGE ASSEMBLY]  ||
                     ||                             ||
                     ++=============================++
                     ||  NEMA 11 Lead Screw Motor   ||
                     ||         (STP-01)            ||
                     ||=============================||
                     ||    [---Linear Rail---]      ||
                     ||    [---Linear Rail---]      ||
                     ||=============================||
                     || Inline S-Type Load Cell     ||
                     ||         (LC-01)             ||
                     ++=============================++
                     ||   Digital Clamshell Servo   ||
                     ||         (SRV-01)            ||
                     +---------------+---------------+
                                    / \
                                   /   \
                              [Scoop 1] [Scoop 2]
                              (Soil Collection Pod)
```
