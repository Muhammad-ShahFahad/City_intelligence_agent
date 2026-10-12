import os
import requests
from dotenv import load_dotenv
load_dotenv(override=True)

from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, ToolMessage
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain_core.prompts import ChatPromptTemplate
from tavily import TavilyClient
from rich import print

#API KEYS
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

# Chat Model
model = init_chat_model(
    "openai/gpt-oss-20b",
    model_provider="groq"
)

# Tools

@tool
def get_weather(city: str):
    """Get current weather of the city"""
    url = "https://api.openweathermap.org/data/2.5/weather"
    params={
        "q":city,
        "appid":OPENWEATHER_API_KEY,
        "units":"metric"
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        return f"Could not get weather for {city}"

    data = response.json()

    return {
    "city": data["name"],
    "temperature": data["main"]["temp"],
    "feels_like": data["main"]["feels_like"],
    "humidity": data["main"]["humidity"],
    "condition": data["weather"][0]["description"],
    "wind_speed": data["wind"]["speed"]
    }

@tool
def get_latest_news(city: str):
    """Search for the latest news about a Pakistani city"""
    query = f"Latest news {city} Pakistan Today"
    response = tavily_client.search(
        query=query,
        search_depth="basic",
        topic="news",
        max_results=5,
    )
    articles = []

    for result in response["results"]:
        articles.append({
            "title": result["title"],
            "url": result["url"],
            "content": result["content"]
        })
    return{
        "city": city,
        "articles": articles
    }

# Creating the model

tools = {
    "get_weather":get_weather,
    "get_latest_news":get_latest_news
}
# Bing the chat model with tools
llm_with_tools = model.bind_tools([get_weather, get_latest_news])
# Chat stared 
# Chat starts
print("The chat model has started. Ask anything related to weather and news")

history = []

print("\nType 'exit' to quit the chat")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() in {"exit", "quit"}:
        break

    history.append(HumanMessage(content=user_input))

    while True:
        # Send the complete conversation to the model
        result = llm_with_tools.invoke(history)

        # Save the AI response, including any tool calls
        history.append(result)

        # Check whether the model requested a tool
        if result.tool_calls:
            for tool_call in result.tool_calls:
                tool_name = tool_call["name"]

                confirm = input(
                    f"{tool_name} call requested. Continue? (y/n): "
                ).strip().lower()

                if confirm != "y":
                    print("Tool call denied")

                    history.append(
                        ToolMessage(
                            content="The user denied the tool call.",
                            tool_call_id=tool_call["id"]
                        )
                    )
                    continue

                # Execute the approved tool
                tool_result = tools[tool_name].invoke(
                    tool_call["args"]
                )

                print(f"Tool result: {tool_result}")

                history.append(
                    ToolMessage(
                        content=str(tool_result),
                        tool_call_id=tool_call["id"]
                    )
                )

            # Ask the model to process the tool results
            continue

        # No tool requested: show the final answer
        print(f"Assistant: {result.content}")
        break

        


