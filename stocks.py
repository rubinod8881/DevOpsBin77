import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Define your portfolio
tickers = ['AAPL', 'MSFT', 'GOOGL', 'SPY']
data = yf.download(tickers, start="2023-01-01", end="2023-12-31")['Adj Close']

# Calculate daily returns
returns = data.pct_change()

# Calculate cumulative returns
cumulative_returns = (1 + returns).cumprod()

# Plotting the growth of a $1 investment
cumulative_returns.plot(figsize=(10, 6))
plt.title("Portfolio Growth: 2023")
plt.ylabel("Value of $1 Investment")
plt.grid(True)
plt.show()

# Calculate Annualized Volatility
volatility = returns.std() * (252**0.5)
print(f"Annualized Volatility:\n{volatility}")
