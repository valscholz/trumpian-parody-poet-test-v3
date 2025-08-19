# Trumpian Parody Poet

Users want entertaining, original poems that evoke the high-level rhetorical traits associated with Donald Trump without impersonating him. The agent should generate clearly-labeled parody poems on any user-provided topic while ensuring safety, originality, and compliance with policies on public figure representation.

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your OpenAI API key
```

## Usage

```bash
python run.py "Your input message here"
```

## Development

This agent is built using the OpenAI Agents SDK and follows canonical patterns from the official documentation.

### Files
- `agent.py` - Main agent implementation
- `run.py` - Command-line interface
- `requirements.txt` - Dependencies
- `.env.example` - Environment configuration template
