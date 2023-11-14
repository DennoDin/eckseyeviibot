import discord
import os
from dotenv import load_dotenv
from main_strings import roll_call_dict, log_dict
from commands import commands_dict

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$'):

        split_message = message.content.split('$')
        split_message = [word.strip() for word in split_message]
        split_message = split_message[1:]

        if split_message[0] == 'rollcall':
            await commands_dict['rollcall'](message.author, message.channel, split_message)
        
client.run(os.getenv("BOT_TOKEN"))
