🌐 Multi-Task Automation Agent:
******************************
This project is a powerful multi-agent assistant built using the OpenAI Agent SDK, function_tool, and real APIs. It can:

🌦️ Get real-time weather updates

📧 Send real email notifications via SMTP

✈️ Book (mock) flights

🍜 Find nearby Chinese restaurants

🗓️ Schedule meetings

🛒 Search products based on filters

filters

🧠 Features:
  *********

Task	          Description

Weather	          Live data from OpenWeatherMap
Email	          SMTP integration for real emails
Flights	          Simulated flight bookings
Restaurants	  Local restaurant recommendations
Meetings	  Schedule team meetings
Products	  Search for best-rated products

🛠️ Tech Stack:
  ***********
Python 3.11+

OpenAI Agent SDK

function_tool for LLM-integrated tools

dotenv for environment variables

smtplib + email for Gmail-based notifications

requests for REST APIs

Asyncio for concurrent prompts



🔐 .env Format

Create a .env file in the root directory with the following keys:

OPENWEATHER_API_KEY=your_openweather_api_key
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_email_password_or_app_password


🧪 Sample Output:
   ************
🔹 Prompt: What's the weather in Lahore right now?
✅ Response: The weather in Lahore is scattered clouds with 34°C.

🔹 Prompt: Send an email to sarah@example.com about the meeting reschedule
✅ Response: ✅ Email sent to sarah@example.com successfully!

🔹 Prompt: Book a flight from Karachi to Istanbul on 2025-07-20
✅ Response: ✈️ Flight booked from Karachi to Istanbul on 2025-07-20. Confirmation ID: #FL-143859

***Possible prompts for each Agent:
Here are the possible prompts for each agent:

Weather Agent

- Possible prompts:
    1. "What is the current weather in [city]?"
    2. "What is the temperature in [city] right now?"
    3. "Is it sunny or cloudy in [city] today?"
    4. "What's the weather forecast for [city] tomorrow?"
    5. "Can you tell me the current humidity in [city]?"
    6. "What's the weather like in [city] during [season]?"
    7. "Can you give me the weather forecast for the next 5 days in [city]?"
    8. "Is there a chance of rain in [city] today?"

Project Date Agent

- Possible prompts:
    1. "Update the project date for [project name] to [new date]"
    2. "What is the current project date for [project name]?"
    3. "Can you send a notification to the team about the project date update?"
    4. "What's the deadline for [project name]?"
    5. "Can you update the project schedule for [project name]?"
    6. "What's the current status of [project name]?"
    7. "Can you notify the stakeholders about the project date change?"
    8. "What's the new project date for [project name]?"

Restaurant Agent

- Possible prompts:
    1. "What are the top [cuisine] restaurants in [city]?"
    2. "Can you recommend some [cuisine] restaurants near [location]?"
    3. "What's the menu for [restaurant name]?"
    4. "Can you provide the hours of operation for [restaurant name]?"
    5. "What's the average price range for [restaurant name]?"
    6. "Can you give me the contact information for [restaurant name]?"
    7. "What's the reservation policy for [restaurant name]?"
    8. "Can you provide the reviews for [restaurant name]?"


Meeting Agent

- Possible prompts:
    1. "Schedule a meeting on [topic] on [date] at [time]"
    2. "Can you arrange a meeting with [team member] on [date] at [time]?"
    3. "What's the agenda for the meeting on [topic]?"
    4. "Can you send a reminder for the meeting on [topic]?"
    5. "What's the meeting schedule for [team]?"
    6. "Can you invite [guest] to the meeting on [topic]?"
    7. "What's the meeting duration for [topic]?"
    8. "Can you provide the meeting minutes for [topic]?"

E-commerce Agent

- Possible prompts:
    1. "What is the price range for [product name] with [quality] quality?"
    2. "Can you recommend some [product category] products?"
    3. "What's the best product for [specific need]?"
    4. "Can you compare the prices of [product name] from different sellers?"
    5. "What's the product description for [product name]?"
    6. "Can you provide the product reviews for [product name]?"
    7. "What's the shipping cost for [product name]?"
    8. "Can you provide the product warranty information for [product name]?"



🧑‍💻 Author:
***********
Gulzar Bano
Built using OpenAI Agent SDK + Gemini-compatible models
<img width="1609" height="904" alt="MultiFunctions-PromptResult" src="https://github.com/user-attachments/assets/ff1b686f-4b39-4d00-87cb-f83af3981542" />
<img width="1615" height="907" alt="Prompts" src="https://github.com/user-attachments/assets/1e847a8b-ce6c-423e-8e7e-d17dfc1adc48" />
