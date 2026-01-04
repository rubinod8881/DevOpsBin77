import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Strategy Data
df = pd.read_csv('multi_portfolio.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# 2. Calculate Cumulative Returns
returns = df.pct_change().dropna()
cum_returns = (1 + returns).cumprod()

# 3. Calculate "Expert" Metrics
# Sharpe Ratio = (Annual Return / Annual Volatility)
sharpe = (returns.mean() / returns.std()) * (252**0.5)

# 4. Visualization: Strategy Comparison
plt.figure(figsize=(12, 7))

# Plot each strategy
plt.plot(cum_returns['High_Risk'], label=f'High Risk (Sharpe: {sharpe["High_Risk"]:.2f})', color='red', alpha=0.8)
plt.plot(cum_returns['Balanced'], label=f'Balanced (Sharpe: {sharpe["Balanced"]:.2f})', color='blue', linewidth=2)
plt.plot(cum_returns['Safe_Haven'], label=f'Safe Haven (Sharpe: {sharpe["Safe_Haven"]:.2f})', color='green', linestyle='--')

# Adding Professional Labels
plt.title('Investment Strategy Comparison: Risk vs. Reward')
plt.ylabel('Growth of $1')
plt.xlabel('Timeline')
plt.legend(loc='upper left')
plt.grid(True, alpha=0.3)

# 5. Save the Expert Report
plt.savefig('Strategy_Comparison_Report.png', dpi=300)
plt.show()

print("Comparison Complete. Which strategy had the best Sharpe Ratio?")