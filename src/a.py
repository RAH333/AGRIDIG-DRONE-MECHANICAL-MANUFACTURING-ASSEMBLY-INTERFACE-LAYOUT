    def drive_plunge_stepper(self, target_depth_mm: float, speed_mm_s: float):
        """Moves linear stepper carriage while evaluating real-time transducer strain."""
        print(f"\n[STEPPER] Moving carriage to depth: {target_depth_mm}mm at speed {speed_mm_s}mm/s")
        while self.stepper_position_mm < target_depth_mm:
            self.stepper_position_mm += speed_mm_s * 0.1
            current_force = self.read_load_cell_transducer()
            
            print(f"  -> Depth: {self.stepper_position_mm:.1f}mm | Force Transducer: {current_force} N")
            
            if current_force >= self.max_force_threshold:
                print(f"  [CRITICAL WARNING] Force threshold exceeding safety envelope ({current_force}N)! Halting Plunge.")
                break
            time.sleep(0.1)
          
