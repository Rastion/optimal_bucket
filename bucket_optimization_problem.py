from qubots.base_problem import BaseProblem
import math
import random

class BucketOptimizationProblem(BaseProblem):
    """
    Bucket Optimization Problem for Qubots.
    
    Given a flat disc of material of area π, design a bucket (defined by bottom radius r,
    top opening radius R, and height h) so that the total surface area used does not exceed π.
    The surface area is:
    
        S = π * r² + π*(R + r)*sqrt((R - r)² + h²)
    
    and the volume is:
    
        V = (π * h)/3 * (R² + R*r + r²).
    
    The goal is to maximize the bucket's volume.
    """
    
    def __init__(self, **kwargs):
        self.PI = 3.14159265359
        # Available material surface area is π.
        self.available_surface = self.PI
    
    def evaluate_solution(self, solution) -> float:
        """
        Evaluates a candidate solution.
        
        Expects:
          solution: a dictionary with keys "R", "r", and "h" (all floats between 0 and 1).
        
        Returns:
          The volume of the bucket if the surface area constraint is satisfied;
          otherwise, returns a high negative penalty.
        """
        R = solution.get("R", 0)
        r = solution.get("r", 0)
        h = solution.get("h", 0)
        # Compute surface area used.
        surface = self.PI * r**2 + self.PI * (R + r) * math.sqrt((R - r)**2 + h**2)
        if surface > self.available_surface:
            # Infeasible solution.
            return -1e9
        # Compute volume.
        volume = self.PI * h / 3 * (R**2 + R*r + r**2)
        return volume
    
    def random_solution(self):
        """
        Generates a random candidate solution.
        
        Returns a dictionary with random values for R, r, and h in [0, 1].
        """
        return {
            "R": random.uniform(0, 1),
            "r": random.uniform(0, 1),
            "h": random.uniform(0, 1)
        }
