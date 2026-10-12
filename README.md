🌆 City Intelligence Agent

An AI-powered city intelligence assistant that answers questions about current weather and the latest news in Pakistani cities using Large Language Models (LLMs) and external APIs.

The agent uses an LLM to understand user queries and decide when to call the appropriate tool. It retrieves real-time weather information from OpenWeatherMap and searches for recent news using Tavily.

✨ Features

Current Weather: Retrieves temperature, feels-like temperature, humidity, weather conditions, and wind speed.

Latest City News: Searches for recent news articles related to Pakistani cities.

LLM-Powered Tool Calling: Uses Groq-hosted openai/gpt-oss-20b to decide which tool is needed.

Interactive CLI: Allows users to ask multiple questions in one session.

Conversation Memory: Maintains conversation history to provide contextual responses.

Tool Execution Approval: Asks the user for permission before executing a requested tool.

🛠️ Tech Stack

Python

Groq API

LangChain

OpenWeatherMap API

Tavily Search API

python-dotenv

Rich

⚙️ How It Works

The user enters a question.

The LLM analyzes the question and decides whether a tool is required.

If a tool is requested, the application asks the user for approval.

The selected tool retrieves weather information or news articles.

The tool result is added to the conversation history.

The LLM processes the result and generates a natural-language response.

Architecture

User Query
    |
    v
LLM (Groq + LangChain)
    |
    v
Tool Required?
    |
    +---- No ----> Generate Response
    |
    +---- Yes ---> Ask User for Approval
                       |
                       v
                  Execute Tool
                       |
             +---------+---------+
             |                   |
             v                   v
        Weather Tool         News Tool
      OpenWeatherMap           Tavily
             |                   |
             +---------+---------+
                       |
                       v
                 Tool Result
                       |
                       v
                Conversation History
                       |
                       v
                 LLM Final Answer

📁 Project Structure

City_intelligence_agent/
│
├── code.py              # Main application
├── .env                 # API keys (not committed to Git)
├── .gitignore           # Files excluded from Git
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation

🚀 Getting Started

1. Clone the Repository

git clone <your-github-repository-url>
cd City_intelligence_agent

2. Create a Virtual Environment

On Windows PowerShell:

python -m venv venv

Activate it:

.\venv\Scripts\Activate.ps1

3. Install Dependencies

pip install -r requirements.txt

4. Configure API Keys

Create a .env file in the project root directory and add your API keys:

OPENWEATHER_API_KEY=your_openweathermap_api_key
TAVILY_API_KEY=your_tavily_api_key
GROQ_API_KEY=your_groq_api_key

Obtain your API keys from:

OpenWeatherMap: https://openweathermap.org/api

Tavily: https://tavily.com/

Groq: https://console.groq.com/

Important: Keep your API keys private. Never upload your .env file to GitHub.

5. Run the Application

python code.py

💬 Example Queries

Weather

What is the current weather in Karachi?

What is the temperature in Lahore?

Tell me the humidity and wind speed in Islamabad.

News

What is the latest news in Karachi?

Find today's news about Lahore.

What are the latest news updates from Islamabad?

General Conversation

What can you do?

Explain the difference between weather and climate.

Weather and news results depend on the availability and accuracy of the external APIs.

🔑 Tools

1. get_weather(city: str)

Uses the OpenWeatherMap Current Weather API to retrieve:

City name

Temperature

Feels-like temperature

Humidity

Weather description

Wind speed

2. get_latest_news(city: str)

Uses Tavily Search to find recent news about a Pakistani city. Returns article titles, URLs, and content snippets.

🧠 Key Concepts Demonstrated

LLM tool calling

Function and tool integration

External API requests

Environment variable management

Conversation history using LangChain messages

Human approval before tool execution

Tool-result handling and iterative LLM calls

🔒 Security and Limitations

API keys must be stored in environment variables.

Tool execution requires user approval.

Weather and news depend on third-party API availability.

News search results may contain outdated or incomplete information.

The application currently runs in a command-line interface and is not deployed as a web application.

🔮 Future Improvements

Add air quality and weather forecast tools.

Add city-based traffic and public transport information.

Improve API error handling and input validation.

Add structured logging and automated tests.

Build a Streamlit or web-based interface.

Deploy the agent as an accessible online service.

👨‍💻 Author

Muhammad Shah Fahad

AI/ML Learner | Exploring Generative AI and AI Agents

This project was built to explore how LLMs can interact with external tools and real-time data sources to create useful AI applications.