from yfinance import Ticker
from datetime import datetime
from typing import List, Dict, Tuple

def get_stock_price(symbol:str) -> float:
    """
    Fetches the current stock price for a given symbol using yfinance.
    
    Args:
        symbol (str): The stock symbol to fetch the price for.
        
    Returns:
        float: The current stock price.
    """
    # Create a Ticker object for the given symbol
    ticker = Ticker(symbol)
    # Fetch the historical market data for the last day
    # Note: yfinance may return empty data if the market is closed or the symbol is invalid
    # We use '1d' to get the latest available data
    # This will return the last available price even if the market is closed
    data = ticker.history(period='1d')
    
    # Check if the data is empty
    if not data.empty:
        latest_price = data['Close'].iloc[-1]
        return float(latest_price)
    else:
        raise ValueError(f"No price data found for symbol: {symbol}. It may be invalid or the market is closed." )


def get_multiple_stock_prices(symbols: List[str]) -> Tuple[Dict[str, float], List[str]]:
    """
    Fetches the current stock prices for a list of symbols.
    Args:
        symbols (List[str]): A list of stock symbols to fetch prices for.
    Returns:
        Tuple[Dict[str, float], List[str]]: A tuple containing a dictionary of stock prices and a list of symbols that failed to fetch.
    """ 
    prices = {}
    failed_symbols = [] 

    # Iterate over the list of symbols and fetch their prices
    for symbol in symbols:
        try:
            price = get_stock_price(symbol)
            prices[symbol] = price
        except ValueError as e:
            print(e)
            failed_symbols.append(symbol)
        
    return prices, failed_symbols

