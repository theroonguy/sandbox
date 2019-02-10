import discord
from discord.ext import commands

TOKEN = 'NTQzOTUzNDM2NTUxNDEzNzcw.D0EFWQ.koaPnK_GT59KJtfKqP4Xis2CqKI'

client = commands.Bot(command_prefix = 's/')

@client.event
async def on_ready():
    print('Awaiting your command')

@client.command()
async def ping():
    await client.say('Pong')

client.run(TOKEN)
