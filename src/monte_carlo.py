# src/monte_carlo.py
import numpy as np

class MonteCarloPricer:
    """
    Monte Carlo pricer for European call options.
    """

    def __init__(self, S0, K, T, r, sigma, n_simulations=100000):
        self.S0 = S0
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.n_simulations = n_simulations

    def simulate(self):
        """
        Simulate asset prices at maturity and compute payoff.
        """
        Z = np.random.standard_normal(self.n_simulations)
        ST = self.S0 * np.exp(
            (self.r - 0.5 * self.sigma**2) * self.T + self.sigma * np.sqrt(self.T) * Z
        )
        payoff = np.maximum(ST - self.K, 0)
        return np.exp(-self.r * self.T) * np.mean(payoff)
