import pandas as pd
import mplfinance as mpf
import numpy as np
import requests
from datetime import date, timedelta

# 1. ROBUST DATA FETCH FUNCTION
def fetch_nifty_history(days=150):
    # Standard browser headers to avoid being blocked
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "accept-language": "en-GB,en;q=0.9",
        "accept-encoding": "gzip, deflate, br",
    }
    
    session = requests.Session()
    # Step A: 'Wake up' the session by visiting the home page to get cookies
    session.get("https://www.nseindia.com", headers=headers, timeout=10)
    
    # Step B: Request the specific historical data
    end_date = date.today().strftime("%d-%m-%Y")
    start_date = (date.today() - timedelta(days=days)).strftime("%d-%m-%Y")
    
    # URL for NIFTY 50 Index history
    url = f"https://www.nseindia.com/api/historical/indicesHistory?indexType=NIFTY%2050&from={start_date}&to={end_date}"
    
    response = session.get(url, headers=headers, timeout=10)
    
    if response.status_code == 200:
        data = response.json()
        # Navigate the JSON structure correctly
        df = pd.DataFrame(data['data']['indexCloseOnlineRecords'])
        return df
    else:
        raise Exception(f"NSE Server returned status code: {response.status_code}")

# 2. RUN THE PROCESS
try:
    print("Connecting to NSE...")
    raw_df = fetch_nifty_history(150)
    
    # Map the specific NSE JSON keys to OHLC format
    df = raw_df[['EOD_TIMESTAMP', 'EOD_OPEN_INDEX_VAL', 'EOD_HIGH_INDEX_VAL', 'EOD_LOW_INDEX_VAL', 'EOD_CLOSE_INDEX_VAL']]
    df.columns = ['Date', 'Open', 'High', 'Low', 'Close']
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date').set_index('Date').astype(float)
    
    print("Success! Data received.")

    # 3. CALCULATE RSI (14 period)
    delta = df['Close'].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(com=13, min_periods=14).mean()
    avg_loss = loss.ewm(com=13, min_periods=14).mean()
    df['RSI'] = 100 - (100 / (1 + avg_gain / avg_loss))

    # 4. PLOTTING (Exactly like the NIFTY chart in your image)
    df_plot = df.tail(100)
    # Target support line from your image
    support_val = 24526 
    
    rsi_plot = mpf.make_addplot(df_plot['RSI'], panel=1, color='orange', ylabel='RSI')
    
    # Dark theme style
    s = mpf.make_mpf_style(base_mpf_style='charles', facecolor='#131722', edgecolor='white', gridcolor='#2a2e39')

    mpf.plot(df_plot, type='candle', style=s, addplot=rsi_plot,
             hlines=dict(hlines=[support_val], colors=['white'], linestyle='-.'),
             title='\nNIFTY 50 Technical Analysis',
             figsize=(12, 8), panel_ratios=(2, 1))

except Exception as e:
    print(f"FAILED: {e}")