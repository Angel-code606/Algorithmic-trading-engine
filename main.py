from risk_profile import calculate_risk_score
from portfolio_optimizer import optimize_portfolio
from rebalance import rebalance_portfolio
from tax_engine import tax_loss_harvesting
from data import assets, expected_returns, cov_matrix
import numpy as np

# Step 1: Risk Profiling
risk_score = calculate_risk_score(
    age=25,
    income_stability=3,
    investment_horizon=15,
    risk_appetite=3
)

print("Risk Score:", risk_score)

# Step 2: Portfolio Optimization
optimal_weights = optimize_portfolio(expected_returns, cov_matrix)

print("\nRecommended Portfolio Allocation:")
for asset, weight in zip(assets, optimal_weights):
    print(f"{asset}: {round(weight * 100, 2)}%")

# Step 3: Rebalancing
current_weights = np.array([0.40, 0.30, 0.20, 0.10])
new_weights = rebalance_portfolio(current_weights, optimal_weights)

print("\nRebalanced Portfolio:", new_weights)

# Step 4: Tax Harvesting Example
current_prices = {"Equity": 90, "Debt": 105}
purchase_prices = {"Equity": 100, "Debt": 100}

losses = tax_loss_harvesting(current_prices, purchase_prices)
print("\nTax Loss Harvesting Opportunities:", losses)
