# Stock & Metal Price Tracker with Agents

This project is an AI-driven agent framework built using [CrewAI](https://docs.crewai.com/) to monitor real-time stock prices and metal prices (like gold and silver), track user-defined thresholds, and generate alerts or summaries based on market changes.

## Features

- **Agent-Based Architecture** using CrewAI
- **Real-Time Price Tracking** of:
  - User-selected stocks (via symbol)
  - Metals like gold, silver, and more in INR
- **Dynamic Threshold Alerts** (see [models/asset.py](models/asset.py))
- **Daily Summary Reports** (planned)
- **Multi-Agent Orchestration**
  - Stock Tracker, Metal Tracker, and other agents
- **Verbose Logging** for debugging and tracking
- **Extensible Design** for adding new asset types or agents

## Project Structure

```
.
├── agents/         # CrewAI agents for stock and metal tracking
│   ├── stock_agent.py
│   ├── metal_agent.py
├── tools/          # Utility modules for fetching prices
│   ├── stock_price_api.py
│   ├── metal_price_api.py
├── tasks/          # Task logic to be assigned to agents
│   ├── track_stocks_task.py
│   ├── track_metals_task.py
├── crews/          # Crew orchestration logic
│   ├── stock_tracking_crew.py
│   ├── metal_tracking_crew.py
├── models/         # Pydantic models for user inputs and configurations
│   ├── asset.py
├── db/             # (Reserved for future database logic)
├── app.py          # Entry point for running the application
├── requirements.txt
└── README.md
```

## Getting Started

### 1. Install Requirements

Make sure you have Python installed. Then, install the required dependencies:

```bash
pip install -r requirements.txt
```

### 2. Run the App

Run the application to start tracking stock and metal prices:

```bash
python app.py
```

### 3. Example Output

The application will fetch stock and metal prices based on the predefined configuration and display the results along with logs. Example output:

```
[INFO] Application Started

[INFO] Starting Stock Tracking Crew...

-------- Stock Price Result --------
{'prices': {'TCS.NS': 3840.0, 'RELIANCE.NS': 2850.0}, 'failed': ['INVALIDSYM']}
-------- End of Stock Price Result --------

-------- Stock Task Log --------
[...task log output...]
-------- End of Stock Task Log --------

[INFO] Starting Metal Tracking Crew...

-------- Metal Price Result --------
{'prices': {'GOLD': 60000.0, 'SILVER': 72000.0}, 'failed': ['INVALIDMETAL']}
-------- End of Metal Price Result --------

-------- Metal Task Log --------
[...task log output...]
-------- End of Metal Task Log --------

[INFO] Application Finished
```

## Models

Asset tracking and alert rules are defined using Pydantic models in [models/asset.py](models/asset.py):

- [`AssetTrackingConfig`](models/asset.py): Configuration for tracking an asset (stock or metal).
- [`AlertRule`](models/asset.py): Defines alert rules for assets.

## Extending

- Add new agents in [agents/](agents/)
- Add new price fetchers in [tools/](tools/)
- Add new tasks in [tasks/](tasks/)
- Add new crews in [crews/](crews/)

## Future Plans

- Add persistent user settings (thresholds, alerts)
- Connect to Telegram/Email for real-time notifications
- Expand to more asset types (e.g., cryptocurrencies, mutual funds)
- Add a chat-based interface for user interaction
- Implement a database for storing historical data and user preferences

## License

This project is licensed under the MIT License. See the LICENSE file for details.
