import pandas as pd
import numpy as np

# 100 days of data for 3 different asset classes
np.random.seed(42)
dates = pd.date_range(start='2025-01-01', periods=100)

# High Risk (Tech: Volatile but high growth)
tech = 100 * np.cumprod(1 + np.random.normal(0.002, 0.03, 100))
# Balanced (Index: Moderate growth)
balanced = 100 * np.cumprod(1 + np.random.normal(0.001, 0.015, 100))
# Safe (Gold: Low growth, low risk)
safe = 100 * np.cumprod(1 + np.random.normal(0.0005, 0.008, 100))

df = pd.DataFrame({'Date': dates, 'High_Risk': tech, 'Balanced': balanced, 'Safe_Haven': safe})
df.to_csv('multi_portfolio.csv', index=False)
print("Strategy dataset 'multi_portfolio.csv' is ready!")