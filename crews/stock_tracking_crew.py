from crewai import Crew
from tasks.track_stocks_task import track_stocks_task

# A simple crew with just one task and one agent

stock_tracking_crew = Crew(
    agents = [track_stocks_task.agent],
    tasks = [track_stocks_task],
    verbose = True,
)
