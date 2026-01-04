import yfinance as yf
import pandas as pd
import mplfinance as mpf
import numpy as np

# 1. FETCH DATA (Stable & Reliable)
print("Fetching NIFTY 50 data from Yahoo Finance...")
# ^NSEI is the ticker for NIFTY 50
df = yf.download('^NSEI', period='150d', interval='1d')

# 2. CALCULATE RSI (Wilder's Smoothing)
def calculate_rsi(data, window=14):
    delta = data.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    
    avg_gain = gain.ewm(com=window - 1, min_periods=window).mean()
    avg_loss = loss.ewm(com=window - 1, min_periods=window).mean()
    
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

df['RSI'] = calculate_rsi(df['Close'])

# 3. SIGNAL LOGIC
# Buy when RSI crosses above 30
df['Buy_Signal'] = np.where((df['RSI'] > 30) & (df['RSI'].shift(1) <= 30), df['Low'] * 0.98, np.nan)
# Sell when RSI crosses below 70
df['Sell_Signal'] = np.where((df['RSI'] < 70) & (df['RSI'].shift(1) >= 70), df['High'] * 1.02, np.nan)

# 4. PLOTTING (Exactly like the NSE chart look)
df_plot = df.tail(100)
support_level = 24526

plots = [
    mpf.make_addplot(df_plot['RSI'], panel=1, color='orange', ylabel='RSI'),
    mpf.make_addplot(df_plot['Buy_Signal'], type='scatter', markersize=100, marker='^', color='lime'),
    mpf.make_addplot(df_plot['Sell_Signal'], type='scatter', markersize=100, marker='v', color='red')
]

s = mpf.make_mpf_style(base_mpf_style='charles', facecolor='#131722', edgecolor='white', gridcolor='#2a2e39')

mpf.plot(df_plot, type='candle', style=s, addplot=plots,
         hlines=dict(hlines=[support_level], colors=['white'], linestyle='-.'),
         title='\nNIFTY 50 - Practical Python Analysis',
         figsize=(14, 10), panel_ratios=(2, 1),
         fill_between=dict(y1=70, y2=30, panel=1, color='gray', alpha=0.1))

print("Analysis Complete!")