import discord
import messages.handler as msg

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}!')

    async def on_message(self, message):
        msg.messages(self, message)
