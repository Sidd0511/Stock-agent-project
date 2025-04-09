from crews.stock_tracking_crew import stock_tracking_crew

# Define the stock symbols to track
symbols_to_track = ["TCS.NS", "RELIANCE.NS", "INVALIDSYM"]

# Run the stock tracking crew with the input symbols
result = stock_tracking_crew.kickoff(input={"symbols": symbols_to_track})

# Print the result of the stock tracking operation
print("-------- Result --------")
print(result)
print("-------- End of Result --------")

# Print the task log for debugging or tracking purposes
print("\n\n\n-------- Task Log --------")
print(stock_tracking_crew.task_log)
print("-------- End of Task Log --------")