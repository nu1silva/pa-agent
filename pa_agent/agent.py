import os
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

# Point LiteLLM to your local Ollama instance
os.environ["OLLAMA_API_BASE"] = "http://localhost:11434"

# Define the local model
local_model = LiteLlm(
    model="ollama_chat/llama3.1", # Use 'ollama_chat/' prefix
    api_base="http://localhost:11434"
)

# Initialize the Agent
root_agent = Agent(
    name="PersonalAgent",
    model=local_model,
    description="An agent running entirely on local hardware.",
    instruction="You are a helpful assistant. Use your tools when needed."
)