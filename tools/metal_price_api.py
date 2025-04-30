import yfinance as yf
from typing import List, Dict, Tuple


def get_usd_to_inr() -> float:
    """
    Fetches the latest USD to INR exchange rate using Yahoo Finance.

    This function retrieves the most recent closing exchange rate for 
    USD to INR by querying the Yahoo Finance API. If no data is available, 
    it raises a ValueError.

    Returns:
        float: The latest closing exchange rate for USD to INR.

    Raises:
        ValueError: If no data is found for the USD to INR conversion.
    """
    usd_inr = yf.Ticker("USDINR=X")
    data = usd_inr.history(period="1d")

    if data.empty:
        raise ValueError("No data found for USD to INR conversion.")

    return data['Close'].iloc[-1]


def get_metal_price(symbol: str) -> float:
    """
    Fetches the current price of a specified metal in Indian Rupees (INR).

    Args:
        symbol (str): The symbol or name of the metal (e.g., 'gold', 'silver', 'platinum', etc.).

    Returns:
        float: The price of the specified metal in INR, rounded to two decimal places.

    Raises:
        ValueError: If the specified metal is not supported or if no data is found for the metal.

    Notes:
        - The function uses Yahoo Finance to fetch the latest price of the metal in USD.
        - The conversion from USD to INR is performed using the `get_usd_to_inr` function.
        - Supported metals and their corresponding Yahoo Finance tickers are:
            - 'gold': 'GC=F'
            - 'silver': 'SI=F'
            - 'platinum': 'PL=F'
            - 'palladium': 'PA=F'
            - 'copper': 'HG=F'
            - 'aluminum': 'ALI=F'
    """
    # Mapping of supported metals to their Yahoo Finance tickers
    metal_symbols = {
        'gold': 'GC=F',
        'silver': 'SI=F',
        'platinum': 'PL=F',
        'palladium': 'PA=F',
        'copper': 'HG=F',
        'aluminum': 'ALI=F',
    }

    # Normalize the input symbol to lowercase
    metal = symbol.lower()

    # Validate if the metal is supported
    if metal not in metal_symbols:
        supported_metals = ', '.join(metal_symbols.keys())
        raise ValueError(f"Unsupported metal: {metal}. Supported metals are: {supported_metals}")

    # Fetch the ticker data from Yahoo Finance
    ticker = yf.Ticker(metal_symbols[metal])
    data = ticker.history(period="1d")

    # Check if data is available
    if data.empty:
        raise ValueError(f"No data found for {metal}.")

    # Get the closing price in USD
    usd_price = data['Close'].iloc[-1]

    # Convert USD price to INR
    usd_to_inr_rate = get_usd_to_inr()
    inr_price = usd_price * usd_to_inr_rate

    # Return the price rounded to two decimal places
    return round(inr_price, 2)


def get_multiple_metal_prices(metals: List[str]) -> Tuple[Dict[str, float], List[str]]:
    """
    Fetches the prices of multiple metals in Indian Rupees (INR).

    Args:
        metals (List[str]): A list of metal symbols or names.

    Returns:
        Tuple[Dict[str, float], List[str]]:
            - A dictionary containing the prices of metals in INR.
            - A list of errors for metals that could not be fetched.

    Notes:
        - The function uses `get_metal_price` to fetch the price of each metal.
        - Errors are logged and returned as part of the result.
    """
    prices = {}
    failed_metals = []

    for metal in metals:
        try:
            prices[metal] = get_metal_price(metal)
        except ValueError as e:
            print(f"[ERROR] {e}")
            failed_metals.append(metal)

    return prices, failed_metals
