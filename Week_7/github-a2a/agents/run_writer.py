#!/usr/bin/env python3
"""Start the Writer A2A agent server."""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import uvicorn
from agents.writer import WriterAgent
from config import WRITER_PORT

agent = WriterAgent()

if __name__ == "__main__":
    uvicorn.run(agent.app, host="0.0.0.0", port=WRITER_PORT, log_level="info")
