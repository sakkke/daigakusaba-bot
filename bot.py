from dotenv import load_dotenv
from discord import Bot, Intents
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

from pdf import PDF

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

bot.add_cog(PDF(bot))

def run_httpd(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8080)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

httpd_thread = Thread(target=run_httpd, daemon=True)
httpd_thread.start()

bot.run(os.getenv('TOKEN'))
