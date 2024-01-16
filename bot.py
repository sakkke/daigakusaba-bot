from dotenv import load_dotenv
from discord import Bot
import os

load_dotenv()

bot = Bot()

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

@bot.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')

bot.run(os.getenv('TOKEN'))
