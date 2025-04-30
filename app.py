from crews.stock_tracking_crew import stock_tracking_crew
from crews.metal_tracking_crew import metal_tracking_crew

# Function to handle stock tracking
def run_stock_tracking():
    """
    Run the Stock Tracking Crew to fetch stock prices for specified symbols.
    """
    print("\n\n[INFO] Starting Stock Tracking Crew...")
    symbols_to_track = ["TCS.NS", "RELIANCE.NS", "INVALIDSYM"]  # Define stock symbols to track
    result = stock_tracking_crew.kickoff(input={"symbols": symbols_to_track})  # Run the crew

    # Print the result of the stock tracking operation
    print("\n-------- Stock Price Result --------")
    print(result)
    print("-------- End of Stock Price Result --------")

    # Print the task log for debugging or tracking purposes
    print("\n-------- Stock Task Log --------")
    print(stock_tracking_crew.task_log)
    print("-------- End of Stock Task Log --------")


# Function to handle metal tracking
def run_metal_tracking():
    """
    Run the Metal Tracking Crew to fetch metal prices for specified metals.
    """
    print("\n\n[INFO] Starting Metal Tracking Crew...")
    metals = ["GOLD", "SILVER", "INVALIDMETAL"]  # Define metals to track
    result = metal_tracking_crew.kickoff(input={"metals": metals})  # Run the crew

    # Print the result of the metal tracking operation
    print("\n-------- Metal Price Result --------")
    print(result)
    print("-------- End of Metal Price Result --------")

    # Print the task log for debugging or tracking purposes
    print("\n-------- Metal Task Log --------")
    print(metal_tracking_crew.task_log)
    print("-------- End of Metal Task Log --------")


# Main function to execute both tracking crews
if __name__ == "__main__":
    print("[INFO] Application Started")
    run_stock_tracking()  # Run stock tracking
    run_metal_tracking()  # Run metal tracking
    print("[INFO] Application Finished")