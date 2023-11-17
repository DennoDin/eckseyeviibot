from main_strings import log_dict, rollcall_dict, separator_dict
import os

async def rollcall(author, channel, message_parts):
    print(f'{log_dict["roll_call_executed"].format(author)}')

    if(len(message_parts) == 2):
        print(f'{log_dict["roll_call_with_time"]}')
        roll_call_message = roll_call_dict["base"] + roll_call_dict["time"].format(message_parts[1]) + roll_call_dict["react"]
        await channel.send(roll_call_message)
        
    else:
        print(f'{log_dict["roll_call_default"]}')
        roll_call_message = roll_call_dict["base"] + roll_call_dict["react"]
        await channel.send(roll_call_message)

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