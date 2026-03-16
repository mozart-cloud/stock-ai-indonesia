import os
import pandas as pd
import yfinance as yf

from config import UNIVERSE_FILE, PRICE_DATA_FOLDER


def load_universe():
    df = pd.read_csv(UNIVERSE_FILE)
    return df["ticker"].dropna().tolist()


def download_price_data(ticker, start_date="2010-01-01"):
    print(f"Downloading {ticker}...")
    data = yf.download(ticker, start=start_date, auto_adjust=False)

    if data.empty:
        print(f"No data for {ticker}")
        return

    filename = ticker.replace(".JK", "") + ".csv"
    output_path = os.path.join(PRICE_DATA_FOLDER, filename)

    os.makedirs(PRICE_DATA_FOLDER, exist_ok=True)
    data.to_csv(output_path)

    print(f"Saved to {output_path}")


def main():
    tickers = load_universe()

    for ticker in tickers:
        download_price_data(ticker)


if __name__ == "__main__":
    main()
