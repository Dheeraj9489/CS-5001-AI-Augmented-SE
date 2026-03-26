# GitHub A2A Agent Pipeline — Agent-to-Agent Protocol

Re-implementation of the **Week 5 GitHub Agent** (Reviewer → Planner → Writer) using **A2A (Agent-to-Agent) protocol** for inter-agent communication. Each agent runs as an independent HTTP server; a coordinator discovers them and chains tasks sequentially.

## Architecture

```
                        ┌──────────────┐
                        │  Coordinator │
                        │  (CLI)       │
                        └──────┬───────┘
                               │  HTTP
              ┌────────────────┼────────────────┐
              ▼                ▼                 ▼
     ┌────────────────┐ ┌───────────────┐ ┌───────────────┐
     │ Reviewer :8201 │ │ Planner :8202 │ │ Writer  :8203 │
     │ diff analysis  │ │ action plan   │ │ draft content │
     └────────────────┘ └───────────────┘ └───────────────┘
            │                   │                  │
            └───────────────────┴──────────────────┘
                            Ollama LLM
```

## Pipeline Flow

1. **Reviewer** — Reads the git diff, analyses changes (category, risk, issues)
2. **Planner** — Receives review as context, decides action (create_issue / create_pr / no_action)
3. **Writer** — Receives review + plan as context, drafts a GitHub issue or PR body

## A2A Protocol

Each agent implements:
- `GET /.well-known/agent.json` — Agent Card (name, skills, endpoint)
- `POST /tasks/send` — Accepts `{task_id, message, context}`, returns `{task_id, status, output, agent}`

The coordinator discovers agents via their cards, then delegates tasks with context chaining.

## Prerequisites

- **Python 3.10+**
- **Ollama** running locally with a model (e.g. `qwen3:0.6b`)

## Setup

```bash
cd Week_7/github-a2a
pip install -r requirements.txt
cp .env.example .env    # edit if needed
```

## Running

Start each agent in a separate terminal:

```bash
# Terminal 1
python agents/run_reviewer.py

# Terminal 2
python agents/run_planner.py

# Terminal 3
python agents/run_writer.py
```

Then run the coordinator:

```bash
# Terminal 4
python demo_pipeline.py /path/to/your/repo
python demo_pipeline.py /path/to/your/repo --base main
```
