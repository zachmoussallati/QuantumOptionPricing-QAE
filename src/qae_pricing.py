# src/qae_pricing.py

import numpy as np

class SimulatedQAEPricer:
    """
    Simulated Quantum Amplitude Estimation (QAE) for European Call Option.
    Uses a classical probabilistic simulation to mimic QAE behaviour.
    """

    def __init__(self, S0, K, T, r, sigma, num_qubits=3, n_shots=10000):
        self.S0 = S0
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.num_qubits = num_qubits  # used to scale precision
        self.n_shots = n_shots        # total number of “quantum measurements”

    def price(self):
        """
        Simulate QAE to compute European Call Option price.
        Returns a float price.
        """
        # Simulate a discretized log-normal distribution
        mu = (self.r - 0.5 * self.sigma**2) * self.T
        sigma = self.sigma * np.sqrt(self.T)
        low, high = 0, 2 * self.S0

        # Discretize the probability space into 2^num_qubits points
        n_points = 2 ** self.num_qubits
        prices = np.linspace(low, high, n_points)
        probs = (1 / (prices * sigma * np.sqrt(2 * np.pi))) * \
                np.exp(-((np.log(prices / self.S0) - mu) ** 2) / (2 * sigma ** 2))
        probs = np.nan_to_num(probs)  # avoid NaNs for prices=0
        probs /= probs.sum()  # normalize

        # Monte Carlo sampling to mimic amplitude estimation
        sampled_indices = np.random.choice(n_points, size=self.n_shots, p=probs)
        sampled_prices = prices[sampled_indices]
        payoff = np.maximum(sampled_prices - self.K, 0)
        discounted_payoff = np.exp(-self.r * self.T) * payoff.mean()

        return discounted_payoff










