import math
import scipy.constants as const

class AstrodynamicsEngine:
    def __init__(self):
        # Gravitational constant (m^3 kg^-1 s^-2)
        self.G = const.G

    def calculate_delta_v(self, exhaust_velocity: float, initial_mass: float, final_mass: float) -> float:
        """
        Calculates the maximum change in velocity (Delta-v) using the Tsiolkovsky rocket equation.
        """
        if final_mass <= 0 or initial_mass < final_mass:
            raise ValueError("Invalid mass parameters.")
        return exhaust_velocity * math.log(initial_mass / final_mass)

    def escape_velocity(self, planetary_mass: float, radius: float) -> float:
        """
        Calculates the velocity required to escape a planetary body's gravitational influence.
        """
        return math.sqrt((2 * self.G * planetary_mass) / radius)

    def hohmann_transfer_delta_v(self, mu: float, r1: float, r2: float) -> tuple:
        """
        Calculates the two Delta-v burns required for a Hohmann transfer orbit between two circular orbits.
        mu: Standard gravitational parameter of the central body.
        """
        v_initial = math.sqrt(mu / r1)
        v_final = math.sqrt(mu / r2)
        
        # Velocity at periapsis and apoapsis of the transfer ellipse
        a_transfer = (r1 + r2) / 2
        v_transfer_periapsis = math.sqrt(mu * ((2 / r1) - (1 / a_transfer)))
        v_transfer_apoapsis = math.sqrt(mu * ((2 / r2) - (1 / a_transfer)))
        
        delta_v1 = abs(v_transfer_periapsis - v_initial)
        delta_v2 = abs(v_final - v_transfer_apoapsis)
        
        return delta_v1, delta_v2
