import pandas_datareader.data as web
import pandas as pd
import mplfinance as mpf
import numpy as np
import os
from datetime import datetime, timedelta

# --- 1. CONFIGURATION ---
if not os.path.exists('Nifty_Reports'):
    os.makedirs('Nifty_Reports')

today_str = datetime.now().strftime("%Y-%m-%d")
report_path = f"Nifty_Reports/Nifty_Analysis_{today_str}.png"

# --- 2. STABLE DATA FETCH ---
ticker = "^NSE" 
print("Connecting to Stooq Servers for " + ticker + "...")

end = datetime.now()
# We need at least 300 days of data to calculate a 200-day Moving Average
start = end - timedelta(days=450) 

try:
    df = web.DataReader(ticker, 'stooq', start, end)
    
    if df is None or df.empty:
        print("Initial ticker failed. Trying fallback symbol...")
        df = web.DataReader('NIFTY50.IN', 'stooq', start, end)

    if df is None or df.empty:
        raise ValueError("The server returned no data.")

    df.columns = [col.capitalize() for col in df.columns]
    df = df.sort_index()
    print("Data Downloaded Successfully.")
except Exception as e:
    print("ERROR DURING FETCH: " + str(e))
    exit()

# --- 3. CALCULATIONS ---
# RSI
delta = df['Close'].diff()
gain = delta.clip(lower=0)
loss = -delta.clip(upper=0)
avg_gain = gain.ewm(com=13, min_periods=14).mean()
avg_loss = loss.ewm(com=13, min_periods=14).mean()
df['RSI'] = 100 - (100 / (1 + avg_gain / avg_loss))

# Volatility
df['Returns'] = np.log(df['Close'] / df['Close'].shift(1))
df['Volatility'] = df['Returns'].rolling(window=20).std() * np.sqrt(252) * 100

# 200-Day Moving Average (Trend Filter)
df['SMA200'] = df['Close'].rolling(window=200).mean()

# --- 4. PREPARE PLOT ---
# We only plot the last 100 days for clarity
df_plot = df.tail(100)
current_rsi = round(df_plot['RSI'].iloc[-1], 2)
current_price = df_plot['Close'].iloc[-1]
current_sma = df_plot['SMA200'].iloc[-1]

# Logic for Trend Message
trend_status = "BULLISH" if current_price > current_sma else "BEARISH"

# Define the subplots
plots = [
    mpf.make_addplot(df_plot['SMA200'], color='yellow', width=1.5), # On main panel
    mpf.make_addplot(df_plot['RSI'], panel=1, color='orange', ylabel='RSI'),
    mpf.make_addplot(df_plot['Volatility'], panel=2, color='cyan', ylabel='Vol %')
]

# --- 5. EXECUTE PLOT & SAVE ---
print("Generating Chart. Market is currently: " + trend_status)

s = mpf.make_mpf_style(base_mpf_style='charles', facecolor='#131722', edgecolor='white', gridcolor='#2a2e39')

mpf.plot(df_plot, 
         type='candle', 
         style=s, 
         addplot=plots,
         title=f'\nNIFTY 50: {trend_status} Trend (RSI: {current_rsi})',
         figsize=(14, 12), 
         panel_ratios=(3, 1, 1),
         savefig=report_path)

print("SUCCESS! Final Report saved as: " + report_path)