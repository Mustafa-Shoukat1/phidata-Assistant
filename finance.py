from phi.assistant import Assistant
from langchain_google_genai import ChatGoogleGenerativeAI
from phi.tools.yfinance import YFinanceTools

assistant = Assistant(
    llm=ChatGoogleGenerativeAI(model="gemini-pro",api_key="AIzaSyDPv0Rrqv7YoEYaHXz3Mn4Gxz_-voAYbjU"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    show_tool_calls=True,
    markdown=True,
)
assistant.print_response("What is the stock price of NVDA")
assistant.print_response("Write a comparison between NVDA and AMD, use all tools available.")
