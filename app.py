# You can find this code for Chainlit python streaming here (https://docs.chainlit.io/concepts/streaming/python)

# OpenAI Chat completion
import os
from openai import AsyncOpenAI  # importing openai for API usage
import chainlit as cl  # importing chainlit for our app
from dotenv import load_dotenv
import logging
from prompt_router import analyze_and_enhance_prompt

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# System message template
SYSTEM_MESSAGE = """You are a helpful assistant who always speaks in a pleasant tone!
Think through your response step by step."""

@cl.on_chat_start  # marks a function that will be executed at the start of a user session
async def start_chat():
    settings = {
        "model": "gpt-3.5-turbo",
        "temperature": 0,
        "max_tokens": 500,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0,
    }

    cl.user_session.set("settings", settings)


@cl.on_message  # marks a function that should be run each time the chatbot receives a message from a user
async def main(message: cl.Message):
    settings = cl.user_session.get("settings")
    client = AsyncOpenAI()

    # Analyze and enhance the user's prompt
    enhanced_message = await analyze_and_enhance_prompt(message.content)
    
    # Debug message using both Chainlit's message and logging
    await cl.Message(
        content=f"Debug - Enhanced message: {enhanced_message}",
        author="System"
    ).send()
    logger.info(f"Enhanced message: {enhanced_message}")

    messages = [
        {"role": "system", "content": SYSTEM_MESSAGE},
        {"role": "user", "content": enhanced_message}
    ]

    msg = cl.Message(content="")

    # Call OpenAI
    async for stream_resp in await client.chat.completions.create(
        messages=messages, stream=True, **settings
    ):
        token = stream_resp.choices[0].delta.content
        if token is not None:
            await msg.stream_token(token)

    await msg.send()
