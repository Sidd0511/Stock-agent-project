from crewai import Task
from agents.stock_agent import StockTrackerAgent

stockagent = StockTrackerAgent(verbose=True)

track_stocks_task = Task(
    description="Fetch current prices for user-specified stock symbols.",
    expected_output="Dictionary with the stock prices and list of failed symbols.",
    agent=stockagent,
    async_execution=False
)
