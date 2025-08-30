# QuantumOptionPricing-QAE

This project explores **quantum-inspired amplitude estimation (QAE)** for pricing European options.  
It compares QAE-based pricing against a classical Monte Carlo baseline to demonstrate how quantum techniques can achieve quadratic error reduction in principle.

## Objective
- Price European call options using:
  - Classical Monte Carlo (with variance reduction).
  - Quantum-inspired amplitude estimation (QAE).
- Compare convergence rates and error performance.
- Provide reproducible simulations with clear visualisations.

## Features
- Simulates Geometric Brownian Motion (GBM) stock prices.
- Implements classical Monte Carlo with antithetic variates.
- Implements quantum-inspired amplitude estimation (QAE) emulation.
- Generates plots comparing error vs sample complexity.

## Skills Demonstrated
- Python (NumPy, SciPy, Pandas, Matplotlib)
- Computational finance (option pricing, GBM)
- Quantum computing concepts (QAE, error scaling)
- Scientific visualisation and reproducible research

## Usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt

