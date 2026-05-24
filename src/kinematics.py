import math
import numpy as np
import scipy.constants as const

class AdvancedKinematicsEngine:
    def __init__(self, gravity: float = const.g, atmospheric_density: float = 1.225):
        # Default gravity (9.80665 m/s^2) and sea-level Earth air density (1.225 kg/m^3)
        self.g = gravity
        self.rho = atmospheric_density

    def trajectory_with_drag(
        self, 
        initial_velocity: float, 
        angle_degrees: float, 
        mass_kg: float, 
        area_sq_meters: float, 
        drag_coefficient: float = 0.47, 
        time_step: float = 0.01
    ) -> dict:
        """
        Calculates the true trajectory of a projectile passing through an atmosphere
        using numerical integration (Euler method).
        """
        theta = math.radians(angle_degrees)
        
        # Initial velocities
        v_x = initial_velocity * math.cos(theta)
        v_y = initial_velocity * math.sin(theta)
        
        # Initial positions
        x, y = 0.0, 0.0
        
        # Tracking metrics
        points = [(x, y)]
        time_elapsed = 0.0
        max_height = 0.0
        
        # Calculate the drag constant: 0.5 * rho * Cd * A
        # Divided by mass to easily convert force to acceleration (a = F/m)
        drag_constant = (0.5 * self.rho * drag_coefficient * area_sq_meters) / mass_kg
        
        # Simulate flight until the projectile hits the ground (y < 0)
        while y >= 0:
            # Current absolute velocity
            v_total = math.sqrt(v_x**2 + v_y**2)
            
            # Acceleration due to drag (opposes the direction of motion)
            a_x = -drag_constant * v_total * v_x
            a_y = -self.g - (drag_constant * v_total * v_y)
            
            # Update velocities (v_new = v_old + a*dt)
            v_x += a_x * time_step
            v_y += a_y * time_step
            
            # Update positions (p_new = p_old + v*dt)
            x += v_x * time_step
            y += v_y * time_step
            
            # Track apex
            if y > max_height:
                max_height = y
                
            points.append((x, y))
            time_elapsed += time_step

        return {
            "flight_time_seconds": time_elapsed,
            "max_height_meters": max_height,
            "range_meters": x,
            "trajectory_points": points
        }

# --- Usage Example ---
if __name__ == "__main__":
    engine = AdvancedKinematicsEngine()
    
    # Simulating a 155mm artillery shell (approx 43kg, 0.0188 m^2 area)
    result = engine.trajectory_with_drag(
        initial_velocity=800, # 800 m/s
        angle_degrees=45,
        mass_kg=43.0,
        area_sq_meters=0.0188,
        drag_coefficient=0.29 # Aerodynamic shell profile
    )
    
    print(f"Atmospheric Range: {result['range_meters']:.2f} m")
    print(f"Maximum Altitude: {result['max_height_meters']:.2f} m")
    print(f"Flight Time: {result['flight_time_seconds']:.2f} s")
