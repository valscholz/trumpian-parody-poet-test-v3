#!/usr/bin/env python3
"""Run script for Trumpian Parody Poet"""

import asyncio
import argparse
from agent import agent
from agents import Runner

async def main():
    parser = argparse.ArgumentParser(description='Trumpian Parody Poet')
    parser.add_argument('input', nargs='?', default="Hello, please demonstrate your functionality.", 
                       help='Input message for the agent')
    
    args = parser.parse_args()
    
    try:
        result = await Runner.run(agent, args.input)
        print(result.final_output)
    except Exception as e:
        print(f"Error: {e}")

# Add simple web server for health checks and API access
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import os
from datetime import datetime

app = FastAPI(title="trumpian_parody_poet", description="OpenAI Agent API")

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@app.get("/health")
async def health():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        # Use the agent from agent.py
        from agent import run_sync
        response = run_sync(request.message)
        return ChatResponse(response=response)
    except Exception as e:
        return ChatResponse(response=f"Error: {str(e)}")

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
