import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_HOST  = os.getenv("OLLAMA_HOST",  "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen3:0.6b")

REVIEWER_PORT = int(os.getenv("REVIEWER_PORT", "8201"))
PLANNER_PORT  = int(os.getenv("PLANNER_PORT",  "8202"))
WRITER_PORT   = int(os.getenv("WRITER_PORT",   "8203"))
