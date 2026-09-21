# System Architecture & Design Specifications

## 1. Aerial Platform & Configuration
* **Frame Configuration:** X-8 Coaxial Octocopter configuration (provides high torque, extreme redundancy, and compact small-size frame footprint for handling ground interaction forces).
* **Wheelbase / Size:** 450 mm diagonal motor-to-motor.
* **Target Weight (MTOW):** 3.5 kg (Drone: 2.2 kg, Payload Mechanism: 0.8 kg, Soil Sample Capacity: 0.5 kg).

## 2. Integrated Digging & Picking Mechanism
* **Actuation System:** High-torque NEMA 11 planetary gear stepper motor driving a central lead screw ($8\text{ mm}$ lead) for heavy vertical plunging.
* **End Effector:** Coaxial dual-scoop clamshell mechanism actuated via a secondary $25\text{ kg}\cdot\text{cm}$ waterproof metal-gear digital servo.
* **Force Feedback:** Miniature inline S-type load cell ($0\text{-}50\text{ N}$) located between the plunge carriage and the main subframe to measure ground resistance and prevent structural stalls.
