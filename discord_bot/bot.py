import discord
from discord.ext import commands
import pprint
import requests

url = 'http://api.openweathermap.org/data/2.5/weather?q=Fairfax,us&appid=ac7c75b9937a495021393024d0a90c44'
res = requests.get(url)
data = res.json()

temp = data['main']['temp']
wind_speed = data['wind']['speed']
description = data['weather'][0]['description']
    
TOKEN = 'NTQzOTUzNDM2NTUxNDEzNzcw.D0EFWQ.koaPnK_GT59KJtfKqP4Xis2CqKI'

client = commands.Bot(command_prefix = 's/')


@client.event
async def on_ready():
    print('Awaiting your command')

@client.command()
async def ping():
    await client.say('Pong')

@client.command()
async def weather():

<<<<<<< HEAD
    await client.say('Temperature : {} degree celcius'.format(temp))
=======
    temp = data['main']['temp']
    wind_speed = data['wind']['speed']

    latitude = data['coord']['lat']
    longitude = data['coord']['lon']

    description = data['weather'][0]['description']

    await client.say('Temperature : {} degree fahrenheit'.format(temp))
>>>>>>> bdb3e354acd1fd29e83f584904c98999b6c915f5
    await client.say('Wind Speed : {} m/s'.format(wind_speed))
    await client.say('Description : {}'.format(description))

@client.command()
async def wind():
    await client.say('Wind Speed: {} m/s'.format(wind_speed))

@client.command()
async def desc():
    await client.say('Description: {}'.format(description))

@client.command()
async def temp():
    await client.say('Temperature: {}'.format(temp))

@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)

client.run(TOKEN)
