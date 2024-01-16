from dotenv import load_dotenv
import discord
import os

load_dotenv()

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

client = MyClient()
client.run(os.getenv('TOKEN'))
