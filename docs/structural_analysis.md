# Analytical Simulation & Physics Modeling

## 1. Aerodynamic Thrust Simulation Model
To maintain stable hover at Maximum Takeoff Weight (MTOW) while managing ground ground-effect dynamics:
$$T_{\text{total}} = m \cdot g \cdot FOS$$
* Where $m = 3.5\text{ kg}$, $g = 9.81\text{ m/s}^2$, and Factor of Safety ($FOS$) = $2.0$ (for rapid recovery during tool retraction).
* Required Total Thrust: $68.67\text{ N}$ (or $8.58\text{ N}$ per motor across 8 motors).

## 2. Ground Interaction FEA Boundary Conditions
* **Plunge Force ($F_z$):** Maximum linear force applied by lead screw system before motor stall $= 120\text{ N}$.
* **Frame Stress Distribution:** Carbon fiber plates ($2.0\text{ mm}$ thickness) analyzed under a $120\text{ N}$ localized central reaction.
* **Maximum Von Mises Stress:** Calculated at $42.3\text{ MPa}$ near the subframe mounts, well below the tensile yield strength of structural Carbon Fiber ($V_f = 60\%$, $\sigma_y \approx 600\text{ MPa}$), delivering an operational FOS of $14.1$.
