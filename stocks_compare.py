import pandas as pd
import matplotlib.pyplot as plt

# Load the local data we just made
try:
    df = pd.read_csv('my_stocks.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

    # 1. Calculate Daily Returns (Standard Financial Practice)
    returns = df.pct_change().dropna()

    # 2. Portfolio Comparison: Tech (AAPL+MSFT) vs Gold
    tech_portfolio = (1 + returns[['AAPL', 'MSFT']].mean(axis=1)).cumprod()
    gold_portfolio = (1 + returns['GOLD']).cumprod()

    # 3. Visualization
    plt.figure(figsize=(10, 5))
    plt.plot(tech_portfolio, label='Tech Portfolio (AAPL/MSFT)', color='blue', marker='o')
    plt.plot(gold_portfolio, label='Safe Haven (Gold)', color='orange', marker='s')

    plt.title('Portfolio Analysis: Growth of $1 Investment')
    plt.ylabel('Cumulative Return ($)')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    print("Analysis Complete: Portfolio Chart Displayed.")

except Exception as e:
    print(f"Error: {e}")
    
# 1. Load your local data
df = pd.read_csv('my_stocks.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# 2. Calculate Daily Returns
returns = df.pct_change().dropna()

# 3. Create Portfolios
tech_returns = returns[['AAPL', 'MSFT']].mean(axis=1)
gold_returns = returns['GOLD']

# --- EXPERT ANALYSIS SECTION ---

# A. Calculate Total Profit Percentage
tech_total_return = ( (1 + tech_returns).prod() - 1 ) * 100
gold_total_return = ( (1 + gold_returns).prod() - 1 ) * 100

# B. Calculate Risk (Standard Deviation of Daily Returns)
# Higher number = higher risk
tech_risk = tech_returns.std() * 100
gold_risk = gold_returns.std() * 100

print("--- PORTFOLIO PERFORMANCE REPORT ---")
print(f"Tech Portfolio Profit: {tech_total_return:.2f}%")
print(f"Tech Daily Risk:      {tech_risk:.2f}%")
print("-" * 35)
print(f"Gold Portfolio Profit: {gold_total_return:.2f}%")
print(f"Gold Daily Risk:      {gold_risk:.2f}%")