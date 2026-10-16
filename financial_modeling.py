#!/usr/bin/env python3
"""Financial modeling techniques for MSME cash flow."""
import numpy as np
from numpy_financial import npv, irr

def calculate_npv(cashflows, rate=0.12):
    """Net Present Value of a series of cash flows."""
    return npv(rate, cashflows)

def calculate_irr(cashflows):
    """Internal Rate of Return."""
    return irr(cashflows)

def sensitivity_analysis(base_cashflows, rate_range=None):
    """Simple sensitivity of NPV to discount rate."""
    if rate_range is None:
        rate_range = np.linspace(0.08, 0.18, 6)
    results = {}
    for r in rate_range:
        results[round(r, 2)] = calculate_npv(base_cashflows, r)
    return results

if __name__ == "__main__":
    # Example: initial investment + 5 years of cash flows
    cfs = [-200000, 50000, 60000, 70000, 80000, 90000]
    print(f"NPV @ 12%: ₹{calculate_npv(cfs):,.0f}")
    print(f"IRR: {calculate_irr(cfs)*100:.1f}%")
    print("Sensitivity (rate -> NPV):", sensitivity_analysis(cfs))
