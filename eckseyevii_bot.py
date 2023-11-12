import discord
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

raid_role_call_message = 'This is our role call for the next gathering.\nPlease react with your role if you\'re able to join us, a question mark if you\'re unsure, or a X if you cannot.'

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$roll-call'):
        await message.channel.send(raid_role_call_message)

client.run(os.getenv("BOT_TOKEN"))
