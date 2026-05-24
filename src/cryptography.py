import sympy
import hashlib
import secrets

class SovereignCryptoEngine:
    def __init__(self):
        # Secp256k1 curve parameters (Bitcoin/Ethereum standard)
        self.p = 2**256 - 2**32 - 977
        self.a = 0
        self.b = 7

    def generate_large_prime(self, bit_length: int = 2048) -> int:
        """
        Generates a cryptographically secure random prime number.
        Crucial for RSA and Black Folder foundational encryption.
        """
        while True:
            # Generate a random number of the specified bit length
            num = secrets.randbits(bit_length)
            # Ensure it is odd and has the highest bit set
            num |= (1 << (bit_length - 1)) | 1
            if sympy.isprime(num):
                return num

    def is_point_on_curve(self, x: int, y: int) -> bool:
        """
        Verifies if a specific coordinate lies on the elliptic curve.
        """
        left = (y ** 2) % self.p
        right = (x ** 3 + self.a * x + self.b) % self.p
        return left == right

    def sha256_hash(self, data_string: str) -> str:
        """Generates a deterministic 256-bit hash for data verification."""
        return hashlib.sha256(data_string.encode('utf-8')).hexdigest()
