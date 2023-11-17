import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from messages import bot as bot_messages, log as log_messages

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def setAdminRole(ctx, arg):
    if(ctx.author == ctx.guild.owner):
        admin_name = arg.strip()
        os.environ["LEAD_ROLE_NAME"] = admin_name
        print(log_messages.admin['set_admin_tag'].format(admin_name))
        await ctx.send(log_messages.admin['set_admin_tag'].format(admin_name))
    else:
        await ctx.send(bot_messages.forbidden['owner'].format(ctx.guild.owner))

@bot.command()
async def rollcall(ctx, *arg):
    admin_role = discord.utils.get(ctx.guild.roles, name=os.getenv("LEAD_ROLE_NAME"))
    if ctx.author == bot.user or (admin_role and admin_role not in ctx.author.roles) :
        return

    if len(arg) == 0:
        content = bot_messages.rollcall['base'] + bot_messages.rollcall['react']
        message = await ctx.send(content)

bot.run(os.getenv("BOT_TOKEN"))
