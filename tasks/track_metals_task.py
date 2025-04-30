from crewai import Task
from agents.metal_agent import metal_agent

# Define the task for tracking metal prices
track_metals_task = Task(
    description="Fetch current prices in INR for user-specified metal symbols.",
    expected_output="Dictionary with the metal prices in INR and list of failed symbols.",
    agent=metal_agent,
    async_execution=False
)