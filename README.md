# eckseyeviibot
A discord bot for use my XIV raid group. Automates sending messages with pings to specified roles.

The bot is currently deployed with an AWS EC2 instance.

## Required Packages
```
discord.py >= 2.3.2
python-dotenv >= 1.0.0
```

## Adding the bot to your server
You can add my deployed bot onto your server by using [this link](https://discord.com/oauth2/authorize?client_id=376849913109282836&permissions=139855260752&scope=bot)

## Running Locally
### Start bot
```
py -3 .\main_script.py
```

## Commands
Commands are executed by typing the command with the `$` in the channel with bot.

All commands can always be run by the server owner.

#### $setAdminRole \<role id>
Used for setting the role which can execute commands.
Empty by default.

#### $rollcall
Used for starting roll call for the following week. By default does not include a time.
Bot will automatically react with Tank, Healer, DPS, Question, and Cross emojis.

*epoch time parameter currently disabled

```
example:
$rollcall 1699809133
```