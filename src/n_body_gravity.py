import numpy as np
import scipy.constants as const

class NBodyGravityEngine:
    def __init__(self):
        self.G = const.G # 6.67430e-11 m^3 kg^-1 s^-2

    def gravitational_force(self, mass1: float, mass2: float, pos1: np.ndarray, pos2: np.ndarray) -> np.ndarray:
        """
        Calculates the gravitational force vector exerted on mass1 by mass2.
        Positions should be 3D numpy arrays [x, y, z].
        """
        displacement = pos2 - pos1
        distance = np.linalg.norm(displacement)
        
        if distance == 0:
            return np.zeros(3) # Prevent division by zero if objects perfectly overlap
            
        force_magnitude = self.G * (mass1 * mass2) / (distance**2)
        force_direction = displacement / distance # Unit vector
        
        return force_magnitude * force_direction

    def calculate_system_accelerations(self, masses: list, positions: list) -> list:
        """
        Calculates the instantaneous acceleration vectors for a system of N bodies 
        (e.g., a solar system) interacting simultaneously.
        """
        num_bodies = len(masses)
        accelerations = [np.zeros(3) for _ in range(num_bodies)]
        
        for i in range(num_bodies):
            for j in range(num_bodies):
                if i != j:
                    force = self.gravitational_force(masses[i], masses[j], positions[i], positions[j])
                    # a = F/m
                    accelerations[i] += force / masses[i]
                    
        return accelerations
