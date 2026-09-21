# AGRIDIG-DRONE-MECHANICAL-MANUFACTURING-ASSEMBLY-INTERFACE-LAYOUT

# Agricultural AgriDig-Drone Project Repository

This repository contains the complete design, analysis framework, and firmware integration files for a small-scale, multi-functional agricultural drone capable of soil digging and sample picking.

## Repository Structure

```text
â”œâ”€â”€ README.md                      # Project Overview and Quickstart
â”œâ”€â”€ docs/
â”‚   â”œâ”€â”€ design_specifications.md   # Detailed Mechanical & System Architecture
â”‚   â””â”€â”€ structural_analysis.md    # FEA, Motor Thrust, & Analytical Calculations
â”œâ”€â”€ hardware/
â”‚   â”œâ”€â”€ geometry_cad_bom.csv       # Component Dimensions, Weights, Materials, & BOM
â”‚   â””â”€â”€ drone_assembly_drawing.txt # ASCII Technical Manufacturing Layout
â””â”€â”€ src/
    â”œâ”€â”€ main_controller.ino        # Flight Control & Mission Sequence State Machine
    â””â”€â”€ actuator_sensor_driver.py  # Transducer, Sensor, & Actuator Interface Driver
```

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
