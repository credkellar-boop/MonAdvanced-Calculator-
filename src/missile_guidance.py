class MissileGuidanceEngine:
    def __init__(self, navigation_constant: float = 3.0):
        # N' is typically between 3 and 5 for optimal interception
        self.N_prime = navigation_constant

    def proportional_navigation(self, closing_velocity: float, line_of_sight_rate: float) -> float:
        """
        Calculates the lateral acceleration command required to intercept a moving target.
        """
        return self.N_prime * closing_velocity * line_of_sight_rate

    def time_to_intercept(self, distance_to_target: float, closing_velocity: float) -> float:
        """Estimates the remaining time before missile impact."""
        if closing_velocity <= 0:
            return float('inf') # Target is matching speed or pulling away
        return distance_to_target / closing_velocity
