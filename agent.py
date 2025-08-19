from agents import Agent, Runner
import asyncio

agent = Agent(
    name="Storyteller",
    instructions="Tell engaging stories with vivid details.",
)

async def main():
    # Stream the response as it's generated
    async for chunk in Runner.run_stream(agent, "Tell me a short story about a robot"):
        print(chunk.content, end="", flush=True)
    print()  # New line at the end

if __name__ == "__main__":
    asyncio.run(main())