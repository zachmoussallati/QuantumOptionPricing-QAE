# QuantumOptionPricing-QAE

This repository explores **quantum-inspired amplitude estimation (QAE)** for pricing European call options. It compares QAE-based pricing against a classical Monte Carlo baseline to demonstrate how quantum-inspired techniques can achieve quadratic error reduction in principle.

---

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Objective

* Price European call options using:

  * Classical Monte Carlo (with optional variance reduction).
  * Quantum-inspired amplitude estimation (QAE) emulation on a classical simulator.
* Compare convergence rates and error performance.
* Provide reproducible simulations with clear visualisations and a short demo notebook.

## Features

* Simulates Geometric Brownian Motion (GBM) stock prices.
* Implements classical Monte Carlo pricing (plain + control variates / antithetic sampling optional).
* Implements quantum-inspired amplitude estimation (QAE) emulation.
* Generates plots comparing error vs. sample complexity and convergence behaviour.

## Skills Demonstrated

* Python (NumPy, SciPy, Pandas, Matplotlib)
* Computational finance (option pricing, GBM)
* Quantum computing concepts (QAE, amplitude estimation, error scaling)
* Scientific visualisation and reproducible research

## Repository structure

```
QuantumOptionPricing-QAE/
├── demo/                         # Report, visualisations, derivations, Black–Scholes checks
│   └── notebooks/
│       └── QuantumOptionPricing_QAE_Demo.ipynb
├── src/                          # Source code for pricers and utilities
│   ├── instruments.py            # Option / payoff dataclasses
│   ├── monte_carlo.py            # Classical Monte Carlo pricer and variance-reduction helpers
│   ├── qae_pricing.py            # QAE emulation / wrapper that mimics amplitude estimation
│   └── utils.py                  # GBM sampler, RNG helpers, plotting utilities
├── run_experiments.py            # Script to sweep parameters and reproduce figures
├── requirements.txt              # Python dependencies (pin versions for reproducibility)
├── LICENSE
└── README.md
```

> Note: The demo notebook contains reproducible cells that generate the figures used in the short report.

## Quickstart

1. Create a virtual environment (recommended) and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate      # macOS / Linux
.\.venv\Scripts\activate     # Windows (PowerShell)
pip install -r requirements.txt
```

2. Run the demo notebook (recommended for first look):

```bash
jupyter notebook demo/notebooks/QuantumOptionPricing_QAE_Demo.ipynb
```

3. Or run the experiments script to reproduce core results and save figures locally:

```bash
python run_experiments.py --output-dir results/ --n-repeats 50
```

## Example usage (from Python)

```python
from src.instruments import EuropeanCall
from src.monte_carlo import monte_carlo_price
from src.qae_pricing import qae_emulation_price

# define option
opt = EuropeanCall(S0=100, K=110, T=1.0, r=0.01, sigma=0.2)

# classical estimate
mc_price, mc_std = monte_carlo_price(opt, n_samples=100_000)

# QAE-emulated estimate (runs classical emulation routine)
qae_price, qae_conf = qae_emulation_price(opt, n_shots=1024, n_iterations=6)

print(f"MC: {mc_price:.6f} ± {mc_std:.6f}\nQAE (emulated): {qae_price:.6f} ± {qae_conf:.6f}")
```

## Reproducibility

* Seed RNGs where appropriate (see `src/utils.py`) and pin package versions in `requirements.txt` for deterministic experiments.
* Use `--output-dir` with `run_experiments.py` to collect figures and raw results for later analysis.

## Development & Tests

* Install development extras (if provided in `requirements-dev.txt`) and run unit tests:

```bash
pip install -r requirements-dev.txt
pytest -q
```

* Linting: `flake8 src/` (optional)

## Contributing

Contributions are welcome. Please open an issue for discussion before implementing large features. Small fixes may be submitted as pull requests.

## License

This project is released under the MIT License. See `LICENSE` for details.

---

If you'd like, I can also:

* generate a `.gitignore` and `requirements.txt` template,
* add a lightweight GitHub Actions workflow to run tests on push,
* or produce the demo notebook skeleton used by the README.

