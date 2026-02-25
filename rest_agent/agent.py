import os
from google.adk.models.lite_llm import LiteLlm
from google.adk.agents.llm_agent import Agent

from rest_agent.tools import get_request

# Point LiteLLM to your local Ollama instance
os.environ["OLLAMA_API_BASE"] = "http://localhost:11434"

# Define the local model
local_model = LiteLlm(
    model="ollama_chat/llama3.1", # Use 'ollama_chat/' prefix
    api_base="http://localhost:11434"
)

root_agent = Agent(
    model=local_model,
    name='RestApiAgent',
    description='An agent that can execute REST API calls based on specifications and return the results.',
    instruction='You are a REST API executor. Your task is to:\n' \
    '1. Read the provided API specification and understand the required API calls.\n' \
    '2. Use the get_request tool to perform the necessary API calls as specified.\n' \
    '3. Return the status, headers, and body of the API response.\n' \
    'Always use the provided tools to execute API calls and never attempt to call APIs directly without using the tools.',
    tools=[get_request]
)
