class AtomicLedger:
    def __init__(self):
        # A foundational dataset of elements. 
        # (Expanded to all 118 elements in full deployment)
        self.elements = {
            1: {"symbol": "H", "name": "Hydrogen", "mass_u": 1.008, "density_kg_m3": 0.08988},
            2: {"symbol": "He", "name": "Helium", "mass_u": 4.0026, "density_kg_m3": 0.1786},
            6: {"symbol": "C", "name": "Carbon", "mass_u": 12.011, "density_kg_m3": 2267.0}, # Graphite
            8: {"symbol": "O", "name": "Oxygen", "mass_u": 15.999, "density_kg_m3": 1.429},
            14: {"symbol": "Si", "name": "Silicon", "mass_u": 28.085, "density_kg_m3": 2329.0},
            22: {"symbol": "Ti", "name": "Titanium", "mass_u": 47.867, "density_kg_m3": 4506.0},
            26: {"symbol": "Fe", "name": "Iron", "mass_u": 55.845, "density_kg_m3": 7874.0},
            74: {"symbol": "W", "name": "Tungsten", "mass_u": 183.84, "density_kg_m3": 19250.0},
            79: {"symbol": "Au", "name": "Gold", "mass_u": 196.97, "density_kg_m3": 19300.0},
            92: {"symbol": "U", "name": "Uranium", "mass_u": 238.03, "density_kg_m3": 19050.0}
        }

    def get_element_by_atomic_number(self, z: int) -> dict:
        """Retrieves absolute properties of an element by its proton count."""
        return self.elements.get(z, "Element not found in base ledger.")

    def calculate_moles(self, mass_kg: float, atomic_number: int) -> float:
        """Calculates the number of moles in a given mass of an element."""
        element = self.get_element_by_atomic_number(atomic_number)
        if isinstance(element, str):
            raise ValueError(element)
        
        # Convert kg to grams, then divide by atomic mass (u ≈ g/mol)
        mass_g = mass_kg * 1000
        return mass_g / element["mass_u"]
