import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from messages import bot as bot_messages, log as log_messages
import emoji

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)

authorized_roles = {}
role_emojis = []

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

    guild = bot.get_guild(int(os.getenv("BOT_GUILD")))
    global role_emojis
    role_emojis = [discord.utils.get(guild.emojis, name=emoji_name) for emoji_name in bot_messages.custom_emojis.values()]

@bot.command()
async def setAdminRole(ctx, arg):
    if(ctx.author == ctx.guild.owner):
        admin_name = arg.strip()
        global authorized_roles
        authorized_roles[ctx.guild.id] = admin_name
        print(log_messages.admin['set_admin_tag'].format(admin_name))
        await ctx.send(log_messages.admin['set_admin_tag'].format(admin_name))
    else:
        await ctx.send(bot_messages.forbidden['owner'].format(ctx.guild.owner))

@bot.command()
async def rollcall(ctx, *arg):
    if not await is_authorized(ctx):
        return

    if len(arg) == 0:
        content = bot_messages.rollcall['base'] + bot_messages.rollcall['react']
        message = await ctx.send(content)
        await rollcall_react(message)

async def is_authorized(ctx):
    guild_id = str(ctx.guild.id)
    
    if ctx.author == ctx.guild.owner or (guild_id in authorized_roles and authorized_roles[guild_id] in ctx.author.roles):
        return True
    else:
        content = bot_messages.forbidden['default']
        if not guild_id in authorized_roles:
            content = content + bot_messages.admin['not_set']
        await ctx.send(content)
        return False

async def rollcall_react(message):
    for custom_emoji in role_emojis:
        await message.add_reaction(custom_emoji)
    await message.add_reaction(emoji.question())
    await message.add_reaction(emoji.x())

bot.run(os.getenv("BOT_TOKEN"))
