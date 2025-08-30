# src/instruments.py
class EuropeanCallOption:
    """
    Simple data structure for a European Call Option.
    """

    def __init__(self, S0, K, T, r, sigma):
        self.S0 = S0
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma

    def summary(self):
        """Return a dictionary summary of option parameters."""
        return {
            "Initial Price (S0)": self.S0,
            "Strike (K)": self.K,
            "Maturity (T, years)": self.T,
            "Risk-free Rate (r)": self.r,
            "Volatility (sigma)": self.sigma,
        }
