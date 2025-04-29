from crewai import Agent
from tools.stock_price_api import get_multiple_stock_prices
from typing import List, Dict


# class StockTrackerAgent:
#     """
#     A class to represent a stock tracking agent.

#     This agent is responsible for fetching the latest stock prices for user-specified symbols.
#     It uses an external API to retrieve stock prices and provides verbose logging if enabled.
#     """

#     def __init__(self, verbose: bool = True):
#         """
#         Initialize the StockTrackerAgent.

#         Args:
#             verbose (bool): If True, enables verbose logging. Defaults to True.
#         """
#         self.name = "Stock Tracker Agent"
#         self.role = "Tracks stock prices for user specified symbols."
#         self.goal = " Fetch the latest stock prices."
#         self.verbose = verbose

#     def run(self, symbols: List[str]) -> Dict[str, float]:
#         """
#         Fetch the latest stock prices for the given symbols.

#         Args:
#             symbols (List[str]): A list of stock symbols to fetch prices for.

#         Returns:
#             Dict[str, float]: A dictionary containing:
#                 - "prices": A dictionary of stock symbols and their corresponding prices.
#                 - "failed": A list of stock symbols for which prices could not be fetched.
#         """
#         prices, failed = get_multiple_stock_prices(symbols)

#         if self.verbose:
#             if prices:
#                 print(f"[INFO] Fetched stock prices: {list(prices.keys())}")
#             if failed:
#                 print(f"[WARNING] Could not fetch prices for: {failed}")

#         return {
#             "prices": prices,
#             "failed": failed
#         }


def track_stock_prices_tool(symbols: List[str]) -> Dict[str, float]:
    """
    Fetch the latest stock prices for a list of stock symbols.

    This function uses an external API to retrieve stock prices for the provided symbols.
    It logs information about successfully fetched prices and warnings for any symbols
    that could not be fetched.

    Args:
        symbols (List[str]): A list of stock symbols to fetch prices for.

    Returns:
        Dict[str, float]: A dictionary containing:
            - "prices": A dictionary of stock symbols and their corresponding prices.
            - "failed": A list of stock symbols for which prices could not be fetched.
    """
    prices, failed = get_multiple_stock_prices(symbols)

    if prices:
        print(f"[INFO] Fetched stock prices: {list(prices.keys())}")
    if failed:
        print(f"[WARNING] Could not fetch prices for: {failed}")

    return {
        "prices": prices,
        "failed": failed
    }


stock_agent = Agent(
    role = "Stock Tracker"
    goal = "Monitor stock symbols and report real-time prices.",
    backstory= "You are a real-time financial data analyst specializing in stock tracking.",
    allow_delegation= False
    verbose= True,
    tools = [track_stock_prices_tool]
)

