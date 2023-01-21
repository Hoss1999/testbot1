import discord
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_BOT_TOKEN')


class Bot(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}!')

    async def on_message(self, message):
        print(f' Message from {message.author}: {message.content}')


client = Bot()
client.run(token)
