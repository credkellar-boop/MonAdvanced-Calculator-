import scipy.constants as const

class NuclearAlchemyEngine:
    def __init__(self):
        self.c = const.c # Speed of light
        self.m_p = const.m_p # Mass of proton in kg
        self.m_n = const.m_n # Mass of neutron in kg
        self.eV_to_Joules = const.e # 1 eV in Joules

    def calculate_mass_defect(self, protons: int, neutrons: int, actual_mass_kg: float) -> float:
        """
        Calculates the missing mass (mass defect) that was converted into binding energy.
        """
        predicted_mass = (protons * self.m_p) + (neutrons * self.m_n)
        return predicted_mass - actual_mass_kg

    def calculate_binding_energy(self, mass_defect_kg: float) -> float:
        """
        Returns the nuclear binding energy in Joules using E = mc^2.
        """
        return mass_defect_kg * (self.c ** 2)

    def q_value_transmutation(self, mass_reactants_kg: float, mass_products_kg: float) -> float:
        """
        Calculates the Q-value (energy released or absorbed) during a nuclear reaction.
        Positive Q means exothermic (releases energy), negative means endothermic.
        """
        mass_diff = mass_reactants_kg - mass_products_kg
        return mass_diff * (self.c ** 2)
