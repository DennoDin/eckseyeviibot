import discord
import os
from dotenv import load_dotenv
from bot_commands import commands_dict

load_dotenv()

admin_role_id = int(os.getenv("LEAD_ROLE_ID"))

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

    if message.content.startswith(os.getenv("SEPARATOR")):
        has_role = [role for role in message.author.roles if role.id == admin_role_id];
        if(len(has_role) > 0):
            print(f'Role Found')

        split_message = message.content.split(os.getenv("SEPARATOR"))
        split_message = [word.strip() for word in split_message]
        
        commandStr = split_message[1]
        commandArgs = split_message[2:]

        if commandStr in commands_dict:
            await commands_dict[commandStr](message.author, message.channel, commandArgs)
        
client.run(os.getenv("BOT_TOKEN"))
