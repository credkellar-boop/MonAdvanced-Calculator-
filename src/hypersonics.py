import math

class HypersonicsEngine:
    def __init__(self):
        # Specific heat ratio for standard air
        self.gamma = 1.4

    def mach_angle(self, mach_number: float) -> float:
        """
        Calculates the angle of the shockwave cone (in radians) created by a supersonic object.
        """
        if mach_number <= 1.0:
            raise ValueError("Mach angle is only defined for supersonic speeds (Mach > 1).")
        return math.asin(1.0 / mach_number)

    def stagnation_temperature(self, ambient_temp_kelvin: float, mach_number: float) -> float:
        """
        Calculates the extreme temperature at the leading edge (nose cone) of a vehicle 
        due to air compression at hypersonic speeds.
        """
        heating_factor = 1 + ((self.gamma - 1) / 2) * (mach_number ** 2)
        return ambient_temp_kelvin * heating_factor
