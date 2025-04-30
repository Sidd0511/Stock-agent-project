from crewai import Agent
from typing import List, Dict
from tools.metal_price_api import get_multiple_metal_prices


def track_metal_prices_tool(metals: List[str]) -> Dict[str, float]:
    """
    Fetch the latest metal prices for a list of metal symbols.

    This function uses an external API to retrieve metal prices for the provided symbols.
    It logs information about successfully fetched prices and warnings for any symbols
    that could not be fetched.

    Args:
        metals (List[str]): A list of metal symbols to fetch prices for.

    Returns:
        Dict[str, float]: A dictionary containing:
            - "prices": A dictionary of metal symbols and their corresponding prices.
            - "failed": A list of metal symbols for which prices could not be fetched.
    """
    # Fetch prices and failed symbols
    prices, failed = get_multiple_metal_prices(metals)

    # Log fetched prices
    if prices:
        print(f"[INFO] Fetched metal prices: {list(prices.keys())}")

    # Log failed symbols
    if failed:
        print(f"[WARNING] Could not fetch prices for: {failed}")

    # Return the results
    return {
        "prices": prices,
        "failed": failed
    }


# Define the metal agent
metal_agent = Agent(
    role="Metal Tracker",
    tools=[track_metal_prices_tool],
    goal="Fetch the current metal prices in INR.",
    allow_delegation=False,
    backstory=(
        "You are a seasoned financial analyst expert in commodities and precious metals like gold, silver, copper, etc. "
        "Your task is to provide accurate and up-to-date information about metal prices in Indian Rupees (INR)."
    ),
    verbose=True
)
