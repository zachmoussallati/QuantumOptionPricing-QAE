# QuantumOptionPricing-QAE

This project explores **quantum-inspired amplitude estimation (QAE)** for pricing European options.  
It compares QAE-based pricing against a classical Monte Carlo baseline to demonstrate how quantum techniques can achieve **quadratic error reduction** in principle.

---

## 🎯 Objective
- Price European call options using:
  - **Classical Monte Carlo** (with variance reduction).
  - **Quantum-inspired amplitude estimation (QAE)**.
- Compare convergence rates and error performance.
- Provide reproducible simulations with clear visualisations.

---

## ✨ Features
- Simulates **Geometric Brownian Motion (GBM)** stock prices.
- Implements **classical Monte Carlo with antithetic variates**.
- Implements **quantum-inspired amplitude estimation (QAE) emulation**.
- Generates **plots comparing error vs. sample complexity**.

---

## 🛠️ Skills Demonstrated
- **Python** (NumPy, SciPy, Pandas, Matplotlib)
- **Computational finance** (option pricing, GBM modelling)
- **Quantum computing concepts** (QAE, error scaling)
- **Scientific visualisation** and reproducible research

---

## 🚀 Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/zachmoussallati/QuantumOptionPricing-QAE.git
   cd QuantumOptionPricing-QAE

## Install dependencies:

pip install -r requirements.txt


## Run the demo notebook:

jupyter notebook


## Project Structure
```
QuantumOptionPricing-QAE/
├── notebooks/                # Jupyter notebooks for demos
├── src/                      # Source code
│   ├── instruments.py        # Option and market data classes
│   ├── monte_carlo.py        # Classical Monte Carlo pricer
│   ├── qae_pricing.py        # Quantum-inspired amplitude estimation pricer
│   └── utils.py              # Helper functions
├── run_experiments.py        # Script to run simulations
├── requirements.txt          # Dependencies
└── README.md                 # Project documentation
```

## Results

- Monte Carlo: Error decreases as O(1/√N) with the number of samples.

- QAE (simulated): Error decreases as O(1/N), showing the quadratic speedup expected from quantum algorithms.




