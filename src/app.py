import discord
from dotenv import load_dotenv
import os
import bot

load_dotenv()
token = os.getenv('DISCORD_BOT_TOKEN')
intents = discord.Intents.all()


def main():
    client = bot.Client(intents=intents)
    client.run(token)


if __name__ == "__main__":
    main()
