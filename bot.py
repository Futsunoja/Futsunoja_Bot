import discord
from discord.ext import commands
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix = 'f!')

@bot.event
async def on_ready():
    print("Bot All Ready!")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel()
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel()
    await channel.send(f'{member} leave!')

bot.run(jdata['TOKEN'])