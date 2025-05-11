from phi.agent import Agent
from phi.model.groq import Groq 
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os

from dotenv import load_dotenv
load_dotenv()
openai.api_key=os.getenv("OPEN_AI_API_KEY")

web_search_agent=Agent(
name='Web Search Agent',
role='Search the web for information',
model=Groq(id="deepseek-r1-distill-llama-70b"),
tools=[DuckDuckGo()],
instructions=["Always include Sources"],
show_tool_calls=True,
markdown=True
)


fin_agent=Agent(
    name="Finance Agent",
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    instructions=["Use tables to dispaly the data"],
    show_tool_calls=True,
    markdown=True,
)


multi_ai_agent=Agent(
    team=[web_search_agent,fin_agent],
     model=Groq(id="deepseek-r1-distill-llama-70b"),
    instructions=["Always include sources","Use tables to dspaly the data"],
    show_tool_calls=True,
    markdown=True,
)


multi_ai_agent.print_response("Summarize analyst reccomendation and share the latest news for NVDA",stream=True)