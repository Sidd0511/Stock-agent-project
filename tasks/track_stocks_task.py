from crewai import Task
from agents.stock_agent import stock_agent

# Define the task for tracking stock prices
track_stocks_task = Task(
    description="Fetch current prices for user-specified stock symbols.",
    expected_output="Dictionary with the stock prices and list of failed symbols.",
    agent=stock_agent,
    async_execution=False
)
