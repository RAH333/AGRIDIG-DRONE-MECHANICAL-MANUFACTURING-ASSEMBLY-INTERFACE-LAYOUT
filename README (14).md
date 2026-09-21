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