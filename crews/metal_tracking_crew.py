from crewai import Crew
from tasks.track_metals_task import track_metals_task

metal_tracking_crew = Crew(
    agents=[track_metals_task.agent],
    tasks = [track_metals_task],
    verbose=True,
)
