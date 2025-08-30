# src/utils.py
import numpy as np
import time

def set_seed(seed=42):
    """Set random seed for reproducibility."""
    np.random.seed(seed)

def time_execution(func, *args, **kwargs):
    """Time the execution of a function."""
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    return result, end - start

def pretty_print_results(name, price, elapsed):
    """Print formatted pricing results."""
    print(f"{name} Estimate: {price:.4f} (computed in {elapsed:.4f} seconds)")



