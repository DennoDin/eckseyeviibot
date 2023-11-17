from main_strings import log_dict, roll_call_dict

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

commands_dict = {
    'rollcall': rollcall,
}