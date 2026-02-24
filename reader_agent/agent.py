import os
from google.adk.models.lite_llm import LiteLlm
from google.adk.agents.llm_agent import Agent

from reader_agent.tools import read_api_spec, read_api_spec_as_string, list_api_specs

# Point LiteLLM to your local Ollama instance
os.environ["OLLAMA_API_BASE"] = "http://localhost:11434"

# Define the local model
local_model = LiteLlm(
    model="ollama_chat/llama3.1", # Use 'ollama_chat/' prefix
    api_base="http://localhost:11434"
)

# Define the "Brain"
root_agent = Agent(
    name="SpecSummarizer",
    model=local_model,
    description="An agent that reads API specifications and provides summaries and insights.",
    instruction="""
    You are a technical analyst. Your task is to:
    1. Read the provided specification file using the 'read_api_spec' tool.
    2. Provide a high-level summary followed by key technical requirements.
    3. If the file is an OpenAPI/Swagger spec, list the main endpoints.
    """,
    tools=[read_api_spec, read_api_spec_as_string, list_api_specs]
)