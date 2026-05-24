import mpmath

class InfinitePrecisionCalc:
    def __init__(self, decimal_places=1000):
        # Set the global precision for the environment
        mpmath.mp.dps = decimal_places

    def power(self, base, exponent):
        """Calculates massive exponents without standard float overflow."""
        return mpmath.power(base, exponent)

    def scientific_format(self, number):
        """Formats massive numbers into readable scientific notation."""
        return mpmath.nstr(number, n=15)

if __name__ == "__main__":
    huge_calc = InfinitePrecisionCalc()
    # Calculating an exceptionally massive number
    result = huge_calc.power(10, 33) # 1 Decillion
    print(f"One Decillion: {huge_calc.scientific_format(result)}")