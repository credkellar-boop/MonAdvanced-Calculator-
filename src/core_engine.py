import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

class AdvancedCalculator:
    def __init__(self):
        # Allow implicit multiplication (e.g., "2x" becomes "2*x")
        self.transformations = standard_transformations + (implicit_multiplication_application,)

    def evaluate(self, expression_str: str, **kwargs):
        """
        Evaluates a string expression safely and returns the exact mathematical result.
        Example: "integrate(x**2, x)" -> "x**3/3"
        """
        try:
            # Parse the string into a SymPy expression
            expr = parse_expr(expression_str, transformations=self.transformations)
            
            # Substitute any provided variables
            if kwargs:
                expr = expr.subs(kwargs)
                
            # Simplify and return
            result = sp.simplify(expr)
            return result
        except Exception as e:
            return f"Error evaluating expression: {str(e)}"

    def calculate_derivative(self, expression_str: str, variable: str):
        """Calculates the derivative of an expression with respect to a variable."""
        x = sp.Symbol(variable)
        expr = parse_expr(expression_str, transformations=self.transformations)
        return sp.diff(expr, x)

    def calculate_integral(self, expression_str: str, variable: str):
        """Calculates the indefinite integral of an expression."""
        x = sp.Symbol(variable)
        expr = parse_expr(expression_str, transformations=self.transformations)
        return sp.integrate(expr, x)

# --- Usage Example ---
if __name__ == "__main__":
    calc = AdvancedCalculator()
    
    print("Expression: 2*pi + 3*pi")
    print("Result:", calc.evaluate("2*pi + 3*pi"))  # Output: 5*pi
    
    print("\nCalculus: Derivative of sin(x)*exp(x)")
    print("Result:", calc.calculate_derivative("sin(x)*exp(x)", "x"))