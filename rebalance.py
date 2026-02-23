import numpy as np

def rebalance_portfolio(current_weights, target_weights, threshold=0.05):
    """
    Rebalance only if deviation exceeds threshold
    """
    deviation = np.abs(current_weights - target_weights)

    if any(deviation > threshold):
        return target_weights
    else:
        return current_weights
