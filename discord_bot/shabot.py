import discord
from discord.ext import commands
import pprint
import requests
    

TOKEN = 'NTQzOTUzNDM2NTUxNDEzNzcw.D0EFWQ.koaPnK_GT59KJtfKqP4Xis2CqKI'

client = commands.Bot(command_prefix = 's/')


@client.event
async def on_ready():
    print('Awaiting your command')

@client.command()
async def ping():
    await client.say('Pong')
'''
@client.group(pass_context=True)
async def weather(ctx):
    if ctx.invoked_subcommand is None:
        await client.say('Sorry, I didn\'t understand. Please try again.')

@client.group(pass_context=True)
async def w(ctx):
    if ctx.invoked_subcommand is None:
        await client.say('Sorry, I didn\'t understand. Please try again.')
'''        
@client.command()
async def w(*args):
    output = ''
    for word in args:
        output += word

    url = 'http://api.openweathermap.org/data/2.5/weather?q={},us&appid=ac7c75b9937a495021393024d0a90c44'.format(output)
    res = requests.get(url)
    data = res.json()

    temp = data['main']['temp']
    tempF = round(((data['main']['temp'] - 273.15) * 9/5 + 32),2)
    wind_speed = data['wind']['speed']
    description = data['weather'][0]['description']
    
    ftemp = 'Temperature: {} Degrees Fahrenheit'.format(tempF)
    fwind = 'Wind Speed: {} m/s'.format(wind_speed)
    fdesc = 'Description: {}'.format(description)

    doutput = '**'+str(output)+'**'
    await client.say('Weather in {} is: '.format(doutput))
    await client.say(ftemp+'\n'+fwind+'\n'+fdesc)
    
'''
@weather.command()
async def austin():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Austin,us&appid=ac7c75b9937a495021393024d0a90c44'
    res = requests.get(url)
    data = res.json()

    temp = data['main']['temp']
    tempF = round(((data['main']['temp'] - 273.15) * 9/5 + 32),2)
    wind_speed = data['wind']['speed']
    description = data['weather'][0]['description']
    
    ftemp = 'Temperature: {} Degrees Fahrenheit'.format(tempF)
    fwind = 'Wind Speed: {} m/s'.format(wind_speed)
    fdesc = 'Description: {}'.format(description)

    await client.say(ftemp+'\n'+fwind+'\n'+fdesc)

@w.command()
async def vienna():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Vienna,us&appid=ac7c75b9937a495021393024d0a90c44'
    res = requests.get(url)
    data = res.json()

    temp = data['main']['temp']
    tempF = round(((data['main']['temp'] - 273.15) * 9/5 + 32),2)
    wind_speed = data['wind']['speed']
    description = data['weather'][0]['description']
    
    ftemp = 'Temperature: {} Degrees Fahrenheit'.format(tempF)
    fwind = 'Wind Speed: {} m/s'.format(wind_speed)
    fdesc = 'Description: {}'.format(description)

    await client.say(ftemp+'\n'+fwind+'\n'+fdesc)

@w.command()
async def austin():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Austin,us&appid=ac7c75b9937a495021393024d0a90c44'
    res = requests.get(url)
    data = res.json()

    temp = data['main']['temp']
    tempF = round(((data['main']['temp'] - 273.15) * 9/5 + 32),2)
    wind_speed = data['wind']['speed']
    description = data['weather'][0]['description']
    
    ftemp = 'Temperature: {} Degrees Fahrenheit'.format(tempF)
    fwind = 'Wind Speed: {} m/s'.format(wind_speed)
    fdesc = 'Description: {}'.format(description)

    await client.say(ftemp+'\n'+fwind+'\n'+fdesc)
'''
@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)

client.run(TOKEN)
