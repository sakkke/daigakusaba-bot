from discord.ext import commands

class Chat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{type(self).__name__}: Logged on as {self.bot.user}!')

    @commands.Cog.listener()
    async def on_message(self, message):
        print(f'{type(self).__name__}: Message from {message.author}: {message.content}')
