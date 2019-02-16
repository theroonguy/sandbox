import discord
from discord.ext import commands
import pprint
import requests
    

TOKEN = 'NTQzOTUzNDM2NTUxNDEzNzcw.D0EFWQ.koaPnK_GT59KJtfKqP4Xis2CqKI'

client = commands.Bot(command_prefix = 'pray/')


@client.event
async def on_ready():
    print('Awaiting your command')
      
@client.command()
async def w(*args):
    output = ''
    for word in args:
        output += word

    url = 'http://iphone.halalfire.com/salatomatic.php?l={}&uuid=1&key=O2A8Uo5ACzEXW7NnPYPX'.format(output)
    res = requests.get(url)
    data = res.json()

    name = data['prayerspaces'][0]['name']
    address = data['prayerspaces'][0]['address']
    city = data['prayerspaces'][0]['city']
    state = data['prayerspaces'][0]['state']
    zip = data['prayerspaces'][0]['zip']
    phone = data['prayerspaces'][0]['phone']
    distance = data['prayerspaces'][0]['distance']
        
    fname = '{}'.format(name)
    faddress = '{}'.format(address)
    fcity = '{}'.format(city)
    fstate = '{}'.format(state)
    fzip = '{}'.format(zip)
    fphone = '{}'.format(phone)

    await client.say('**{}**'.format(name))
    await client.say(faddress+'\n'+fcity+', '+fstate' '+fzip'\n'+fphone)
    

@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)

client.run(TOKEN)
