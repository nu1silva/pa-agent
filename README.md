# PA Agent

Personal Assistant Agent built with Google Agents Development Kit (ADK).

## Overview

This project contains AI agents that provide time-related information using local LLM models via Ollama.

## Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) package manager
- [Ollama](https://ollama.ai) with the `gemma3:latest` model

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd pa-agent
```

2. Install dependencies:
```bash
uv sync
```

3. Ensure Ollama is running with the required model:
```bash
ollama pull gemma3:latest
```

## Available Agents

### PA Agent
Provides time information for specified cities using a mock tool.

## Usage

### CLI Mode

Run the agents in interactive CLI mode:

```bash
uv run adk run pa_agent
```

### Web Interface

Launch the web interface to interact with agents:

```bash
uv run adk web pa_agent
```

The web interface will be available at `http://localhost:8080` (or the port specified in output).

## Project Structure

```
pa-agent/
├── pa_agent/
│   ├── __init__.py       # Agent exports
│   ├── agent.py          # Agent definitions and tools
│   └── .adk/             # ADK runtime data
├── pyproject.toml        # Project dependencies
├── README.md             # This file
└── .gitignore            # Git ignore patterns
```

## Development

### Adding New Agents

1. Edit `pa_agent/agent.py` to define new agents
2. Update `pa_agent/__init__.py` to export them
3. Test with `uv run adk run pa_agent`

### Dependencies

- `google-adk>=1.25.0` - Google Agents Development Kit
- `litellm>=1.81.12` - LLM integration layer

## Configuration

The agents use Ollama as the LLM provider. To change the model, update the `model` parameter in `pa_agent/agent.py`:

```python
Agent(
    model='ollama/your-model:tag',
    ...
)
```

## License

MIT
