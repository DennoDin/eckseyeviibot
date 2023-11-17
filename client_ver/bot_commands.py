from main_strings import log_dict, rollcall_dict, separator_dict
from emoji import emoji_dict
import os

async def rollcall(author, channel, arguments):
    print(f'{log_dict["roll_call_executed"].format(author)}')

    if(len(arguments) == 1):
        print(f'{log_dict["roll_call_with_time"]}')
        content = rollcall_dict["base"] + rollcall_dict["time"].format(arguments[0]) + rollcall_dict["react"]
        message = await channel.send(content)
        await add_role_reactions(message)

    else:
        print(f'{log_dict["roll_call_default"]}')
        content = rollcall_dict["base"] + rollcall_dict["react"]
        message = await channel.send(content)
        await add_role_reactions(message)

async def add_role_reactions(message):
    await message.add_reaction(emoji_dict['?'])
    await message.add_reaction(emoji_dict['x'])

async def separator(author, channel, arguments):
    if len(arguments) < 1:
        await channel.send(separator_dict["get"].format(os.environ['SEPARATOR']))
        return
    elif len(arguments) == 1:
        print(f'Separator changed to {arguments[0]}')
        os.environ['SEPARATOR'] = arguments[0]

commands_dict = {
    'rollcall': rollcall,
    'separator': separator,
}