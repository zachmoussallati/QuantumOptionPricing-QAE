# QuantumOptionPricing-QAE

This project explores **quantum-inspired amplitude estimation (QAE)** for pricing European call options.  
It compares QAE-based pricing against a classical Monte Carlo baseline to demonstrate how quantum-inspired techniques can achieve quadratic error reduction in principle.

## Objective
- Price European call options using:
  - Classical Monte Carlo (with optional variance reduction).
  - Quantum-inspired amplitude estimation (QAE) emulation.
- Compare convergence rates and error performance.
- Provide reproducible simulations with clear visualisations.

## Features
- Simulates Geometric Brownian Motion (GBM) stock prices.
- Implements classical Monte Carlo pricing.
- Implements quantum-inspired amplitude estimation (QAE) emulation on a classical simulator.
- Generates plots comparing error vs. sample complexity.

## Skills Demonstrated
- Python (NumPy, SciPy, Pandas, Matplotlib)
- Computational finance (option pricing, GBM)
- Quantum computing concepts (QAE, error scaling)
- Scientific visualisation and reproducible research

## Project Structure
QuantumOptionPricing-QAE/
├── demo (report, visualisations, derivations, and Black-Scholes Model)
├── src/ # Source code for pricers and utilities
│ ├── instruments.py
│ ├── monte_carlo.py
│ ├── qae_pricing.py
│ └── utils.py
├── run_experiments.py # Script to run simulations
├── requirements.txt # Python dependencies
└── README.md


## Usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
2. Run the demo notebook:
  jupyter notebook notebooks/QuantumOptionPricing_QAE_Demo.ipynb
3. Or run the experiments script:
  python run_experiments.py

License

MIT License

