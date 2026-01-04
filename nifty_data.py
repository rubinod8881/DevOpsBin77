import pandas as pd
import mplfinance as mpf
from scipy.signal import argrelextrema
import numpy as np

# 1. Load Data
df = pd.read_excel('nifty_data.xlsx')
df.set_index('Date', inplace=True)

# 2. Automated Support Detection
# Finds local minima within a 20-day window
df['min'] = df.iloc[argrelextrema(df.Low.values, np.less_equal, order=20)[0]]['Low']

# Filter the most significant support level (most touches/recent)
support_level = df['min'].dropna().iloc[-1] 
print(f"Detected Support Level: {support_level}")

# 3. Calculate RSI (14-period)
delta = df['Close'].diff()
gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
rs = gain / loss
df['RSI'] = 100 - (100 / (1 + rs))

# 4. Plotting with Auto-Support
apds = [mpf.make_addplot(df['RSI'], panel=1, color='orange', ylabel='RSI')]

mpf.plot(df, type='candle', style='charles',
         addplot=apds,
         hlines=dict(hlines=[support_level], colors=['white'], linestyle='--'),
         title=f"NIFTY Auto-Analysis (Support at {support_level:.2f})",
         figsize=(12, 8),
         panel_ratios=(2, 1))