import discord
import os
from dotenv import load_dotenv
from main_strings import roll_call_dict, log_dict

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

    if message.content.startswith('$roll-call'):
        message_parts = message.content.split('!');
        message_parts = [word.strip() for word in message_parts]
        print(f'{log_dict["roll_call_executed"].format(message.author)}')
        if(len(message_parts) == 2):
            print(f'{log_dict["roll_call_with_time"]}')
            roll_call_message = roll_call_dict["base"] + roll_call_dict["time"].format(message_parts[1]) + roll_call_dict["react"]
            await message.channel.send(roll_call_message)
        else:
            print(f'{log_dict["roll_call_default"]}')
            roll_call_message = roll_call_dict["base"] + roll_call_dict["react"]
            await message.channel.send(roll_call_message)

client.run(os.getenv("BOT_TOKEN"))
