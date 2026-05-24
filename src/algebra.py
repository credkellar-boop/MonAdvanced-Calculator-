import sympy as sp
import numpy as np

class AdvancedAlgebraEngine:
    def __init__(self):
        pass

    def solve_polynomial(self, expression_str: str, variable: str = 'x') -> list:
        """
        Finds the exact symbolic roots (real and complex) of a polynomial equation.
        Example: "x**2 + 1" returns [I, -I]
        """
        x = sp.Symbol(variable)
        expr = sp.sympify(expression_str)
        return sp.solve(expr, x)

    def calculate_eigen_system(self, matrix_array: list) -> dict:
        """
        Calculates the eigenvalues and eigenvectors of a square matrix.
        Critical for assessing system stability and tensor transformations.
        """
        matrix = sp.Matrix(matrix_array)
        eigenvects = matrix.eigenvects()
        
        results = {}
        for val, mult, vects in eigenvects:
            results[str(val)] = {
                "multiplicity": mult,
                "vectors": [str(v) for v in vects]
            }
        return results

    def matrix_determinant_and_inverse(self, matrix_array: list):
        """Calculates the determinant and inverse of a matrix symbolically."""
        matrix = sp.Matrix(matrix_array)
        det = matrix.det()
        inv = matrix.inv() if det != 0 else None
        return det, inv
