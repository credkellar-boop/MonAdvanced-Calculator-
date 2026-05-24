import numpy as np
import scipy.constants as const

class QuantumMechanicsEngine:
    def __init__(self):
        self.hbar = const.hbar # Reduced Planck constant

    def qubit_superposition(self, alpha: complex, beta: complex) -> np.ndarray:
        """
        Defines the state vector of a single qubit. 
        Ensures the probabilities (|alpha|^2 + |beta|^2) sum perfectly to 1.
        """
        state = np.array([alpha, beta])
        magnitude = np.linalg.norm(state)
        
        if not np.isclose(magnitude, 1.0):
            # Normalize the state vector if it is imperfect
            state = state / magnitude
            
        return state

    def apply_hadamard_gate(self, state_vector: np.ndarray) -> np.ndarray:
        """
        Applies the Hadamard transformation matrix to place a deterministic 
        qubit into a perfect, equal superposition of states.
        """
        hadamard_matrix = (1 / np.sqrt(2)) * np.array([
            [1,  1],
            [1, -1]
        ])
        return np.dot(hadamard_matrix, state_vector)

    def calculate_photon_energy(self, frequency_hz: float) -> float:
        """E = h * nu. Calculates exact quantum energy levels."""
        return const.h * frequency_hz
