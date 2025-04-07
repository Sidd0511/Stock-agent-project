# Stock & Metal Price Tracker with Agents

This project is an AI-driven agent framework built using [CrewAI](https://docs.crewai.com/) and [LangChain](https://docs.langchain.com/) to monitor real-time stock prices and metal prices (like gold and silver), track user-defined thresholds, and generate alerts or summaries based on market changes.

## Features

- **Agent-Based Architecture** using CrewAI
- **Real-Time Price Tracking** of:
  - User-selected stocks (via symbol)
  - Gold and Silver in INR
- **Dynamic Threshold Alerts**
  - Users can define price change percentage or absolute value
- **Daily Summary Reports**
- **Multi-Agent Orchestration**
  - Stock Tracker, Metal Tracker, News Fetcher, Alert Handler, and Summarizer
- **Chat-Based Interface (WIP)**

## Project Structure

.
├── agents/         # CrewAI agents like stock_agent.py, metals_agent.py
├── tools/          # Price fetchers, alert notifiers, etc.
├── tasks/          # Task logic to be assigned to agents
├── crews/          # Crew orchestration logic
├── models/         # Pydantic models for user inputs and configs
├── db/             # SQLite handler and storage logic
├── app.py          # Entry point (chat interface)
├── requirements.txt
└── README.md

## Getting Started

### 1. Install Requirements

```bash
pip install -r requirements.txt

2. Run the App

python app.py

(Or run interactively via Replit or GitHub Codespaces terminal.)

Future Plans
	•	Add persistent user settings (thresholds, alerts)
	•	Connect to Telegram/Email for real-time notifications
	•	Expand to more asset types (crypto, mutual funds)

License

MIT License

---

### Add it to Your Codespace
Run this in your Codespaces terminal:
```bash
touch README.md

Then paste the content above into the file.

Let me know once you’re ready, and we’ll jump back to building the model.
