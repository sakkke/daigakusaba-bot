from discord.ext import commands
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

class Chat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.llm = ChatOpenAI()
        prompt = ChatPromptTemplate.from_messages([
            ('system', 'You are world class assistant. Please answer concisely and directly.'),
            ('user', '{input}'),
        ])
        output_parser = StrOutputParser()
        self.chain = prompt | self.llm | output_parser

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{type(self).__name__}: Logged on as {self.bot.user}!')

    @commands.Cog.listener()
    async def on_message(self, message):
        print(f'{type(self).__name__}: Message from {message.author}: {message.content}')

    @commands.slash_command()
    async def chat(self, ctx, text: str):
        await ctx.defer()
        await ctx.respond(self.chain.invoke({'input': text}))
