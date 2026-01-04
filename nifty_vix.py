import yfinance as yf
import pandas as pd
import mplfinance as mpf
import numpy as np

# 1. Fetch Data (NIFTY 50)
df = yf.download('^NSEI', period='150d', interval='1d')

# 2. RSI Calculation (Same as before)
delta = df['Close'].diff()
gain = delta.clip(lower=0)
loss = -delta.clip(upper=0)
avg_gain = gain.ewm(com=13, min_periods=14).mean()
avg_loss = loss.ewm(com=13, min_periods=14).mean()
df['RSI'] = 100 - (100 / (1 + avg_gain / avg_loss))

# 3. VOLATILITY CALCULATION (20-day Rolling Standard Deviation)
# We calculate log returns first for better statistical accuracy
df['Returns'] = np.log(df['Close'] / df['Close'].shift(1))
df['Volatility'] = df['Returns'].rolling(window=20).std() * np.sqrt(252) * 100 # Annualized %

# 4. PLOTTING (3 Panels: Price, RSI, and Volatility)
df_plot = df.tail(100)

plots = [
    mpf.make_addplot(df_plot['RSI'], panel=1, color='orange', ylabel='RSI'),
    mpf.make_addplot(df_plot['Volatility'], panel=2, color='cyan', ylabel='Vol %'),
]

# Professional Dark Style
s = mpf.make_mpf_style(base_mpf_style='charles', facecolor='#131722', edgecolor='white', gridcolor='#2a2e39')

mpf.plot(df_plot, type='candle', style=s, addplot=plots,
         title='\nNIFTY 50: Price, RSI & Volatility',
         figsize=(14, 12), 
         panel_ratios=(3, 1, 1)) # Price chart gets most space