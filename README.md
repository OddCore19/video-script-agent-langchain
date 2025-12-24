# Video Script Agent (LangChain)

A multimodal video-script agent prototype built with LangChain. This repo starts with notebook demos and a minimal Python entrypoint for quick iteration.

## Structure

- `notebooks/`: exploratory demos and prototypes
- `src/`: Python packages for agents, chains, tools, models, and utilities
- `sys_prompts/`: prompt templates
- `data/`, `assets/`, `outputs/`: inputs and generated artifacts
- `ui/`: future UI work

## Quickstart

1) Create a virtual environment and install dependencies:

```bash
pip install -r requirements.txt
```

2) Set your API key:

```bash
export OPENAI_API_KEY="..."
```
**or** create ```.env``` environment file and set it there.

3) Run the sample chain:

```bash
python -m src.main --topic "AI video prompt design" --audience "创作者"
```

## Notes

- The notebook demo lives at `notebooks/gen_script.ipynb`.
- Prompts used by the agent are in `sys_prompts/`.
