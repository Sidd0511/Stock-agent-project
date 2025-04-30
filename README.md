# Stock & Metal Price Tracker with Agents

This project is an AI-driven agent framework built using [CrewAI](https://docs.crewai.com/) and [LangChain](https://docs.langchain.com/) to monitor real-time stock prices and metal prices (like gold and silver), track user-defined thresholds, and generate alerts or summaries based on market changes.

## Features

- **Agent-Based Architecture** using CrewAI
- **Real-Time Price Tracking** of:
  - User-selected stocks (via symbol)
  - Metals like gold, silver, and more in INR
- **Dynamic Threshold Alerts**
  - Users can define price change percentage or absolute value
- **Daily Summary Reports**
- **Multi-Agent Orchestration**
  - Stock Tracker, Metal Tracker, and other agents
- **Verbose Logging** for debugging and tracking
- **Extensible Design** for adding new asset types or agents

## Project Structure

```
.
├── agents/         # CrewAI agents like stock_agent.py, metal_agent.py
│   ├── stock_agent.py   # Agent for tracking stock prices
│   ├── metal_agent.py   # Agent for tracking metal prices
│   └── __init__.py      # Package initialization
├── tools/          # Utility modules for fetching prices, sending alerts, etc.
│   ├── price_fetcher.py # Fetches real-time stock and metal prices
│   ├── alert_notifier.py # Sends alerts via email, SMS, etc.
│   └── __init__.py      # Package initialization
├── tasks/          # Task logic to be assigned to agents
│   ├── stock_tasks.py   # Tasks related to stock tracking
│   ├── metal_tasks.py   # Tasks related to metal tracking
│   └── __init__.py      # Package initialization
├── crews/          # Crew orchestration logic
│   ├── main_crew.py     # Main crew managing all agents
│   └── __init__.py      # Package initialization
├── models/         # Pydantic models for user inputs and configurations
│   ├── stock_model.py   # Models for stock-related data
│   ├── metal_model.py   # Models for metal-related data
│   └── __init__.py      # Package initialization
├── db/             # SQLite handler and storage logic (future use)
│   ├── database.py      # Database connection and query logic
│   └── __init__.py      # Package initialization
├── app.py          # Entry point for running the application
├── requirements.txt # List of dependencies
└── README.md       # Project documentation
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

The application will fetch stock and metal prices based on the predefined configuration and display the results along with logs.

## Future Plans

- Add persistent user settings (thresholds, alerts)
- Connect to Telegram/Email for real-time notifications
- Expand to more asset types (e.g., cryptocurrencies, mutual funds)
- Add a chat-based interface for user interaction
- Implement a database for storing historical data and user preferences

## License

This project is licensed under the MIT License. See the LICENSE file for details.
