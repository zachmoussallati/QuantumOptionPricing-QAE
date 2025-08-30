from src.instruments import EuropeanCallOption
from src.monte_carlo import MonteCarloPricer
from src.qae_pricing import SimulatedQAEPricer
from src.utils import set_seed, time_execution, pretty_print_results

# Fix random seed for reproducibility
set_seed(123)

# Define an example European Call option
option = EuropeanCallOption(
    S0=100,   # initial stock price
    K=105,    # strike
    T=1.0,    # maturity in years
    r=0.05,   # risk-free rate
    sigma=0.2 # volatility
)

print("Option Parameters:")
print(option.summary())
print("-" * 40)

# Classical Monte Carlo pricing
mc_pricer = MonteCarloPricer(option.S0, option.K, option.T, option.r, option.sigma, n_simulations=5000)
mc_price, mc_time = time_execution(mc_pricer.simulate)
pretty_print_results("Monte Carlo", mc_price, mc_time)

# Simulated QAE pricing
sim_qae_pricer = SimulatedQAEPricer(option.S0, option.K, option.T, option.r, option.sigma, num_qubits=5, n_shots=10000)
qae_price, qae_time = time_execution(sim_qae_pricer.price)
pretty_print_results("Simulated QAE", qae_price, qae_time)

