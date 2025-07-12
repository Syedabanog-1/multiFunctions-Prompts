import os
from dotenv import load_dotenv
import google.generativeai as genai
import requests
from datetime import datetime

# Dummy decorator to simulate function_tool
def function_tool(func):
    return func

# Load environment variables
load_dotenv()
WEATHER_API = os.getenv("OPENWEATHER_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Gemini setup
genai.configure(api_key=GEMINI_API_KEY)

@function_tool
def ask_gemini(prompt: str) -> str:
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Gemini API error: {str(e)}"

@function_tool
def get_weather(city: str, datetime_str: str) -> str:
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API}&units=metric"
        res = requests.get(url).json()
        condition = res['weather'][0]['description']
        temp = res['main']['temp']
        return f"🌤️ The weather in {city} is {condition} with {temp}°C."
    except Exception as e:
        return f"❌ Error fetching weather: {str(e)}"

@function_tool
def send_email_notification(to: str, subject: str, message: str) -> str:
    # Simulate email notification
    return f"📧 Email notification to {to} about '{subject}' has been simulated successfully!"

@function_tool
def book_flight(from_where: str, to: str, date: str) -> str:
    return f"✈️ Flight booked from {from_where} to {to} on {date}. Confirmation ID: #FL-{datetime.now().strftime('%H%M%S')}"

@function_tool
def find_chinese_restaurants(location: str) -> str:
    return f"🥡 Chinese restaurants near {location}:\n- Golden Dragon\n- Hakkasan"

@function_tool
def schedule_meeting(team: str, date: str, time: str, topic: str) -> str:
    return f"📅 Meeting with {team} scheduled on {date} at {time} about '{topic}'."

@function_tool
def search_product(product_type: str, max_price: int, reviews: str) -> str:
    return f"🔍 Best {product_type} under ${max_price} with {reviews} reviews: Sony WH-CH520 - $69."

class Agent:
    def __init__(self, name, tools, system_message=""):
        self.name = name
        self.tools = {tool.__name__: tool for tool in tools}
        self.system_message = system_message

    def respond(self, prompt):
        prompt_lower = prompt.lower()

        if "weather" in prompt_lower:
            return self.tools["get_weather"]("Karachi", str(datetime.now()))
        elif "restaurant" in prompt_lower or "chinese" in prompt_lower:
            return self.tools["find_chinese_restaurants"]("Karachi")
        elif "email" in prompt_lower:
            return self.tools["send_email_notification"](
                "syeda@example.com", "Project Deadline Update", 
                "The project deadline has been moved to the last week of this month."
            )
        elif "flight" in prompt_lower:
            return self.tools["book_flight"]("Karachi", "Singapore", "2025-07-25")
        elif "meeting" in prompt_lower:
            return self.tools["schedule_meeting"]("Marketing Team", "2025-07-20", "15:00", "Quarterly strategy review")
        elif "product" in prompt_lower or "camera" in prompt_lower:
            return self.tools["search_product"]("camera", 500, "excellent")
        elif "gemini" in prompt_lower or "ai" in prompt_lower:
            return self.tools["ask_gemini"]("How to stay productive while working from home?")
        else:
            return "🤖 I didn't understand the request."

class Runner:
    @staticmethod
    def run_sync(agent, prompt):
        class Result:
            output = agent.respond(prompt)
        return Result()

multi_tool_agent = Agent(
    name="MultiToolAgent",
    tools=[
        get_weather,
        send_email_notification,
        book_flight,
        find_chinese_restaurants,
        schedule_meeting,
        search_product,
        ask_gemini
    ],
    system_message="You are a helpful assistant capable of handling multiple utility tasks."
)

def main():
    prompts = [
        "What's the weather here in current location  right now?",
        "Find nearby Chinese restaurants based on the user's current location using the Google Places API.",
        "Send an email to syeda@example.com about the project deadline moved by last week this month.",
        "Book a flight from Karachi to Singapore on 2025-07-25.",
        "Schedule a meeting with a specified date, time, participants, and agenda.",
        "Search for a digital product (like a camera) online by specifying product name or category.",
        "Ask a general question or request help with a task using Gemini's generative AI capabilities."
    ]

    for prompt in prompts:
        result = Runner.run_sync(multi_tool_agent, prompt)
        print(f"\n🔹 Prompt: {prompt}")
        print(f"✅ Response: {result.output}")

if __name__ == "__main__":
    main()
