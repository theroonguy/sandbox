import discord
from discord.ext import commands
import pyowm

TOKEN = 'NTQzOTUzNDM2NTUxNDEzNzcw.D0EFWQ.koaPnK_GT59KJtfKqP4Xis2CqKI'

client = commands.Bot(command_prefix = 's/')

owm = pwowm.OWM()
observation = owm.weather_at_place('Vienna,VA')
w = observation.get_weather()

@client.event
async def on_ready():
    print('Awaiting your command')

@client.command()
async def ping():
    await client.say('Pong')

@client.command()
async def weather():
    wind=w.get_wind()
    humidity=w.get_humidity()
    client.say('Wind: '+wind)
    client.say('Humidity: '+humidity)

@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)

client.run(TOKEN)
