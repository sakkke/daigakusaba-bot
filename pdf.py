from discord.ext import commands
from aiohttp import ClientSession
from io import BytesIO
from pdf2image import convert_from_bytes
from discord import File

class PDF(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{type(self).__name__}: Logged on as {self.bot.user}!')

    @commands.Cog.listener()
    async def on_message(self, message):
        print(f'{type(self).__name__}: Message from {message.author}: {message.content}')

        for attachment in message.attachments:
            if attachment.filename.endswith('.pdf'):
                files = []
                async with ClientSession() as session:
                    async with session.get(attachment.url) as response:
                        binary = await response.read()

                        with BytesIO() as pdf_stream:
                            pdf_stream.write(binary)
                            pdf_stream.seek(0)
                            pages = convert_from_bytes(pdf_stream.read())

                            for i, page in enumerate(pages, 1):
                                with BytesIO() as page_stream:
                                    page.save(page_stream, 'JPEG')
                                    page_stream.seek(0)
                                    file = File(page_stream, f'image-{i}.jpg')
                                    files.append(file)

                for i, file in enumerate(files, 1):
                    if i % 10 == 0:
                        await message.channel.send(files=files[slice(i - 10, i)])
                    elif len(files) == i:
                        await message.channel.send(files=files[slice(i - i % 10, i)])
