import math
import scipy.constants as const
import numpy as np

class KinematicsEngine:
    def __init__(self, gravity: float = const.g):
        # Default gravity is Earth's (9.80665 m/s^2), but can be set for any planet
        self.g = gravity

    def calculate_firing_solution(self, velocity: float, angle_degrees: float, initial_height: float = 0.0) -> dict:
        """
        Calculates the maximum height (apex of the arch), total flight time, 
        and maximum range of a projectile.
        """
        theta = math.radians(angle_degrees)
        
        # Total flight time using quadratic formula for when y(t) = 0
        v_y = velocity * math.sin(theta)
        flight_time = (v_y + math.sqrt(v_y**2 + 2 * self.g * initial_height)) / self.g
        
        # Max height (Apex)
        max_height = initial_height + (v_y**2) / (2 * self.g)
        
        # Total horizontal range
        v_x = velocity * math.cos(theta)
        max_range = v_x * flight_time
        
        return {
            "flight_time_seconds": flight_time,
            "max_height_meters": max_height,
            "range_meters": max_range
        }

    def generate_trajectory_points(self, velocity: float, angle_degrees: float, steps: int = 100) -> list:
        """Generates the X, Y coordinates to plot the physical arc of the projectile."""
        solution = self.calculate_firing_solution(velocity, angle_degrees)
        t_values = np.linspace(0, solution["flight_time_seconds"], steps)
        
        theta = math.radians(angle_degrees)
        points = []
        for t in t_values:
            x = velocity * math.cos(theta) * t
            y = (velocity * math.sin(theta) * t) - (0.5 * self.g * (t**2))
            points.append((x, y))
            
        return points
