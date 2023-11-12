import discord
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

raid_role_call_message = 'This roll call for the next raid day.\nPlease react with your role if you\'re able to join us, a :question:if you\'re unsure, or a :x:if you cannot.'

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$roll-call'):
        message_parts = message.content.split('!');
        print(f'LOG: Roll call executed by {message.author}')
        if(len(message_parts) == 2):
            print(f'LOG: Roll call with time sent')
            await message.channel.send(raid_role_call_message)
        else:
            print(f'LOG: Default roll call message sent')
            await message.channel.send(raid_role_call_message)

client.run(os.getenv("BOT_TOKEN"))
