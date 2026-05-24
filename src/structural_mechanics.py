import math

class StructuralMechanicsEngine:
    def __init__(self):
        # Gravitational baseline (Earth standard, override for exoplanets)
        self.gravity = 9.80665 

    def calculate_axial_stress(self, force_newtons: float, area_sq_meters: float) -> float:
        """
        Calculates the internal stress (in Pascals) a structural beam experiences 
        under a given load.
        """
        if area_sq_meters <= 0:
            raise ValueError("Cross-sectional area must be strictly positive.")
        return force_newtons / area_sq_meters

    def calculate_strain(self, change_in_length: float, original_length: float) -> float:
        """
        Calculates the physical deformation (strain) of a material. 
        Strain is a dimensionless ratio.
        """
        return change_in_length / original_length

    def youngs_modulus_check(self, stress_pa: float, strain: float, material_yield_strength_pa: float) -> dict:
        """
        Evaluates material elasticity and checks for catastrophic structural failure.
        """
        if strain == 0:
            return {"modulus": float('inf'), "status": "NO DEFORMATION"}
            
        modulus = stress_pa / strain
        
        if stress_pa > material_yield_strength_pa:
            status = "FAILURE IMMINENT: Material has passed its yield strength."
        else:
            status = "STABLE: Deformation is strictly elastic."
            
        return {
            "youngs_modulus_pa": modulus,
            "structural_status": status
        }

    def maximum_beam_deflection(self, load_newtons: float, length_meters: float, youngs_modulus: float, area_moment_of_inertia: float) -> float:
        """
        Calculates the maximum bend (deflection) at the center of a simply supported 
        beam under a concentrated central point load.
        Formula: delta = (F * L^3) / (48 * E * I)
        """
        numerator = load_newtons * (length_meters ** 3)
        denominator = 48 * youngs_modulus * area_moment_of_inertia
        return numerator / denominator
