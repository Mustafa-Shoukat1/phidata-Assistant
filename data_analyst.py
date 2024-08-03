import json
import streamlit as st

from phi.llm.openai import OpenAIChat
from phi.assistant.duckdb import DuckDbAssistant

data_analyst = DuckDbAssistant(
    llm=OpenAIChat(model="gpt-4o",api_key="sk-proj-swWK8vxxyKlbO2hRkHo1T3BlbkFJBjg6VlbZIU0z38eod7uO"),
    semantic_model=json.dumps(
        {
            "tables": [
                {
                    "name": "movies",
                    "description": "Contains information about movies from IMDB.",
                    "path": "imdb-top-1000.csv",
                }
            ]
        }
    ),
)

data_analyst.print_response("Highest rated movie in 2022? Show me the SQL.", markdown=True)
data_analyst.print_response("Different category of movies", markdown=True)