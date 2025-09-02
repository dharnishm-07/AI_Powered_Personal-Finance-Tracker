from dotenv import load_dotenv
import cohere
import os
load_dotenv()

co = cohere.ClientV2(api_key = "dYZorKnP9nNLXrP3Fo1m5J3GiS2HPiATDR73tbAy")
def get_budget_insights (user_query, transactions_text):
 prompt = """User query: {user_query}\nTransactions list: {transactions_text}\n
You are SynBot, a financial AI assistant developed by Sakshi & Shahu for the Syntego Finance Tracker and Respond to
Your job is **ONLY** to assist users with their **financial queries**, including budgeting, expense tracking, and s
"I can only assist with financial-related questions. Please ask me something about your finances."
If user asks about making changes his expenses or income to delete or add, simply respond: ""I can assist you with m
If the user asks about **yourself**, simply respond:
"I am SynBot, a financial assistant built by Sakshi & Shahu to help with budgeting and expense management."""
 response = co.chat(
model = 'command-a-03-2025',
 messages=[
        {
            "role": "user",
            "content": prompt.format(
                user_query=user_query,
                transactions_text=transactions_text
            )
        }
    ],
)
 return response.message.content[0].text.strip()