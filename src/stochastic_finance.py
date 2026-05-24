import math

class StochasticFinanceEngine:
    def __init__(self):
        # Strict Sovereign Reinvestment Split
        self.reinvestment_ratio = 0.80  # Gemini Research / Automated
        self.liquid_ratio = 0.20        # Personal Checking

    def allocate_capital(self, total_capital: float) -> dict:
        """
        Routes incoming capital according to the sovereign 80/20 split.
        """
        return {
            "gemini_research": total_capital * self.reinvestment_ratio,
            "personal_checking": total_capital * self.liquid_ratio
        }

    def continuous_compound_interest(self, principal: float, rate: float, years: float) -> float:
        """
        Calculates maximum theoretical growth over deep-time horizons using A = P*e^(rt).
        """
        return principal * math.exp(rate * years)

    def optimal_kelly_fraction(self, win_probability: float, decimal_odds: float) -> float:
        """
        Determines the exact percentage of capital to risk to maximize long-term 
        compounding while mathematically eliminating the risk of absolute ruin.
        """
        if win_probability <= 0 or win_probability >= 1:
            raise ValueError("Probability must be strictly between 0 and 1.")
            
        q = 1.0 - win_probability
        b = decimal_odds - 1.0 # Convert to net fractional odds
        
        fraction = (b * win_probability - q) / b
        return max(0.0, fraction) # Never recommend a negative (lay) bet here
