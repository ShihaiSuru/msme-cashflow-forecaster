#!/usr/bin/env python3
"""Simple cash flow forecaster for MSMEs."""

def forecast_cashflow(opening_balance, inflows, outflows, days=30):
    balance = opening_balance
    projection = []
    for day in range(1, days + 1):
        daily_in = inflows.get(day, 0)
        daily_out = outflows.get(day, 0)
        balance += daily_in - daily_out
        projection.append((day, balance))
        if balance < 0:
            print(f"Warning: Shortfall on day {day}: {balance}")
    return projection

if __name__ == "__main__":
    sample_in = {1: 50000, 15: 75000}
    sample_out = {5: 20000, 10: 30000, 20: 15000}
    result = forecast_cashflow(100000, sample_in, sample_out)
    print("30-day projection (day, balance):")
    for day, bal in result:
        print(f"Day {day}: ₹{bal:,.0f}")
