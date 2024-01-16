from dotenv import load_dotenv
from discord import Bot, Intents
import os

load_dotenv()

intents = Intents.default()
intents.message_content = True

bot = Bot(intents=intents)

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

@bot.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')

bot.run(os.getenv('TOKEN'))
