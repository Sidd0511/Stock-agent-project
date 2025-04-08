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
    ticker = Ticker(symbol)
    data = ticker.history(period='1d')
    
    if not data.empty:
        latest_price = data['Close'].iloc[-1]
        return float(latest_price)
    else:
        raise ValueError(f"No price data found for symbol: {symbol}. It may be invalid or the market is closed." )

def get_multiple_stock_prices(symbols: List[str]) -> Tuple[Dict[str, float], List[str]]:
    """
    Fetches the current stock prices for a list of symbols using yfinance.
    
    Args:
        symbols (List[str]): A list of stock symbols to fetch the prices for.
        
    Returns:
        Dict[str, float]: A dictionary mapping each symbol to its current stock price.
    """
    prices = {}
    failed_symbols = [] 

    for symbol in symbols:
        try:
            price = get_stock_price(symbol)
            prices[symbol] = price
        except ValueError as e:
            print(e)
            failed_symbols.append(symbol)
        
    return prices, failed_symbols

